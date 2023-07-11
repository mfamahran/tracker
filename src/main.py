from flask import Flask, send_file, Response
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    if os.path.isfile('/tmp/ok'):
        return 'OK', 200
    else:
        return 'Service Unavailable', 503

@app.route('/img')
def img():
    app.logger.info('Image request')
    return send_file('static/1x1.gif', mimetype='image/gif')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
