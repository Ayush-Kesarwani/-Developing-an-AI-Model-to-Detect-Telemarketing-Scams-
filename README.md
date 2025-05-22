# -Developing-an-AI-Model-to-Detect-Telemarketing-Scams-
Architected an AI-driven model to detect purpose and legitmacy of the calls with 93.05% accuracy using OpenAI’s GPT-4 and Whisper models.

Implementation Workflow
The implementation involves several stages, including audio preprocessing, transcription, scam classification, and result generation. The workflow is as follows:
Step 1: Audio Processing & Preprocessing
•	Objective: Convert raw telemarketing audio files into a format suitable for transcription.
•	Process:
•	The pydub library is used to load and preprocess the audio.
•	Each audio file is trimmed to the first 15 seconds to ensure only the initial part is analyzed.
•	The trimmed audio is saved in .wav format.
 

Step 2: Audio Transcription using Whisper AI
•	Objective: Convert speech from the audio file into text for further analysis.
•	Process:
o	The trimmed .wav file is passed to OpenAI’s Whisper model for speech-to-text conversion.
o	The transcribed text is stored for scam classification.
 
Figure 4.2.2 Transcribed text output
•	Key Advantage:
Whisper AI ensures high transcription accuracy, even in the presence of background noise and different accents.
Step 3: Scam Classification Using GPT-4
•	Objective: Classify the telemarketing call based on its content.
•	Process:
•	The transcribed text is analyzed using GPT-4 to extract key details:
	Company Name (if mentioned)
	Purpose of the Call (e.g., product promotion, scam, emergency)
	Legitimacy (Legitimate / Scam)
•	A structured prompt ensures precise classification.
 
