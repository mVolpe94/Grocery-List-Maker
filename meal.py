import inflect

class Meal:
  def __init__(self, title, ingredients, sheet, amount = 1):
    self.title = title
    self.sheet = sheet
    self.ingredients = ingredients
    self.amount = amount

  def __eq__(self, other):
    return self.title == other.title

  def get_match_list(self):
    p = inflect.engine()
    match_list = []
    for ingredient in self.ingredients:
      singular = p.singular_noun(ingredient)
      if singular != False:
        singular_lower = singular.lower()
        match_list.append(singular_lower)
      else:
        match_list.append(ingredient.lower())
    return match_list