from pydantic import BaseModel #serializa los modelos que van saliendo

class PredictionRequest(BaseModel): #las variables del modelo y se le pone el type 
    opening_gross: float
    screens : float
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: int
    cast_total_facebook_likes: float
    budget: float
    imdb_score: float

class PredictionResponse(BaseModel): #lo que se predice con su respectivo type
    worldwide_gross: float