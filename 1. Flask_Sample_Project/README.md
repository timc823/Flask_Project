# Interactive Website by Using Flask App


## Introduction:

I have provided all of the code to deploy an example Flask application. The purpose of this example app is to demonstrate the inner-working of a flask app, providing a reference for how the different files in the app interact with one another. In order to run the application, follow the instructions detailed below. We also provide
instructions for how to deploy your webapp live on the internet via a website called **pythonanywhere**.


## Outcome of the Project

I have created a project by using Flask include some CSS design. Please visit the website if you want to get some idea of creating this project.

* [Final Outcome - Flask App Project](http://ist341.pythonanywhere.com/)

## Example Functions
There are sample functions included in this sample project. Here's the explanation of the functions: 

1. ASCII art: take text input and generate text output.
2. Invert Image: take image input and invert image color from RGB to BGR

## How to Use

### Running the App Locally

Note that Steps 1-3 deal with running your flask app from a virtual environment with virtualenv. Many tutorials online use virtualenv, but just know that these steps are entirely optional.  

1. Step into the ExampleApp directory

2. If you have not done so, use the command:

```pip install virtualenv``` 

If above command is not working, try:

```pip3 install virtualenv``` 

Then create a new virtual environment using the following command: (second venv is for the name of folder)

```python3 -m venv venv```

This will create a new virtual environment in a folder called venv.


3. To run your virtual environment use the following command:

```
for Mac/Linux Users:    source venv/bin/activate

for Windows:            venv\Scripts\activate 
```

For any trouble with virtual environments, visit the website below

* [Virtual Environment Troubleshooting](https://docs.python-guide.org/dev/virtualenvs/)


4. Run the following commands to ensure that all of the necessary libraries 
   have been downloaded

```
pip (or conda) install Flask twilio
pip (or conda) install Pillow
```

For help with installing the necessary libraries, visit the following sites

* [Setting up Python and Flask Environment](https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment)

* [Installing Pillow Library](https://pillow.readthedocs.io/en/stable/installation.html)

5. Run the following commands 

For Mac:

```
export FLASK_APP=project.py
flask run
```

For Windows:

```
set FLASK_APP=project.py
flask run
```

Following command allows you to run `Flask Run` automatically when you start virtual environment, without enter the command `FLASK_APP=project.py` every time.

```
pip install python-dotenv
```

6. Visit the website:

http://localhost:5000/

The webapp should be active and functional if you followed the above steps correctly.

7. Tutorial

If you would like to develop your own Flask App from scratch, be sure to check out this tutorial. 
It provides an in depth tutorial that covers everything one might need to get started in creating
web apps. 

* [Intro Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Deploy website by pythonanywhere

There are many ways to deploy a website, and pythonanywhere is the easiest I found for a small project. Pythonanywhere provides a 512 MB plan for free user and you can upgrade if you need more space. It also provide the bash console which allows you to clone the repo from GitHub. 

* [pythonanywhere - homepage](https://www.pythonanywhere.com/)
* [pythonanywhere - Flask Tutorial on YouTube](https://www.youtube.com/watch?v=M-QRwEEZ9-8)


 



