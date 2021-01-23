class App:
    def __init__(self, server):
        self.server = server

    def start(self):
        self.server.start()