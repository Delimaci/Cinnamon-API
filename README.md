# Cinnamon API

Welcome to the Cinnamon API! This is a fun and interactive FastAPI-based backend that allows you to communicate with Cinnamon, your pet. The API handles various commands and returns cute responses based on the input it receives. You can ask Cinnamon to perform tasks like feeding, playing, or even say hello and goodbye!

This API is powered by **FastAPI** and includes fuzzy string matching to understand a variety of commands and phrases. It serves as a backend for your interactive chatbot experience.

## Features

- Responds to various commands (e.g., "feed", "play", "hello", "how are you").
- Supports fuzzy matching for user input, making it tolerant of typos.
- Offers a wide range of commands and responses, including greetings, emotions, and actions.
- Can be easily integrated into web and mobile applications to create a fun pet chatbot experience.

## Installation

### Prerequisites

- Python 3.7+
- `pip` for installing Python dependencies

### Steps to Run Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/delimaci/cinnamon-api.git
   cd cinnamon-api

2. **Create a virtual environment (optional but recommended):**

#python -m venv venv
#source venv/bin/activate  # For Windows, use venv\Scripts\activate
#Install the dependencies:

#pip install -r requirements.txt
#run the app uvicorn app:app --reload

API Endpoints
POST /ask-pet
This is the main endpoint where you can interact with Cinnamon. Send a POST request with a text parameter, and you'll get a response from Cinnamon!

Request Body
json
Copy code
{
  "text": "feed"
}
Response
json
Copy code
{
  "response": "Yum! Thanks for the food!"
}
Example Commands and Responses
Here are some example commands you can use to interact with Cinnamon:

feed: "Yum! Thanks for the food!" or "I'm full now! That was delicious!"
play: "Yay! Let's play!" or "This is so much fun!"
how are you: "I'm doing well, thanks for asking!" or "I'm good, how about you?"
hello: "Hi there!" or "Hello, how can I help?"
goodbye: "Goodbye! See you soon!" or "Bye! Have a great day!"
thanks: "You're welcome!" or "Anytime!"
Feel free to expand the commands with your own creative interactions!

Project Structure
graphql
Copy code
cinnamon-api/
│
├── app/                # Main FastAPI app directory
│   ├── __init__.py     # Initializes the app
│   ├── app.py          # Contains the FastAPI application
│   ├── pet_responses.json # JSON file with all the responses and commands
│
├── requirements.txt    # List of Python dependencies
└── README.md           # This file
Deployment
This API can be easily deployed on platforms like Render, Heroku, or AWS. If you're using Render, you can follow these steps to deploy:

Create a new Web Service on Render.

Link the GitHub repository to Render.

Choose Python as the runtime and add the appropriate start command:

bash
Copy code
gunicorn app:app --workers 4
Deploy your app, and you're all set!

Once deployed, you will be able to make API requests to the live endpoint!

Contributing
We welcome contributions! If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes. Here's how you can help:

Add more responses and commands to Cinnamon.
Fix bugs or improve the fuzzy matching algorithm.
Update the README or improve the codebase.
To contribute, please follow these steps:

Fork the repository
Clone your forked repository locally
Create a new branch for your changes
Commit and push your changes
Open a pull request
License
This project is licensed under the MIT License - see the LICENSE file for details.



