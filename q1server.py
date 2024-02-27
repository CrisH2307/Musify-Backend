import socket
import os
import pickle

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server listening for incoming connections...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()

            print("Connection to:", client_address)

            # Receive pickled file data
            pickled_data = client_socket.recv(1024)  # Adjust buffer size as needed
            file_data = pickle.loads(pickled_data)
            
             # Print the received file content (optional)
            print("Received file content:", file_data.decode())

            # Save file to server_files directory (create if needed)
            save_dir = "server_files"
            os.makedirs(save_dir, exist_ok=True)
            file_name = "file.txt"  # Replace with desired filename
            with open(os.path.join(save_dir, file_name), "wb") as file:
                file.write(file_data)

            print("File received and saved successfully!")

            # Send acknowledgement to client
            client_socket.sendall("File received!".encode())

        except KeyboardInterrupt:
            print("Server shutting down...")
            break  # Exit the loop to stop listening for connections

        except pickle.UnpicklingError:
            print("Error unpickling file.")
        except OSError as e:
            print("Error saving file:", e)
        finally:
            client_socket.close()

    # Close the server socket
    server_socket.close()
    print("Server stopped.")

if __name__ == "__main__":
    run_server()
