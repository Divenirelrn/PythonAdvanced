#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lu zhao
# Python 3.6.7
from __future__ import division
import tornado.web
from tornado import gen
from tornado.httpserver import HTTPServer
import tornado.options
from tornado.web import RequestHandler
from copy import deepcopy
import json
import time

from utils.database_ import connect_db, insert_data, user_find, group_find, device_find
from utils.util import get_logger, timestamp2strtime

import multiprocessing
import ws_server as wb_server
from ws_server import data_put

# 获取日志对象
logger = get_logger("er_log")

############ get collection ##################
# 连接数据库,获取指定集合
try:
    mydb = connect_db('localhost:27017', 'hy_bitbox')#, 'event')
    mycol = mydb["event"]
    logger.info("collection:{}".format(mycol))

    usercol = mydb['user_info']
    logger.info("user collection:{}".format(usercol))
    devicecol = mydb['device']
    logger.info("collection:{}".format(devicecol))
except Exception as e:
    logger.error(str(e))
      

print("database connected!")

############## json_result ##############
def call_result(result_code, result_data, error_state='错误'):
    json_result = {}
    json_result["resultCode"] = result_code
    json_result["resultMsg"] = error_state
    json_result["resultData"] = result_data

    logger.info(json_result)
    return json_result


class EventReceiverHandler(RequestHandler):
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        request_result = dict()
        try:
            senceinfo_dict = json.loads(self.request.body)
        except Exception as e:
            logger.error(e.value)
            senceinfo_dict = dict()

        # 参数校验
        try:
            face_list = senceinfo_dict["face_list"]
            ipc_id = senceinfo_dict["ipc_id"]
            threshold = senceinfo_dict["threshold"]

            # 存日志时，去除请求中的base64图像数据
            face_list_new = deepcopy(face_list)
            for face in face_list_new:
                if "image" in face["user_info"].keys():
                    face["user_info"]["image"] = ""
            logger.info("Request body:{}".format(face_list_new))
            del face_list_new
        except KeyError:
            return self.write(json.dumps(call_result(50002, request_result, '请求参数缺失'), ensure_ascii=False))

        try:
            # 发送结果（LJ）
            print("send result")
            for face in face_list:
                # 参数解析
                user_info = face["user_info"]
                user_id = user_info["user_id"]
                user_type, user_name = user_find(usercol, user_id)
                group_name = group_find(usercol, user_id)
                device_type = device_find(devicecol, ipc_id)

                json_data = {
                    "identity_id": user_id,
                    "identity_name": user_name,
                    "group_name": group_name,
                    "device_id": ipc_id,
                    "timestamp": time.time(),
                    "score": user_info["score"],
                    "ext_data": {
                        "device_ip": "",
                        "spot_pic": user_info["image"],
                        "device_type": device_type,
                        "recognize_face": "",
                        "recognize_face_attr": {
                            "age": 12,
                            "gender": "male",
                            "glasses": "no glasses"
                        }
                    }
                }
                # 发送数据
                print("json_data:", json_data)
                data_put(json_data)

            print("save data to database")
            # res = api_caller("172.18.68.99", "11494", "/test_api", face_list)
            # logger.info("Result sent status:{}".format(res))
            # 结果写入数据库
            for face in face_list:
                # 参数解析
                addtime = timestamp2strtime(time.time())
                user_info = face["user_info"]
                doc = {"face_detect": {  # 注意base64是否可以写入
                    "location": face["location"],
                    "face_prob": face["face_prob"],
                    "user_id": user_info["user_id"],
                    "image": user_info["image"],
                    "score": user_info["score"],
                    "ipc_id": ipc_id,
                    "threshold": threshold,
                    "addtime": addtime
                }}
                write_status = insert_data(mycol, doc)  # 0-succeed, -1-faild
                logger.info("Result write to db status:{}".format(write_status))

                if write_status == -1:
                    return self.write(json.dumps(call_result(40001, request_result, '写库失败')))

            return self.write(json.dumps(call_result(50000, request_result, '正确')))
        except:
            return self.write(json.dumps(call_result(90000, request_result, '接口内部错误，请联系工作人员'), ensure_ascii=False))


def make_app():
    return tornado.web.Application([
        (r"/http_events_receiver", EventReceiverHandler),
    ])


def main():
    #开启web_socket
    pool = multiprocessing.Pool(processes=1)
    pool.apply_async(wb_server.wb_svr_start)
    print("web socket start...")

    #开启http server
    app = make_app()
    server = HTTPServer(app)
    server.bind(10087)
    server.start(1)  # 设置启动多少个进�?
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
