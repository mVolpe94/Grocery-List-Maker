import excel_reader as er
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def splash_message(path = "splash.txt"):
  '''Displays a .txt file at path onto the console.'''
  with open(path, "r") as splash:
    lines = splash.read().split('\n')
  for line in lines:
    print(line)


def display_meal_cat_menu(sheets):
  '''
    Takes list of excel sheet titles and displays meal categories
  '''
  print("Please select what category of meals by typing the number beside your choice")
  print()
  length = len(sheets)
  for num in range(length):
    print(f"{num + 1}) {sheets[num]}")
  print()


#Error where after selecting a different meal category and there is only one selection in a previous category
#the temp_selections dict ignores the previous choice in that categroy
def display_cur_choices(meal_obj_list, sheets):
  if len(meal_obj_list) > 0:
    print()
    print(f"{Fore.GREEN}Here are all of your selections so far:{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Enter 'r' to remove any current selections.{Style.RESET_ALL}")
    print()
    category = ""
    temp_selections = {}
    for meal_obj in meal_obj_list:
      amount = ""
      if meal_obj.amount > 1:
        amount = f" ({meal_obj.amount})"
      if category != meal_obj.sheet:
        category = meal_obj.sheet
        temp_selections[category] = []
      temp_selections[category].append(meal_obj.title + amount)

    keys = list(temp_selections.keys())
    print(meal_obj_list[0].title)
    print(temp_selections)
    for sheet_name in sheets:
      if keys.count(sheet_name) > 0:
        print(f"{sheet_name}:")
        for meal_title in temp_selections[sheet_name]:
          print(f" - {meal_title}")
        print()


def input_int_check(inp, range):
  try:
    sel = int(inp)
  except:
    return False
  if sel > 0 and sel <= len(range):
    return True
  else:
    return False