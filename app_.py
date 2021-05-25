from flask import Flask
from flask_restx import Resource, Api
from todo import Todo

app = Flask(__name__)
api = Api(
    app,
    version='0.1',
    title="orclord's API Server",
    description="orclord bitcoin API Server!",
    terms_url="/",
    contact="orclord82@gmail.com",
    license="MIT"
)

api.add_namespace(Todo, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)