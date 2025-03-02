from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic for user registration
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/account', methods=['GET'])
def account():
    # Logic to display account information
    return render_template('daoai.html')

@app.route('/deposit', methods=['POST'])
def deposit():
    # Logic for handling deposits
    flash('Deposit successful!', 'success')
    return redirect(url_for('account'))

@app.route('/withdraw', methods=['POST'])
def withdraw():
    # Logic for handling withdrawals
    flash('Withdrawal successful!', 'success')
    return redirect(url_for('account'))

@app.route('/')

def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
