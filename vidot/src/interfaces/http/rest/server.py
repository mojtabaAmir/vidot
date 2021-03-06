from flask import Flask, Blueprint

class Server:
    def __init__(self, config, user_controller):
        self.config = config
        self.app = Flask(__name__)
        
        # Register bp dynamically
        self.app.register_blueprint(user_controller.router, url_prefix='/{}/{}/user'.format(config["base_url"], config["app_version"]))

    def start(self):
        self.app.run(**self.config["app"])
