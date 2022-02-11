import sys, socket

def get(url, verbose):
    # url= "www.httpbin.org/get?course=networking&assignment=1%27"
    host = "www.httpbin.org"
    args = "/get?course=networking&assignment=1%27"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    message  = str.encode('GET ' + args + ' HTTP/1.1\r\n')
    message += str.encode('Host: ' + host + ':80\r\n')
    message += b'Connection: close\r\n'
    message += b'\r\n'
    s.sendall(message)
    result = s.recv(10000)
    result = result.decode("utf-8")

    headers = result.split("\r\n\r\n")[0]
    body = result.split("\r\n\r\n")[1]
    if verbose:
        print(headers + "\n")
    print(body)
    s.close()