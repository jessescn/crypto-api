from flask import Flask
from crypto.routes.coins import datasets

app = Flask(__name__)
app.register_blueprint(datasets)

@app.route('/')
def api_status():
    """Method that returns an message if the API is running"""
    return 'API is on and running!', 200

if __name__ == '__main__':
    app.run(debug=True)
