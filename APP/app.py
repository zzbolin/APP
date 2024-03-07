from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Vercel with Python!'

if __name__ == '__main__':
    app.run(debug=True)
