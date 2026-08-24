# Telkom University TAK Autoform 

An automated browser extension to extract information from PDF certificates using **Google Gemini AI** and seamlessly inject it into the Telkom University Student Activity Transcript (TAK) web form.

This project has evolved from a Python/Selenium script into a lightweight, secure, and fast **Chromium Browser Extension**.

## Features
* **AI-Powered Extraction:** Uses Gemini AI to intelligently read certificate details, including durations, titles, and organizers.
* **Smart Angular Bypass:** Smartly handles dynamic dropdowns and bypasses restrictive DOM resets on the Telkom University portal using Native Setters.
* **Smart Date Calculation:** Automatically calculates logical start dates based on the course duration stated on the certificate.
* **Privacy First (BYOK):** Bring Your Own Key. Your Gemini API Key is stored securely in your browser's local storage, not on any external server.
* **Cross-Platform:** Works directly in the browser on Windows, macOS, and Linux—no Python installation or terminal required!

## System Requirements
* A Chromium-based browser (Microsoft Edge, Google Chrome, Brave, etc.).
* An active Google Gemini API Key. You can get it for free at [Google AI Studio](https://aistudio.google.com/app/apikey).

## Installation Guide (Browser Extension)

1. **Download the Project:** Clone this repository or download it as a `.zip` file and extract it to a folder on your local machine.
2. **Open Extensions Page:** 
   * In Microsoft Edge: Go to `edge://extensions/`
   * In Google Chrome: Go to `chrome://extensions/`
3. **Enable Developer Mode:** Turn on the **Developer mode** toggle (usually located in the sidebar or top right corner).
4. **Load the Extension:** Click the **Load unpacked** button and select the `extension` folder from the extracted project directory.
5. *Voila!* The Autoform TAK icon will now appear in your browser's toolbar.

## 📖 How to Use

1. **Set Up API Key:** Click the extension icon, paste your Gemini API Key into the provided field, and click **Save Key**. (You only need to do this once).
2. **Open the TAK Portal:** Log in to your SITU Telkom University account and navigate to the TAK input page.
3. **Inject Data:** 
   * Click the extension icon again.
   * Upload your certificate file (`.pdf`, maximum size 2MB).
   * Click **Analyze & Inject Form**.
4. **Review & Submit:** Wait for the AI to process the document. You will see the dropdowns and text fields being filled automatically. Review the injected data to ensure accuracy, then submit the form manually on the website!

---
*Note: The original Python script is still available in the root repository (`autoform.py`) for legacy or terminal-based usage, but the Browser Extension method above is highly recommended for the best and most seamless experience.*