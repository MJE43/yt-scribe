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
   git clone https://github.com/yourusername/yt-scribe.git
   cd yt-scribe

	2.	Ensure you have Python 3.11 installed:
	•	You can use pyenv to manage Python versions:

pyenv install 3.11.9
pyenv local 3.11.9


	3.	Install Poetry:
	•	If you don’t have Poetry installed, you can install it using the following command:

curl -sSL https://install.python-poetry.org | python3 -


	4.	Install the required dependencies:
	•	Use Poetry to install the dependencies:

poetry install



Usage

	1.	Run the Streamlit app:

poetry run streamlit run main.py


	2.	Open your web browser and go to http://localhost:8501.
	3.	Enter your OpenAI API key and the YouTube URL to start transcribing and summarizing.

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

For any inquiries or support, please contact [yourname@example.com].

### License (LICENSE file)

```markdown
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.