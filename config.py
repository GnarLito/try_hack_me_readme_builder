template = {
  "room": """
# {room_name}
[Room](https://www.tryhackme.com/room/{room_name})
{tasks}
""",

  "task": """
## {taskNo}. {taskTitle}{questions}
""",

  "question": """
  {questionNo}. **{question}**
  > `{submission} `
""",
  "no_answer": "{answerDesc}",
  "placeholder": "{answerDesc}",
}

config = {
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
    , 'thead'   , '/thead'
    , 'table'   , '/table'
    , 'td'      , '/td'
    , 'th'      , '/th'
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