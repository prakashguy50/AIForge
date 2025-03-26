# AIForge-MLPlatform

A scalable Machine Learning platform with backend APIs and ML pipelines designed for real-world production systems.

---

## Project Structure

### Backend (Java)
- **Controllers**
  - `MLController.java`
- **Services**
  - `ModelService.java`
- **Exceptions**
  - `CustomException.java`
- **Configuration**
  - `application.properties`
- **Tests**
  - `MLControllerTest.java`

### ML Pipelines (Python)
- `data_ingestion.py` - Handles data ingestion logic.
- `data_preprocessing.py` - Preprocessing workflows.
- `model_training.py` - Training scripts for ML models.
- `model_evaluation.py` - Evaluation and metrics calculations.
- `model_deployment.py` - Model deployment script.

### Integrations
- **AWS Integration**
  - `s3_integration.py`
- **Kubernetes**
  - `kubernetes_deployment.yaml`
- **Airflow**
  - `airflow_dag.py`

### Infrastructure
- **Docker**
  - `backend.dockerfile`, `pipeline.dockerfile`, `docker-compose.yml`
- **Kubernetes**
  - Deployment and service YAMLs.
- **Terraform**
  - Infrastructure as code for cloud setup.

### Documentation
- Architecture details, API guides, deployment instructions.

---

## Key Features

- REST APIs for managing ML pipelines and models.
- ML workflows for ingestion, preprocessing, training, and evaluation.
- Cloud deployment using Kubernetes, Docker, and AWS integrations.
- Automated testing framework for backend and pipelines.
- Infrastructure as code with Terraform.

---

## Setup Instructions

### Backend Setup
1. Navigate to `src/backend/`.
2. Update `application.properties` with required configurations.
3. Build the project:
   ```bash
   mvn clean install
