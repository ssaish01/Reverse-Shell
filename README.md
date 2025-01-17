
# Multi-Client & Single-Client Communication System

This repository contains two communication systems using Python's `socket` and `threading` libraries:
1. **Single-Client Communication**: A system that handles communication between a server and a single client.
2. **Multi-Client Communication**: A system that allows communication between a server and multiple clients simultaneously, with each connection handled by a separate thread.

---

## Prerequisites
- Python 3.x installed on both server and client machines.
- Both machines must be connected to the same network.

---

## Setup

### 1. **Single-Client Communication**

1. Edit the `client.py` file to set the correct server IP address:
    ```python
    host = '192.168.1.6'  # Replace with the server's IP address
    port = 9999
    ```

2. Modify the port number to your convenience. Ensure that the port is open and not blocked by firewalls.

---

## Running the Single-Client Program

### Step 1: Start the Server
1. Run the server script:
   ```bash
   python single_client_server.py
   ```
2. The server will bind to the specified port and wait for a client connection.

### Step 2: Start the Client
1. Run the client script:
   ```bash
   python client.py
   ```
2. The client will connect to the server, and you can begin sending commands.

---

## Setup for Multi-Client Communication

### 1. **Multi-Client Communication**

1. Edit the `client_1.py` and `client_2.py` files to set the correct server IP address:
    ```python
    host = '192.168.1.6'  # Replace with the server's IP address
    port = 9999
    ```

2. Modify the port number to your convenience. Ensure that the port is open and not blocked by firewalls.

---

## Running the Multi-Client Program

### Step 1: Start the Server
1. Run the server script:
   ```bash
   python multi_client_server.py
   ```
2. The server will bind to the specified port (`9999`) and start accepting multiple client connections.

### Step 2: Start the Clients
1. Run the client scripts:
   ```bash
   python client_1.py
   python client_2.py
   ```
2. Each client will connect to the server. You can use the server to interact with any connected client.

---

## Usage

### Single-Client Communication

- The server can send commands to the single connected client and get responses.
- Use the command `quit` to terminate the connection.

### Multi-Client Communication

#### Server Commands:
- `list`: Displays all connected clients with their indices and addresses.
- `select <index>`: Selects a specific client to interact with.
- `<command>`: Sends a shell command to the selected client (e.g., `dir` or `ls`).
- `quit`: Disconnects from the selected client or exits the reverse shell.

---

## Example Interaction
You can find the output screenshots in the 'Screenshots' folder.

### Single-Client Interaction
#### Server:
```bash
Binding the port 9999
Connection has been established
Ip: 192.168.1.7
Port: 53698
ls   # Example command
Volume in drive C has no label.
Volume Serial Number is ABCD-EFGH

Directory of C:\Users\Username

12/25/2024  10:30 AM    <DIR>          .
12/25/2024  10:30 AM    <DIR>          ..
12/25/2024  10:30 AM    <DIR>          Documents
C:\Users\Username> 
```

#### Client:
```bash
 Volume in drive C has no label.
 Volume Serial Number is ABCD-EFGH

 Directory of C:\Users\Username

12/25/2024  10:30 AM    <DIR>          .
12/25/2024  10:30 AM    <DIR>          ..
12/25/2024  10:30 AM    <DIR>          Documents
```

### Multi-Client Interaction
#### Server:
```bash
reverse_shell> list
------Clients------
0 192.168.1.10 52010
1 192.168.1.11 52011

reverse_shell> select 0
You are now connected to: 192.168.1.10:52010
(192.168.1.10:52010)> dir
 Volume in drive C has no label.
 Volume Serial Number is ABCD-EFGH

 Directory of C:\Users\Username

12/25/2024  10:30 AM    <DIR>          .
12/25/2024  10:30 AM    <DIR>          ..
12/25/2024  10:30 AM    <DIR>          Documents
(192.168.1.10:52010) C:\Users\Username>
```

#### Client:
```bash
 Volume in drive C has no label.
 Volume Serial Number is ABCD-EFGH

 Directory of C:\Users\Username

12/25/2024  10:30 AM    <DIR>          .
12/25/2024  10:30 AM    <DIR>          ..
12/25/2024  10:30 AM    <DIR>          Documents
```

---

## Notes
- The server can manage multiple clients, but it interacts with one client at a time.
- Use this project responsibly, as executing arbitrary shell commands on clients can pose significant security risks.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contribution

Feel free to open issues or submit pull requests to improve this project.
