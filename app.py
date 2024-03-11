from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)

# Load your pre-trained model
model = load_model('your_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the POST request
    img_file = request.files['image']

    # Process the image for prediction
    img = Image.open(img_file.stream).convert('L')  # Convert to grayscale
    img = img.resize((256, 256))  # Resize to match your model's input size
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)

    # Process the prediction result
    class_index = np.argmax(prediction)
    classes = ['Normal', 'Hemorrhage']
    result = classes[class_index]

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
##fastapi