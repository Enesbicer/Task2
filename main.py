from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json

app = FastAPI()

# Model ve sınıf isimleri
model = tf.keras.models.load_model('traffic_signs_model.h5')

with open('class_names.json', 'r') as f:
    class_names = json.load(f)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Görüntüyü yükle ve işle
    image = Image.open(io.BytesIO(await file.read())).convert('RGB')
    image = image.resize((32, 32))  # Model input boyutu
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    
    # Tahmin yap
    predictions = model.predict(image_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[str(predicted_class_index)]
    
    return {"predicted_class": predicted_class}
