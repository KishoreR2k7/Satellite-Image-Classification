import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model("static_cnn_colab_final.keras")

class_names = ['cloudy', 'desert', 'green_area', 'water']

def predict_image(img):
    img = img.resize((128,128))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions)

    return f"{predicted_class} ({confidence*100:.2f}%)"

iface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Satellite Image Classifier",
    description="Upload a satellite image and the model will predict its class (cloudy, desert, green_area, water)."
)

iface.launch(share=False)