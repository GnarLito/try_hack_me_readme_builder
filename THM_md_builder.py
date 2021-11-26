#!/usr/bin/env python3

import getopt
import sys
import re
import tryhackme
from tryhackme.question import Question
from tryhackme.task import RoomTask

# TODO: use slots to get attributes instead of trying to hard code this
def get_attr(thm: tryhackme.Client, room: tryhackme.Room, task: tryhackme.RoomTask=None, question: tryhackme.Question=None):
    attr = {
      "room_name":       room.name
      , "authenticated": thm.authenticated
      , "task_count":    room.tasks.__len__()
      , "total_questions_count": room.question_count
      , "id": room.id
      , "description": room.description
      , "created": room.created
      , "type": room.type
      , "difficulty": room.difficulty
    }
    if task is not None:
      attr.update({
        "taskTitle": task.title
        , "taskDesc": task.description
        , "taskType": task.type
        , "taskNo": task.number
        , "taskCreated": task.created
        , "uploadId": task.uploadId
        , "question_count": task.question_count
      })
    
    if question is not None:
      attr.update({
        "question": question.question
        , "hint": question.hint
        , "questionNo": question.number
        , "questionDesc": question.description
        , "extraPoints": question.extra_points
        , "submission": question.submission
        , "noAnswer": not question.has_answer
        , "correct": question.correct
        , "attemps": question.attempts
      })
    return attr

  
def replace_attr(self, rstring: str, pattrn: str, attrs:dict):
  for tag in re.findall(pattrn, rstring):
    if tag not in attrs: continue
    rstring = rstring.replace("{"+tag+"}", str(attrs[tag]))
  return rstring

def main(room_name, out_file=None, session=None, skip_answers=False):
  thm = tryhackme.Client()

  thm.login(session)
  room = thm.get_room(room_name)
  
  




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
