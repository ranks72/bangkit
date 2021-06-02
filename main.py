from flask import Flask, request
from Predict import ProccessText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Flask!"

@app.route('/test', methods=['POST'])
def predict():
    args = request.args.get("kalimat")
    text = ProccessText(args)






    return text.result()

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port='5000')