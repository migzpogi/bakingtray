from flask import Flask, Response, url_for, render_template
import json
import socket

from commonlib.initproperties import InitProperties

# Initialize Flask related properties
webapp_properties = InitProperties('Properties.ini').webapp()
app = Flask(__name__)


# Used for stubbing
def stub_test():
    return True


# Helper method for site-map
def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


# Root, uses render_templete to generate HTML with CSS styling
@app.route('/')
def index():
    return render_template('index.html')


# Sample JSON response
@app.route("/json-response")
def json_response():
    body = {
        'name': 'John Dela Cruz',
        'age': 25
    }
    response_object = Response(
        response=json.dumps(body),
        mimetype='application/json'
    )
    response_object.headers['Trace'] = socket.gethostname()
    return response_object


# Shows the different routes
@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return links


if __name__ == '__main__':
    app.run(host=webapp_properties['host'], port=webapp_properties['port'])