import socket

def server_program():
    host = "192.168.1.5"
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance

    try:
        server_socket.bind((host, port))  # bind host address and port together
    except socket.error as e:
        print(f"Error binding to socket: {e}")
        return

    server_socket.listen(2)
    print(f"Server listening on {host}:{port}\n")

    try:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
    except socket.error as e:
        print(f"Error accepting connection: {e}")
        return  
    
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                msg = "error" 
                conn.send(msg.encode()) 
                # if data is not received, break
                print("No data received")
                continue
            print("\nfrom connected client: " + str(msg))
            
            data = input(' -> ')
            if data == "":
                data = "Hi"
            conn.send(data.encode()) 

        except socket.error as e:
            print(f"Error during communication: {e}")
            break
        except KeyboardInterrupt:
            break
    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
