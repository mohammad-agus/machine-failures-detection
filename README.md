![Workflow](https://github.com/mohammad-agus/machine-failures-detection/blob/master/images/workflow.gif?raw=true)

# Machine Failures Detection
This project demonstrates an end-to-end machine learning workflow, from data preparation and model training to building and deploying a containerized machine learning model API. The API serves predictions from the selected model and is deployed to Google Cloud Platform (GCP) using Artifact Registry and Cloud Run. Additionally, an interactive web interface is created using Streamlit to allow users to interact with the deployed API and solve classification problems—specifically, **detecting machine failures**.

## **Key Features**
- **End-to-End Workflow**: Covers the entire machine learning lifecycle, from data preparation to deployment and user interaction.
- **Data Preparation**: Explore, preprocess, and engineer features.
- **Model Training**: Train and evaluate multiple classification models (e.g., Logistic Regression, Decision Tree, Random Forest, XGBoost).
- **Model Serving**: Build an API to serve predictions in real-time.
- **Containerization**: Package the API into a Docker container for easy deployment.
- **Model Deployment**: Deploy the trained model to GCP using Artifact Registry and Cloud Run.
- **Interactive Interface**: Build a Streamlit web app to interact with the deployed API.

## **Technologies Used**
- **Python**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, XGBoost, Flask, Streamlit.
- **Docker**: Containerization for consistent deployment.
- **Google Cloud Platform (GCP)**:
  - **Artifact Registry**: Store and manage Docker images.
  - **Cloud Run**: Deploy the API as a serverless container.

## **Machine Learning Workflow**

### **1. Data Collection**
- Collect raw data from [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset).

### **2. Data Exploration, Preprocessing, and Feature Engineering**
- Perform exploratory data analysis (EDA) using `pandas` and `matplotlib`.
- Encode categorical variables and standardize numerical features.

### **4. Model Training, Validation, and Evaluation**
- Split the data into training, validation, and test sets.
- Train multiple classification models (Logistic Regression, Decision Tree, Random Forest, XGBoost).
- Tune hyperparameters
- Evaluate models using the ROC-AUC metric.

### **5. Model Selection and Persistence**
- Select the best-performing model based on evaluation metrics.
- Save the selected model and the trained encoder using `pickle`.

> [!Tip]
> Check out [the project's Jupyter notebook](https://github.com/mohammad-agus/machine-failures-detection/blob/master/project_notebook.ipynb) for the complete code.


## **API Development and Deployment**

### **1. Building & Containerizing the API**
- Copy the model's binary file into the API development directory.
- Load the model and the encoder:
  ```python
  import pickle
  with open('saved_model.bin', 'rb') as f:
      model, encoder = pickle.load(f)
  ```
- Build the API using `Flask` & `gunicorn` with a `/predict` endpoint and port `9696`.
- Test the API locally:
  ```bash
  gunicorn --bind 0.0.0.0:9696 predict:app
  ```
- Create a Dockerfile and pyproject.toml for dependecy management
- Build the Docker image of the API
  ```bash
  docker build -t <api-image-name> .
  ```
- Test run the Docker image locally
  ```bash
  docker run -it -p 9696:9696 <api-image-name>
  ```
> [!Tip]
> - Go to [machine-failures-detection-service](https://github.com/mohammad-agus/machine-failures-detection/tree/master/machine-failures-detection-service) directory for complete API code and Dockerfile.
> - Check out this [course](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment) for building an API using Flask and containerization.

### **2. Deploy to GCP**
- Install and authenticate [`gcloud cli`](https://cloud.google.com/sdk/docs/install-sdk).
  ```bash
  gcloud auth login
  ```
- Create an [Artifact Registry repository](https://cloud.google.com/artifact-registry/docs).
- Ensure user or service account has [the roles/artifactregistry.writer](https://cloud.google.com/iam/docs/understanding-roles).
- Push docker image to Artifact Registry repo.
  ```bash
  docker tag <artifact_registry_repo_url>/<api_image_name>:version
  docker push <artifact_registry_repo_url>/<api_image_name>:version
  ```
- Build and push the docker image (if the image has not been created).
  ```bash
  cd <api-dir>
  docker build -t artifact_registry_repo_url/<api_image_name>:version .
  docker push artifact_registry_repo_url/<api_image_name>:version
  ```
- After the docker image has been pushed, go to [Cloud Run and choose Deploy Service](https://cloud.google.com/artifact-registry/docs/integrate-cloud-run) or check out this [tutorial](https://www.youtube.com/watch?v=cw34KMPSt4k&t=270s).
- Copy the Cloud Run deployed-API url, add `/predict` endpoint, and test the API using `curl` or using below Python script:
  ```python
  import requests

  sample = {
    'type': 'l',
    'air_temperature_k': 300.5,
    'process_temperature_k': 309.6,
    'rotational_speed_rpm': 1390,
    'torque_nm': 60,  # 48.4,
    'tool_wear_min': 194,
    'machine_failure': 0
  }

  url = 'cloud_run_api_url/predict'
  response = requests.post(url=url, json=sample).json()
  print(response)
  ```

### **3. Build A Web App Using Streamlit to Demonstrate the Deployed API**
