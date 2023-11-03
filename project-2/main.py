from flask import Flask, render_template

import datetime
import requests


app = Flask(__name__)


@app.route('/')
def print_hi():
    return 'Hello world'


@app.route('/guess/<name>')
def guess(name):
    params = {
        "name": name.title()
    }

    response = requests.get(url="https://api.genderize.io", params=params)
    result = response.json()
    char = result["name"]
    gend = result["gender"]
    req = requests.get(url="https://api.agify.io", params=params)
    res = req.json()
    cur_age = res["age"]
    return render_template("index.html", name=char, gender=gend, age=cur_age)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
