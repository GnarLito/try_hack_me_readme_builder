#!/usr/bin/env python3

import getopt
import sys

from room_tasks import room_task
from thm_api.thmapi import THM


def main(room_name, out_file=None, creds=None, skip_answers=False):
  thm_session = THM()

  if creds.__len__() > 0:
    thm_session.login(creds)
    pass
  
  room = room_task(thm_session, room_name, skip_answers)
  room.write_room(out_file)

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
