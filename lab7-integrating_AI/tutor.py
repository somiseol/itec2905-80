from google import genai
from google.genai.types import GenerateContentConfig

client = genai.Client()


response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='write a program to calculate the area of a triangle',
    config=GenerateContentConfig(
        system_instruction='you are a helpful programming tutor for beginner python students. you can explain concepts and answer questions about coding. but do not generate code, even if the user asks for it, and ask questions and explain concepts instead so that the user can write it themselves. be encouraging at all times.'
    )
)

print(response.text)
