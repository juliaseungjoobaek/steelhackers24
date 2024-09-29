# [🚀SteelHackers '24] Rate your Pitt Meal
Our project allows for the user, who is eating at Pitt's eatery, to create a healthier eating lifestyle for themselves.

All the items under the branch Julia includes the AI that was created with google gemini and used to create an output on the website.

All the items under the branch Niki includes the python resposible for getting all the list of user information for the AI and list of information on foods in the eatery.

All the items under the branch Angelina includes the front end of the project with the website interface all made from html and css.


## Contributors
Angelina Riveros (anr463@pitt.edu)  
Nicky Chung (nic216@pitt.edu)  
Julia Baek (seb337@pitt.edu)

## Inspiration
The inspiration for "Rate your Pitt Meal" came from the need for college students to make healthier eating choices amidst busy schedules and limited time to focus on nutrition. We wanted to create a tool that leverages AI and science to empower students to better understand the healthiness of their meals on campus. With so much nutritional information available, we aimed to simplify the process, helping students make more informed decisions quickly and easily.

## What is does
"Rate your Pitt Meal" is a personalized nutrition assessment platform that evaluates the healthiness of meals based on an individual’s personal information and the nutritional content of the food from the Pitt Dining app. The platform uses advanced AI models like Gemini to assess meals using chain-of-thought reasoning and integrates PubMed-based scientific insights through Llama-Index to provide users with a scientifically-backed health score. It also offers personalized dietary recommendations tailored to each user’s health profile and goals, supported by the latest research from PubMed, which is summarized by Gemini for clear, actionable feedback.

## How we built it
<img width="873" alt="Screenshot 2024-09-29 110359" src="https://github.com/user-attachments/assets/006690ca-02ec-4dc8-b2c4-eef52e31502b">

We built "Rate your Pitt Meal" using a combination of AI technologies and data retrieval systems. The backend is powered by Gemini-based models, which utilize chain-of-thought reasoning to evaluate the healthiness of meals. The Llama-Index serves as the retrieval system for relevant PubMed data, allowing us to integrate scientific findings into the evaluations and recommendations. We also integrated the Pitt Dining app’s nutritional data directly into the system for easy meal tracking. The frontend was developed using React, while the backend relies on Python and Flask to manage the AI interactions and data processing.

## Challenges we ran into
One of the main challenges was ensuring that the AI model could accurately interpret and apply scientific research from PubMed to individual health cases. We also had to work on optimizing the chain-of-thought reasoning in Gemini to ensure that it evaluated meals logically and provided consistent results. Additionally, integrating the Pitt Dining app’s nutrition data into our platform in a user-friendly way while maintaining accuracy was challenging. Ensuring the scalability and responsiveness of the system with real-time data was also a significant hurdle.

# Accomplishments that we're proud of
We’re proud of the successful integration of advanced AI with real-world applications, such as the Pitt Dining app and PubMed data. Creating a system that not only evaluates the healthiness of meals but also provides scientifically-backed and personalized dietary recommendations is a significant accomplishment. The user-friendly interface that allows students to easily assess their meals and receive actionable feedback is another highlight we’re particularly proud of.

## What we learned
Through this project, we learned a great deal about integrating AI models like Gemini with chain-of-thought reasoning into practical applications. We also gained insights into retrieving and applying scientific data from PubMed to personalized health recommendations. Understanding how to structure AI prompts to ensure that models provide both accurate evaluations and meaningful recommendations was a key takeaway. Additionally, we learned about the importance of user experience in health tech applications, ensuring that the platform remained easy to use and accessible.

## What's next for Rate your Pitt Meal
Moving forward, we plan to expand "Rate your Pitt Meal" by adding features such as real-time meal tracking, enhanced customization of dietary goals, and improved integration with campus dining services. We aim to continuously update our AI models with the latest research and user feedback to improve the accuracy and personalization of recommendations. Additionally, we are looking into partnerships with nutritionists and dietitians to further validate and refine our platform's health assessments and suggestions, making it an even more valuable tool for student health.
