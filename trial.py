import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://go-boldly-us-3.openai.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="nice car",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
