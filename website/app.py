from flask import Flask, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    dish = request.form.get('dish')
    print(f"Dish received in app.py: {dish}")
    
    result = subprocess.run(['python3', '/home/yoojin.baek/steelhackers/src/main.py', dish], capture_output=True, text=True)
    
    output = result.stdout
    
    return f"Dish received and processed by main.py: {output}"

if __name__ == '__main__':
    app.run(debug=True)
