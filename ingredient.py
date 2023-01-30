import inflect

class Ingredient:
  def __init__(self, title, amount, unit = ""):
    p = inflect.engine()
    self.title = title
    self.match = str.lower(p.singular_noun(title))
    self.amount = int(amount)
    self.listentry = self.tostring()

  def tostring(self):
    return f"{self.amount} {self.title}"
