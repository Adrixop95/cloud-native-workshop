import socket
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Cloud",
            "Hostname": socket.gethostname()}
