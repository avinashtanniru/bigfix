from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import datetime, os
import pkg
app = Flask(__name__)

app.config['UPLOAD_PATH'] = '/home/ventanni/Desktop/uploads/'
upload_path = app.config['UPLOAD_PATH']
# main_pyfile = url_for('static',filename='py/__main__.py')

@app.route('/')
def home():
    # return "Hello World!"
    now = datetime.datetime.now()
    year = str(now.year)
    return render_template('index.html',year=year)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/package')
def package(name):
    return "Hello {}!".format(name)

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    # uploaded_files = request.files.getlist("file[]")
    # print uploaded_files
    # return "updated {}!".format(uploaded_files)
    def pkgBuild():
		pkg.mcopy()
		pkg.build()

    if request.method == 'POST' and 'files' in request.files:
        for f in request.files.getlist('files'):
            f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
            # return 'Upload completed.'
        pkgBuild()
        download = "download"
        return render_template('index.html', download=download)
    # return render_template('upload.html')
    return "You are not Allowed	...!!!"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
