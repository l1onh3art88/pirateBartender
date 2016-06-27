#Bartender asks for users' preference in their drink and then creates one 
#usings ingredients based on their preference. Bartender will continue to serve
#until users no longer want another drink


import sys
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

preferences = {}
def survey():
    """Asks users how they prefer their drinks"""
    print("This functions name is {}\n".format(survey.__name__))
    for question in questions:
        if input(questions.get(question) + "\n") in ['y', 'yes']:
            preferences[question] = True
        else:
            preferences[question] = False
       
def drinkBuilder(preferences):
    """Builds a drink based on the user's preferences"""
    print("Your drink consists of: ")
    for ingredient in ingredients:
        if preferences[ingredient] == True:
            print(random.choice(ingredients.get(ingredient)))

if __name__ == '__main__':
    while input("Do you want a drink?\n") in ['y', 'yes']:    
        survey()
        drinkBuilder(preferences)
        
    