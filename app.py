from flask import Flask, request, render_template
from pymongo import MongoClient
import gridfs

app = Flask(__name__)

# MongoDB setup
client = MongoClient("your_mongodb_connection_string")
db = client['file_db']
fs = gridfs.GridFS(db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        file_id = fs.put(file, filename=file.filename)
        return f'File successfully uploaded with id: {file_id}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

