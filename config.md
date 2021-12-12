# Config.py
config.py lets u customize your markdown file.
Below u will find the options u can set.
To use an option encapsulate the option between `{}`

the template options are backwards usable, 
meaning in the questions template are tasks and global options available to use
and from the tasks template are the global template options available to use.

More room options will be on the way.
## TEMPLATE OPTIONS:

### ROOM:
```ini
room_name           = the name of the room
authenticated       = true if signed in (session)
room_id             = Room id
room_title          = title is the same as the name
room_description    = description of the room
room_created        = time of creation
room_published      = time of publishing
room_users          = number of users that have joined the room
room_type           = room type
room_public         = if the room is public 
room_difficulty     = room difficulty
room_freeToUse      = if the room is free to use
room_ctf            = if the room is a ctf
room_tags           = the room tags
room_ipType         = the ip type of the room
room_simpleRoom     = if the room is considerd simple
room_locked         = if the room is locked
room_comingSoon     = if the room is coming out soon
room_views          = number of views
room_certificate    = if the room has a certificate to achieve
room_timeToComplete = time in seconds to complete
room_userCompleted  = if the room is already completed
tasks_count         = the number of tasks in room
tasks               = sets where tasks get printed
```
### TASKS:
```ini
task_title              = name of the task
task_description        = description of the task
task_deadline           = deadline of the task
task_type               = type of the task (VM, downloadable, none)
task_number             = task number
task_created            = creation time of the task (Ex. "2019-08-01T17:02:09.503Z")
task_uploadId           = Id for downloads/starting VM
task_questions_count    = the number of questions in the task
questions               = sets where questions get printed
```
### QUESTIONS:
```ini
question_question = question name
question_number   = question number
question_hint     = question hint
```
>When signed in (session) can u access the following:
```ini
question_description    = placeholder text in answer textarea
question_correct        = if a correct answer has been given
question_extra_points   = amount of extra point given for this question
question_attempts       = attempts before the answer was correct
question_submission     = the answer given
question_has_answer     = if the question needs an answer
```
### miscellaneous
- `no_answer` and `placeholder` can use all template options above, to use them encapsulate the option between `{}`
```ini
no_answer       = sets the submission field when `has_answers` is not set
placeholder     = sets the submission field when `correct` is not set
```
___
