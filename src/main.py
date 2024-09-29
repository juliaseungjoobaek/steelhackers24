import google.generativeai as genai
import os
from llama_index.readers.papers import PubmedReader
from argparse import ArgumentParser
import openai
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
import food
from prompt_const import get_chat_prompt_template, SYSTEM_1, SYSTEM_2  


HF_TOKEN = "" # your huggingface token
model = genai.GenerativeModel("gemini-1.5-flash")

def setup_args():
    parser = ArgumentParser() 
    parser.add_argument("--model", type=str, default="meta-llama/Meta-Llama-3-8B-Instruct")
    parser.add_argument("--temp", type=float, default=0.6)
    parser.add_argument("--topp", type=float, default=0.9)
    parser.add_argument("-k", "--keywords", nargs="+", help="keyword list", required=True)

    return parser.parse_args()


def main(args):
        tokenizer = AutoTokenizer.from_pretrained(
        args.model,
        token=HF_TOKEN,
    )

'''
def tokenize_input(text):
    # Tokenize the input text
    tokens = tokenizer.tokenize(text)
    print(f"Tokenized Text: {tokens}")
    return tokens
'''

def pubmed_papers(search_query, max_results):
    # Initialize PubmedReader and load papers
    loader = PubmedReader()
    documents = loader.load_data(search_query=search_query, max_results=max_results)

    # Extract text from each document and store it in a list
    papers = [doc.text for doc in documents]

    return papers


def genai_pubmed_papers(keywords:str):
    # Configure the API key for Generative AI
    genai.configure(api_key=os.environ["API_KEY"])
    # Get papers from PubMed
    papers = pubmed_papers(keywords, max_results=5)  # Replace "dietary" with your actual search query
    summary = []

    # Process each paper
    for paper in papers:
        # Create the prompt using each paper's text
        prompt = f"This is a PubMed paper:\n\n{paper}\n\nPlease summarize this PubMed paper, focusing on the sections that provide insights or inferences related to diet and nutrition."
        # Generate content using the generative model
        response = model.generate_content(prompt)
        #print(response.text)
        summary.append(response.text)
        final_summary = ''.join(summary)

    return final_summary


def genai_eval(personal_info: str, nutrition_info: str, pubmed_data: str):
    # Configure the API key for Generative AI
    genai.configure(api_key=os.environ["API_KEY"])
    '''
    # Example of current reasoning, can be fetched from a conversation history or logs
    current_reasoning = [
        ("user", "Please evaluate the healthiness of my meal."),
        ("assistant", "Sure! Let's start by looking at your personal health details and the food you consumed."),
    ]
    '''
    # ----- System 1: Healthiness Evaluation -----
    # Generate the System 1 prompt for healthiness evaluation
    system_1_prompt = SYSTEM_1.format(personal_info=personal_info, nutrition_info=nutrition_info, pubmed_data=pubmed_data)
    
    # Get the chat prompt template for System 1
    #chat_prompt_1 = get_chat_prompt_template(system_1_prompt, current_reasoning)
    
    # Generate content using the chat prompt for System 1
    response_1 = model.generate_content(system_1_prompt)

    # Print the healthiness evaluation result
    print("Healthiness Evaluation (System 1):")
    print(response_1.text)

    # ----- System 2: Dietary Recommendations -----
    # Generate the System 2 prompt for dietary recommendations
    system_2_prompt = SYSTEM_2.format(personal_info=personal_info, nutrition_info=nutrition_info, pubmed_data=pubmed_data)

    # Get the chat prompt template for System 2
    #chat_prompt_2 = get_chat_prompt_template(system_2_prompt, current_reasoning)
    
    # Generate content using the chat prompt for System 2
    response_2 = model.generate_content(system_2_prompt)

    # Print the dietary recommendations result
    print("Dietary Recommendations (System 2):")
    print(response_2.text)



if __name__ == "__main__":
'''Whole - cereal bar
    Pico de gallo - Table 33
    Roasted Corn - Flourish
'''
    foods = food.Food()
    foods.load_nutrition_info()
    nutrition_info = foods.get_nutrition_info()
    personal_info = "Gender: Male, Age: 20, Weight: 200 pounds, Height: 6 feets"
    nutrition_info = foods.get_nutrition_info()
    pubmed_data = genai_pubmed_papers(keywords='muscle gain')

    genai_eval(personal_info, nutrition_info, pubmed_data)
