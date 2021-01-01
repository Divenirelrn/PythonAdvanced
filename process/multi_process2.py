import multiprocessing as mp
import os, time


def copy_file(file_name, src, dst, q):
    file_src = os.path.join(src, file_name)
    with open(file_src, 'rb') as fp:
        data = fp.read()
    file_dst = os.path.join(dst, file_name)
    with open(file_dst, 'wb') as fo:
        fo.write(data)

    q.put(file_name)


def main():
    po = mp.Pool(10)
    q = mp.Manager().Queue(10)
    src_dir = r"D:\files\AI\Projects\object_detection\yolov3-8\coco128\images\train2017"
    dst_dir = r"D:\files\AI\Projects\python_advanced\data"
    file_list = os.listdir(src_dir)
    start = time.time()
    for file in file_list:
        po.apply_async(copy_file, args=(file, src_dir, dst_dir, q))

    po.close()
    # po.join()
    file_len = len(file_list)
    copy_num = 0
    for i in range(len(file_list)):
        q.get()
        copy_num += 1
        print("\r拷贝进度：%.2f %%" % (100 * copy_num / file_len), end="")
    print("\n")
    end = time.time()
    print("copy time:", end - start)


if __name__ == "__main__":
    main()