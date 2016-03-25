from flask import Flask, jsonify
app = Flask(__name__)

geofences = [
	{
		'id':1,
		'latitude': 40.6,
		'longitude': -73.95,
		'radius': '10' #in meters
	}
	 ,

	 {
	 	'id':2,
	 	'latitude': 90,
	 	'longitude':90,
	 	'radius':'90'
	 }
]

@app.route('/fences', methods=['GET'])
def get_fences():
    return jsonify({'geofences': geofences})

@app.route('/fences/<int:fence_id>', methods=['GET'])
def get_fence(fence_id):
    fence = [fence for fence in geofences if fence['id'] == fence_id]
    if len(fence) == 0:
        abort(404)
    return jsonify({'geofence': fence[0]})

if __name__ == '__main__':
    app.run()
