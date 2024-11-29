from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/man')
def man():
    return render_template('man.html')

@app.route('/woman')
def woman():
    return render_template('woman.html')

if __name__ == '__main__':
    app.run(debug=True)
