from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return "hello wolrd"

if __name__ == '__main__':
    app.run(debug=True)