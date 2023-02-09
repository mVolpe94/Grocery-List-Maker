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
  
  display_numbered_list(sheets)


#Error where after selecting a different meal category and there is only one selection in a previous category
#the temp_selections dict ignores the previous choice in that categroy
def display_cur_choices(meal_obj_list, sheets):
  if len(meal_obj_list) > 0:
    print(f"{Fore.LIGHTGREEN_EX}Here are all of your selections so far:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Enter 'r' to remove any current selections.{Style.RESET_ALL}")
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


def display_meal_menu(sheet):
  meals = er.get_col_names(sheet)

  print("Please type the number of each meal you would like to add separated by a space")
  print()

  display_numbered_list(meals)

  return meals


def display_remove_menu(meal_obj_list):
  print(f"{Fore.YELLOW}Select from the menu which meals you would like to remove:{Style.RESET_ALL}")
  print(f"{Fore.YELLOW}Enter 'e' to exit this menu{Style.RESET_ALL}")
  print()

  meal_obj_list_disp = []
  for obj in meal_obj_list:
    if obj.amount > 1:
      meal_obj_list_disp.append(f"{obj} ({obj.amount})")
    else:
      meal_obj_list_disp.append(obj)

  display_numbered_list(meal_obj_list_disp)


def display_numbered_list(string_list):
  if isinstance(string_list, list):
    for num in range(len(string_list)):
      print(f"{num + 1}) {string_list[num]}")
    print()
  else:
    raise TypeError("List object expected")


def display_help_screen():
  print(f"{Fore.YELLOW}Welcome to the Help Screen{Style.RESET_ALL}")
  print("Below is a list of commands and what they do:")
  print()
  print()
  print("- r - Brings up the meal removal screen")
  print()
  print("- b - Brings you back to the previous page")
  print()
  print("- h - Brings up the help screen")
  print()
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

