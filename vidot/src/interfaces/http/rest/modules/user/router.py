from flask import Blueprint
class Router:
    def __init__(self, user_controller):
        self.bp = Blueprint('user_api', __name__)

        self.bp.add_url_rule('/', 'getUsers', user_controller.get)

    @property
    def router(self):
        return self.bp
