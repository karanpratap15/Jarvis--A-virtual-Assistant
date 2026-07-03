from google import genai

# Initialize the client. 
# Best practice: It automatically looks for an environment variable named GEMINI_API_KEY.
# Or, you can pass your string key directly inside the quotes below:
client = genai.Client()

# Ask Gemini your question
response = client.models.generate_content(
    model="gemini-2.5-flash", # Highly recommended: incredibly fast, smart, and completely free-tier eligible
    contents="What is coding?"
)

# Extract just the text from the response object
print(response.text)