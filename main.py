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
from fuzzywuzzy import fuzz
import random

def get_pet_response(user_input, responses):
    user_input = user_input.lower()  # Ensure user input is in lowercase
   # print(f"User input: '{user_input}'")  # Debug log for user input
    
    # Extract commands from the dataset
    commands = [entry['command'] for entry in responses]
   # print(f"Available commands: {commands}")  # Debug log for commands
    
    # 1. Apply fuzzy matching to both commands and their variations
    closest_match = None
    best_score = 0
    
    # Loop through commands and variations to find the best match
    for command in commands:
       # print(f"Checking command: '{command}'")  # Debug log for command checking
        
        # First, check fuzzy matching for the command itself
        command_score = fuzz.partial_ratio(command.lower(), user_input)
        if command_score >= 70 and command_score > best_score:
            closest_match = command
            best_score = command_score
           # print(f"Fuzzy match for command '{command}' with score {command_score}")
        
        # Now, check fuzzy matching for variations related to this command
        for variation in [item for item in responses if item['command'] == command][0]['variations']:
            variation_text = variation['text'].lower()
           # print(f"Fuzzy checking variation: '{variation_text}'")  # Debug log for variation checking
            
            variation_score = fuzz.partial_ratio(variation_text, user_input)
            if variation_score >= 60 and variation_score > best_score:
                closest_match = command
                best_score = variation_score
                #print(f"Fuzzy match for variation '{variation_text}' with score {variation_score}")
    
    if closest_match:
      #  print(f"Command matched: '{closest_match}'")  # Debug log for command match
        # Find the corresponding entry for the matched command
        match = next(item for item in responses if item['command'] == closest_match)

        # Check variations for exact matches first
        for variation in match['variations']:
            variation_text = variation['text'].lower()  # Ensure variation text is in lowercase
          #  print(f"Checking variation: '{variation_text}'")  # Debug log for variation checking
            if variation_text == user_input:
                # If there's an exact match, return a response
                response = random.choice(match['responses'])
                #print(f"Exact match found: '{variation_text}'")  # Debug log for exact match
                return response
        
        # If no exact match for variation, apply fuzzy matching to variations (lower threshold)
        for variation in match['variations']:
            variation_text = variation['text'].lower()  # Ensure variation text is in lowercase
          #  print(f"Fuzzy checking variation: '{variation_text}'")  # Debug log for fuzzy checking
            
            # Perform fuzzy matching on each variation text
            match_score = fuzz.partial_ratio(variation_text, user_input)
           # print(f"Match score for variation '{variation_text}': {match_score}")  # Debug log for fuzzy score
            if match_score >= 60:  # Threshold for fuzzy matching of variations
                response = random.choice(match['responses'])
              #  print(f"Fuzzy match found: '{variation_text}'")  # Debug log for fuzzy match
                return response
        
        # If no variation matches, return a random response for the command
        response = random.choice(match['responses'])
      #  print(f"No variation match found, returning random response.")  # Debug log for fallback
        return response
    else:
      #  print(f"No command match found.")  # Debug log for no command match
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
