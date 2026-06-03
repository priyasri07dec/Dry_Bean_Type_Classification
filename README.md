# Dry_Bean_Type_Classification
### Application Preview

![App]()


### Project Overview
This project is a Machine Learning-based web application that predicts the type of a dry bean using its physical characteristics. The application is built with Streamlit and uses a trained Support Vector Machine (SVM) model for classification.

Users can enter bean feature values through an interactive web interface and receive an instant prediction of the bean type.

### Features
* Interactive Streamlit web application
* Predicts Dry Bean Type from input features
* Data preprocessing using StandardScaler
* Label encoding for target classes
* Trained Support Vector Machine (SVM) model
* User-friendly and responsive interface

### Dataset
The project uses the Dry Bean Dataset.

Target Classes:

* BARBUNYA
* BOMBAY
* CALI
* DERMASON
* HOROZ
* SEKER
* SIRA

### Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

### Machine Learning Workflow

The project follows a complete Machine Learning pipeline from data preprocessing to model deployment.

#### 1. Data Collection
The Dry Bean Dataset was used, containing multiple features of dry beans.

#### 2. Exploratory Data Analysis
* Analyzed dataset structure and feature distributions.
* Checked for missing values and duplicates.
* Explored class distribution.
* Visualized correlations among features.

#### 3. Data Preprocessing
Several preprocessing techniques were applied to improve model performance:

##### Feature Scaling
Since Support Vector Machine (SVM) is sensitive to feature magnitudes, all numerical features were standardized using StandardScaler.

Benefits:

Places features on a common scale.
Improves convergence and model performance.
Prevents features with larger values from dominating the model.

##### Label Encoding
The target variable (bean type) was converted into numerical labels using LabelEncoder before training.

#### 4. Handling Class Imbalance
To address class imbalance in the dataset, SMOTE (Synthetic Minority Oversampling Technique) was applied to the training data.

Benefits:

* Generates synthetic samples for minority classes.
* Improves model generalization.
* Reduces bias toward majority classes.

#### 5. Train-Test Split
The dataset was divided into:

* Training Set: 80%
* Testing Set: 20%

Random state was fixed to ensure reproducibility.

#### 6. Model Training
Multiple Machine Learning algorithms were initially evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors
* Gaussian Naive Bayes
* Support Vector Machine (SVM)

The models were compared using performance metrics on both training and testing datasets.

#### 7. Hyperparameter Tunung
To improve model performance, hyperparameter tuning was performed using GridSearchCV.

Parameters explored included:

* C (Regularization Parameter)
* Kernel Type
* Gamma

This process helped identify the optimal combination of hyperparameters for the SVM model.

#### 8. Final Model Selection
After evaluation and tuning, the Support Vector Machine (SVM) model achieved the best balance between:

* Accuracy
* Precision
* Recall
* F1 Score
* Generalization Performance

Therefore, SVM was selected as the final model.

#### 9. Pickle Files
The trained artifacts were saved using Joblib:

* svm_model.pkl
* scaler.pkl
* label_encoder.pkl
* model_columns.pkl

These files are loaded directly into the Streamlit application for real-time predictions

#### 10. Deployment

The trained model was deployed using Streamlit Cloud, allowing users to interact with the model through a web interface.

#### 11. Streamlit Web Link

https://priya-srivastava-drybeantypeclassification.streamlit.app/







































