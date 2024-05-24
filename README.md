# YT Scribe

YT Scribe is a powerful Streamlit web app designed to transcribe and summarize YouTube videos using OpenAI's Whisper and GPT-4 models. This tool allows users to easily extract insights and summaries from video content with a user-friendly interface.

## Features

- **Download Audio**: Extract audio from YouTube videos.
- **Transcribe Audio**: Convert audio to text using OpenAI's Whisper model.
- **Generate Summaries**: Summarize transcriptions with OpenAI's GPT-4 model.
- **User-Friendly Interface**: Simple and intuitive UI for ease of use.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MJE43/yt-scribe.git
   cd yt-scribe
   ```

2. **Ensure you have Python 3.11 installed**:
   - You can use `pyenv` to manage Python versions:
     ```bash
     pyenv install 3.11.9
     pyenv local 3.11.9
     ```

3. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

2. **Open your web browser and go to [http://localhost:8501](http://localhost:8501)**.
3. Enter your OpenAI API key and the YouTube URL to start transcribing and summarizing.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or support, please contact [eisner.michaelj@gmail.com](mailto:eisner.michaelj@gmail.com).