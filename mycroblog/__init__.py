from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config
from flask import request, jsonify, abort

db = SQLAlchemy()

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('config.py')
    db.init_app(app)

    from mycroblog.models import Entry

    @app.route('/entry', methods=['post'])
    def create():
        text = str(request.data.get('text', ''))
        if text:
            entry = Entry(text=text)
            entry.save()
            response = jsonify({
                'id': entry.id,
                'text': entry.text,
                'date_created': entry.date_created
            })
            response.status_code = 201
            return response
        else:
            response = jsonify({
                'message': 'We cannot save the entry'
            })
            response.status_code = 405
            return response


    return app

