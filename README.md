# 🚀 DevOps CI/CD Kubernetes Project

## 📌 Overview

This project demonstrates a complete DevOps workflow:

* Build a Flask application
* Containerize using Docker
* Deploy on Kubernetes (Minikube)
* Implement CI/CD using GitHub Actions

---

## 🧱 Architecture

```
Developer → GitHub → GitHub Actions (CI/CD)
            ↓
        DockerHub (Image Registry)
            ↓
        Kubernetes (Minikube)
```

---

## ⚙️ Tech Stack

* Python (Flask)
* Docker
* Kubernetes (Minikube)
* GitHub Actions
* DockerHub

---

## 🐳 Docker Workflow

### Build Image

```
docker build -t sumeetpy121/devops-app:latest .
```

### Run Locally

```
docker run -d -p 8080:8080 devops-app:latest
```

---

## ☸️ Kubernetes Deployment

### Apply Deployment

```
kubectl apply -f deployment.yaml
```

### Apply Service

```
kubectl apply -f service.yaml
```

### Access App

```
minikube service devops-app -n devops-lab
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

### Workflow Summary

1. Checkout code
2. Build Docker image
3. Push to DockerHub
4. Update Kubernetes deployment

---

### Workflow File

```yaml
name: CI-CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build Docker image
      run: |
        docker build -t sumeetpy121/devops-app:${{ github.sha }} \
                     -t sumeetpy121/devops-app:latest .

    - name: Push Docker images
      run: |
        docker push sumeetpy121/devops-app:${{ github.sha }}
        docker push sumeetpy121/devops-app:latest

    - name: Set up kubeconfig
      run: |
        mkdir -p ~/.kube
        echo "${{ secrets.KUBE_CONFIG }}" > ~/.kube/config

    - name: Update deployment image
      run: |
        kubectl set image deployment/devops-app \
        devops-app=sumeetpy121/devops-app:${{ github.sha }} \
        -n devops-lab
```

---

## 🔐 Secrets Used

| Secret Name     | Purpose                   |
| --------------- | ------------------------- |
| DOCKER_USERNAME | DockerHub login           |
| DOCKER_PASSWORD | DockerHub password/token  |
| KUBE_CONFIG     | Kubernetes cluster access |

---

## 🧠 Key Learnings

### 1. Kubernetes Debugging

* ImagePullBackOff → wrong image/tag
* CrashLoopBackOff → app crash
* Pending → insufficient resources
* Service not working → selector mismatch

---

### 2. CI/CD Concepts

* CI = Build + Push image
* CD = Deploy automatically
* Use unique image tags (`github.sha`)
* Avoid using only `latest`

---

### 3. Real-world Limitation

GitHub Actions cannot directly access local Minikube.

👉 In production:

* Use cloud Kubernetes (EKS/GKE/AKS)
* Or use GitOps tools (ArgoCD)

---

## 🚀 Future Improvements

* Deploy to AWS EKS
* Add monitoring (Prometheus + Grafana)
* Use Helm charts
* Implement GitOps (ArgoCD)

---

## ❤️ Author

Sumeet Patel
