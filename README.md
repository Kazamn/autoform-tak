Telkom University TAK Autoform

An automation script to extract information from PDF certificates using **Google Gemini AI** and automatically input it into the Telkom University Student Activity Transcript (TAK) web form.

System Requirements
* Windows and Mac operating systems.
* Chromium-based browser (Edge / Chrome / Brave / Opera).
* Active Google Gemini API Key (via Google AI Studio).

Installation & Usage

1. Download the script

2. Configure API Key
Create a new file named `.env` in the project folder, then populate it using the following format:

GEMINI_API_KEY=insert_gemini_api_key_here

3. Prepare Certificate Documents
Run the script for the first time so that the `certificate_pdf` folder is automatically created. Move all certificate files (maximum 2MB per file) into that folder.

4. Run the Application
Open the application by double-clicking the `autoform.bat` file or run it directly from the terminal:

python autoform.py


⚠️ Important Note
Ensure you are logged into the Telkom University TAK portal in the browser window that opens automatically before pressing the ENTER key in the terminal to start the data injection process.
