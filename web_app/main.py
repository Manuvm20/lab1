from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Note: Use a colon (:) after the function name, not a semicolon (;)
    return render_template('index.html', file="home page")

if __name__ == '__main__':
    # 'True' must be capitalized in Python
    app.run(host='127.0.0.1', port=8080, debug=True)
