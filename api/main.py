from fastapi import FastAPI
from .app.model import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI(docs_url='/') #intanciando para que la api este en el origen y podamos testear

@app.post('/v1/prediction') #aca decimos que estamos en la versión 1
def make_model_prediction(request: PredictionRequest): # aqui es el request para retornar la predicción
    return PredictionResponse(worldwide_gross=get_prediction(request))