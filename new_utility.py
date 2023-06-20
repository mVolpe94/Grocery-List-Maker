import excel_reader as er
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def splash_message(path = "splash.txt"):
  '''
    Displays a .txt file at path onto the console.
  '''
  with open(path, "r") as splash:
    lines = splash.read().split('\n')
  for line in lines:
    print(line)


def display_meal_cat_menu(sheets):
  '''
    Takes list of excel sheet titles and displays meal categories
      sheets: A list of strings of the sheet names found in the excel file.
  '''
  print("Please select what category of meals by typing the number beside your choice")
  print()
  display_numbered_list(sheets)


def display_cur_choices(meal_obj_list, sheets):
  '''
    Takes all current meal choices made by the user and displays them in a tiered list.
      meal_obj_list: A list of Meal objects
      sheets: A list of strings of the sheet names found in the excel file.
  '''
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
    for sheet_name in sheets:
      if keys.count(sheet_name) > 0:
        print(f"{sheet_name}:")
        for meal_title in temp_selections[sheet_name]:
          print(f" - {meal_title}")
        print()


def display_meal_menu(sheet):
  '''
    Displays the list of meals found in the currently selected meal category.
      sheet: string containing the name of a meal category found in the excel file.
  '''
  meals = er.get_col_names(sheet)

  print("Please type the number of each meal you would like to add separated by a space")
  print()

  display_numbered_list(meals)

  return meals


def display_remove_menu(meal_obj_list):
  '''
    This displays the meal removal menu text.
      meal_obj_list: List containing Meal objects
  '''
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


def display_send_menu(ingt_obj_list):
  '''
    Displays the ingredient list with amounts to the user for final check before
    sending out to google keep.
      ingt_obj_list: List of ingredient objects
  '''
  print(f"{Fore.LIGHTGREEN_EX}Here are all the igredients for the meals you have selected:{Style.RESET_ALL}")
  print(f"{Fore.YELLOW}Enter 'r' to go back to the meal removal screen.{Style.RESET_ALL}")
  for ingt in ingt_obj_list:
    print(f" - {ingt.tostring()}")


def display_numbered_list(string_list):
  '''
    Displays a list of strings as those strings with numbers in sequence before them
      string_list: List of strings
  '''
  if isinstance(string_list, list):
    for num in range(len(string_list)):
      print(f"{num + 1}) {string_list[num]}")
    print()
  else:
    raise TypeError("List of strings object expected")


def display_help_screen():
  '''
    Displays the help screen, informs user on some keys they can always enter and what they do.
  '''
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
  '''
    This checks if inp is an integer, then checks if its value is between 0 and range.
      inp: user input integer to check
      range: What max range to check
  '''
  try:
    sel = int(inp)
  except:
    return False
  if sel > 0 and sel <= len(range):
    return True
  else:
    return False


def display_final_screen():
  '''
    Displays final screen text.
  '''
  print(f"{Fore.LIGHTGREEN_EX}Sent!")
  print()
  print(f"{Fore.YELLOW}Your grocery list was created and sent.")
  print(f"{Fore.MAGENTA}Have a great day!{Style.RESET_ALL}")
  print()
  print()