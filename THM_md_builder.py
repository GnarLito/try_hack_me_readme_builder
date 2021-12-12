#!/usr/bin/env python3

import os
import getopt
import sys
import re
import tryhackme
import config

def get_attr(thm: tryhackme.Client, room: tryhackme.Room, task: tryhackme.RoomTask=None, question: tryhackme.Question=None):
    attr = {
      "room_name":       room.name
      , "authenticated": thm.authenticated
      , "task_count":    room.tasks.__len__()
    }
    for slot in list(filter(lambda a : not a.startswith("_"),list(tryhackme.Room.__slots__))):
      attr["room_" + slot] = getattr(room, slot)
    
    if task is not None:
      task_slots = ("question_count", )
      for slot in list(filter(lambda a : not a.startswith("_"),list(tryhackme.RoomTask.__slots__))):
        attr["task_" + slot] = getattr(task, slot)
      for task_slot in task_slots:
        attr["task_" + slot] = getattr(task, task_slot)
      
    if question is not None:
      for slot in list(filter(lambda a : not a.startswith("_"),list(tryhackme.Question.__slots__))):
        attr["question_" + slot] = getattr(question, slot)
    
    return attr

  
def replace_attr(rstring: str, pattrn: str, attrs:dict):
  for tag in re.findall(pattrn, rstring):
    if tag not in attrs: continue
    rstring = rstring.replace("{"+tag+"}", str(attrs[tag]))
  return rstring

def write_room(file_loc: str, write_string):
    if file_loc is None:                                  file_loc = f"./README.md"
    if file_loc.endswith("/") or file_loc.endswith("\\"): file_loc += "README.md"
    elif not file_loc.endswith(".md"):                    file_loc += ".md"
      
    if '/' in file_loc or '\\' in file_loc:
      try: os.makedirs(os.path.dirname(file_loc), exist_ok=True)
      except: 
        print("couldn't create directory..")
        return

    with open(f"{file_loc}", "w") as out:
      out.write(write_string)
    print(f"Output written to {file_loc}")

def main(room_name, out_file=None, session=None, skip_answers=False):
  thm = tryhackme.Client(session)

  room = thm.get_room(room_name)

  tasks_string = ""
  for task in room.tasks:
    
    task_attrs = get_attr(thm, room, task)
    questions_string = ""
    for question in task.questions:
      question_attr = get_attr(thm, room, question=question)
      question_attr.update(task_attrs)
      if not question.has_answer and question.correct:
        question.submission = replace_attr(config.template['no_answer'], r"{(.*?)}", question_attr)
      elif not question.correct:
        question.submission = replace_attr(config.template['placeholder'], r"{(.*?)}", question_attr)
    
      if skip_answers:
        questions_string += replace_attr(config.template["question"].replace("{question_submission}", ""), r"{(.*?)}", question_attr)
      else:
        questions_string += replace_attr(config.template["question"], r"{(.*?)}", question_attr)
    
    task_attrs.update({"questions": questions_string})
    tasks_string += replace_attr(config.template["task"], r"{(.*?)}", task_attrs)

  room_attrs = get_attr(thm, room)
  room_attrs.update({"tasks": tasks_string})
  out_string = replace_attr(config.template["room"], r"{(.*?)}", room_attrs)
  write_room(out_file, out_string)
  




if __name__ == "__main__":
  room = None
  out_file = None
  session = None
  skip_answers = False
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hr:o:s:a",["help","ofile=","room=", "session=", "no_answers"])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        print(f"{sys.argv[0]} -r <room> -o <outFile> [-s <session: connect.sid> [-a (dont fill answers)]]")
        exit(0)
      elif opt in ("-r", "--room"):
        room = arg
      elif opt in ("-o", "--ofile"):
        out_file = arg
      elif opt in ("-s","--session"):
        session = arg
      
      elif opt in ("-a","--no_answer"):
        skip_answers = True
      
  
  except getopt.GetoptError:
    print(f"{sys.argv[0]} -r <room> -o <outFile> [-s <session: connect.sid> [-a (dont fill answers)]]")
    sys.exit(2)

  if room is None:
    print("Room needs be supplied\nsee '-h'")
    exit(1)
  
  main(room, out_file, session, skip_answers)
