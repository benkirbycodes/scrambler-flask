from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from uri import uri

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


engine = create_engine(uri)


@app.route('/sentences', methods=['GET'])
def sentences():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
