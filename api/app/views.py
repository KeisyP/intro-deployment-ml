from .model import PredictionRequest
from .utils import get_model, transform_to_dataframe

model = get_model()

#recibe la data que se usa, luego la transforma a dataframe y se genera la predicción
def get_prediction(request: PredictionRequest) -> float: 
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return max(0, prediction) 
    #aqui se trata la predicción por si hay un error y hay negativos la saca como 0