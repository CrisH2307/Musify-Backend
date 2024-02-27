import socket
import pickle

def send_task(task_func, args, server_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(server_address)

        # Pickle task and arguments
        pickled_data = pickle.dumps((task_func, args))  # Pass an empty string as the second argument

        # Send pickled data
        client_socket.sendall(pickled_data)

        # Receive result
        data = client_socket.recv(1024)
        result = pickle.loads(data)

        print("Result:", result)

    except socket.error as e:
        print("Error connecting to server:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    # Define your task function
    def add(x, y):
        return x + y

    # Server address (replace with actual IP and port)
    server_address = ('localhost', 12345)

    # Send task with arguments
    send_task(add, (5, 3), server_address)
