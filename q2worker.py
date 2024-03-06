import socket
import pickle

def run_worker(server_address):
    worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker_socket.bind(server_address)
    worker_socket.listen(1)

    print("Worker listening for tasks...")

    while True:
        client_socket, client_address = worker_socket.accept()

        try:
            # Receive pickled data
            data = client_socket.recv(1024)
            task_func, args = pickle.loads(data)

            # Execute task and get result
            result = task_func(*args)

            # Pickle result and send back
            pickled_result = pickle.dumps(result)
            client_socket.sendall(pickled_result)

        except pickle.UnpicklingError:
            print("Error unpickling task data.")
        except Exception as e:
            print("Error processing task:", e)
        finally:
            client_socket.close()

if __name__ == "__main__":
    # Server address (replace with actual IP and port)
    server_address = ('localhost', 12345)
    run_worker(server_address)
