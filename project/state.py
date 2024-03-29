import excel_reader as er
import meal
import ingredient


#This class controls all the data for this app
class State:
  def __init__(self):
    self.CONTROL = ["start", "meal_cat", "meal_select", "add_more", "remove", "send", "help", "fin"]
    self.next = self.CONTROL[0]
    self.SHEETS = er.get_sheet_names()
    self.prev_frames = []
    self.running = True

    self.inp = ""
    self.meal_sheet = ""
    self.meal_selections = []

    self.ingt_obj_list = []
    self.meal_obj_list = []


  def add_meal(self, title, sheet):
    '''
      Adds meal to the meal_obj_list, ensures the amount attribute on the meal 
      object is updated to reflect any duplicates.
    '''
    meal_obj = self.create_meal_obj(title, sheet)

    is_repeat = False
    for obj in self.meal_obj_list:
      if meal_obj == obj:
        obj.amount += 1
        is_repeat = True

    if is_repeat == False:
      self.meal_obj_list.append(meal_obj)


  def create_meal_obj(self, title, sheet):
    '''
      Gathers data from excel sheet on a particular meal and 
      creates a meal object.
    '''
    ingredients = er.get_col_data(title, sheet)
    meal_obj = meal.Meal(title, ingredients, sheet)

    return meal_obj


  def fill_ingt_list(self):
    '''
      Fills ingredient list with ingredient objects based 
      on current state of the meal object list
    '''
    self.ingt_obj_list.clear()
    for meal in self.meal_obj_list:
      self.add_ingts(meal)


  def add_ingts(self, meal):
    '''
      Iterates over the ingredients list for the meal given, 
      takes in the amount of each meal and the amount of each ingredient
      and ensures the correct amount of each ingredient gets added to the 
      ingt_obj_list.
    '''
    for ingredient in meal.ingredients:
      ingt_split = ingredient.split(" ")
      title = ""
      amount = meal.amount
      if ingt_split[0].isdigit():
        amount = int(int(ingt_split[0]) * meal.amount)
        title = ""
        for index in range(len(ingt_split)):
          if index > 0:
            title += ingt_split[index] + " "
        title = title.strip()
      else:
        for word in ingt_split:
          title += word + " "
        title = title.strip()

      ingredient = self.create_ingt_obj(title, amount)

      is_ingt_exist = self.check_ingt_exists(ingredient)
      if not is_ingt_exist:
        self.ingt_obj_list.append(ingredient)


  def create_ingt_obj(self, title, amount=1):
    '''
      Handles creating the actual ingredient object to be added to
      ingt_obj_list
    '''
    ingt = ingredient.Ingredient(title, amount)
    return ingt


  def check_ingt_exists(self, ingredient):
    for ingt_index in range(len(self.ingt_obj_list)):
      if self.ingt_obj_list[ingt_index] == ingredient:
        self.ingt_obj_list[ingt_index].amount += ingredient.amount
        return True
    return False


  def remove_meal(self, index):
    '''
      Removes a meal from the meal_obj_list based on index.
      Used only when user wants to take a meal off the list.
    '''
    if index < len(self.meal_obj_list):
      obj = self.meal_obj_list[index]
      if obj.amount > 1:
        obj.amount -= 1
      else:
        self.meal_obj_list.remove(obj)
