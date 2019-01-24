from flask import Flask
from flask import render_template
from flask_profiler import Profiler

profile = Profiler()

app = Flask (__name__, template_folder="data")

app.config["DEBUG"] = True
app.config["flask_profiler"] = {
        "enabled": app.config["DEBUG"],
        "storage": {
                "engine": "sqlite"
        },
        "basicAuth":{
                "enabled": False,
                "login": "admin",
                "password": "admin"
        },
        "ignore": [
                "^/static/.*",
        ],
        "endpointRoot" : "metrics"
}
        
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/version')
def version():
	return 'v2.0.1'

@app.route('/readiness')
def readiness():
	return 'OK'

@app.route('/healthz')
def healthz():
	return 'OK'

profile.init_app(app)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
