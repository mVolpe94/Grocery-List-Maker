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



s = state.State()
is_correct = True
error_message = None

while s.running:
  os.system("cls")
  utl.splash_message()
  print()

  if s.next == s.CONTROL[0]:
    print(f"{Fore.LIGHTYELLOW_EX}Welcome to Kate's Grocery List Maker!{Style.RESET_ALL}")
    print()
    s.next = s.CONTROL[1]
  elif s.next != s.CONTROL[4]:
    utl.display_cur_choices(s.meal_obj_list, s.SHEETS)

  frame = s.CONTROL.index(s.next)
  
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
        s.next = s.CONTROL[2]

    #Meal Selection Frame
    case 2:
      meals = utl.display_meal_menu(s.meal_sheet)
      if not is_correct:
        print(f"{Fore.RED}ERROR: One or more selections were out of range, please try again.{Style.RESET_ALL}")
        print(f"{Fore.LIGHTRED_EX}Previous Attempt: {s.inp}{Style.RESET_ALL}")

      s.inp = input("Selection(s): ")
      inp_list = s.inp.split(" ")
      
      for inp in inp_list.copy():
        if inp == "":
          inp_list.remove(inp)
        else:
          check_buffer = utl.input_int_check(inp, meals)
          is_correct = True
          if check_buffer == False:
            is_correct = False
            break
      
      if is_correct:
        for inp in inp_list:
          s.add_meal(meals[int(inp) - 1], s.meal_sheet)
        s.next = s.CONTROL[3]

    #Add More? Frame
    case 3:
      if not is_correct:
        print(f"{Fore.RED}ERROR: Input not recognized, please press enter or type a 'y' or 'n' to proceed.{Style.RESET_ALL}")
      s.inp = input("Would you like to select more meals? (Y/n): ")

      if s.inp == "" or s.inp.lower() == "y":
        s.next = s.CONTROL[1]
      elif s.inp.lower() == "n":
        s.next = s.CONTROL[5]
      else:
        is_correct = False

    #Remove Selections Frame
    case 4:
      utl.display_remove_menu(s.meal_obj_list)
      if not is_correct:
        print(f"{Fore.RED}ERROR: One or more selections were out of range, please try again.{Style.RESET_ALL}")
        print(f"{Fore.LIGHTRED_EX}Previous Attempt: {s.inp}{Style.RESET_ALL}")

      s.inp = input("Selection(s): ")
      input_list = s.inp.split(" ")

      for inp in input_list.copy():
        if inp == "":
          input_list.remove("")
        else:
          check_buffer = utl.input_int_check(inp, s.meal_obj_list)
          is_correct = True
          if check_buffer == False:
            is_correct

      

    #Send? Frame
    case 5:
      ...
  
  
  if s.inp.lower() == "r":
    s.next = s.CONTROL[4]
    is_correct = True
  


  #Display current meal choices
  # utl.display_cur_choices(s.meal_obj_list)

  #Meal category menu


