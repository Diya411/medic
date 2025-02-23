# Uncomment if not using pipenv and .env file
from dotenv import load_dotenv
load_dotenv()

# Step 1: Setup GROQ API key
import os
import base64
from groq import Groq

# Directly set the API key here (no environment variables needed)
GROQ_API_KEY = "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"

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)


# Step 2: Convert image to required format
image_path = "acne.jpg"

def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Setup Multimodal LLM
query = "Is there something wrong with my face?"
model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ],
        }
    ]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

# Encode the image
encoded_image = encode_image(image_path)

# Run the analysis
result = analyze_image_with_query(query, model, encoded_image)

# Print the result
print(result)

print(os.environ.get("GROQ_API_KEY"))