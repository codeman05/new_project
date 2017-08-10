from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/testing/')
def testing():
    return render_template('testing_services.html')

@app.route('/crew/')
def crew():
    return render_template('blue_heaven_crew.html')

@app.route('/contact/')
def contact():
    return render_template('contact_us.html')
