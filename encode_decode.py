from base64 import encodestring, decodestring


string = 'string data'

encode_data = encodestring(string)

#encode_data = 'c3RyaW5nIGRhdG' # 'c3RyaW5nIGRhdGE='

def decodeString(encode_data):
    """"""
    encode_data += '=' * (4 - len(encode_data) % 4)
    return decodestring(encode_data)
    #try:
        #if(len(encode_data)%4 == 0):
            #return decodestring(encode_data)
        #else:
            #missing_padding = 4 - len(encode_data) % 4
            #if missing_padding:
                #encode_data += '=' * missing_padding
                #print encode_data
            #return decodestring(encode_data)
    #except Exception, err:
        #raise Exception("Error getting while decoding string", err)

print decodeString(encode_data);
