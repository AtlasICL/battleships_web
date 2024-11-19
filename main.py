from flask import Flask

app = Flask(__name__)

@app.route('/ExampleRoute', methods=['GET', 'POST'])
def some_function():
    return "some_function1"

@app.route('/ExampleRoute2', methods=['GET'])
def some_function2():
    return "some_function2"

@app.route('/ExampleRoute3', methods=['GET'])
def some_function3():
    return "some_function3"


if __name__ == "__main__":
    app.run()


