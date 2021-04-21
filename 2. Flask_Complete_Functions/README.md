# Flask_learning_progress


## Introduction
In this repository, I created more functions but keep the website as a plain website. It doesn't include the CSS design. However, what I changed from the sample project was I added the **BluePrint** to the project. It allows you to distribute the functions into different folders. Below are the tips on how to create the **BluePrint** to the project.



## BluePrint and Tips for this project

**Create New Directory for BluePrint**
1. Create new BluePrint Directory.
2. Create __init__.py
3. Create routes.py
4. Create BluePrint in routes.py, change the blueprint name 

    `Blueprint_name = Blueprint('Blueprint_name', __name__)`

5. Register BluePrint under /project/__init__.py, change `new_directory below`

    `from project.new_directory.routes import new_directory`

    `project.register_blueprint(new_directory)`

6. Import Blueprint to routes.py

    `from project.new_directory import python_file_name`

7. Create HTML file

    ```
    {% extends "base.html" %}
        {% block content %}
            <h1>Hi, {{ user.message }}!</h1>
            <div> Messages Here</div>
        {% endblock %}```                
8. Link routes to html files.

    ```
    @Blueprint.route('/html_file_namename', methods=['GET','POST'])
    def function_name():
        user = {'message': 'welcome to ASCII arts page!'}
        if request.method =='POST':
            return render_template(Result_html_file, title=Title_name)
        return render_template('html_file', title=Title_name, user=user)```
**Tips**
1. If there are two upload folders, need to modify upload extensions.  
2. In the Html file, {{ url_for('**BluePrint.'Function_name'** in routes.py') }}
3. in the routes.py file, @**BluePrint**.route('/**Html Filename**', methods=['GET', 'POST'])

  
