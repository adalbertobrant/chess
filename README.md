# ♟️ AI Chess Coach with Streamlit and Gemini ♟️

## Overview

This project provides an interactive AI Chess Coach application built with Streamlit. It leverages the power of Google's Gemini 1.5 Flash model to analyze chess games (provided in PGN format) and offer personalized, beginner-friendly feedback. Forget about complex chess jargon; this coach explains your game in simple terms, highlights key moments, and provides actionable tips for improvement.

## Features

-   **PGN Analysis:** Paste your game in Portable Game Notation (PGN) format.
-   **Player-Centric Feedback:** Get analysis tailored to whether you played as White or Black.
-   **Beginner-Friendly Explanations:** The AI avoids technical chess notation, focusing on clear, understandable language.
-   **Structured Feedback:** Analysis is broken down into sections: Overview, Opening, Middlegame, Endgame, General Summary (with a star rating for various aspects), and Tips for Improvement.
-   **Secure API Key Handling:** Uses a `.env` file to securely manage your Gemini API key.

## Getting Started

Follow these steps to set up and run the AI Chess Coach on your local machine.

### Prerequisites

-   Python 3.8+
-   A Google Gemini API Key (get one from [Google AI Studio](https://aistudio.google.com/))

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/adalbertobrant/chess.git
    cd xadrez
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Create a `.env` file:**
    In the root directory of the project, create a file named `.env` and add your Gemini API key:
    ```
    API_KEY_GEMINI="YOUR_GEMINI_API_KEY"
    ```
    Replace `"YOUR_GEMINI_API_KEY"` with your actual API key.

2.  **Review the AI Persona:**
    The AI's behavior and analysis style are defined in `prompts/prompts.txt`. You can review or modify this file to adjust the coach's persona.

### Running the Application

1.  **Ensure your virtual environment is active.**
2.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

3.  **Access the application:**
    Your web browser will automatically open to the Streamlit application (usually at `http://localhost:8501`).

## Usage

1.  Paste the PGN of your chess game into the provided text area.
2.  Select whether you played as "Brancas" (White) or "Pretas" (Black).
3.  Click the "Analisar Partida" button.
4.  The AI Chess Coach will generate a detailed analysis of your game.

## Project Structure

```
.
├── .env                  # Environment variables (e.g., API keys)
├── README.md             # Project documentation
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
└── prompts/
    └── prompts.txt       # AI persona and instructions for Gemini model
```

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

## License

[MIT License]
