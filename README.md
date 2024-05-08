# OpenSource LLMS using LangChain in Streamlit Library

Welcome to my GitHub repository dedicated to an OpenSource Learning Management System (LLMS) powered by LangChain and integrated into the Streamlit library. 

## Getting Started

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Setting Up a Virtual Environment (Optional but Recommended)
3. Create a virtual environment using venv:
    ```
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
    ```
    venv\Scripts\activate
    ```
    - On macOS and Linux:
    ```
    source venv/bin/activate
    ```

5. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```

6. Set up your environment variables by creating a `.env` file and adding the following variables:
    - `LANGCHAIN_API_KEY`: Your LangChain API key.
    - `OPENAI_API_KEY`: Your OpenAI API key.
    - `LANGCHAIN_PROJECT`: Specify the project name (e.g., "Chatbot").

## Usage

1. Run the `app.py` file using Streamlit: 
    ```
    streamlit run app.py
    ```

2. Access the application through your web browser and start exploring the LLMS functionalities.
3. Interact with the chatbot to receive assistance and guidance on language learning topics.

## Contributing

We welcome contributions from the community to enhance and improve our LLMS project. Feel free to submit pull requests, report issues, or suggest new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

For any inquiries or support, please reach out to our team. Thank you for your interest and contribution to our OpenSource LLMS project!
