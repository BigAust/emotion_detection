 # Import necessary libraries
import openai  # Import OpenAI library for GPT model
import os  # Operating system library for environment variables
from dotenv import load_dotenv, find_dotenv  # Load environment variables from .env file
import streamlit as st  # Import Streamlit for creating web application
import time  # Time library for time-related operations

# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)
openai.api_key = os.getenv('OPENAI_API_KEY')  # Set OpenAI API key from environment variables

# Define function to classify text sentiment using OpenAI's GPT model
def classify_sentiment(user_input, emotions):
    # System prompt for sentiment classification
    system_prompt = f'''Please classify the sentiment of the user's text using one of these emotions: {emotions}.
    Reply with the emotion only after analyzing the text.'''
    
    try:
        # Create chat completion request to OpenAI's GPT model
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': system_prompt},  # System prompt role and content
                {'role': 'user', 'content': user_input}  # User prompt role and content
            ],
            max_tokens=20,  # Maximum tokens for response
            temperature=0  # Temperature for response generation
        )

        classified_emotion = response['choices'][0]['message']['content']  # Get response content
        if classified_emotion == '':  # Check if response is empty
            classified_emotion = 'N/A'  # Set to 'N/A' if empty
        return classified_emotion  # Return classified emotion

    except openai.error.RateLimitError:
        st.error("Rate limit exceeded. Please check your OpenAI plan and usage.")  # Handle rate limit error
        return 'Rate limit exceeded'  # Return error message
    except openai.error.OpenAIError as e:
        st.error(f"An error occurred: {e}")  # Handle general OpenAI errors
        return 'Error occurred'  # Return error message

# Apply custom CSS for better aesthetics
st.markdown(
    """
    <style>
    .main {
        background-color: navy;  /* Set background color */
        color: white;  /* Set text color */
        font-family: 'Arial', sans-serif;  /* Set font */
    }
    .stButton>button {
        background-color: #f57c00;  /* Set button background color */
        color: white;  /* Set button text color */
        border: none;  /* Remove button border */
        border-radius: 4px;  /* Set button border radius */
        padding: 10px 24px;  /* Set button padding */
        text-align: center;  /* Center-align button text */
        text-decoration: none;  /* Remove text decoration */
        display: inline-block;  /* Display as inline block */
        font-size: 16px;  /* Set button font size */
        margin: 4px 2px;  /* Set button margin */
        cursor: pointer;  /* Change cursor to pointer on hover */
        transition-duration: 0.4s;  /* Set transition duration */
    }
    .stButton>button:hover {
        background-color: white;  /* Change button background color on hover */
        color: black;  /* Change button text color on hover */
        border: 2px solid #003366;  /* Add border on hover */
    }
    .stTextInput>div>div>input {
        background-color: #333333;  /* Set input background color */
        color: white;  /* Set input text color */
        border: 1px solid #ccc;  /* Set input border */
        border-radius: 4px;  /* Set input border radius */
        padding: 8px;  /* Set input padding */
    }
    .stTextArea>div>div>textarea {
        background-color: #333333;  /* Set textarea background color */
        color: white;  /* Set textarea text color */
        border: 1px solid #ccc;  /* Set textarea border */
        border-radius: 4px;  /* Set textarea border radius */
        padding: 8px;  /* Set textarea padding */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main program start
if __name__ == '__main__':
    st.title('Emotion Detection Portal')  # Main title of the web app
    st.write("This website is intended for Morgan State Students")  # Description of the web app

    # Morgan State Bears Image
    st.image('https://i.ibb.co/pXLM5SL/robot.jpg') 

    # Form section for user input
    with st.form(key='my_form'):
        default_emotions = 'positive, negative, neutral'  # Default emotions for classification
        emotions_input = st.text_input('Emotions: ', value=default_emotions)  # Text input for emotions
        user_text_input = st.text_area(label='Input your feelings in the box below: ')  # Text area for user input
        submit_button = st.form_submit_button(label='Examine')  # Submit button for form

        if submit_button:
            classified_emotion = classify_sentiment(user_text_input, emotions_input)  # Classify sentiment using GPT model
            result_text = f'{user_text_input} => {classified_emotion} \n'  # Format result
            st.write(result_text)  # Display result
            st.divider()  # Insert divider

            # Saving history of results
            if 'history' not in st.session_state:
                if result_text:
                    st.session_state['history'] = result_text  # Store result in session state
                else:
                    st.session_state['history'] = ''  # Initialize empty history if no result
            else:
                st.session_state['history'] += result_text  # Append result to existing history

            if st.session_state['history']:  # Display history if it exists
                st.text_area(label='History', value=st.session_state['history'], height=400)  # Text area for history display

    st.write("### Additional Options")  # Additional options section title
    st.button("Settings")  # Button for Settings
    st.button("Help")  # Button for Help
