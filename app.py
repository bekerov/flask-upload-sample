import os
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/'
port = int(os.getenv("PORT", 9099))


@app.route("/")
def get_files():
    files = os.listdir(os.path.join('.', 'data'))
    print(files)
    return render_template('render_files.html', files=files)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('uploaded_file.html')

    return render_template('upload_files.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)