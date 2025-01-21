from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
	compose = 'casa-compose.yml'
	sites = []
	f = open(compose, 'r')
	lines = f.readlines()

	for line in lines:
		if "http" in line and "Host" in line:
			spline = line.split('`')
			sites.append(spline[1])
	return render_template('main.html', sites=sites)

if __name__ == "__main__":
	app.run(debug=True)
