# hugging_face_sagemaker_api_deployment
Repository showing how to deploy and use a hugging face model through sagemaker and API gateway

# Running the server locally

The command below will start the api server locally and expose the endpoints

```uvicorn api_app:app --reload --env-file .env```

# Deploying to AWS

```serverless deploy```
