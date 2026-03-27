## End to End Machine Learning Student Performance Indicator Project(Regression)

## 📌 Project Setup

### 1️⃣ Environment Setup

* Create a virtual environment using the required setup package.
* Install dependencies from `requirements.txt`.
* Create `setup.py` for packaging the project.

---

### 2️⃣ Project Structure

### 2️⃣.1️⃣ 📂 Create `notebook` Folder (Jupyter Work)

#### Exploratory Data Analysis (EDA)

* Perform EDA in a Jupyter Notebook.
* Check for missing and duplicate values.
* Analyze each feature using:
  * Histograms
  * KDE plots
* Analyze score distributions using subplots.
* Perform multivariate analysis using subplots.

#### 2️⃣.2️⃣Model Training (Jupyter Notebook)

* Separate numerical and categorical columns.
* Apply:
  * StandardScaler on numerical columns
  * OneHotEncoder on categorical columns
* Perform train-test split.
* Train multiple machine learning models.
* Evaluate models using:
  * MAE (Mean Absolute Error)
  * MSE (Mean Squared Error)
  * R² Score
* Compare actual vs predicted values.
* Check the difference between actual and predicted outputs.

### 2️⃣.3️⃣ 📂 Create `src` Folder

* Inside the `src` folder:
    * Create a compenents folder.
    * Create a pipeline folder.
    * Create a custom exception file.
    * Create a custom logging file.
    * Create a utlis file.

#### 2️⃣.4️⃣ 📥 Data Ingestion
* Create a `DataIngestionConfig` class to define paths for:
  * Train dataset
  * Test dataset
  * Raw dataset
* Create a `DataIngestion` class to:
  * Read raw data (`stud.csv`) from `notebook/data/stud.csv`
  * Apply `train_test_split` on the raw dataset
  * Save `train.csv` and `test.csv` into the `artifacts` folder using paths defined in `DataIngestionConfig`

#### 2️⃣.5️⃣ 🔄 Data Transformation
* Read the train and test datasets.
* Create separate pipelines for:
  * Numerical columns
  * Categorical columns
* Create a `ColumnTransformer` using numeric and categorical pipelines.
* Drop the target feature from the training and test datasets.
* Apply the preprocessing pipeline on the training dataset using `fit_transform`.
* Apply the preprocessing pipeline on the test dataset using `transform`.
* Save the preprocessing object (`preprocessor.pkl`) in the `artifacts` folder using `pickle.dump`.

#### 2️⃣.6️⃣ 🤖 Model Trainer

* Create a dictionary of multiple machine learning models.
* Create another parameter dictionary with multiple hyperparameters for tuning.
* Perform hyperparameter tuning using `GridSearchCV`.
* Calculate the R² score for each model and save it.
* Select the best model based on the highest R² score.
* Save the best model object (`model.pkl`) in the `artifacts` folder using `pickle.dump`.


---

### 3️⃣ Create Website Application for Model Prediction
* Create a Flask application.
    * Create a `/predictdata` route with:
        * `GET` request → To render the input form
        * `POST` request → To receive user input data
    * Convert the form input data into a Pandas DataFrame after receiving it from the web form.
* Create a **Prediction Pipeline**:
    * Load `model.pkl` and `preprocessor.pkl` using `pickle.load`
    * Transform the fetched input data using the preprocessor object
    * Predict the result using the trained model object
* Return the predicted result to `home.html` inside a result dictionary.

---


### 4️⃣ 🚀 Deployment Process

4️⃣.1️⃣ Docker Setup

* Create a Dockerfile

* Build Docker image:
    * Create a Dockerfile: docker build -t hassankhan7571/studentperformance-app .
* Run Docker container:
    * docker run -p 5000:5000 hassankhan7571/studentperformance-app
* Verify application runs on:
    * http://localhost:5000

4️⃣.2️⃣ GitHub Actions CI/CD Setup
* Create GitHub Workflow file inside:
    * .github/workflows/deploy.yml
* Configure workflow to:
    * Build Docker image
    * Push image to Amazon ECR
    * Deploy to EC2


4️⃣.3️⃣ AWS IAM Configuration
* Create a new IAM User in AWS
* Assign required policies:
    * AmazonEC2FullAccess
    * AmazonEC2ContainerRegistryFullAccess
* Generate Access Key ID and Secret Access Key
* Save credentials securely

4️⃣.4️⃣ Amazon ECR Setup
* Create a new Elastic Container Registry (ECR) repository
* Copy and save the ECR repository URI

4️⃣.5️⃣ EC2 Instance Setup
* Launch a new EC2 instance (Ubuntu recommended)
* Connect to EC2 via SSH

* Update System
    * sudo apt-get update -y
    * sudo apt-get upgrade -y
* Install Docker
    * curl -fsSL https://get.docker.com -o get-docker.sh
    * sudo sh get-docker.sh
* Configure Docker Permissions
    * sudo usermod -aG docker ubuntu
    * newgrp docker
    * docker
    * docker --version
    * docker run hello-world


4️⃣.6️⃣ Self-Hosted GitHub Action Runner Setup
* Go to GitHub → Repository → Settings → Actions → Runners
* Create new Self-hosted Runner
* Copy and paste the provided commands into the EC2 instance terminal
* Runner will connect to your EC2 machine

4️⃣.7️⃣ Add GitHub Secrets

* In your GitHub repository: Settings → Secrets and variables → Actions
* Add the following secrets:
    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    * AWS_REGION
    * ECR_REPOSITORY


