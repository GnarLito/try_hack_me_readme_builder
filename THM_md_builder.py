#!/usr/bin/env python3

import requests
import json
import sys, getopt
from html_to_text import *

endpoint = "https://tryhackme.com"

def Get_room(room, cookie=None):

  r = requests.get(f"{endpoint}/api/tasks/{room}", cookies=cookie)
  if r.status_code != 200:
    print(f"{endpoint}/api/tasks/{room}\nGave status: {r.status_code}\nShuting down")
    return 1

  json_data = json.loads(r.text)

  if json_data['totalTasks'] < 1:
    print(f"No tasks found in room {room}")
    return 1

  for i in json_data['data']:
    i['taskDesc'] = deHTML(i['taskDesc'], '__')
    i['taskTitle'] = deHTML(i['taskTitle'], '__')
    for j in i['questions']:
      j['question'] = deHTML(j['question'])

  return json_data


def Write_tasks(name, room_data, out_file):
  out_string = "# "+ name;
  for task in room_data['data']:
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
  cookie = None
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hr:o:c:",["ofile=","room=", "cookie="])
    for opt, arg in opts:
      if opt == '-h':
        print(f"{sys.argv[0]} -r <room> -o <outFile> [-c <cookie: connect.sid>]")
        exit(0)
      elif opt in ("-r", "--room"):
        room = arg
      elif opt in ("-o", "--ofile"):
        out_file = arg
      elif opt in ("-c","--cookie"):
        cookie = json.loads('{"connect.sid": "'+arg+'"}')

  except getopt.GetoptError:
    print(f"{sys.argv[0]} -r <room> -o <outFile> [-c <cookie: connect.sid>]")
    sys.exit(2)

  if room is None:
    print("Room needs be supplied\nsee '-h'")
    exit(1)
  if out_file is None:
    print("Output file needs be supplied\nsee '-h'")
    exit(1)
  # get Task to readme.md file
  task_list = Get_room(room, cookie)
  if task_list == 1:
    exit(1)
  else:
    Write_tasks(room, task_list, out_file)
