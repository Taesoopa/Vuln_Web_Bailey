from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'

@app.route('/')
def index():
    return '''
        <h1>Upload ton avatar</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    statistiques = os.popen(f"wc -c {file_path}").read() 
    
    return f"Fichier bien reçu. Taille du fichier : {statistiques}"

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)
    with open("flag.txt", "w") as f: f.write("Flag{MIAAAAAWWWW}")
    app.run(port=5002)