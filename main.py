import streamlit as st
import yt_dlp as yt
from openai import OpenAI
import logging
import re
import os

# Set up logging
logging.basicConfig(level=logging.INFO)


def is_valid_youtube_url(url):
  youtube_regex = re.compile(
      r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')
  return youtube_regex.match(url)


def download_audio(youtube_url):
  ydl_opts = {
      'format':
      'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'm4a',
          'preferredquality': '192',
      }],
      'outtmpl':
      'audio.%(ext)s',
      'noplaylist':
      True
  }
  try:
    with yt.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(youtube_url, download=True)
      audio_file = ydl.prepare_filename(info)
      audio_file = audio_file.rsplit(
          '.', 1)[0] + '.m4a'  # Ensure correct file extension
    return audio_file
  except Exception as e:
    logging.error(f"Error downloading audio: {e}")
    st.error(f"Error downloading audio: {e}")
    return None


def transcribe_audio(file_path, client, language=None, prompt=None):
  try:
    with open(file_path, "rb") as audio_file:
      transcript = client.audio.transcriptions.create(model="whisper-1",
                                                      file=audio_file,
                                                      language=language,
                                                      prompt=prompt,
                                                      response_format="json")
    return transcript["text"]
  except Exception as e:
    logging.error(f"Error transcribing audio: {e}")
    st.error(f"Error transcribing audio: {e}")
    return None


def summarize_text(transcript_text, client, length="brief"):
  prompt = f"Summarize the following text in a {length} summary:\n\n{transcript_text}"
  try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": prompt
        }])
    summary = response.choices[0].message["content"].strip()
    return summary
  except Exception as e:
    logging.error(f"Error generating summary: {e}")
    st.error(f"Error generating summary: {e}")
    return None


st.set_page_config(page_title="YouTube Transcription App", layout="centered")
st.title("YouTube Transcription App")
st.write("Transcribe and download YouTube video transcripts easily.")

# Input for OpenAI API key
st.sidebar.subheader("Enter OpenAI API Key")
secret = st.sidebar.text_input(
    "API Key",
    type="password",
    help=
    "Enter your OpenAI API key. This will be used for the current session and not stored."
)

if not secret:
  st.error("Please enter your OpenAI API key in the sidebar to proceed.")
else:
  # Initialize OpenAI client
  client = OpenAI(api_key=secret)

  with st.form("youtube_url_form"):
    st.subheader("Enter YouTube URL")
    youtube_url = st.text_area(
        "YouTube URL",
        placeholder="Enter the YouTube URL",
        help="Paste the URL of the YouTube video you want to transcribe.")
    language = st.text_input(
        "Language (optional)",
        placeholder="e.g., en",
        help="Specify the language in ISO-639-1 format for better accuracy.")
    prompt = st.text_input(
        "Prompt (optional)",
        placeholder=
        "Provide an optional prompt to guide the model's style or continue a previous audio segment."
    )
    summarize = st.checkbox(
        "Generate Summary",
        help="Create a brief summary of the transcription.")
    summary_length = st.selectbox("Summary Length", ["brief", "detailed"],
                                  help="Choose the length of the summary.")
    submit_button = st.form_submit_button("Transcribe")

  if youtube_url:
    if not is_valid_youtube_url(youtube_url):
      st.error("Please enter a valid YouTube URL.")
    else:
      st.video(youtube_url)

  if submit_button and youtube_url:
    if not youtube_url.strip():
      st.error("Please enter a valid YouTube URL.")
    else:
      try:
        with st.spinner('Downloading audio... Please wait.'):
          audio_file_path = download_audio(youtube_url)
        if audio_file_path:
          with st.spinner('Transcribing audio... Please wait.'):
            transcript_text = transcribe_audio(audio_file_path, client,
                                               language, prompt)
          if transcript_text:
            st.session_state.transcript_text = transcript_text
            if summarize:
              with st.spinner('Generating summary... Please wait.'):
                summary_text = summarize_text(transcript_text, client,
                                              summary_length)
              if summary_text:
                st.session_state.summary_text = summary_text
      except Exception as e:
        logging.error(f"Error: {e}")
        st.error(f"Error: {e}", icon="🚨")

  if "transcript_text" in st.session_state:
    st.subheader("Video Transcript")
    st.markdown(st.session_state.transcript_text)
    st.download_button("Download Transcript",
                       st.session_state.transcript_text,
                       file_name="transcript.txt",
                       mime="text/plain")

  if "summary_text" in st.session_state:
    st.subheader("Summary")
    st.markdown(st.session_state.summary_text)
    st.download_button("Download Summary",
                       st.session_state.summary_text,
                       file_name="summary.txt",
                       mime="text/plain")
