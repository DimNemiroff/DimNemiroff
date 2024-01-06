import struct



with open('expert.bin', 'rb') as dh:
    # pass
    sign, a, b = struct.unpack('3s6s3s', dh.read(12))
    print(sign, a, b)
    while True:
        slen, = struct.unpack('H', dh.read(2))
        name, = struct.unpack('%ds' %slen, dh.read(slen))
        print(name.decode('cp1251'))

