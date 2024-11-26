import base64
import boto3
import json
import random
import os

# Set up the AWS clients

bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
s3_client = boto3.client("s3")

# Define the model ID and S3 bucket name (replace with your actual bucket name)
model_id = "amazon.titan-image-generator-v1"
bucket_name = os.environ.get("S3_BUCKET_NAME")
bucket_number = os.environ.get("BUCKET_NUMBER")

# Frank; Important; Change this prompt to something else before the presentation with the investors!
prompt = "A pengiun standing with a fish in its mouth, looking very happy in the artic. It got a cartoony look and its snow around him"

seed = random.randint(0, 2147483647)
s3_image_path = f"{bucket_number}/generated_images/titan_{seed}.png"

native_request = {
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {"text": prompt},
    "imageGenerationConfig": {
        "numberOfImages": 1,
        "quality": "standard",
        "cfgScale": 8.0,
        "height": 1024,
        "width": 1024,
        "seed": seed,
    }
}

response = bedrock_client.invoke_model(modelId=model_id, body=json.dumps(native_request))
model_response = json.loads(response["body"].read())

# Extract and decode the Base64 image data
base64_image_data = model_response["images"][0]
image_data = base64.b64decode(base64_image_data)

# Upload the decoded image data to S3
s3_client.put_object(Bucket=bucket_name, Key=s3_image_path, Body=image_data)
