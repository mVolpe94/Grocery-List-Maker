import excel_reader as er
import meal

class State:
  def __init__(self):
    self.CONTROL = ["start", "meal_cat", "meal_select", "add_more", "remove", "send", "fin"]
    self.next = self.CONTROL[0]
    self.SHEETS = er.get_sheet_names()
    self.running = True
    
    self.inp = ""
    self.meal_sheet = ""
    self.meal_selections = []

    self.meal_obj_list = []

  def add_meal(self, title, sheet):
    meal_obj = self.create_meal_obj(title, sheet)

    is_repeat = False
    for obj in self.meal_obj_list:
      if meal_obj == obj:
        obj.amount += 1
        is_repeat = True
    
    if is_repeat == False:
      self.meal_obj_list.append(meal_obj)
        

  def create_meal_obj(self, title, sheet):
    ingredients = er.get_col_data(title, sheet)
    meal_obj = meal.Meal(title, ingredients, sheet)

    return meal_obj
  

  def remove_meal(self, index):
    if index < len(self.meal_obj_list):
      obj = self.meal_obj_list[index]
      if obj.amount > 1:
        obj.amount -= 1
      else:
        self.meal_obj_list.remove(obj)