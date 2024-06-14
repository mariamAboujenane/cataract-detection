from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from inference_sdk import InferenceHTTPClient

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

CLIENT = InferenceHTTPClient(
    api_url="https://classify.roboflow.com",
    api_key="XQCScTGDTrzWbJ0P7iPu"
)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert_image', methods=['GET', 'POST'])
def insert_image():
    result_text = None
    accuracy = None
    if request.method == 'POST':
        if 'fileUpload' not in request.files:
            return redirect(request.url)
        file = request.files['fileUpload']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Call the Roboflow API
            result = CLIENT.infer(filepath, model_id="oculacare/1")
            print(result)

            # Extract the highest confidence prediction
            predictions = result.get('predictions', {})
            if predictions:
                highest_class = max(predictions, key=lambda x: predictions[x]['confidence'])
                result_text = highest_class
                accuracy = predictions[highest_class]['confidence']

            os.remove(filepath)
            return render_template('insert_image.html', result_text=result_text, accuracy=accuracy)

    return render_template('insert_image.html')

if __name__ == '__main__':
    app.run(debug=True)
