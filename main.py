# This code will generate a list of groceries based on user 
# selected meals found in excel database and save it to a file.

import ingredient
import excel_reader as er
import meal
import utility as utl
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

os.system("cls")
SHEETS = er.get_sheet_names()

meal_obj_list = []
running = True


utl.splash_message()

# try:
cycle_count = 0
while running:
  #Display Splash Screen on entry
  if cycle_count == 0:
    print()
    print(f"{Fore.LIGHTYELLOW_EX}Welcome to Kate's Grocery List Maker!{Style.RESET_ALL}")
    print()
  cycle_count += 1
  #Displays any current meal selections
  utl.display_cur_choices(meal_obj_list)

  #Gathers meal names for later comparison
  #May not need
  cur_meal_names = []
  for meals in meal_obj_list:
    cur_meal_names.append(meals.title)

  #Menu System
  meal_cat = utl.meal_cat_selector()
  if meal_cat == 'r':
    meal_obj_list = utl.remove_choices_menu(meal_obj_list)
    continue
  meal_cat_index = meal_cat - 1
  sheet = SHEETS[meal_cat_index]
  meals = utl.meal_selector(sheet)
  if meals == 'r':
    meal_obj_list = utl.remove_choices_menu(meal_obj_list)
    continue
  

  #Processing Menu Selections
  meal_names = utl.get_meal_names(meals, sheet)
  all_ingredients = utl.get_ingredients(meal_names, sheet)
  for key in all_ingredients.keys():
    meal_obj = meal.Meal(key, all_ingredients[key], sheet)
    is_repeat = meal_obj in meal_obj_list
    if is_repeat:
      for obj in meal_obj_list:
        if meal_obj == obj:
          obj.amount += 1
    else:
      meal_obj_list.append(meal_obj)

  #Add more or remove selections?
  add_more = utl.more_choices_menu(meal_obj_list)
  if add_more == "r":
    meal_obj_list = utl.remove_choices_menu(meal_obj_list)
    running = True
  else:
    running = add_more


# except:
#   print(f"{Fore.RED}AN ERROR OCCURED. RESTART APP.{Style.RESET_ALL}")
      
    
