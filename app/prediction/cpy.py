from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
# Get path to images folder
# Create variables for your project
def get_image(a):
    publish_iteration_name = "Iteration1"
    project_id = "9e7820ba-5b71-4b2c-b5b7-aba3feeca08b"
    # Create variables for your prediction resource
    prediction_key = "421309d49a0b4b2a90560b008ad1ece4"
    endpoint = "https://centralindia.api.cognitive.microsoft.com/"
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)
    # Open an image and make a prediction
    #image_contents = open( f"app\prediction\images\{a}", "rb")
    image_contents = a
    results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())
    # Display the results
    # for prediction in results.predictions:
    #     print(f"{prediction.tag_name}: {prediction.probability * 100 :.2f}%")
    print(f"result : {results.predictions[0].tag_name} {results.predictions[0].probability * 100 :.2f}%")
    return 1 if results.predictions[0].tag_name == "garbage" else 0
