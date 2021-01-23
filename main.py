#!venv/bin/python3
from vidot.src.container import Container

if __name__ == "__main__":
    app = Container.app()

    app.start()
