import socket
import ssl
import threading

# Thong tin server
server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    while True:
        try:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhan:", data.decode('utf-8'))
        except: 
            pass
        finally:
            ssl_socket.close()
            print("Kết nối da dong.")

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE  # Không kiểm tra chứng chỉ
context.check_hostname = False  # Không kiểm tra tên máy chủ

# Thiết lập kết nối SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

ssl_socket.connect(server_address)

# Bắt đầu luồng để nhận dữ liệu tu server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Gửi dữ liệu đến server
try:
    while True:
        message = input("Nhap tin nhan: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()
    