# Next day RainFall prediction using Machine learning

## Requirenments
Install requirements from requirements.txt file using pip install -r requirements.txt

## You can use answerbook.ipynb to re-train models and see analysis of data.

## aap.py is flask app which takes input weather parameters in form of list of dicts and give rainfall prediction. To run this app use python app.py and hit /predict POST request ## from postman. Sample input given below:

## Input:
{
"data": [
           {"Location": "Cobar",
           "Rainfall": 0.0,
           "Sunshine": 13.0,
           "WindGustDir": "S",
           "WindGustSpeed": 37.0,
           "WindDir9am": "SSE",
           "WindDir3pm": "SSE",
           "WindSpeed9am": 19.0,
           "WindSpeed3pm": 19.0,
           "Humidity3pm": 8.0,
           "Pressure3pm": 1012.1,
           "Cloud9am": 1.0,
           "Cloud3pm": 1.0,
           "RainToday": "No"},
          {"Location": "Albury",
           "Rainfall": 15.6,
           "Sunshine": 0.0,
           "WindGustDir": "W",
           "WindGustSpeed": 61.0,
           "WindDir9am": "NNW",
           "WindDir3pm": "NNW",
           "WindSpeed9am": 28.0,
           "WindSpeed3pm": 28.0,
           "Humidity3pm": 93.0,
           "Pressure3pm": 993.0,
           "Cloud9am": 3.700765396042097,
           "Cloud3pm": 3.878283575306357,
           "RainToday": "Yes"}
           ]
}



