# 🚦 Traffic Sign Recognition API

This project transforms a traffic sign recognition model, previously trained on Google Colab, into a robust web service using FastAPI. Simply run it with Docker and upload an image to identify traffic signs instantly.

## 📋 Overview

This API service provides the following functionality:

- **Image Upload**: Accepts traffic sign images as input
- **AI Processing**: Processes images using a pre-trained TensorFlow model
- **JSON Response**: Returns prediction results in a clean JSON format
- **Easy Deployment**: Containerized with Docker for simple setup

## 🛠️ Prerequisites

Before getting started, ensure you have the following installed:

- **Docker** - Container platform for running the application
- **Git** - Version control system (optional but recommended)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Enesbicer/traffic-sign-api.git
cd traffic-sign-api
```

### 2. Launch the Service

```bash
docker-compose up
```

### 3. Access the API

Once the service is running, you can interact with it through the interactive Swagger UI:

<img width="1687" alt="image" src="https://github.com/user-attachments/assets/b1a62402-37d7-4db8-8133-7753e7c1e7d0" />


1. **Open your browser** and navigate to: `http://localhost:7001/docs`
2. **Locate the endpoint**: Find the `POST /predict` endpoint
3. **Test the API**:
   - Click the **"Try it out"** button
   - Click **"Choose File"** and select a traffic sign image
   - Click **"Execute"** to process the image

### 4. View Results

The API will return a JSON response containing the prediction:

```json
{
  "predicted_class": "Stop"
}
```

## 🔧 API Endpoints

| Method | Endpoint  | Description                                     |
|--------|-----------|-------------------------------------------------|
| POST   |`/predict` | Upload an image and get traffic sign prediction |
| GET    |`/docs`    | Interactive API documentation (Swagger UI)      |


**Note**: Make sure Docker is running on your system before executing the `docker-compose up` command.
