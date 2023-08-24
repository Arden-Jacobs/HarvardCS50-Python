# nutrition.py - Display the calories of a selected fruit

# Prompt user for a fruit
fruit = input("Enter a fruit: ").lower()

# Dictionary of fruits and their respective calorie counts
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grape": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# Display the calories of the selected fruit
if fruit in fruits:
    print("Calories: {}".format(fruits[fruit]))



# Explanation:
# This code prompts the user to enter a fruit and then displays the calorie count of that fruit. The program
# uses a dictionary called fruits to store the names of fruits as keys and their respective calorie counts
# as values.

# It prompts the user for a fruit name and converts it to lowercase for case-insensitive comparison. Then, it
# checks if the entered fruit exists in the fruits dictionary. If the fruit is found, the program
# prints "Calories: " followed by the corresponding calorie count. If the fruit is not found in
# the dictionary, it prints nothing
