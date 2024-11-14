from fastapi import FastAPI
from pydantic import BaseModel
import json
import random
from fuzzywuzzy import fuzz, process
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific URLs like ["http://localhost:3000"] if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow any HTTP methods (e.g., GET, POST, etc.)
    allow_headers=["*"],  # Allow any headers
)


# Load the dataset from JSON file
def load_responses():
    try:
        with open('pet_responses.json', 'r') as file:
            responses = json.load(file)
        return responses
    except FileNotFoundError:
        return None
        

# Function to get a random response based on user input
def get_pet_response(user_input, responses):
    user_input = user_input.lower()
    commands = [entry['command'] for entry in responses]
    closest_match = process.extractOne(user_input, commands, scorer=fuzz.partial_ratio, score_cutoff=65)

    if closest_match:
        best_command = closest_match[0]
        match = next(item for item in responses if item['command'] == best_command)
        
        for variation in match['variations']:
            if variation['text'] in user_input:
                response = random.choice(match['responses'])
                return response

        response = random.choice(match['responses'])
        return response
    else:
        return "I don't understand that command. Try 'feed', 'play', or 'how are you'."

class UserInput(BaseModel):
    text: str

@app.post("/ask-pet")
async def ask_pet(user_input: UserInput):
    responses = load_responses()
    if responses is not None:
        pet_response = get_pet_response(user_input.text, responses)
        return {"response": pet_response}
    else:
        return {"response": "Error: Pet responses not found."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
