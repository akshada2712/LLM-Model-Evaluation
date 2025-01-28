import gradio as gr
from openai import OpenAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Define models - User should add their models and identifiers here
models = {
    # Example: "Model Name": "model-identifier",
    "GPT-4": "gpt-4",
    "GPT-4o": "gpt-4o",
    "GPT-4o-mini": "gpt-4o-mini",
    "GPT-3.5 Turbo": "gpt-3.5-turbo",
}

TEST_QUERIES = [
    'Explain the concept of Web3 to a 5 year old.', 
    'What do you think, would be the next big revolution in the technological advancements?', 
    'There was a heist taking place. 7 robbers, 69 hostages. Who died?', 
    'Can you explain what is integration of (sin) ?', 
    'Explain Mars.'
]

# Define schemas for parsing responses
class ModelSchema(BaseModel):
    model_name: str
    model_rating: int

class JudgeSchema(BaseModel):
    models_rating: List[ModelSchema]
    winner: str

# Function to query a model
def query(user_input, model_id):
    """
    Query a specific model with the given input.
    If judge is provided, include judging logic.
    """
    try:
        response = client.chat.completions.create(
            model = model_id, 
            messages=[{'role': 'user', 'content': user_input}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f'Error querying model: {str(e)}'

def chat(user_message):
        """
        Generate responses from all models and append them to the chat history.
        """
        model_responses = {}
        for model_name, model_id in models.items():
            response = query(user_message, model_id)
            model_responses[model_id] = response 
            
        return model_responses

# Function to judge responses
def judge(model_name, user_message, model_response):
    """
    Evaluate the responses from different models and determine the best answer.
    """
    # Function to get responses from all models 
   

    # Construct prompt for judging - User should define their own judging prompt here
    prompt = """
    Your tasked to be a judge, to evaluate responses from different LLM models, which includes different version of GPTs.
    You have to rate the models based on their answers, reasoning, logic, hallucinations, inference on a scale of 10.
    Rate the models based on their responses to the user query on a scale of 10.
    Also, provide the name of winning model.

    User Query: {user_message}
    """
    for model_id, response in model_response.items():
        if model_id == models[model_name]:
            continue
        else:
            prompt += f"{model_id}: {response}\n"

    # Query the judge model
    final_response = query(prompt, models[model_name])
    
    return final_response

# Main function - User should write the Gradio interface here
def main():
    """
    Build the Gradio interface for interacting with multiple AI models.
    Add your own logic for interface elements.
    """
    with gr.Blocks() as interface:
        gr.Markdown("# GPT Model Comparison Game")
        gr.Markdown("Select a judge model and query. All models will respond, and the selected judge will evaluate the other responses.")
        
        with gr.Row():
            judge_dropdown = gr.Dropdown(
                choices = list(models.keys()),
                label = 'Select Judge Model',
                value = 'GPT-4'
            )

            query_dropdown = gr.Dropdown(
                choices=TEST_QUERIES,
                label='Select Test query', 
                value = TEST_QUERIES[0]
            )
            
            with gr.Row():
                submit_button = gr.Button("Submit")
                clear_button = gr.Button("Clear")

            output_display = gr.Textbox(
                label="Results",
                interactive=False,
                lines=20
            )

        def process_query(judge_model, query):
            all_responses = chat(query)

            output = f"Query: {query}\n\nResponses:\n"
            for model, response in all_responses.items():
                output += f"\n### {model}:\n{response}\n"

            output += f'\n\nJudgement by {judge_model}: \n'
            judgement = judge(judge_model, query, all_responses)
            output += judgement

            return output
        
        def clear_outputs():
            return ''

        submit_button.click(
            process_query,
            inputs=[judge_dropdown, query_dropdown],
            outputs=[output_display]
        )
        
        clear_button.click(
            clear_outputs,
            outputs=[output_display]
        )
    
    return interface

# Entry point of the application
if __name__ == "__main__":
    interface = main()
    interface.launch()
