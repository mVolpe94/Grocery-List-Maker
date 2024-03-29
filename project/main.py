'''
Thank you for using Kate's Grocery List Maker! Kate is my wife's name, this was made to help her meal plan 
for us you the week. Hope it can help you too!


This app assists the user in creating grocery lists and sends them to a Google Keep List for use when shopping.
It requires some setup to be useful to you. The most important is the excel file that the excel_reader.py will
pull all the meal data from. 


Directions to set up the excel file:

1) Each new sheet will be a new category of meals (Breakfast, Lunch, Dinner, Dessert, etc.)

2) The title of each meal should be in the A row, not column

3) The ingredients needed for each meal should be found underneath the meal title
  | Each ingredient can have an integer amount in front of it and this will be used to determine the amount of that ingredient. Units and floats are not supported at this time.

4) Place the file in the same directory as excel_reader.py



There are two json files that need to be set by the user so the grocery list gets sent to the correct 
gmail accounts.

The first file should be titled: "auth.json"

It should contain this json object with your own email and password:

{

  "user": "yourreallycoolemail@gmail.com",

  "pass": "yoursupersecurepassword",

  "master": null

}

I believe you can use environment variables for this to make it more secure, however, 
for my purposes this was enough, I think...



The second file is only there if you want to add any other users to the note so 
they can see the grocery list too.

It should be titled: "collab.json"

It should contain this json object with two added emails:

{

    "email1": "yoursupercoolemail@gmail.com",

    "email2": "yourSOssupercoolemail@gmail.com"

}
'''


import gkeep
import state
import utility as utl
import os
from colorama import Fore
from colorama import Style


#Setup Variables
s = state.State()
is_correct = True
response = True
error_message = None


#Main Loop
while s.running:
  os.system("cls")
  utl.splash_message()
  print()

  if s.next == s.CONTROL[0]:
    print(f"{Fore.LIGHTYELLOW_EX}Welcome to Kate's Grocery List Maker!{Style.RESET_ALL}")
    print()
    s.next = s.CONTROL[1]
  elif s.next != s.CONTROL[4]:
    if s.next != s.CONTROL[6]:
      utl.display_cur_choices(s.meal_obj_list, s.SHEETS)
  
  frame = s.CONTROL.index(s.next)
  
  s.prev_frames.append(frame)
  
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
      if s.inp.lower() == "e":
          s.next = s.CONTROL[3]

      input_list = s.inp.split(" ")

      for inp in input_list.copy():
        if inp == "":
          input_list.remove("")
        else:
          check_buffer = utl.input_int_check(inp, s.meal_obj_list)
          is_correct = True
          if check_buffer == False:
            is_correct = False
            break

      if is_correct:
        for inp in input_list:
          s.remove_meal(int(inp) - 1)
      else:
        if s.inp.lower() == "e":
          s.next = s.CONTROL[3]
          is_correct = True

    #Send? Frame
    case 5:
      s.fill_ingt_list()
      utl.display_send_menu(s.ingt_obj_list)
      if not is_correct:
        print(f"{Fore.RED}ERROR: Input not recognized, please press enter to send or type 'y' or 'n' to proceed. {Style.RESET_ALL}")
      elif not response:
        print(f"{Fore.RED}ERROR: Could not reach Google Keep service, check internet connection and try again.")
        print(f"If you see this message again after ensuring internet connection, check error.log for more info{Style.RESET_ALL}")
      s.inp = input("Send? (Y/n):")
      if s.inp == "" or s.inp.lower() == "y":
        is_correct = True
        response = gkeep.send(s.ingt_obj_list)
        if response:
          s.next = s.CONTROL[7]
      elif s.inp.lower() == "n":
        s.next = s.CONTROL[3]
        is_correct = True
      else:
        s.next = s.CONTROL[5]
        is_correct = False

    #Help Frame
    case 6:
      utl.display_help_screen()
      s.inp = input("Press enter to leave help screen: ")
      if s.inp.strip() == "":
        s.inp = "b"

    #Fin Frame
    case 7:
      utl.display_final_screen()
      s.inp = input("Press enter to exit")
      s.running = False
  

  #Input checks
  if s.inp.lower() == "r":
    s.next = s.CONTROL[4]
    is_correct = True
  elif s.inp.lower() == "h":
    s.next = s.CONTROL[6]
    is_correct = True
  elif s.inp.lower() == "b":
    if len(s.prev_frames) >= 2:
      prev_frame = s.prev_frames[len(s.prev_frames) - 2]
      s.next = s.CONTROL[prev_frame]
      s.prev_frames.pop()
      s.prev_frames.pop()
    else:
      s.next = s.CONTROL[1]
      s.prev_frames.pop()
    is_correct = True


if __name__ == "__main__":
  s.running = True