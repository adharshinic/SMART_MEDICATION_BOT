from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Specify the absolute path where files will be stored
UPLOAD_FOLDER = 'C:\\Users\\ADHARSHINI\\Documents\\UiPath\\ADVANCED DRUG SEEKER BOT\\uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't already exist

# Configure the upload folder for Flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'prescription' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['prescription']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Save the file to the specified upload folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({'message': f'Failed to save file: {str(e)}'}), 500

    # Trigger UiPath bot or other processing logic here
    # For now, just return success with file path
    return jsonify({'message': 'File uploaded successfully!', 'file_path': file_path})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
