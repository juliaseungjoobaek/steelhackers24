import json

restaurant = input("Which resturant do you went?")
food = input("What did you get?")
total_Calories = total_Protein = total_Carbohydrates = total_Sugar = total_Fat = total_DietaryFiber = total_Sodium = 0

keep_choosing = True
done_or_not = ""

# open and read the nutrition.json file
with open('nutrition.json', 'r') as file:
    nutrition = json.load(file)

# access the key
while(keep_choosing == True):
    where = nutrition[restaurant]
    what = nutrition[restaurant][food]
    total_Calories += nutrition[restaurant][food]['Calories']
    total_Protein += nutrition[restaurant][food]['Protein']
    total_Carbohydrates += nutrition[restaurant][food]['Carbohydrates']
    total_Sugar += nutrition[restaurant][food]['Sugar']
    total_Fat += nutrition[restaurant][food]['Fat']
    total_DietaryFiber += nutrition[restaurant][food]['Dietary Fiber']
    total_Sodium += nutrition[restaurant][food]['Sodium']

    done_or_not = input("Enter 'yes' if you are done choosing or 'no' if you still want to add food to your cart:")
    if(done_or_not == "yes"):
        keep_choosing = False
    

print("Total calories served:", total_Calories)
print("Total protein served:", total_Protein)
print("Total carbohydrates served:", total_Carbohydrates)
print("Total sugar served:", total_Sugar)
print("Total fat served:", total_Fat)
print("Total dietary fiber served:", total_DietaryFiber)
print("Total sodium served:", total_Sodium)
