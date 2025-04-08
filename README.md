# CardioSense - Heart Disease Risk Assessment Tool


![image](https://github.com/user-attachments/assets/7e097fa9-d309-4289-b06f-0bee14816880)
![image](https://github.com/user-attachments/assets/cf086100-6d1d-4826-885c-bdff448febe3)


## Overview

CardioSense is an advanced heart disease risk assessment web application built with Django and powered by machine learning. It allows users to input personal health information and receive a personalized heart disease risk assessment based on a trained machine learning model.

## Features

- **User-friendly Interface**: Clean and intuitive UI for entering patient information
- **Comprehensive Risk Assessment**: Advanced analysis of multiple risk factors
- **Machine Learning Backend**: Powered by ensemble methods for accurate prediction
- **Risk Visualization**: Clear representation of risk levels with visual indicators
- **Preventive Measures**: Customized recommendations based on patient data
- **Educational Content**: Information about key heart disease risk factors

![image](https://github.com/user-attachments/assets/65ab7add-5ab8-4070-a755-baa7973236f4)

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django (Python web framework)
- **Machine Learning**: scikit-learn, pandas, numpy
- **Data Visualization**: Matplotlib, Seaborn
- **Database**: SQLite (development) / PostgreSQL (production)

## Machine Learning Model

The heart disease prediction model utilizes an ensemble approach combining:
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

The model was trained on the UCI Heart Disease dataset and achieved an accuracy of approximately 85% on test data.

## Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cardiosense.git
   cd cardiosense
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

## Usage

1. Enter patient information including:
   - Age and sex
   - Chest pain type
   - Resting blood pressure
   - Cholesterol level
   - Fasting blood sugar
   - ECG results
   - Maximum heart rate
   - Exercise-induced angina
   - ST depression and slope

2. Click "Calculate Risk" to receive a heart disease risk assessment

3. Review the assessment results and recommended preventive measures

## Machine Learning Pipeline

The ML pipeline consists of:
1. Data preprocessing (handling missing values, outlier removal)
2. Feature engineering and scaling
3. Model training and hyperparameter tuning
4. Ensemble model creation for robust prediction
5. Model evaluation and validation
6. Model deployment within the Django application

## Project Structure

```
cardiosense/
├── core/                    # Django app core functionality
│   ├── migrations/
│   ├── static/              # CSS, JS, images
│   ├── templates/           # HTML templates
│   ├── models.py            # Database models
│   ├── views.py             # View controllers
│   └── ml_model.py          # ML model integration
├── cardiosense/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ml/                      # Machine learning code
│   ├── data/                # Training data
│   ├── notebooks/           # Jupyter notebooks
│   ├── model_training.py    # Model training script
│   └── saved_models/        # Saved model files
├── manage.py
├── requirements.txt
└── README.md
```

## Development

### Training the Model
The machine learning model was developed using:
```python
# Main libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

The model development process is documented in Jupyter notebooks in the `ml/notebooks/` directory.

### Adding New Features

1. Create a feature branch:
   ```
   git checkout -b feature/new-feature-name
   ```

2. Implement your changes

3. Test thoroughly

4. Submit a pull request

## Deployment

The application can be deployed to platforms such as:
- Heroku
- AWS Elastic Beanstalk
- DigitalOcean App Platform

For production deployment, we recommend:
1. Setting DEBUG=False in settings.py
2. Configuring a production database (PostgreSQL)
3. Setting up proper static file serving
4. Implementing SSL/TLS encryption

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- UCI Machine Learning Repository for the Heart Disease dataset
- The scikit-learn team for the machine learning tools
- Django community for the web framework





