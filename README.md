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
- Save the trained model using `pickle` for reuse in the API.

> [!Tip]
> Check out [the project's Jupyter notebook](https://github.com/mohammad-agus/machine-failures-detection/blob/master/project_notebook.ipynb) for the complete code.


## **API Development and Deployment**

### **1. Building the API**
- Use Flask to create an API with a `/predict` endpoint.
- Test the API locally.

### **2. Containerization**
- Package the API into a Docker container for consistent deployment.
- Test the container locally to ensure it works as expected.

### **3. Deploy to GCP**
1. **Push Docker Image to Artifact Registry**:
   - Authenticate Docker to GCP:
     ```bash
     gcloud auth configure-docker <your-region>-docker.pkg.dev
     ```
   - Tag and push the Docker image:
     ```bash
     docker tag ml-classification-api <your-region>-docker.pkg.dev/<your-project-id>/<your-repo-name>/ml-classification-api:latest
     docker push <your-region>-docker.pkg.dev/<your-project-id>/<your-repo-name>/ml-classification-api:latest
     ```

2. **Deploy to Cloud Run**:
   - Deploy the containerized API to Cloud Run:
     ```bash
     gcloud run deploy ml-classification-api \
         --image <your-region>-docker.pkg.dev/<your-project-id>/<your-repo-name>/ml-classification-api:latest \
         --platform managed \
         --region <your-region> \
         --allow-unauthenticated
     ```
   - Cloud Run will provide a URL for your deployed API.

### **4. Test the Deployed API**
- Use `curl` or Postman to test the API:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"features": [1, 2, 3, 4]}' https://<your-cloud-run-url>/predict