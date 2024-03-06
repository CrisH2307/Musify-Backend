import socket
import pickle
import threading

HOST = 'localhost'
PORT = 3000

clients = []
lock = threading.Lock()  # Lock for thread-safe access to clients list

def handle_client(client_socket, address):
    print(f"[INFO] Connected by {address}")
    data_buffer = b''
    while True:
        received_data = client_socket.recv(1024)
        if not received_data:
            break
        data_buffer += received_data

        try:
            message = pickle.loads(data_buffer)
            # Process the message and broadcast
            broadcast(message, client_socket)
            data_buffer = b''  # Reset buffer after successful unpickling
        except pickle.UnpicklingError:
            print(f"[ERROR] Unpickling error from {address}")
        if not client_socket.fileno() > 0:  # Check if client disconnected
            break

    with lock:
        clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.sendall(pickle.dumps(message))
                except ConnectionError:
                    print(f"[INFO] Client {client.getpeername()} disconnected during broadcast")
                    clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[INFO] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
        with lock:
            clients.append(client_socket)

if __name__ == "__main__":
    start_server()
