from flask import Flask

from commonlib.initproperties import InitProperties

# Initialize Flask related properties
webapp_properties = InitProperties('Properties.ini').webapp()
app = Flask(__name__)


# Used for stubbing
def stub_test():
    return True


@app.route("/")
def index():
    return "root"


if __name__ == '__main__':
    app.run(host=webapp_properties['host'], port=webapp_properties['port'])