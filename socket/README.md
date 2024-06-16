# Socket Connection

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

## State Diagram for Server and Client Model

![state diagram](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/diagram_socket.png)

## Stages for Server

### Create Socket

```python
import socket

# Create socket instance
server_socket = socket.socket() 
```

### Bind

```python
host = "192.168.1.5"
port = 5000  # initiate port no above 1024

server_socket.bind((host, port)) 
```

### Listen

```python
# number client is accepted
server_socket.listen(2)
```

### Accept

```python
# accept new connection
# conn: instace of connection
# address: address connection

conn, address = server_socket.accept() 
```

## Stages for Client

### Create Socket

```python
import socket

# Create socket instance
client_socket = socket.socket()
```

### Connect

```python
host = "192.168.1.5"
port = 5000  

client_socket.connect((host, port))
```

## Reference

![`Result`](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/socket_connection.png)
