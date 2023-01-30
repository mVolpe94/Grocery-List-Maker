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


def meal_cat_selector():
  '''Displays menu for selecting meal category. Returns user input if acceptable.'''
  sheets = er.get_sheet_names()
  
  while True:
    print("Please select what category of meals by typing the number beside your choice")
    length = len(sheets)
    for num in range(length):
      print(f"{num + 1}) {sheets[num]}")
    print()
    inp = input("Selection: ")

    if inp.lower() == "r":
      return inp

    if input_int_check(inp, sheets):
      os.system("cls")
      splash_message()
      return int(inp)
    else:
      os.system("cls")
      splash_message()
      print(f"{Fore.RED}ERROR: Selection out of range, please try again.{Style.RESET_ALL}")
      print()


def meal_selector(meal_cat_name):
  '''Displays all meals in the sheet titled meal_cat_name, returns user inputs as a list of strings.'''
  meals = er.get_col_names(meal_cat_name)

  while True:
    print()
    print("Please type the number of each meal you would like to add separated by a space")
    print()
    length = len(meals)
    for num in range(length):
      print(f"{num + 1}) {meals[num]}")
    print()

    inp = input("Selection(s): ")
    inp_list = inp.split(' ')
    all_set = True

    if inp.lower() == "r":
      return inp

    for num in inp_list:
      if input_int_check(num, meals) == False:
        all_set = False
        os.system("cls")
        splash_message()
        print(f"{Fore.RED}ERROR: One or more selections were out of range, please try again.{Style.RESET_ALL}")
        print()
        print(f"Previous attempt: {inp}")
    if all_set:
      os.system("cls")
      splash_message()
      return inp_list


def get_meal_names(inp_list, sheet):
  '''Takes user inp_list and returns the names of the meals in the selected sheet as a list of strings.'''
  meals = er.get_col_names(sheet)
  meal_names = []
  for num in inp_list:
    i = int(num) - 1
    meal_names.append(meals[i])
  return meal_names


def get_ingredients(meal_names, sheet):
  '''Takes list meal_names on a selected sheet and returns a dictionary of the name and a list of all the ingredients for each meal.'''
  all_ingredients = {}
  for meal in meal_names:
    ingredients = er.get_col_data(meal, sheet)
    all_ingredients[meal] = ingredients
  return all_ingredients

#Error where after selecting a different meal category and there is only one selection in a previous category
#the temp_selections dict ignores the previous choice in that categroy
def display_cur_choices(meal_obj_list):
  if len(meal_obj_list) > 0:
    print()
    print(f"{Fore.GREEN}Here are all of your selections so far:{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Enter 'r' to remove any current selections.{Style.RESET_ALL}")
    print()
    sheets = er.get_sheet_names()
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


def more_choices_menu(meal_obj_list):
  '''
    Takes in list of Meal objects, displays that list in the console organized by meal category. Asks if user would like to choose more.
    Returns true or false or 'r' to go to removal screen.
  '''
  display_cur_choices(meal_obj_list)
  is_error = False

  while True:
    if is_error == True:
      display_cur_choices(meal_obj_list)
      print(f"{Fore.RED}ERROR: Input not recognized, please press enter or type a 'y' or 'n' to proceed.{Style.RESET_ALL}")
      is_error = False
    inp = input("Would you like to select more meals? (Y/n): ")
    os.system("cls")
    splash_message()
    
    if inp == "" or inp.lower() == "y":
      return True
    elif inp.lower() == "n":
      return False
    elif inp.lower() == "r":
      return inp
    else:
      is_error = True


def remove_choices_menu(meal_obj_list):
  print()
  print(f"{Fore.YELLOW}Select from the menu which meals you would like to remove:{Style.RESET_ALL}")
  print()

  for i in range(len(meal_obj_list)):
    print(f" {i + 1}) {meal_obj_list[i].title}")
  print()

  inp = input("Selection(s): ")




def input_int_check(inp, range):
  try:
    sel = int(inp)
  except:
    return False
  if sel > 0 and sel <= len(range):
    return True
  else:
    return False
  


if __name__ == "__main__":
  sheets = er.get_sheet_names()
  print("[SPLASH TEST]")
  splash_message()
  print("[END SPLASH TEST]")

  print("[MEAL CAT SELECT TEST]")
  val = meal_cat_selector() - 1
  print(sheets[val])
  print("[END MEAL CAT SELECT TEST]")
  print("[MEAL SELECTOR TEST]")
  selects = meal_selector(sheets[val])
  print(selects)
  print("[END MEAL SELECTOR TEST]")
  print("[GET MEAL NAMES TEST]")
  meal_names = get_meal_names(selects, sheets[val])
  print(meal_names)
  print("[END GET MEAL NAMES TEST]")
  print("[GET INGREDIENTS TEST]")
  colname = ["Test Meal 1", "Test Meal 2 "]
  sheet = "Breakfast"
  ingr = get_ingredients(colname, sheet)
  print("[END GET INGREDIENTS TEST]")