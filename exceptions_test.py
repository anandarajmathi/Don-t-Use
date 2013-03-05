#! /usr/bin/python

from base64 import encodestring, decodestring

def decodeString(data1):
    try:
        if((len(data1)%4) == 0):
            return decodestring(data1)
        else:
            data1 += '=' * (4 - len(data1) % 4)
            return decodestring(data1)
    except Exception, error:
        raise Exception("Erron message1", error)

def encodeAndDecode():
    """ """
    data = "Python exceptions handling"
    print data
    data1 = 'UHl0aG9uIGV4Y2VwdGlvbnMgaGFuZGxpb'
    #data1 = encodestring(data)
    print "Encoded data : ",  data1
    try:
        print decodeString(data1)
        return "success"
    except Exception, error:
        raise Exception("Erron message", error)

print encodeAndDecode()
