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

meal_obj_list = []
SHEETS = er.get_sheet_names()

running = True
control = "start"

while running:
  utl.splash_message()
  print() 
  if control == "start":
    print(f"{Fore.LIGHTYELLOW_EX}Welcome to Kate's Grocery List Maker!{Style.RESET_ALL}")
    print()
    control = "mea"
  
  #Display current meal choices
  utl.display_cur_choices(meal_obj_list)

  #Meal category menu
  if inp == 

