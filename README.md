#🚦 Traffic Sign Recognition API

This project turns a traffic sign recognition model, previously trained on Google Colab, into a web service using FastAPI.
You can easily run it with Docker and upload an image to find out which traffic sign it is.

##📂 What Does This Project Do?

Takes a traffic sign image as input
Processes the image and predicts using a TensorFlow model
Returns the prediction result in JSON format

##🧰 Requirements

You need to have the following software installed on your machine:

Docker
Git (optional but recommended)

##🚀 Setup and Run Instructions

###1. Clone the repo:
git clone https://github.com/Enesbicer/traffic-sign-api.git
cd traffic-sign-api

###2. Start the Docker service:
docker-compose up

###3. Open the Swagger UI in your browser:
Go to http://localhost:7001/docs
Find the POST /predict endpoint
Click the Try it out button
Click Choose File and select an image file
Click Execute
You will see a JSON response on the same page like this:
{
  "predicted_class": "Stop"
}
