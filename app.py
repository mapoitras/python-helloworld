from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/status")
def status():
    logging.debug('Status')
    return app.response_class(
        response = json.dumps({'result': 'OK - healthy'}),
        status = 200,
        mimetype='application/json'
        )

@app.route("/metrics")
def metrics():
    logging.debug('Metrics')
    return app.response_class(
        response = json.dumps({'status': 'success', 'code': 0, 'data': {'UserCount': 140, 'UserCountActive': 23}}),
        status = 200,
        mimetype='application/json'
    )

@app.route("/")
def hello():
    logging.debug('Hello')
    return "Hello World!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',
                        encoding='utf-8',
                        level=logging.DEBUG,
                        format='%(asctime)s, %(message)s endpoint was reached')

    app.run(host='0.0.0.0')
