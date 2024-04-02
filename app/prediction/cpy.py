from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os
# Get path to images folder
# Create variables for your project
def get_image(a):
    publish_iteration_name = "Iteration1"
    project_id = "697f508c-5326-4bdc-a6b2-ef7223ada2ce"
    # Create variables for your prediction resource
    prediction_key = "c772308225124734a5cd99a24d10d3dc"
    endpoint = "https://southcentralus.api.cognitive.microsoft.com/"
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
    return 1 if results.predictions[0].tag_name == "Waste" else 0
