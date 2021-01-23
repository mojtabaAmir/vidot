from dependency_injector import containers

class Configs(containers.DeclarativeContainer):
    config = { 
        "app": {
            "host": "0.0.0.0",
            "port": 9382
        } 
    }
