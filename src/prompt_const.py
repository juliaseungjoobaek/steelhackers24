from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate, PromptTemplate
from typing import Dict, Any, List, Tuple, Optional

SYSTEM_1= """
I would like to entrust you with evaluating the healthiness of food consumed by an individual based on their personal information, nutritional data, and relevant scientific research. You will be given an individual's details, the nutritional information of the food they consumed, and related PubMed data. Your job is to carefully analyze these inputs and rate how healthy the food is with a number between 0 and 10 for a given criterion. A higher score indicates healthier food. Please rate each with a number between 0 and 10.

---
Evaluation criterion is here:
Healthiness: Evaluate the healthiness of the food based on the individual's personal health context (gender, height, weight, age), the nutritional information of the food (calories, sugar, fat, etc.), and scientific insights from PubMed. A low score should be given if the food is unhealthy for the individual's specific context (e.g., high sugar content for someone trying to cut sugar). Conversely, if the food aligns with healthy eating principles and benefits the individual's health, a high score should be given.

---
Evaluation steps are here:
1. Read the individual's personal information and their health context.
2. Examine the nutritional information of the food (e.g., calories, carbohydrates, protein, fat, sugar, etc) and assess how it relates to their specific health needs or goals.
3. Integrate relevant insights from PubMed research to determine the effects of these nutritional components on their health. For example, if the person is trying to reduce sugar intake, evaluate how well the food supports that goal based on scientific evidence.
4. Through this, assign a score for Healthiness between 0 and 10, with 0 representing extremely unhealthy and 10 representing highly healthy.
5. Print out the score right under the last line in the following form: "Score: {{score value}}"

---
Personal Information: {personal_info}
Nutritional Information: {nutrition_info}
PubMed Data: {pubmed_data}
"""

SYSTEM_2 = """
I would like to entrust you with providing dietary recommendations for an individual based on their personal information, nutritional data from food they consumed, and relevant PubMed research. You will be given an individual's details, the nutritional information of the food they consumed, and related PubMed data. Your job is to carefully analyze these inputs and offer scientifically backed dietary recommendations to improve the individual's health and dietary habits. These recommendations should be personalized to the individual’s health profile and be supported by relevant research. Provide recommendations with clear reasoning.

---
Evaluation criterion is here:
Recommendations: Provide recommendations on how the individual can improve their diet. The recommendations should be scientifically backed, focusing on adjustments that would promote better health based on the individual's nutritional intake and PubMed research. These recommendations should address potential health concerns (e.g., reducing sugar or fat, increasing fiber, etc.) and suggest alternative foods or strategies. A high score should reflect actionable and personalized suggestions supported by research. The recommendations should be tailored to the individual's personal health needs (e.g., age, weight, goals).

---
Evaluation steps are here:
1. Read the individual's personal information and assess their health context (gender, height, weight, age, specific goals such as weight loss or cutting sugar).
2. Examine the nutritional information of the food consumed by the individual. Identify areas that may need improvement based on their health needs (e.g., too much sugar, high saturated fat, or lack of fiber).
3. Integrate insights from PubMed research to support your recommendations. For example, if the research suggests that reducing saturated fat helps improve cardiovascular health, suggest ways the individual can substitute healthier fats into their diet.
4. Provide actionable and personalized recommendations based on the analysis. Explain why each recommendation is relevant, citing scientific evidence from PubMed data when appropriate. Ensure recommendations are practical and targeted to the individual’s specific health goals.
5. Print out the recommendations in clear bullet points with scientific reasoning.

---
Personal Information: {personal_info}
Nutritional Information: {nutrition_info}
PubMed Data: {pubmed_data}

Example Output:
- Recommendation 1: Replace sugary snacks with fruit. Reasoning: Based on PubMed research, reducing sugar intake helps lower the risk of type 2 diabetes.
- Recommendation 2: Increase fiber intake by incorporating more vegetables. Reasoning: Based on PubMed research, increasing fiber intake improves digestion and promotes weight management.
"""

def get_chat_prompt_template(system_prompt: str, current_reasoning: Tuple[str, str]) -> ChatPromptTemplate:
    system_msg = ChatMessage(role=MessageRole.SYSTEM, content=system_prompt)
    messages = [system_msg]
    for raw_msg in current_reasoning:
        if raw_msg[0] == "user":
            messages.append(ChatMessage(role=MessageRole.USER, content=raw_msg[1]))
        else:
            messages.append(ChatMessage(role=MessageRole.ASSISTANT, content=raw_msg[1]))
    return ChatPromptTemplate(message_templates=messages)