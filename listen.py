import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 69))
server_ip = socket.gethostbyname(socket.gethostname())
print("Listening port 69")

while True:
    data, addr = sock.recvfrom(516)
    if data[:2] == b'\x00\x01':
        try:
            filename = data[2:].split(b'\x00')[0].decode()
            print(f"Request from {addr[0]} for tftp://{server_ip}/{filename}")
        except:
            continue
