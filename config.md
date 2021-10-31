# Config.py
config.py lets u customize your markdown file.
Below u will find the options u can set.
To use an option encapsulate the option between `{}`

the template options are backwards usable, 
meaning in the questions template are tasks and global options available to use
and from the tasks template are the global template options.

More room options will be on the way.
## TEMPLATE OPTIONS:

### ROOM:
```ini
room_name       = the name of the room
authenticated   = true if signed in (session)
tasks_count     = the number of tasks in room
tasks           = sets where tasks get printed
```
### TASKS:
```ini
taskTitle       = Name of the task
taskType        = type of the task (VM, downloadable, none)
taskNo          = task number
taskCreated     = creation time of the task (Ex. "2019-08-01T17:02:09.503Z")
uploadId        = Id for downloads/starting VM
questions_count = the number of questions in the task
questions       = sets where questions get printed
```
### QUESTIONS:
```ini
question        = Question name
questionNo      = Question number
```
>When signed in (session) can u access the following:
```ini
hint            = question hint
correct         = only true when correct answer given
extraPoints     = amount of extra point given for this question
attempts        = attempts before the answer was correct
submission      = the answer given
noAnswer        = true if no answer needed for the question
answerDesc      = placeholder text in answer textarea
```
### miscellaneous
- `no_answer` and `placeholder` can use all template options above, to use them encapsulate the option between `{}`
```ini
no_answer       = sets the submission field when `noAnswers` is set
placeholder     = sets the submission field when `correct` is not set
```
___
## CONFIG OPTIONS:
```ini
REPLACE_TAGS    = list set for replacing HTML codes
HTML_TAGS       = list set for removing HTML tags
auth_only       = set of options inaccessable when not signed in (session)
```