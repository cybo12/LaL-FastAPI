# the only one important
from fastapi import FastAPI
# to do some versionning
from fastapi_versioning import VersionedFastAPI, version
#just to get the UID of the running container
import socket
from pi import pi

docker_short_id = socket.gethostname()

app = FastAPI(title="Lunche and Learn - FastApi")
app = VersionedFastAPI(app, default_api_version=(1, 2))


@app.get("/")
@version(1, 0)
def read_root():
    return {"Hello": docker_short_id}

@app.get("/pi/{nb_digits}")
@version(1, 0)
def read_digits_number(nb_digits: int):
    if(nb_digits)>5000:
        return{"it's to much for a test"}
    return {pi(nb_digits), f"running version {version} on container {docker_short_id}"}