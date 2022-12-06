from flask import Flask, render_template, request
from sort import MainSort


app = Flask(__name__, template_folder="./templates")


@app.route('/')
def render():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def input_data():
    if request.method == 'POST':
        data = request.form['input_name']
        main_sort = MainSort(str(data))
        sort_d = main_sort.sort_data(20, 5)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
