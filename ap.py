from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hi():
    return render_template('main.html')


@app.route('/reg', methods=['POST'])
def reg():
    if (request.form('Name') == ''):
        return 'Fail'
    return 'Registration will be here'


if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0', port=8080)

sum([1])