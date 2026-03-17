import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/fashion_mnist_cnn_model.h5"

# Load the pre-trained model
model = tf.keras.models.load_model(model_path)

# Define class labels for Fashion MNIST dataset
class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot'
]

# Function to preprocess the uploaded image
def preprocess_image(image_file):
    img = Image.open(image_file)
    img = img.resize((28, 28))
    img = img.convert('L')  # Convert to grayscale
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape((1, 28, 28, 1))
    return img_array  # ✅ Fixed: was missing return statement

# Streamlit app
st.set_page_config(page_title="Fashion Item Classifier", page_icon="👗")
st.title('👗 Fashion Item Classifier')
st.write("Upload a clothing or accessory image and the model will classify it into one of 10 categories.")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])  # ✅ Fixed: type= keyword

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Image")
        resized_img = image.resize((200, 200))
        st.image(resized_img)

    with col2:
        st.subheader("Prediction")
        if st.button('Classify'):
            with st.spinner("Classifying..."):
                img_array = preprocess_image(uploaded_image)
                result = model.predict(img_array)
                predicted_class = np.argmax(result)
                confidence = float(np.max(result)) * 100
                prediction = class_names[predicted_class]

            st.success(f'Prediction: **{prediction}**')  # ✅ Fixed: st.sucess → st.success
            st.info(f'Confidence: {confidence:.2f}%')

            # Show full probability distribution
            st.subheader("Class Probabilities")
            prob_dict = {class_names[i]: float(result[0][i]) for i in range(10)}
            st.bar_chart(prob_dict)
