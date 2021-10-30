
"""
EXAMPLE:
### room
[room](https://www.tryhackme.com/room/room)


# 1. task 1
  1. **question 1**
  > Not needed.
  
  2. **question 2**
  > my answer

# 2. task 2
  1. **question 1**
  > my answer
  
  2. **question 2**
  > my answer

"""
template = {
  "global": """
### {room_name}
[Room](https://www.tryhackme.com/room/{room_name})
{task}
""",

  "task": """
# {taskNo}. {taskTitle}{question}
""",

  "question": """
  {questionNo}. **{question}**
  > {submission}
"""
}

config = {
  "no_answer": "Non needed.",
  "REPLACE_TAGS": [
    ['&amp;', ''],
    ['&lt;', '<'],
    ['&gt;', '>'],
    ['<code>', '`'],
    ['</code>', '`'],
    ['\n`', '`']
  ],
  "HTML_TAGS": [
    'span'      , '/span'
    , 'p'       , '/p'
    , 'a'       , '/a'
    , 'em'      , '/em'
    , 'b'       , '/b'
    , 'strong'  , '/strong'
    , 'div'     , '/div'
    , 'tbody'   , '/tbody'
    , 'table'   , '/table'
    , 'td'      , '/td'
    , 'tr'      , '/tr'
    , 'br'      , 'img'
  ],
  "auth_only": [
    "submission"
    , "correct"
    , "extraPoints"
    , "attempts"
    , "noAnswer"
    , "answerDesc"
  ]
}