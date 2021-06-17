# django_assignment

1. Create a Python 3.8 virtualenv

2. Install dependencies:
   
   Goto django_ass directory
   
   Use Following Command: pip install -r requirements.txt

3. Configure your database in settings.py file

4. To Create tables, use given command:
   
   
   - python manage.py makemigrations


   - python manage.py migrate

6. Run the server:

   python manage.py runserver

7. api's and request data:   
   
   Comment api: Method: HTTP POST
   
   url: /api/v1/ass/assignment/comments/
   
   request data: {
    "comment":"",
    "commentID"
   }
   
   Comment api: Method: HTTP GET
   
   url: /api/v1/ass/assignment/comments/
   
   Comment api: Method: HTTP DELETE
   
   url: /api/v1/ass/assignment/comments/{id}
   
   
   Comment api: Method: HTTP PUT
   
   url: /api/v1/ass/assignment/comments/{id}
   
   request data: {
      "comment":""
   }
  
