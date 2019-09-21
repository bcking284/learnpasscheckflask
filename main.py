from flask import Flask,render_template,request
from checks import length_check,caps_check,num_check

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    password = request.args.get('password')
    length = length_check(password)
    caps = caps_check(password)
    num = num_check(password)


    return render_template('report.html', length = length, caps = caps, num = num)


if __name__ == "__main__":
    app.run(debug=True)
