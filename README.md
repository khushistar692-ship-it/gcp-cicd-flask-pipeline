# gcp-cicd-flask-pipeline
# GCP CI/CD Flask Pipeline

An end-to-end DevOps portfolio project: a small Flask web application delivered through an automated CI/CD pipeline on Google Cloud Platform.

## Status

Work in progress. Currently implemented:

- [x] Flask app with `/` and `/health` endpoints
- [x] Automated tests with pytest
- [ ] Docker, Terraform, Ansible, Jenkins, SonarQube, GKE, Prometheus/Grafana

## Run locally (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest -v
flask --app wsgi run
```

Then open http://127.0.0.1:5000/health

## Project structure

```
app/          Flask application package
tests/        pytest tests
wsgi.py       application entry point
pytest.ini    pytest configuration
requirements.txt / requirements-dev.txt
```