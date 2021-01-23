from dependency_injector import containers

class Configs(containers.DeclarativeContainer):
    config = { 
        "base_url": "api",
        "app_version": "1.0.0",
        "app": {
            "host": "0.0.0.0",
            "port": 9382,
            "debug": True
        } 
    }
