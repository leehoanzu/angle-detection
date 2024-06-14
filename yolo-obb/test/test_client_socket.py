import socket
import time

def client_program():
    host = "192.168.1.8"
    port = 3000  # socket server port number
    client_socket = socket.socket()  # instantiate

    try:
        client_socket.connect((host, port))  # connect to the server
        print("Connect successfully!\n")
    except socket.error as e:
        print(f"Error connecting to server: {e}")
        return

    # Send message to server
    message = input(' -> ')

    while message.lower().strip() != "bye":
        try:
            if message == "":
                message = "error"
            client_socket.send(message.encode())

            t0 = time.time()
            data = client_socket.recv(1024).decode()  # receive response
            if not data:
                # break
                pass
            print('Received from server: ' + data)  # show in terminal
            print(f'Done. ({time.time() - t0:.3f}s)')

        except socket.error as e:
            print(f"Error during communication: {e}")
            break
        except KeyboardInterrupt:
            break

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
