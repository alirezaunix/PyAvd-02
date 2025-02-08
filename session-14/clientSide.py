import socket

def send_text_to_server(text, host='192.168.216.10', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(text.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

if __name__ == "__main__":
    send_text_to_server("Hello, Server!")