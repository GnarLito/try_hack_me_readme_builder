# Config.py
config.py lets u customize your markdown file.
Below u will find the options u can set.
To use an option encapsulate it between `{}`

## TEMPLATE OPTIONS:

### GLOBAL:
```ini
room_name = the name of the room
authed    = true if signed in (session)
task      = sets where tasks get printed
```
### TASKS:
```ini
taskTitle   = Name of the task
taskType    = type of the task (VM, downloadable, none)
taskNo      = task number
taskCreated = creation time of the task (Ex. "2019-08-01T17:02:09.503Z")
uploadId    = Id for downloads/starting VM
question    = sets where questions get printed
```
### QUESTIONS:
```ini
question    = Question name
questionNo  = Question number
```
>When signed in (session) can u access the following:
```ini
hint        = question hint
correct     = only true when correct answer given
extraPoints = yea no clue..
attempts    = attempts before the answer was correct
submission  = the answer given
noAnswer    = true if no answer needed for the question
answerDesc  = placeholder text in answer textarea
```

___
## CONFIG OPTIONS:
```ini
no_answer     = sets the text when `noAnwers` is true
placeholder   = sets the anwser field to this while not filled
REPLACE_TAGS  = list set for replacing HTML codes
HTML_TAGS     = list set for removing HTML tags
auth_only     = set of options inaccessable when not signed in (session)
```