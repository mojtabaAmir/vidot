from flask import Flask

class Server:
    def __init__(self, config):
        self.config = config
        self.app = Flask(__name__)

    def start(self):
        self.app.run(**self.config["app"])
