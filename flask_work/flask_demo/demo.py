import flask
from flask import Flask, jsonify, request
from flask_restful import reqparse
from datetime import datetime

import flask_restful
import mariadb
import json
import uuid

app = Flask(__name__)
# app.config["DEBUG"] = True
api = flask_restful.Api(app)

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'mysql',
    'database': 'mydb'
}

class Delivery(flask_restful.Resource):
    def __init__(self):
        self.conn = mariadb.connect(**config)
        self.cursor = self.conn.cursor()
    def get(self):
        sql = '''select delivery_id, order_json, status, created_at 
                 from delivery_status order by id desc'''
        self.cursor.execute(sql)
        result_set = self.cursor.fetchall()

        row_headers = [x[0] for x in self.cursor.description]

        json_data = []
        for result in result_set:
            json_data.append(dict(zip(row_headers, result)))

        return jsonify(json_data)

class DeliveryUpdate(flask_restful.Resource):
    def __init__(self):
        self.conn = mariadb.connect(**config)
        self.cursor = self.conn.cursor()

    def put(self, delivery_id):
        json_data = request.get_json()
        status = json_data['status']

        # DB insert
        sql = '''UPDATE delivery_status SET status=? 
                 WHERE delivery_id=?'''

        self.cursor.execute(sql, [status, delivery_id])
        self.conn.commit()

        response = jsonify(json_data)
        response.status_code = 201
        
        return response

api.add_resource(Delivery, '/delivery-ms')
api.add_resource(DeliveryUpdate, '/delivery-ms/<string:delivery_id>')

if __name__ == '__main__':
    app.run(port=6000)
