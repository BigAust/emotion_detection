# Morgan State Bears Emotion Detection Portal

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)

## Introduction
The Morgan State Bears Emotion Detection Portal is a Streamlit application designed to leverage OpenAI's GPT-3.5-turbo model for real-time sentiment analysis. Tailored for Morgan State University students, this tool enables users to input text for sentiment classification based on predefined emotions. The portal not only displays analysis results but also maintains a session history, providing valuable insights into students' emotional well-being.

## Features
- **Interactive Interface**: Utilizes GPT-3.5-turbo to analyze emotions for Morgan State University students.
- **Session History**: Keeps a record of all emotion analyses performed during a session, offering a comprehensive overview of emotional states.

## Requirements
To run the Morgan State Bears Emotion Detection Portal, ensure you have:
- Python 3.6+
- OpenAI API key
- Streamlit
- python-dotenv
- openai

## Setup
1. Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd emotion_detection
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your OpenAI API key (Must be a paid OPENAI account or else it will not work):
   ```plaintext
   OPENAI_API_KEY=your_api_key_from_openai
   ```
5. Run the Streamlit application:
   ```bash
   streamlit run emotion_detection.py
   ```

## Usage
1. Launch the application and enter text for emotion classification in the 'Emotions' section.
2. Click 'Examine' to classify the sentiment of the text based on predefined emotions.
3. View the result displayed below the 'Examine' button and review the history in the 'History' section.

## Contributing
1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add your feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request to merge your changes into the main branch.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- OpenAI for developing GPT-3.5-turbo.
- Streamlit for providing a powerful framework for Python applications.
- Morgan State University for their support and inspiration.