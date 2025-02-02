![Workflow](https://github.com/mohammad-agus/machine-failures-detection/blob/master/images/workflow.gif?raw=true)
# Description
This project demonstrates an **end-to-end machine learning workflow**, from data preparation and model training to building a **deployed containerized machine learning model API** to solve classification problem, and in this case is **to detect the failures of the machines**. The API serves predictions from a dockerized trained selected  model and to be deployed to Google Cloud Platform using Artifact Registry and Cloud Run.

## **Key Features**
- **End-to-End Workflow**: Covers the data preparation to deployment.
- **Data Preparation**: Explore, preprocess, and engineer features.
- **Model Training**: Train and evaluate multiple classification models (e.g., Logistic Regression, Decision Tree, Random Forest, XGBoost).
- **Model Serving**: Build a REST API to serve predictions in real-time.
- **Containerization**: Package the API into a Docker container for easy deployment.
- **Scalability**: Designed to be deployed to any container orchestration platform (e.g., Kubernetes, AWS ECS).