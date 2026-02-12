# Kite
*Minimalistic ToDo without pressure, focus on the important*    

[kite365.pythonanywhere.com](https://kite365.pythonanywhere.com)  

---

## Stack:
### Backend
- Python 3.13
- django 6.0.1
- database - sqlite3
- django-positions
### Frontend
- htmx 2.0.8
- django-widget-tweaks
- html
- css
- JavaScript
### Deploy
- pythonanywhere

---

## Installation:

- ```git clone https://github.com/BugganeHuman/kite```
- ```python -m venv venv```
- ```source venv/bin/activate (`venv\Scripts\activate` if you use Windows)```
- ```pip install -r requirements.txt```
- ```python manage.py migrate```
- ```python manage.py runserver```

---
## Project Structure:
### Kite is divided for 4 sections:
- main - this section is intended for regular everyday tasks,
such as going grocery shopping or depositing money into 
a bank account.<br><br>
- work - This section is intended for work tasks,
I use it for IT tasks. <br><br>

- notes - This section is needed for tests that are similar to notes.
I'll give you an example: you need to make a backup every day
It doesn't need to be put into a regular task,
it's just a reminder. This section can also be used as notes.
<br><br>
- completed tasks - This is simply an archive of completed tasks
with a timestamp of when you completed them.
It is needed so that if you accidentally deleted a task,
you could copy it back or so you could look at
the history of your actions.
---

### my email - bugganehuman@gmail.com