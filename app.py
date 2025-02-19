from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, you are deploying Flask App at Vercel!"

if __name__ == "__main__":
    app.run(debug=True)

    
