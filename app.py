from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello My First Flask Project, Phisan Sookkhee"


@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body['queryResult']['queryText'])
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
