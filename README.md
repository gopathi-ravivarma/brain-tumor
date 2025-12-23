📌 Project Overview

Brain tumors are abnormal cell growths in the brain that can be life-threatening if not detected early. This project leverages Convolutional Neural Networks (CNN) to automatically analyze MRI scan images and classify them as Tumor or Normal, helping in early diagnosis and decision-making.

The system integrates:

->Deep Learning model training

->Image preprocessing

->Web-based prediction interface

🎯 Objectives

->Detect brain tumors from MRI scan images

->Segment and analyze tumor-affected regions

->Achieve high prediction accuracy using CNN

->Provide a simple and user-friendly web interface

🧩 Technologies Used

Programming Language: Python

Deep Learning: TensorFlow, Keras

Web Framework: Flask

Image Processing: PIL, NumPy

Frontend: HTML, CSS, Bootstrap

Development Environment: Anaconda (Conda)

🧠 Model Details

Model Type: Convolutional Neural Network (CNN)

Image Size: 224 × 224

Dataset Source: Kaggle – Brain MRI Images

Training Accuracy: ~98%

Model Format: .h5

📁 Project Structure

CODE

├── app.py                        # Flask application

├── requirements.txt              # Required Python libraries

├── save.h5                       # Trained deep learning model

│

├── static/                       # CSS, JS, vendor files

├── templates/                    # HTML pages

├── model/                        # Training notebooks & model files

├── upload/                       # Uploaded MRI images

└── MPIP06/                       # Supporting project files


⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/gopathi-ravivarma/brain-tumor.git

cd brain-tumor

2️⃣ Create & Activate Conda Environment
conda create -n mini python=3.9
conda activate mini

3️⃣ Install Required Dependencies
pip install -r requirements.txt

▶️ How to Run the Project
Step-by-Step Execution (Anaconda Prompt)
cd C:\Users
conda activate mini
python app.py

🌐 Access the Application

Open your browser and visit:

http://127.0.0.1:5000/


Upload an MRI image to get the prediction result.

📊 Features

->MRI image upload and preprocessing

->Deep learning–based tumor prediction

->Accuracy, precision, recall visualization

->Interactive web interface

🔮 Future Enhancements

->Support for multi-class tumor classification

->Integration with real-time hospital systems

->Cloud deployment

->Improved segmentation techniques
