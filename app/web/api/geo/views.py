from __future__ import absolute_import
from flask import request, jsonify
from flask_restful import Resource

import requests
import json


class TestView(Resource):
	def get(self):
		return "Hello ojenfo3nfr"


class CoordinatesView(Resource):
	def get(self):
		send_url = 'http://freegeoip.net/json'
		r = requests.get(send_url)
		data = json.loads(r.text)

		return data


class Sensor(Resource):
	def get(self):

		now_lat = float(request.args.get('latitude', 0))
		now_lon = float(request.args.get('longitude', 0))

		send_url = 'http://freegeoip.net/json'
		r = requests.get(send_url)
		j = json.loads(r.text)

		trigger_lat = float(j['latitude'])
		trigger_lon = float(j['longitude'])

		if now_lat ==  trigger_lat and now_lon == trigger_lon:
			alert = True
		else:
			alert = False

		return jsonify(alert)