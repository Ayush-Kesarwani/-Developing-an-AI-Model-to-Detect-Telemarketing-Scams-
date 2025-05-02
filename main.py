from openai import OpenAI
from pydub import AudioSegment
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from environment variables
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
print("API Key:", os.getenv("OPENAI_API_KEY"))

# Now you can use the OpenAI API
client = OpenAI()

# Function to trim audio to the first 15 seconds
def trim_audio(audio_file_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)
    
    # Trim to 15 seconds if the file is longer than that
    if len(audio) > 15000:  # 15 seconds = 15000 milliseconds
        audio = audio[:15000]
    
    # Save the trimmed audio to a temporary file
    trimmed_audio_path = "trimmed_audio.wav"
    audio.export(trimmed_audio_path, format="wav")
    
    return trimmed_audio_path
    

# Function to classify the telemarketing call from transcribed text
def classify_telemarketing_call_from_text(transcribed_text):
    prompt = f"""
        You are an expert conversation analyst. Your task is to analyze a recorded conversation, identify key details, and classify its intent. Please focus on extracting only the essential information.

        Analyze the conversation below and provide the following details:
        1. The name of the telemarketing company or organization involved (if mentioned). If not mentioned, state "Not provided."
        2. The specific purpose of the call (e.g., product promotion, survey, donation request, emergency, alert, scam). Ensure the purpose is as specific as possible.
        3. Determine if the call appears to be legitimate or a scam. Base your decision on language cues, the stated purpose, and any indicators of fraud.

        Here is the transcribed conversation:
        '{transcribed_text}'

        Respond with your analysis in the following format:
        - Company Name: [Name or "Not provided"]
        - Purpose: [Purpose]
        - Legitimacy: [Legitimate/Scam]

        Ensure your response is concise, unambiguous, and directly follows this format. Do not include any additional commentary.
        """
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content



# Path to your audio file
audio_file_path = "Technician-Assignment.wav"

# Trim the audio to the first 15 seconds
trimmed_audio_path = trim_audio(audio_file_path)

# Open the trimmed audio file and pass it for transcription
with open(trimmed_audio_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

# Print the transcribed text
transcribed_text = transcription.text
print("Transcription Text:", transcribed_text)

# transcribed_text = "হ্যালো, আমি সঞ্জয়, আপনার প্যাকেজটি আজ আমাদের ডেলিভারি দলের মাধ্যমে পাঠানো হবে। আপনি যদি কোনো সমস্যার মুখোমুখি হন, তবে দয়া করে আমাদের গ্রাহক সহায়তা নম্বরে যোগাযোগ করুন। ধন্যবাদ!"
# transcribed_text="Allô, c'est une urgence ! J'ai besoin d'une ambulance immédiatement ! Mon ami est tombé et il perd beaucoup de sang. Il se trouve au 25 rue de la République, s'il vous plaît, aidez-nous !"

# Classify the telemarketing call using GPT-4
classification = classify_telemarketing_call_from_text(transcribed_text)
print("Classification Result:\n", classification)
