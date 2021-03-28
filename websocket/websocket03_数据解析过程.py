"""

"""
def send_msg(conn, msg_bytes):
    import struct

    token = b"\x81"
    length = len(msg_bytes)
    if length < 126:
        token += struct.pack("B", length)
    elif length <= 0xFFFF:
        token += struct.pack("!BH", 126, length)
    else:
        token += struct.pack("!BQ", 127, length)

    msg = token + msg_bytes
    conn.send(msg)
    return True

while True:
    info = conn.recv(8096)
    #b'\x81\x85\xd3\xdf\x9f\xd0\xbb\xba\xf3\xbc\xbc'
    """
    opcode = info[0] & 15
    fin = info[0] >> 7
    payload_len = info[1] & 127
    if payload_len < 126:
        pass
    elif payload_len == 126: #头部往后延伸16位
        pass
    else: #头部往后延伸64位
        pass
    """
    #头部+mask key(4个字节)+数据（通过mask key对数据进行解密）
    payload_len = info[1] & 127
    if payload_len == 126:
        extend_payload_len = info[2:4] #extend_payload_length
        mask = info[4:8] #mask
        decode = info[8:] #数据
    elif payload_len == 127:
        extend_payload_len = info[2:10]
        mask = info[10:14]
        decode = info[14:]
    else:
        extend_payload_len = None
        mask = info[2:6]
        decode = info[6:]

    bytes_list = bytearray()
    for i in range(len(decode)):
        chunk = decode[i] ^ mask[i % 4]
        bytes_list.append(chunk)
    body = str(bytes_list, encoding='utf-8')
    # print(body)

    body += 'aaaaaaaaaaa'
    send_msg(conn, bytes(body, encoding='utf-8'))