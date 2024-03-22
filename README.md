# Dataframe Chatbot Streamlit

A Streamlit-based application that enables users to interactively query and explore data from CSV files through a conversational AI interface. Utilizing the power of language models, this application provides an intuitive way for users to ask questions and receive insights about their data without needing to write complex queries or code.

## Features

- **Interactive Chat Interface**: Engage with your data through a simple and intuitive chat interface.
- **Multiple Dataset Support**: Choose between different datasets to explore and analyze.
- **Powered by Language Models**: Leverages OpenAI's GPT-3.5 Turbo model for understanding and generating responses based on the data.
- **Session-based Conversation History**: Maintains a history of your queries and the AI's responses for the duration of the session.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- An OpenAI API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/fabricofdreams/dataframe-chatbot-streamlit.git
```

2. Navigate to the project directory:

```bash
cd dataframe-chatbot-streamlit
```

3. Install the required Python packages:

```bash
poetry install --no-root
```

4. Set up your API keys in a '.env' file:

```plaintext
API_KEY=api_key_here
```

### Running the Application

To start the application, run the following command in your terminal:

```bash
streamlit run app.py
```

Navigate to the provided URL to access the web interface.

## How to Use

1. **Select a Dataset**: Use the sidebar to choose between the available datasets.
2. **Ask Questions**: Type your questions into the chat input box and press enter to submit.
3. **View Responses**: The AI will analyze the data and provide answers based on the selected dataset.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

```
