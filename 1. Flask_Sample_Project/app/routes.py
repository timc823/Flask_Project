# Home page Route
from app import ascii_art
try:
    from flask import render_template, redirect, url_for, request, send_from_directory, flash
except:
    print("Make sure to pip install Flask twilio")
from app import app
import os
from werkzeug import secure_filename
try:
    from PIL import Image
    import PIL.ImageOps
except:
    print("Make sure to pip install Pillow")

# TODO: Make sure you go through first two chapters of the Flask tutorial (link include in README)


@app.route('/')
@app.route('/index')
# HINT:
# This is an example of how to print out the message on index.html
# You may want to go through base.html. index.html, routes.py to understand first function.
def index():
    user = {'message': 'Welcome to IST341!!!!'}
    return render_template('index.html', title='Home Page', user=user)

@app.route('/printRect', methods=['GET','POST'])
def printRect():
    user = {'message': 'welcome to ASCII arts page!'}
    if request.method =='POST':
        width = request.form['width']
        height = request.form['height']
        symbol = request.form['symbol']
        output = ascii_art.printRect(width,height,symbol)
        # print(output)
        return render_template('ASCII_Result.html', title='ASCII Result', output=output)
    return render_template('ascii_art.html', title='ASCII arts', user=user)



# Used for uploading pictures
@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static',filename)

# Image uploading page,
@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # if the image is valid, do the following
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Create a path to the image in the upload folder, save the upload
            # file to this path
            save_old=(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(save_old)
            # Take the image, make a new one that is inverted
            img = Image.open(save_old)
            rbg_img = img.convert('RGB')
            inverted_image = PIL.ImageOps.invert(rbg_img)
            save_new=(os.path.join(app.config['UPLOAD_FOLDER'], 'new_'+filename))
            inverted_image.save(save_new)
            # Render template with inverted picture
            rt = render_template('imageResults.html', filename='new_'+filename)
            return rt
    return render_template('image.html')

# allowed image types
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['ALLOWED_EXTENSIONS']=ALLOWED_EXTENSIONS

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']