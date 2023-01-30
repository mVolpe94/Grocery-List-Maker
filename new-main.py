# This code will generate a list of groceries based on user 
# selected meals found in excel database and save it to a file.

import ingredient
import excel_reader as er
import state
import meal
import utility as old_utl
import new_utility as utl
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

os.system("cls")

s = state.State()

while s.running:

  utl.splash_message()
  print()
  utl.display_cur_choices(s.meal_obj_list, s.SHEETS)

  match s.control.index(s.next):
    case 0:
      print(f"{Fore.LIGHTYELLOW_EX}Welcome to Kate's Grocery List Maker!{Style.RESET_ALL}")
      print()
      s.next = s.control[1]
    case 1:
      utl.display_meal_cat_menu(s.SHEETS)
    case 2:
      ...
    case 3:
      ...
    case 4:
      ...
    case 5:
      ...
    case 6:
      ...
  
  
  #Display current meal choices
  utl.display_cur_choices(s.meal_obj_list)

  #Meal category menu


