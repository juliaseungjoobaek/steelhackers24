from flask import Flask, request, redirect, url_for, render_template
import json

app = Flask(__name__)

# Load nutrition data
with open('nutrition.json', 'r') as file:
    nutrition = json.load(file)

total_Calories = total_Protein = total_Carbohydrates = total_Sugar = total_Fat = total_DietaryFiber = total_Sodium = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global total_Calories, total_Protein, total_Carbohydrates, total_Sugar, total_Fat, total_DietaryFiber, total_Sodium
    restaurant = request.form['place']
    food = request.form['dish']  # Assuming you have a default food item

    # Access the nutrition information
    what = nutrition[restaurant][food]
   
    total_Calories += what['Calories']
    total_Protein += what['Protein']
    total_Carbohydrates += what['Carbohydrates']
    total_Sugar += what['Sugar']
    total_Fat += what['Fat']
    total_DietaryFiber += what['Dietary Fiber']
    total_Sodium += what['Sodium']

    return redirect(url_for('result'))

@app.route('/result')
def result():
    global total_Calories, total_Protein, total_Carbohydrates, total_Sugar, total_Fat, total_DietaryFiber, total_Sodium
    return (f"Total calories served: {total_Calories} (cal)<br>"
            f"Total protein served: {total_Protein} (g)<br>"
            f"Total carbohydrates served: {total_Carbohydrates} (g)<br>"
            f"Total sugar served: {total_Sugar} (g)<br>"
            f"Total fat served: {total_Fat} (g)<br>"
            f"Total dietary fiber served: {total_DietaryFiber} (g)<br>"
            f"Total sodium served: {total_Sodium} (mg)")

if __name__ == '__main__':
    app.run(debug=True)


