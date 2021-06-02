from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Flask!"

@app.route('/test', methods=['POST'])
def predict():
    file = request.files['image'].read()
    requestToImage = RequestToImage(file)
    img = requestToImage.result()


    # return send_file(filename, mimetype='image/gif')
    return predict()

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port='5000')