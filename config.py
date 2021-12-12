template = {
  "room": """
# {room_name}
[Room](https://www.tryhackme.com/room/{room_name})
{tasks}
""",

  "task": """
## {task_number}. {task_title}
{questions}
""",

  "question": """  {question_number}. **{question_question}**
  > `{question_submission} `
""",
  "no_answer": "{question_description}",
  "placeholder": "{question_description}",
}
