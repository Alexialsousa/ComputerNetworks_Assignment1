import sys, socket

def get(url, verbose):
    # url= "www.httpbin.org/get?course=networking&assignment=1%27"
    url= "www.httpbin.org"
    # url= "www.google.ca"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url, 80))
    message  = b'GET / HTTP/1.1\r\n'
    message += str.encode('Host: ' + url + ':80\r\n')
    message += b'Connection: close\r\n'
    message += b'\r\n'
    s.sendall(message)
    result = s.recv(10000)
    result = result.decode("utf-8")
    if verbose:
        print("\n")
        print(result)
    # while (len(result) > 0):
    #     print(result)
    #     result = s.recv(10000)
    s.close()
