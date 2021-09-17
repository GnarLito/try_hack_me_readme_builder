#!/usr/bin/env python3

import requests
import json
import sys, getopt
from thmapi import THM
from html_to_text import *


def main(room, out_file=None, creds=None):
  thm = THM()
  thm.login(creds)
  if creds.__len__() > 1:
    pass
  print(thm.session.cookies)
  room_data = thm.room_tasks(room)
  
  if room_data.__len__() < 1:
    print(f"Room: {room} is empty")
    return 1;
  
  room_data = format_data(room_data)
  Write_tasks(room, room_data, out_file)


def Write_tasks(name, room_data, out_file):
  out_string = "# "+ name;
  for task in room_data:
    # add TASK
    out_string += f"# {task['taskTitle']}\n"
    for quest in task['questions']:
      # add QUESTIONS
      out_string += f"{quest['questionNo']}. **{quest['question']}**\n\n"
      out_string += " > "
      # if answer exist write it
      if task['tasksInfo'].__len__() > 1 and task['tasksInfo'][int(quest['questionNo'])-1]['correct']:
      
        if not task['tasksInfo'][int(quest['questionNo'])-1]['noAnswer']:
          out_string += f"{task['tasksInfo'][int(quest['questionNo'])-1]['submission'].strip()}\n"
        else: 
          out_string += "None needed.\n"
      
      else:
        out_string += "\n"

      out_string += "\n"

  with open(f"{out_file}", "w") as out:
    out.write(out_string)
  print(f"file write done | in: {out_file}")



if __name__ == "__main__":
  room = None
  out_file = None
  cred = {};
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hr:o:u:p:s:",["help","ofile=","room=", "username=", "password=", "session="])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(f"{sys.argv[0]} -r <room> -o <outFile> [-c <cookie: connect.sid>]")
        exit(0)
      elif opt in ("-r", "--room"):
        room = arg
      elif opt in ("-o", "--ofile"):
        out_file = arg
      elif opt in ("-u","--username"):
        cred.update({"username": arg})
      elif opt in ("-p","--passowrd"):
            cred.update({"password": arg})
      elif opt in ("-s","--session"):
        cred.update({"session": arg})
      
  
  except getopt.GetoptError:
    print(f"{sys.argv[0]} -r <room> -o <outFile> [-c <cookie: connect.sid>]")
    sys.exit(2)

  if room is None:
    print("Room needs be supplied\nsee '-h'")
    exit(1)
  if out_file is None:
    print("Output file needs be supplied\nsee '-h'")
    exit(1)
  
  if   cred.__len__() > 1 and "session"  not in cred and "username" not in cred:
    print("Missing the Username.\nsee '-h'")
    exit(1)
  elif cred.__len__() > 1 and "session"  not in cred and "password" not in cred:
    print("Missing the Password.\nsee '-h'")
    exit(1)
  elif cred.__len__() > 1 and "username" not in cred and "session"  not in cred:
    print("missing the Session.\nsee '-h'")
    exit(1)
  
  main(room, out_file, cred)