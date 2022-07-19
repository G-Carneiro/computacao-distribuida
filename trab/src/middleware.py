from concurrent.futures import process
import socket

class Middleware:

    def __init__(self, n_process, host, port, processes_address, dad_process):
        self.buffer = [list() for i in range(n_process)]
        self.input_buffer = [0 for i in range(n_process)]
        self.output_buffer = [0 for i in range(n_process)]
        self.host = host
        self.port = port
        self.processes_address = processes_address
        self.dad_process = dad_process
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);


    def __str__(self):
        return (self.buffer, self.input_buffer, self.output_buffer)

    def parse_id_msg(self, data):
        splitted = data.split("#")
        msg_id = splitted[1]
        return msg_id

    def parse_msg(self, data):
        '''
        Example: ProcessID # MsgID # MsgTxt
        '''

        splitted = data.split("#")
        process_id = splitted[0]
        msg_id = splitted[1]
        msg = splitted[2]

        return (process_id, msg_id, msg)

    def check_buffer(self, id_proc):
        for msg in self.buffer[id_proc]:
            id_msg, msg_parsed = self.parse_id_msg(msg)
            id_msg_input = self.input_buffer[id_proc]

            if id_msg == id_msg_input:
                self.dad_process.deliver_msg(msg_parsed)
                self.input_buffer[id_proc] += 1
                self.check_buffer(id_proc)
                break
            
    def on_send(self, msg, id_proc_dest):
        id_msg = self.input_buffer[id_proc_dest]
        send_to_socket(id_proc_dest, id_msg, msg)
        self.input_buffer[id_proc_dest] += 1

    def on_recv(self, msg):
        id_proc, id_msg, msg_parsed = self.parse_msg(msg)
        id_msg_input = self.input_buffer[id_proc]

        if id_msg == id_msg_input:
            self.dad_process.deliver_msg(msg_parsed)
            self.input_buffer[id_proc] += 1
            self.check_buffer(id_proc) 

        else:
            self.buffer[id_proc].append(msg)

    def start_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    self.on_recv(data)
                    if not data:
                        break
                    conn.sendall(data)

    def send_to_socket(id_proc_dest, id_msg, msg):
        clientSocket.connect(("127.0.0.1",9090));
        
 

