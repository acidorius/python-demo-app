from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
	return 'Hello World'

@app.route('/version')
def version():
	return 'v1.0.0'

@app.route('/readiness')
def readiness():
	return 'OK'

@app.route('/healthz')
def healthz():
	return 'OK'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
