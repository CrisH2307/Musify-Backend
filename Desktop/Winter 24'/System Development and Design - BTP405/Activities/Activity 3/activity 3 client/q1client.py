import socket
import pickle

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)  # Adjust server IP/port as needed
    client_socket.connect(server_address)

    try:
        # Get file path from user
        file_path = input("Enter file path: ")

        # Open file in binary mode
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Pickle file data
        pickled_data = pickle.dumps(file_data)

        # Send pickled file data to server
        client_socket.sendall(pickled_data)

        print("File sent successfully!")

    except FileNotFoundError:
        print("Error: File not found.")
    except pickle.PickleError:
        print("Error pickling file.")
    except socket.error as e:
        print("Error connecting to server:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()
