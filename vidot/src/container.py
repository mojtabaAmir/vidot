from dependency_injector import providers, containers

from vidot.config.main import Configs
from vidot.src.interfaces.http.rest.server import Server
from vidot.src.app import App

class Container(containers.DeclarativeContainer):
    server = providers.Singleton(Server, Configs.config)
    app = providers.Singleton(App, server)
