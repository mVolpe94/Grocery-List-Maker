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


def get_collab(file="collab.json"):
  '''
    This method grabs collaborator data from external json file
  '''
  with open(file) as collab:
    json_str = collab.read()
    return jsonpickle.unpickler.decode(json_str)
  

def send(ingt_obj_list):
  '''
    This method gathers all necessary data for send to google keep and sends it
    via the sync call
      ingt_obj_list: List of ingredient objects from current state
  '''
  try:
    #Get creds and collabs
    auth = get_auth()
    collab = get_collab()

    #Set title text
    date = dt.datetime.now().strftime("%m-%d-%Y")
    title = f"Grocery List: {date}"

    #Set up ingredient list for send
    ingredient_list = ingt_keep_list(ingt_obj_list)

    #Set up Keep object
    keep = gkeepapi.Keep()
    keep.login(auth["user"], auth["pass"])

    #Create Keep List and collabs
    glist = keep.createList(title, ingredient_list)
    glist.collaborators.add(collab["email1"])
    glist.collaborators.add(collab["email2"])

    #Send to Google Keep
    keep.sync()
    return True
  
  except Exception as e:
    cur_time = dt.datetime.now().strftime("%m-%d-%y %H:%M:%S")
    with open("error.log", 'a') as log:
      log.write(f"[Error: {cur_time}] \n")
      log.write(str(e) + "\n")
      log.write("\n")
      log.close()
    return False



def ingt_keep_list(ingt_obj_list):
  ingt_str_list = []
  for ingredient in ingt_obj_list:
    title = ingredient.tostring()
    ingt_str_list.append((title, False))
  return ingt_str_list

if __name__ == "__main__":
  get_auth()