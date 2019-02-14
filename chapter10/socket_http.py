import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过 socket 请求 html
    url = urlparse(url)
    host = url.netloc  # 主域名
    path = url.path  # 子路径
    if path == '':
        path = '/'

    # 建立连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
    data  = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    html_data = data.split('\r\n\r\n')[1]
    print(html_data)
    client.close()

if __name__ == '__main__':
    get_url('http://www.baidu.com')
