from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hellos1111a sdsworld!!!!!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)