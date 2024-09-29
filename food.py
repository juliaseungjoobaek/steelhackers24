import json

# Attempt to read the nutrition data

with open('nutrition.json', 'r') as file:
    nutrition = json.load(file)

total_Calories = total_Protein = total_Carbohydrates = total_Sugar = total_Fat = total_DietaryFiber = total_Sodium = 0

keep_choosing = True

while keep_choosing:
    restaurant = input("Which restaurant did you went? ")
    food = input("What food item did you get? ")
    
    # Access the nutrition information
    what = nutrition[restaurant][food]
    
    total_Calories += what['Calories']
    total_Protein += what['Protein']
    total_Carbohydrates += what['Carbohydrates']
    total_Sugar += what['Sugar']
    total_Fat += what['Fat']
    total_DietaryFiber += what['Dietary Fiber']
    total_Sodium += what['Sodium']

    done_or_not = input("Enter 'yes' if you are done choosing or 'no' if you still want to add food to your cart: ")
    if done_or_not.lower() == "yes":
        keep_choosing = False

    
# Print total nutrition information
print("Total calories served:", total_Calories, "(cal)")
print("Total protein served:", total_Protein, "(g)")
print("Total carbohydrates served:", total_Carbohydrates, "(g)")
print("Total sugar served:", total_Sugar, "(g)")
print("Total fat served:", total_Fat, "(g)")
print("Total dietary fiber served:", total_DietaryFiber, "(g)")
print("Total sodium served:", total_Sodium, "(mg)")
