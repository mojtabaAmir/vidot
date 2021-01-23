from vidot.src.interfaces.http.rest.modules.user.router import Router

class UserController:
    def __init__(self, response, user_repository):
        self.response = response
        self.user_repository = user_repository

        self.bp = Router(self).router

    @property
    def router(self):
        return self.bp

    def get(self):
        return self.response.ok(self.user_repository.getUsers())
