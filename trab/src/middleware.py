from asyncio.windows_events import NULL


class Middleware:

    def __init__(self, n_process):
        self.buffer = [list() for i in range(n_process)]
        self.input_buffer = [0 for i in range(n_process)]
        self.output_buffer = [0 for i in range(n_process)]

    def __str__(self):
        print(self.buffer)
        print(self.input_buffer)
        print(self.output_buffer)

    def on_recv(self, msg):
        id_proc, id_msg = parse_msg(msg)
        id_msg_input = self.input_buffer[id_proc]

        if id_msg == id_msg_input:
            deliver_msg(msg)
            self.input_buffer[id_proc] += 1
            check_buffer(id_proc) 
             
        else:
            self.buffer[id_proc].append(msg)

    def parse_msg(msg):
        return NULL, NULL
    
    def parse_id_msg(msg):
        return id_msg

    def check_buffer(self, id_proc):
        for msg in self.buffer[id_proc]:
            id_msg = parse_id_msg(msg)
            id_msg_input = self.input_buffer[id_proc]

            if id_msg == id_msg_input:
                deliver_msg(msg)
                self.input_buffer[id_proc] += 1
                check_buffer(self, id_proc)
                break
            
    def on_send(self, id_proc_dest):
        id_msg = self.input_buffer[id_proc_dest]
        send(id_msg, msg)
        self.input_buffer[id_proc_dest] += 1



