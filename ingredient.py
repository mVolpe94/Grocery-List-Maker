import inflect

class Ingredient:
  def __init__(self, title, amount=1):
    p = inflect.engine()
    self.title = title
    self.match = str.lower(p.singular_noun(title))
    self.amount = int(amount)
    self.listentry = self.tostring()


  def __eq__(self, other):
    return self.match == other.match


  def tostring(self):
    return f"{self.amount} {self.title}"
