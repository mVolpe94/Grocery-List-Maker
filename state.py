import excel_reader as er

class State:
  def __init__(self):
    self.control = ["start", "meal_cat", "meal_select", "add_more", "remove", "send", "fin"]
    self.next = self.control[0]
    self.SHEETS = er.get_sheet_names()
    self.running = True
    
    self.inp = ""
    self.meal_sheet = ""
    self.meal_selections = []

    self.meal_obj_list = []

