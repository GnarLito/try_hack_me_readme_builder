#!/usr/bin/env python3

import sys, getopt, os
from thm_api.thmapi import THM
from html_to_text import *


def main(room, out_file=None, creds=None, skip_answers=False):
  thm = THM()

  if creds.__len__() > 0:
    thm.login(creds)
    pass
  
  room_data = thm.room_tasks(room)
  
  if room_data.__len__() < 1:
    print(f"Room: {room} is empty")
    return 1;
  
  room_data = format_data(room_data)
  Write_tasks(room, room_data, out_file, skip_answers)


def Write_tasks(name, room_data, out_file, skip_answers):
  out_string = "# "+ name + "\n\n";
  for task in room_data:
    # add TASK
    out_string += f"# {task['taskTitle'].strip()}\n"
    for quest in task['questions']:
      # add QUESTIONS
      out_string += f"{quest['questionNo']}. **{quest['question'].strip()}**\n\n"
      out_string += " > "
      # if answer exist write it
      if not skip_answers and task['tasksInfo'].__len__() > 1 and task['tasksInfo'][int(quest['questionNo'])-1]['correct']:
      
        if not task['tasksInfo'][int(quest['questionNo'])-1]['noAnswer']:
          out_string += f"{task['tasksInfo'][int(quest['questionNo'])-1]['submission'].strip()}\n"
        else: 
          out_string += "None needed.\n"
      
      else:
        out_string += "\n"

      out_string += "\n"

  if out_file is None:
    out_file = f"./README.md"
  if out_file.endswith("/") or out_file.endswith("\\"):
    out_file += "README.md"
  elif not out_file.endswith(".md"):
    out_file += ".md"

  os.makedirs(os.path.dirname(out_file), exist_ok=True)
  with open(f"{out_file}", "w") as out:
    out.write(out_string)
  print(f"Output written to {out_file}")



if __name__ == "__main__":
  room = None
  out_file = None
  cred = {}
  skip_answers = False
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hr:o:u:p:s:a",["help","ofile=","room=", "username=", "password=", "session=", "no_answers"])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(f"{sys.argv[0]} -r <room> -o <outFile> [-s <session: connect.sid> [-a (dont fill answers)]]")
        exit(0)
      elif opt in ("-r", "--room"):
        room = arg
      elif opt in ("-o", "--ofile"):
        out_file = arg
      elif opt in ("-u","--username"):
        print("User accout doesn't yet work :(\nUse session instead")
        exit(1)
        cred.update({"username": arg})
      elif opt in ("-p","--passowrd"):
        print("User accout doesn't yet work :(\nUse session instead")
        exit(1)
        cred.update({"password": arg})
      elif opt in ("-s","--session"):
        cred.update({"session": arg})
      
      elif opt in ("-a","--no_answer"):
        skip_answers = True
      
  
  except getopt.GetoptError:
    print(f"{sys.argv[0]} -r <room> -o <outFile> [-s <session: connect.sid> [-a (dont fill answers)]]")
    sys.exit(2)

  if room is None:
    print("Room needs be supplied\nsee '-h'")
    exit(1)
  
  if   cred.__len__() > 0 and "session"  not in cred and "username" not in cred:
    print("Missing the Username.\nsee '-h'")
    exit(1)
  elif cred.__len__() > 0 and "session"  not in cred and "password" not in cred:
    print("Missing the Password.\nsee '-h'")
    exit(1)
  elif cred.__len__() > 0 and "username" not in cred and "session"  not in cred:
    print("missing the Session.\nsee '-h'")
    exit(1)
  
  main(room, out_file, cred, skip_answers)