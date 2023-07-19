import os
from flask import Flask, flash, request, redirect, url_for, send_file, render_template
from werkzeug.utils import secure_filename

import applib


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def prp(msg):
    print(str(msg))
    print(type(msg))
    print(len(str(msg)))


@app.route('/uploadsecretpath', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            lower_filename = filename.lower()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], lower_filename))
            return render_template("upload_result.html", img_name = lower_filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/width/<width>/<img_name>', methods=['GET', 'POST'])
def get_img(width, img_name):
    prp(width)
    prp(img_name)

    # check if target_path exists
    target_path = "resized/w" + str(width) + "_" + secure_filename(img_name)
    if os.path.isfile(target_path):
        return send_file(target_path)
    else:
        print("not a file")

    # check if images exists in target folder
    upload_path = "uploads/" + secure_filename(img_name)

    prp(upload_path)

    if os.path.isfile(upload_path):
        # resize the image
        print("do resize")
        applib.resize_to_width(upload_path, target_path, int(width))
        return send_file(target_path)
    else:
        print("not a file")


    return "ok"


if __name__ == "__main__":
    app.run('0.0.0.0', 3010, debug = True)