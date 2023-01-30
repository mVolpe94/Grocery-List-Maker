import excel_reader as er

class State:
  def __init__(self):
    self.control = ["start", "meal_cat", "meal_select", "add_more", "remove", "send", "fin"]
    self.next = self.control[0]
    self.SHEETS = er.get_sheet_names()
    self.meal_cat = ""
    self.input_list = []
    self.running = True
    self.meal_obj_list = []