# 🩺 Mediscope – Multiple Disease Prediction System

Mediscope is a Django-based web application that predicts the likelihood of multiple diseases — **Diabetes, Heart Disease, and Parkinson’s** — using pre-trained Machine Learning models.  
Users can input relevant health data, and the system provides predictions instantly with a simple, user-friendly interface.

---

## 🚀 Features
- 📊 **Multiple Disease Prediction**: Supports prediction for Diabetes, Heart Disease, and Parkinson’s Disease.
- 🔍 **Machine Learning Models**: Pre-trained `.sav` models integrated into Django.
- 📁 **CSV Dataset Integration**: Training datasets for transparency and further research.
- 🎨 **Interactive Web Interface**: Simple forms to enter patient data.
- ⚡ **Fast & Accurate Predictions**: Based on trained models from medical datasets.

---

## 🛠 Tech Stack
- **Backend Framework**: Django (Python)
- **ML Models**: scikit-learn
- **Frontend**: HTML, CSS, Bootstrap (in Django templates)
- **Data**: CSV datasets for training/testing
- **Model Format**: `.sav` (Pickle format)

---

## 📂 Folder Structure
<p align="center">
  <img src="Screenshot of project/folder structure.png" width="600" alt="folder structure">
</p>
## ⚡ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/mediscope.git
cd mediscope
```

2️⃣ Create & activate virtual environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3️⃣ Install dependencies
```
pip install -r requirements.txt
```

4️⃣ Apply migrations
```
python manage.py migrate
```

5️⃣ Run the development server
```

python manage.py runserver
```
Now open http://127.0.0.1:8000/ in your browser.

## Screenshot of project
<p align="center">
  <img src="Screenshot of project/Home page.png" width="600" alt="folder structure">
</p>
<p align="center">
  <img src="Screenshot of project/diabetes page.png" width="600" alt="folder structure">
</p>

## for all all screenshot checkout my screenshot folder...

📊 Datasets
The datasets used for model training are included in the dataset/ folder:

Diabetes Dataset → diabetes.csv

Heart Disease Dataset → heart.csv

Parkinson’s Dataset → parkinsons.csv

👨‍💻 Author
Sahil Darji
