import time
import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
        return render_template('index.html')

@app.route('/about')
def about_page():
        return render_template('about.html')

@app.route('/results')
def results_page():
        return render_template('results.html')

@app.route('/', methods=['POST'])
def upload_image():
        if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #print('upload_image filename: ' + filename)
                return render_template('index.html', filename=filename)
        else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
        #print('display_image filename: ' + filename)
        return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/inference/<filename>')
def inference_image(filename):
 
        file_path = '/root/webapp/static/inference/' + filename
        while not os.path.exists(file_path):
           time.sleep(1)
    
        return redirect(url_for('static', filename='inference/' + filename), code=301)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
