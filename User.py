# A Sample class with init method
class User:

    # init method or constructor
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.msg_id = []


    def add_msg_id(self,msg_id):
        self.msg_id.append(msg_id)


    def get_msg_id(self):
        return self.msg_id.pop()