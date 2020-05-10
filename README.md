# Com-249-project-management-system

Introduction

   It is a project management system designed in python and django. The database is sqlite, already built inside python. This app lets the user to login as manager(administrator) and employee(staffs). The administrator part is only functioning right now. When logged in as admin, the user can create a new task, update, and delete the task as needed. The admin can see all the tasks or projects along with the assigned department, date created, deadlines, and task description. The admin can also update the status of project from the range of choices, 'started', 'ongoing', 'postponed', 'completed'.
  Furthermore, the admin of the website can create new users or account for its employee. The admin can put the users into their department (Groups). He/She can create or delete departments as needed.
  
  
# Instructions on running the code
  1. Install python 3
  2. Install latest version of django
  3. Go to  /usr/local/lib/pyton2.7/dist-packages/django/contrib/auth/admin.py
  
        Just before the list_display add this def that seeks for the groups:
        
        def group(self, user):
            groups = []
            for group in user.groups.all():
                groups.append(group.name)
            return ' '.join(groups)
        group.short_description = 'Groups'
        
        list_display = ('username', 'email', 'first_name', 'last_name', 'group')
        
  4. Launch CMD window and go to the directory containing all these files
  5. Type 'python manage.py runserver'
  6. Click on the link from the window (http://127.0.0.1:8000/) and append 'SimpleProject/' at link. Or Directly go to            http://127.0.0.1:8000/SimpleProject
 
 
 # Functioning part of the application
 
 You can login as both manager or employee. When logging as manager, it asks for 'Username' and 'Password'. 
      Username: admin
      Password: admin
      
 When logging as employee, it will ask for username and password. IF you are a new user, you can register by following the 'register' link. IF you are returning or registered user, you can input your username and password, and voila! it does nothing. There is still a lot to work on coding to display employee account interface.
 

