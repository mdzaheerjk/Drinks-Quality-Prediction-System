# End-to-End Drinks Quality Prediction Project Draft

## Project Overview
This project aims to build a robust, end-to-end Machine Learning pipeline for predicting the quality of Drinks based on physicochemical tests. It demonstrates a complete ML workflow, emphasizing modularity, reproducibility, and automation.

The core objective is to predict the Drinks quality score using a Regression model (ElasticNet). The model is trained on a dataset containing various chemical features:
*   **Input Features**: Fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol.
*   **Target Variable**: Quality (score between 0 and 10).

Beyond modeling, this project serves as a template for production-grade ML applications, incorporating:
*   **Modular Codebase**: Organized into clear pipelines for ingestion, validation, transformation, training, and evaluation.
*   **Data Validation**: Ensures data integrity using schema checks.
*   **CI/CD**:  Automated testing and deployment pipelines using GitHub Actions.
*   **Containerization**: Dockerized application for consistent deployment environments.
*   **Web Interface**: A user-friendly Flask app for real-time predictions.

## Project Structure
The project follows a modular structure, separating concerns into distinct pipelines and components:

### Key Components
1.  **Data Pipeline**:
    *   **Stage 01: Data Ingestion**: Downloads and unzips the dataset.
    *   **Stage 02: Data Validation**: Validates the dataset against a defined schema (`schema.yaml`).
    *   **Stage 03: Data Transformation**: Preprocesses the data for modeling.
    *   **Stage 04: Model Trainer**: Trains an ElasticNet regression model using parameters from `params.yaml`.
    *   **Stage 05: Model Evaluation**: Evaluates the trained model.

2.  **Web Application (`app.py`)**:
    *   A Flask-based web interface.
    *   **Routes**:
        *   `/`: Home page.
        *   `/train`: Triggers the training pipeline.
        *   `/predict`: Accepts user input for Drinks features (acidity, sugar, pH, etc.) and returns the predicted quality.

3.  **Configuration**:
    *   `config/config.yaml`: Configuration for file paths and sources.
    *   `params.yaml`: Model hyperparameters (e.g., ElasticNet alpha and l1_ratio).
    *   `schema.yaml`: Defines the expected data types for input columns and the target variable (`quality`).

## Deployment
The project is set up for automated deployment using GitHub Actions and AWS:

*   **Platform**: AWS EC2 (Ubuntu).
*   **Containerization**: Docker. Images are stored in AWS ECR.
*   **CI/CD**: GitHub Actions workflow builds the Docker image, pushes it to ECR, and deploys it to the EC2 instance.

## Technologies Used
*   **Python**: Primary programming language.
*   **Flask**: Web framework for the UI.
*   **Scikit-learn**: Machine learning library (ElasticNet).
*   **Pandas/Numpy**: Data manipulation.
*   **Docker**: Containerization.
*   **AWS (EC2, ECR)**: Cloud infrastructure.
*   **GitHub Actions**: CI/CD automation.
