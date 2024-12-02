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

@app.route('/cart')
def  cart():
    return render_template('cart.html')

@app.route('/order_summary')
def  order_summary():
    return render_template('order_summary.html')

if __name__ == '__main__':
    app.run(debug=True)
