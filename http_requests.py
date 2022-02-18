import socket

def request(command, url, verbose, data, headers):
    host = url.split('//')[1].split('/')[0]
    args = '/' + url.split('//')[1].split('/')[1]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    message = str.encode(command + ' ' + args + ' HTTP/1.0\r\n')
    message += str.encode('Host: ' + host + ':80\r\n')

    if headers is not None:
        for header in headers:
            index = header[0].find(':') + 1
            header = header[0][:index] + " " + header[0][index:]
            message += str.encode(header + "\r\n")

    if data is not None:
        if message.find(b'Content-Length:') == -1:
            message += str.encode('Content-Length: ' + str(len(data)) + '\r\n')
        message += b'\r\n'
        message += str.encode(data + '\r\n')
    message += b'Connection: close\r\n'
    message += b'\r\n'
    s.sendall(message)

    result = s.recv(10000)
    result = result.decode("utf-8")
    head = result.split("\r\n\r\n")[0]
    body = result.split("\r\n\r\n")[1]

    if verbose:
        print(head + "\n")
    print(body)
    s.close()

     