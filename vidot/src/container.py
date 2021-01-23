from dependency_injector import providers, containers

from vidot.config.main import Configs

from vidot.src.app import App

from vidot.src.infra.database.mongo.repositories.user_repository import UserRepository

from vidot.src.infra.response import VidotResponse as Response

from vidot.src.interfaces.http.rest.modules.user.controller import UserController
from vidot.src.interfaces.http.rest.server import Server

class Container(containers.DeclarativeContainer):
    response = providers.Singleton(Response)
    
    user_repository = providers.Singleton(UserRepository)

    user_controller = providers.Singleton(UserController, user_repository=user_repository, response=response)
    
    server = providers.Singleton(Server, Configs.config, user_controller)
    
    app = providers.Singleton(App, server)
