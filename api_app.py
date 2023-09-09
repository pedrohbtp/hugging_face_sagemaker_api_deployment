try:
  import unzip_requirements
except ImportError:
  pass
import os
from sagemaker.huggingface.model import HuggingFacePredictor
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
app = FastAPI(middleware=[
    Middleware(CORSMiddleware, allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],)
])

@app.get("/predict")
def predict(text: str):
    predictor = HuggingFacePredictor(endpoint_name=os.getenv('SAGEMAKER_DEPLOYED_ENDPOINT'))
    resp = predictor.predict({
        "inputs": text,
    })
    return resp

handler = Mangum(app)