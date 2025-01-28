# LLM Model Evaluation Using AI Models

## Overview

This project evaluates multiple AI language models (GPT-4, GPT-4-Turbo, GPT-4-Turbo-Mini, and GPT-3.5 Turbo) by having them judge each other's responses to predefined queries. The system implements a unique approach where each model acts as a judge to evaluate the responses of other models, excluding their own responses from consideration.

## Features

- **Model Selection Interface**: Built using Gradio, allowing users to select which model will act as the judge
- **Predefined Test Queries**: Five carefully selected test queries covering various topics
- **Automated Response Collection**: System automatically collects responses from all models
- **Peer Evaluation System**: Selected model evaluates and scores other models' responses
- **Real-time Results Display**: Shows all responses and the judge's evaluation in a clear format

## Requirements

- Python 3.8+
- OpenAI API key
- Required Python libraries:
```bash
pip install gradio openai python-dotenv
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akshada2712/LLM-Model-Evaluation.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## How It Works

1. **Judge Selection**: User selects which model will act as the judge
2. **Query Selection**: User selects from five predefined test queries
3. **Response Collection**: System collects responses from all models
4. **Evaluation Process**: Selected judge model evaluates other responses
5. **Results Display**: Shows all responses and the judge's evaluation

## Test Queries

The system includes five diverse queries:
1. Explaining quantum entanglement to a 10-year-old
2. Discussing implications of artificial general intelligence
3. Analyzing the trolley problem
4. Exploring creativity's role in scientific discovery
5. Examining climate change and global economics

## Evaluation Criteria

The judge model evaluates responses based on:
1. Accuracy and comprehension
2. Clarity and detail
3. Relevance to the query
4. Overall quality

## Usage

Run the following command to start the Gradio interface:
```bash
python main.py
```

The interface will open in your default web browser, where you can:
1. Select a judge model from the dropdown
2. Choose a test query
3. View responses from all models
4. See the judge's evaluation and scoring

## Models Used

- GPT-4
- GPT-4-Turbo
- GPT-4-Turbo-Mini
- GPT-3.5-Turbo

## Code Structure

```
project/
├── app.py          # Main application file
├── .env             # Environment variables
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

