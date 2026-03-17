# 👗 Fashion MNIST CNN Classifier

A deep learning web application that classifies fashion items into 10 categories using a **Convolutional Neural Network (CNN)** trained on the [Fashion MNIST dataset](https://github.com/zalandoresearch/fashion-mnist). Built with TensorFlow and deployed via Streamlit.

---

## 🚀 Demo

> Upload any clothing or accessory image and get an instant AI-powered prediction with confidence scores.

---

## 🗂️ Project Structure

```
fashion-mnist-classifier/
│
├── main.py                          # Streamlit web application
├── Fashion_Mnist_CNN_Classifier.ipynb  # Model training notebook
├── fashion_mnist_cnn_model.h5       # Pre-trained CNN model
├── requirements.txt                 # Python dependencies
├── sample_images/                   # Sample test images
└── README.md
```

---

## 🏷️ Fashion Categories

The model classifies images into **10 classes**:

| Label | Class         |
|-------|--------------|
| 0     | T-shirt/top  |
| 1     | Trouser      |
| 2     | Pullover     |
| 3     | Dress        |
| 4     | Coat         |
| 5     | Sandal       |
| 6     | Shirt        |
| 7     | Sneaker      |
| 8     | Bag          |
| 9     | Ankle Boot   |

---

## 🧠 Model Architecture

The CNN model was trained on Fashion MNIST (60,000 training images, 10,000 test images):

- **Input:** 28×28 grayscale images
- **Conv layers:** Multiple Conv2D + MaxPooling layers
- **Output:** Softmax over 10 classes
- **Framework:** TensorFlow / Keras

> See `Fashion_Mnist_CNN_Classifier.ipynb` for full training details, accuracy curves, and evaluation metrics.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fashion-mnist-classifier.git
cd fashion-mnist-classifier
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🖼️ How to Use

1. Launch the app with `streamlit run main.py`
2. Click **"Browse files"** and upload a `.jpg`, `.jpeg`, or `.png` image
3. Click **"Classify"**
4. View the predicted label, confidence score, and full class probability chart

---

## 📦 Dependencies

| Package     | Version  | Purpose                     |
|-------------|----------|-----------------------------|
| streamlit   | 1.32.0   | Web application framework   |
| tensorflow  | 2.15.0   | Deep learning model loading |
| numpy       | 1.26.4   | Array operations            |
| Pillow      | 10.2.0   | Image preprocessing         |

---

## 📁 Dataset

**Fashion MNIST** by Zalando Research  
- 70,000 grayscale images (28×28 pixels)  
- 10 fashion categories  
- Drop-in replacement for the original MNIST dataset  
- [Dataset GitHub →](https://github.com/zalandoresearch/fashion-mnist)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**  
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
