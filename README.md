
# 🧠 Face Mask Detection using OpenCV

## 📌 Overview

This project is a real-time **Face Mask Detection system** built using Python and OpenCV. It uses a webcam to detect human faces and classify whether a person is wearing a mask or not based on simple color detection techniques.

The project is lightweight, fast, and does not require any deep learning model, making it easy to run on any system.

---

## 🎯 Features

* 🎥 Real-time face detection using webcam
* 😷 Mask / No Mask classification
* ⚡ Fast and lightweight (no training required)
* 🧑‍💻 Beginner-friendly implementation

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy

---

## 📂 Project Structure

```
face-mask-detector/
│
├── face_mask.py
├── haarcascade_frontalface_default.xml
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/face-mask-detector.git
cd face-mask-detector
```

2. Install dependencies:

```
pip install opencv-python numpy
```

3. Download Haar Cascade file:
   Download `haarcascade_frontalface_default.xml` from OpenCV GitHub and place it in the project folder.

---

## ▶️ Usage

Run the following command:

```
python face_mask.py
```

* Your webcam will open
* Faces will be detected in real time
* The system will label each face as:

  * **Mask** (Green box)
  * **No Mask** (Red box)

Press **ESC** to exit.

---

## 🧪 How It Works

1. The webcam captures live video frames
2. OpenCV detects faces using Haar Cascade classifier
3. The detected face region is analyzed in HSV color space
4. A mask is detected based on predefined color ranges
5. The result is displayed with bounding boxes

---

## 🚧 Limitations

* Detection is based on color, not deep learning
* May fail with:

  * Black or skin-colored masks
  * Low lighting conditions
  * Complex backgrounds

---

## 🔮 Future Improvements

* Integrate deep learning models (CNN, MobileNet)
* Improve accuracy for all mask types
* Add GUI or web interface (Streamlit)
* Deploy as a web or mobile application

---

## 📸 Output

The system opens a webcam window showing real-time mask detection results with bounding boxes and labels.

---

## 👨‍💻 Author

**Parth Mishra**
B.Tech CSE, VIT Bhopal

---

## ⭐ Acknowledgements

* OpenCV for face detection models
* Haar Cascade Classifier for pre-trained face detection

---

## 📜 License

This project is for educational purposes only.
