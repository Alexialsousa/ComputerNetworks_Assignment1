import sys, socket

def get(url, verbose, headers):
    host = url.split('//')[1].split('/')[0]
    args = '/' + url.split('//')[1].split('/')[1]
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

def post(url, verbose, data: str, headers):
    host = url.split('//')[1].split('/')[0]
    args = '/' + url.split('//')[1].split('/')[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    message = str.encode('POST ' + args + ' HTTP/1.1\r\n')
    message += str.encode('Host: ' + host + ':80\r\n')
    for header in headers:
        index = header[0].find(':') + 1
        header = header[0][:index] + " " + header[0][index:]
        message += str.encode(header + "\r\n")

    if message.find(b'Content-Length:') == -1:
        message += str.encode('Content-Length: ' + str(len(data)) + '\r\n')

    message += b'\r\n'
    message += str.encode(data + '\r\n')
    message += b'Connection: close\r\n'
    message += b'\r\n'
    print(message)
    s.sendall(message)
    result = s.recv(10000)
    result = result.decode("utf-8")
    print(result)

     