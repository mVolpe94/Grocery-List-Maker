'''
This contains all the methods to use gkeepapi to add notes to Google Keep

!!!
####YOU MUST SET UP TWO FILES IN THE SAME FOLDER AS THIS FILE####
!!!

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

In the code these two entries are referenced directly, however, with a bit of tinkering
it could be made to loop across many entries in this object.
'''


import datetime as dt
import gkeepapi
import json
import jsonpickle


def get_auth(file="auth.json"):
  '''
    This method grabs auth data from external json file
  '''
  try:
    with open(file) as jsn:
      json_str = jsn.read()
      data = jsonpickle.unpickler.decode(json_str)

    if data["master"] != None:
      auth = {"user": data["user"], "pass": data["master"]}
    else:
      auth = {"user": data["user"], "pass": data["pass"]}
      
    return auth
  except Exception as e:
    print(e)


def get_collab(file="collab.json"):
  '''
    This method grabs collaborator data from external json file
  '''
  try:
    with open(file) as collab:
      json_str = collab.read()
      return jsonpickle.unpickler.decode(json_str)
  except Exception as e:
    print(e)
  

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
