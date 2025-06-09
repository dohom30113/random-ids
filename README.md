# Random ID Generator

A simple web application that displays random IDs from various public APIs. Built with Python FastAPI and designed to be deployed on OpenShift.

## Local Development

### Quick Start
1. Clone the repository:
```bash
git clone <repository-url>
cd random-ids
```

2. Create and activate a Python virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python -m app.main
```

5. Open your browser and visit:
```
http://localhost:8080
```

### Development Features
- Hot reload enabled (changes to code will automatically restart the server)
- API documentation available at:
  - Swagger UI: http://localhost:8080/docs
  - ReDoc: http://localhost:8080/redoc

### Using Anaconda (Alternative)
If you prefer using Anaconda:

1. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate random-ids
```

2. Run the application:
```bash
python -m app.main
```

## Features

- Fetches random IDs from multiple public APIs
- Clean and modern user interface
- Easy to deploy and maintain
- Containerized with Docker
- Helm chart for OpenShift deployment

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t random-id-generator .
```

2. Run the container:
```bash
docker run -p 8080:8080 random-id-generator
```

## OpenShift Deployment with Helm

1. Login to OpenShift:
```bash
oc login <your-openshift-cluster-url>
```

2. Create a new project (if needed):
```bash
oc new-project random-id-generator
```

3. Build and push the Docker image to your registry:
```bash
# Build the image
docker build -t <your-registry>/random-id-generator:latest .

# Push the image
docker push <your-registry>/random-id-generator:latest
```

4. Update the image repository in values.yaml:
```yaml
image:
  repository: <your-registry>/random-id-generator
  tag: latest
```

5. Install/Upgrade the Helm release:
```bash
# Install
helm install random-ids ./helm/random-ids

# Or upgrade if already installed
helm upgrade random-ids ./helm/random-ids
```

6. Get the application URL:
```bash
oc get route random-ids
```

The application will be available at the route provided by OpenShift.

## Configuration

The Helm chart supports the following configurations (in values.yaml):

- `replicaCount`: Number of application replicas
- `image`: Docker image configuration
- `service`: Service configuration
- `resources`: Resource limits and requests
- `route`: OpenShift route configuration

To customize the deployment, create a custom values file and use it with Helm:

```bash
helm install random-ids ./helm/random-ids -f custom-values.yaml
```
