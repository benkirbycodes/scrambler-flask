from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

engine = create_engine(mysql: // scrambler: Cp2g9lu!!xmV@den1.mysql6.gear.host: 3306/scrambler)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
