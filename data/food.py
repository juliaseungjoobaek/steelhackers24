import json

class Food:
    def __init__(self):
        self.total_Calories = 0
        self.total_Protein = 0
        self.total_Carbohydrates = 0
        self.total_Sugar = 0
        self.total_Fat = 0
        self.total_DietaryFiber = 0
        self.total_Sodium = 0

    def load_nutrition_info(self):
        with open('/home/yoojin.baek/steelhackers/data/nutrition.json', 'r') as file:
            nutrition = json.load(file)

        keep_choosing = True

        while keep_choosing:
            restaurant = input("Which restaurant did you visit? ")
            food = input("What food item did you get? ")

            # Access the nutrition information
            if restaurant in nutrition and food in nutrition[restaurant]:
                food_nutrition = nutrition[restaurant][food]

                self.total_Calories += food_nutrition['Calories']
                self.total_Protein += food_nutrition['Protein']
                self.total_Carbohydrates += food_nutrition['Carbohydrates']
                self.total_Sugar += food_nutrition['Sugar']
                self.total_Fat += food_nutrition['Fat']
                self.total_DietaryFiber += food_nutrition['Dietary Fiber']
                self.total_Sodium += food_nutrition['Sodium']
            else:
                print(f"Nutrition information for {food} at {restaurant} not found.")

            done_or_not = input("Enter 'yes' if you are done choosing or 'no' if you still want to add food to your cart: ")
            if done_or_not.lower() == "yes":
                keep_choosing = False

        # Print total nutrition information
        print("Total calories served:", self.total_Calories, "(cal)")
        print("Total protein served:", self.total_Protein, "(g)")
        print("Total carbohydrates served:", self.total_Carbohydrates, "(g)")
        print("Total sugar served:", self.total_Sugar, "(g)")
        print("Total fat served:", self.total_Fat, "(g)")
        print("Total dietary fiber served:", self.total_DietaryFiber, "(g)")
        print("Total sodium served:", self.total_Sodium, "(mg)")

    def get_nutrition_info(self):
        # Return the total nutrition information as a dictionary
        return {
            "Calories": self.total_Calories,
            "Protein": self.total_Protein,
            "Carbohydrates": self.total_Carbohydrates,
            "Sugar": self.total_Sugar,
            "Fat": self.total_Fat,
            "Dietary Fiber": self.total_DietaryFiber,
            "Sodium": self.total_Sodium
        }

if __name__ == "__main__":
    food = Food()
    food.load_nutrition_info()
    nutrition_info = food.get_nutrition_info()
    print("Final Nutrition Info:", nutrition_info)
