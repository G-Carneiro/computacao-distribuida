from trab.src.middleware import Middleware


class Node:

    def __init__(self, middleware):
        self.middleware = middleware
        self.list_of_received_msgs = list()

    def deliver_message(self, msg):
        self.list_of_received_msgs.append(msg)

    def send_message(self, msg, id_proc_dest):
        self.middleware.on_send(msg, id_proc_dest)

 