# Assessment: Drinks Quality Prediction System

## Part 1: Quizzes

### Quiz 1: Project Structure & Workflow
**Q1. Which file is used to define the dataset schema and column types?**
a) params.yaml
b) config.yaml
c) schema.yaml
d) requirements.txt

**Q2. What is the correct command to activate the project environment defined in README?**
a) conda activate env
b) conda activate mlproj
c) source venv/bin/activate
d) python env activate

**Q3. Which pipeline stage is responsible for splitting data and training the model?**
a) Data Ingestion
b) Data Validation
c) Model Trainer
d) Data Transformation

**Q4. Where are the hyper-parameters for the ElasticNet model stored?**
a) main.py
b) params.yaml
c) schema.yaml
d) app.py

### Quiz 2: Implementation Details
**Q1. In `app.py`, what is the purpose of the `/predict` route?**
a) To retrain the model
b) To display the home page
c) To take user input and show prediction results
d) To download the dataset

**Q2. What is the target column for prediction in this dataset?**
a) alcohol
b) density
c) quality
d) pH

**Q3. Which library is used for the web interface in this project?**
a) Streamlit
b) Django
c) Flask
d) FastAPI

---

## Part 2: Assignments

### Assignment 1: Model Tuning
**Objective:** Improve the model performance by tuning hyperparameters.
**Tasks:**
1. Open `params.yaml`.
2. Change `alpha` from `0.2` to `0.5` and `l1_ratio` from `0.1` to `0.5`.
3. Run the training pipeline (`python main.py` or via UI).
4. Check the model evaluation metrics (logs or artifacts) to see if performance improved.

### Assignment 2: Add a New Feature Check
**Objective:** Modify the validation logic.
**Tasks:**
1. In `schema.yaml`, suppose a new column `sugar_density_ratio` is added.
2. Update `schema.yaml` to include this new column.
3. Verify if `stage_02_data_validation` fails or needs update when running the pipeline.
   *(Note: This assignment tests understanding of how changes in schema propagate to validation).*

### Assignment 3: Customize the UI
**Objective:** Personalize the web application.
**Tasks:**
1. Navigate to `templates/index.html` (or `static` folder for CSS).
2. Change the title of the web page from "Wine Quality Prediction" to "Drinks Quality Checker".
3. Add a footer with your name.
4. Run `python app.py` and verify the changes in the browser.

### Assignment 4: API Testing
**Objective:** Test the application endpoints programmatically.
**Tasks:**
1. Ensure the app is running (`python app.py`).
2. Write a purely Python script (`test_api.py`) using `requests` library.
3. Send a POST request to `http://localhost:8080/predict` with sample data.
4. Print the response text to verify it returns a prediction.
