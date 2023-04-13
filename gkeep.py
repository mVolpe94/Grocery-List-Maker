import datetime as dt
import gkeepapi
import json
import jsonpickle


#Send the list of ingredients
#Set up keep object and login using master key stored in auth.json
#Iterate over ingredient data
#Add colaborators
#Fine

def get_auth(file="auth.json"):
  '''
    This method grabs auth data from external json file
  '''
  with open(file) as jsn:
    json_str = jsn.read()
    data = jsonpickle.unpickler.decode(json_str)

  if data["master"] != None:
    auth = {"user": data["user"], "pass": data["master"]}
  else:
    auth = {"user": data["user"], "pass": data["pass"]}
    
  return auth


def send(ingt_obj_list):
  auth = get_auth()

  date = dt.datetime.now().strftime("%m-%d-%Y")
  title = f"Grocery List: {date}"




  keep = gkeepapi.Keep()
  keep.login(auth["user"], auth["pass"])

  note = keep.createList(title, )


def ingt_keep_list(ingt_obj_list):
  for ingredient in ingt_obj_list:
    title = ingredient


if __name__ == "__main__":
  get_auth()