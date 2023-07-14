from fastapi import FastAPI, Request
import pickle
import uvicorn

app = FastAPI()

# Loading model
def load_model():
    try:
        with open('Model/rf_model.pkl', 'rb') as pickle_file:
            rf_model = pickle.load(pickle_file)
        return rf_model
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
        return None

@app.get("/")
async def root():
    response = {
        "status": 200,
        "message": "Your Wine API is up!"
    }
    return response

@app.get('/check')
async def check():
    model = load_model()
    return model

@app.post('/predict')
async def predict(data: Request):
    try:
        # Load request data
        payload = await data.json()
        alcohol = payload.get('alcohol')
        density = payload.get('density')
        sulphates = payload.get('sulphates')
        fixed_acidity = payload.get('fixed_acidity')
        volatile_acidity = payload.get('volatile_acidity')

        # Validate request payload
        if alcohol is None or density is None or sulphates is None:
            raise ValueError("Missing required fields in JSON payload")

        # Load model
        model = load_model()
        if model is None:
            raise ValueError("Failed to load model")

        label = ['bad wine', 'good wine']

        # Make prediction
        prediction = model.predict([[alcohol, density, sulphates, fixed_acidity, volatile_acidity]])

        response = {
            "status": 200,
            "input": [alcohol, density, sulphates, fixed_acidity, volatile_acidity],
            "prediction": label[prediction[0]]
        }
        return response
    except ValueError as e:
        response = {
            "status": 400,
            "message": str(e)
        }
        return response
    except Exception as e:
        response = {
            "status": 500,
            "message": str(e)
        }
        return response

if __name__ == "__main__":
    uvicorn.run("wine-api:app", host="0.0.0.0", port=8000)