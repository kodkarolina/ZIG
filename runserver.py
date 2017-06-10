from App import app
from App.config import HOST_NAME
from App.config import HOST_PORT

app.run(host=HOST_NAME, port=HOST_PORT, debug="true")