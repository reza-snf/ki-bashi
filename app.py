from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def main():
    '''
    main page
    '''
    payload = {'message': "OK!"}
    return jsonify(payload), 200

@app.route('/v1/process')
def process():
    pass

def send_sms():
    pass

def check_serial():
    pass


if __name__ == '__main__':
    app.run(debug=True)