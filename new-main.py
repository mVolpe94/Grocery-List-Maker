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
is_correct = True
error_message = None

while s.running:

  utl.splash_message()
  print()

  if s.next == s.control[0]:
    print(f"{Fore.LIGHTYELLOW_EX}Welcome to Kate's Grocery List Maker!{Style.RESET_ALL}")
    print()
    s.next = s.control[1]
  else:
    utl.display_cur_choices(s.meal_obj_list, s.SHEETS)

  frame = s.control.index(s.next)
  match frame:
    #Meal Category Frame
    case 1:
      utl.display_meal_cat_menu(s.SHEETS)
      if not is_correct:
        print(f"{Fore.RED}ERROR: Selection out of range, please try again.{Style.RESET_ALL}")

      s.inp = input("Selection: ")
      is_correct = utl.input_int_check(s.inp, s.SHEETS)

      if is_correct:
        s.meal_sheet = s.SHEETS[int(s.inp) - 1]
        s.next = s.control[1]
    #Meal Selection Frame
    case 2:
      ...
    #Add More? Frame
    case 3:
      ...
    #Remove Selections Frame
    case 4:
      ...
    #Send? Frame
    case 5:
      ...
  
  
  if s.inp.lower() == "r":
    s.next = s.control[4]
  


  #Display current meal choices
  # utl.display_cur_choices(s.meal_obj_list)

  #Meal category menu


