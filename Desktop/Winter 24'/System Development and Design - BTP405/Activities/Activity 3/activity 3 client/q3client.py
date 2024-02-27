import socket
import pickle

HOST = 'localhost'
PORT = 3000

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        pickled_message = pickle.dumps(message)
        print("Sending:", pickled_message)  # Print the actual pickled data
        client_socket.sendall(pickled_message)
    except ConnectionError as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()  # Ensure socket is closed even in case of exceptions

if __name__ == "__main__":
    while True:
        message = input("Enter message: ")
        send_message(message)
