#!/usr/bin/env python3

import sys, getopt, os, re
from thm_api.thmapi import THM
import config


def main(room, out_file=None, creds=None, skip_answers=False):
  thm_session = THM()

  if creds.__len__() > 0:
    thm_session.login(creds)
    pass
  
  room_data = get_THM_room(thm_session, room)
  
  if room_data.__len__() < 1:
    print(f"Room: {room} is empty")
    return 1;

  write(room, thm_session, room_data, out_file, skip_answers)

def get_THM_room(thm_session, room_name):
  room_tasks = thm_session.room_tasks(room_name)

  # * taskinfo move
  if thm_session.authenticated:
    for task in room_tasks:
      task['questions'] = task['tasksInfo']
      del task['tasksInfo']
    # * submission
      for quest in task['questions']:
        if quest['noAnswer'] and quest['correct']:
          quest['submission'] = config.config['no_answer']
        elif not quest['correct']:
          quest['submission'] = quest[config.config['placeholder']]
  
  return room_tasks

def write(room_name, thm_session, room_data, out_file, skip_answers):
  global_data = {
    "room_name": room_name,
    "authed": str(thm_session.authenticated)
  }
  outdata = config.template['global']
  for global_i in re.findall(r"{(.*?)}",outdata):
      
    if global_i == 'task':
      outdata = outdata.replace("{task}", "")
      for task in room_data:
        outTask = config.template['task']
        for task_i in re.findall(r"{(.*?)}",outTask):
          
          if task_i == 'question':
            outTask = outTask.replace("{question}", "")
            for question in task['questions']:
              outQuest = config.template['question']
              
              if skip_answers: 
                outQuest = outQuest.replace("{submission}", "")
              elif not thm_session.authenticated: 
                for item in config.config['auth_only']: 
                  outQuest = outQuest.replace("{"+item+"}", "")
              
              for quest_i in re.findall(r"{(.*?)}",outQuest):
                if quest_i not in question:
                  print(f"unknown template `{quest_i}` in question. stopping...")
                  exit(1)
                else:
                  outQuest = outQuest.replace("{"+quest_i+"}", deHTML(str(question[quest_i])).strip())
              outTask += outQuest
          
          elif task_i not in task:
            print(f"unknown template `{task_i}` in task. stopping...")
            exit(1)
          
          else:
            outTask = outTask.replace("{"+task_i+"}", deHTML(str(task[task_i]), "_"))
        outdata += outTask
    
    elif global_i not in global_data:
      print(f"unknown template `{global_i}` in global. stopping...")
      exit(1)
    
    else:
      outdata = outdata.replace("{"+global_i+"}", str(global_data[global_i]))
      outdata = object_fill(global_data, global_i, outdata)
  
  
  if out_file is None:
    out_file = f"./README.md"
  if out_file.endswith("/") or out_file.endswith("\\"):
    out_file += "README.md"
  elif not out_file.endswith(".md"):
    out_file += ".md"
    
  if '/' in out_file or '\\' in out_file:
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
  
  with open(f"{out_file}", "w") as out:
    out.write(outdata)
  print(f"Output written to {out_file}")

def deHTML(in_put, replace=''):
  # in_put = re.sub(r"\n", '', in_put);
  for t in config.config['HTML_TAGS']:
    in_put = re.sub(r"<"+ t +"[^<]*>", replace, in_put);
  for t in config.config['REPLACE_TAGS']:
    in_put = re.sub(t[0], t[1], in_put);
  return in_put

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
