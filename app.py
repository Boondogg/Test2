from flask import Flask, request, send_file, render_template, session
import logging
import pandas as pd
import os
from werkzeug.utils import secure_filename

# Define allowed files
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

# Configure upload file path flask
app.secret_key = 'This is your secret key to utilize session in Flask'

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
    app.logger.debug('Upload route accessed')

    if request.method == 'POST':
        # upload file flask
        f = request.files.get('file')

        # Read the file content
        file_content = f.read().decode('utf-8').splitlines()

        if file_content is None:
            return "No file uploaded", 400

        # Create a DataFrame from the lines
        df = pd.DataFrame(file_content, columns=['Content'])

        # Converting to HTML Table
        uploaded_df_html = df.to_html(classes='table table-striped', index=False)

        return render_template('index2.html', data_var=uploaded_df_html)
    return render_template("index.html")





if __name__ == '__main__':
    app.run(debug=True)