import re, os

import config


class room_task:
  def __init__(self, thm_session, room_name, skip_answers=False) -> None:
    self.room_tasks   = None
    self.thm_session  = thm_session
    self.room_name    = room_name
    self.skip_answers = skip_answers
    
    self.get_room_tasks()
  
  def get_room_tasks(self) -> None:
    self.room_tasks = self.thm_session.room_tasks(self.room_name)
    
    if self.room_tasks.__len__() < 1:
      print(f"Room {self.room_name} doesn't exsist or is empty.")
      exit()
    
    if self.authenticated:
      for i in self.room_tasks:
        i['questions'] = i['tasksInfo']
        del i['tasksInfo']

    # * Cleaning HTML from elements
    for task in self.room_tasks:
      for question in task['questions']:
        if "question"   in question: question["question"]   = self.de_HTML(question["question"])
        if "answerDesc" in question: question["answerDesc"] = self.de_HTML(question["answerDesc"])
        if "submission" in question: question["submission"] = self.de_HTML(question["submission"])
        if "hint"       in question: question["hint"]       = self.de_HTML(question["hint"])
      
      if "taskTitle"  in task: task["taskTitle"]  = self.de_HTML(task["taskTitle"])
      if "taskDesc"   in task: task["taskDesc"]   = self.de_HTML(task["taskDesc"])
      if "taskType"   in task: task["taskType"]   = self.de_HTML(task["taskType"])
  
  def de_HTML(self, input: str, replace: str='') -> str:
    if input[-1:] == '\n': input = input[:-1]
    for t in config.config['HTML_TAGS']:
      input = re.sub(r"<"+ t +"[^<]*>", replace, input);
    for t in config.config['REPLACE_TAGS']:
      input = re.sub(t[0], t[1], input);
    return input
  
  @property
  def authenticated(self) -> bool:
    return self.thm_session.authenticated
  
  @property
  def tasks(self) -> list:
    return self.room_tasks
  
  def get_task(self, taskNo: int = -1, index: int = -1) -> dict:
    """
    return a list with questions from a task
    Parameters:
      -taskNo: the taskNo from the task object
      -index: task index
    
    """
    # * cant get questions no valid search term used
    if taskNo == -1 and index == -1: return None

    if taskNo > 0:
      task = [task for task in self.room_tasks if task['taskNo'] == taskNo]
      # * No task found at taskNo
      if task.__len__() < 1: return None
      return task[0]
    
    # * index
    else:
      return self.room_tasks[index]
  
  def get_attr(self, task: dict=None, question: dict=None) -> dict:
    attr = {
      "room_name":       self.room_name
      , "authenticated": self.authenticated
      , "task_count":    self.tasks.__len__()
    }
    if task is not None:
      for i in task:
        if i == 'questions': continue
        attr.update({i: task[i]})
      attr.update({"questions_count": task['questions'].__len__()})
    
    if question is not None:
      for i in question:
        attr.update({i: question[i]})
    
    return attr
  
  def replace_attr(self, rstring: str, pattrn: str, attrs:dict) -> str:
    for tag in re.findall(pattrn, rstring):
      if tag not in attrs: continue
      rstring = rstring.replace("{"+tag+"}", str(attrs[tag]))
    return rstring
  
  def get_questions(self, task=None, taskNo=-1, index=-1) -> list:
    task = task if task is not None else self.get_task(taskNo, index)
    
    if self.authenticated:
      for i in task['questions']:
        if i['noAnswer'] and i['correct']:
          i['submission'] = self.replace_attr(config.template['no_answer'], r"{(.*?)}", self.get_attr(task=task, question=i))
        elif not i['correct']:
          i['submission'] = self.replace_attr(config.template['placeholder'], r"{(.*?)}", self.get_attr(task=task, question=i))
    
    return task['questions']
  
  def get_formatted_room(self) -> str:
    outstr = self.replace_attr(config.template['room'], r"{(.*?)}", self.get_attr())
    outstr = outstr.replace("{tasks}", self.get_formatted_tasks())
    
    return outstr
  
  def get_formatted_tasks(self) -> str:
    outstr = ""
    for task in self.tasks:
      task_str = self.replace_attr(config.template['task'], r"{(.*?)}", self.get_attr(task=task))
      task_str = task_str.replace("{questions}", self.get_formatted_questions(task=task))
      outstr += task_str
    
    return outstr
  
  def get_formatted_questions(self, task: dict=None, taskNo: int=-1, index: int=-1) -> str:
    questions = self.get_questions(task=task, taskNo=taskNo, index=index)
    outstr = ""
    quest_format = config.template['question']
    if self.skip_answers: 
      quest_format = quest_format.replace("{submission}", "")
    if not self.authenticated: 
      for item in config.config['auth_only']: 
        quest_format = quest_format.replace("{"+item+"}", "")
    
    for question in questions:
      outstr += self.replace_attr(quest_format, r"{(.*?)}", self.get_attr(task=task, question=question))
    
    return outstr
  
  def write_room(self, file_loc: str) -> None:
    if file_loc is None:                                  file_loc = f"./README.md"
    if file_loc.endswith("/") or file_loc.endswith("\\"): file_loc += "README.md"
    elif not file_loc.endswith(".md"):                    file_loc += ".md"
      
    if '/' in file_loc or '\\' in file_loc:
      try: os.makedirs(os.path.dirname(file_loc), exist_ok=True)
      except: 
        print("couldn't create directory..")
        return

    with open(f"{file_loc}", "w") as out:
      out.write(self.get_formatted_room())
    print(f"Output written to {file_loc}")
