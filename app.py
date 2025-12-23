from flask import Flask, request, render_template
from PIL import Image, ImageOps
import numpy as np
import base64
import urllib
from io import BytesIO
import os
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model('save.h5')  # Load once at the start

@app.route("/")
@app.route("/first")
def first():
    return render_template('first.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/chart")
def chart():
    return render_template('chart.html')

@app.route("/performance")
def performance():
    return render_template('performance.html')

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload_file():
    try:
        img = Image.open(BytesIO(request.files['imagefile'].read())).convert('RGB')
        img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
    except Exception as e:
        error_msg = f"Please choose a valid image file! Error: {e}"
        return render_template('result.html', **locals())

    args = {'input': img}
    out_pred, out_prob = predict(args)
    out_prob *= 100
    danger = "danger" if "Tumor" in out_pred else "success"

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    png_output = base64.b64encode(img_io.getvalue()).decode()
    processed_file = urllib.parse.quote(png_output)

    return render_template('result.html', **locals())

def predict(args):
    img = np.array(args['input']) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)

    if np.argmax(pred, axis=1)[0] == 0:
        out_pred = "Result: Brain Tumor"
    else:
        out_pred = "Result: Normal"

    return out_pred, float(np.max(pred))

if __name__ == '__main__':
    app.run(debug=True)
