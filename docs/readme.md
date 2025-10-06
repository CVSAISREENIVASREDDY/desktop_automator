# Desktop Automator 

This project is a desktop assistant that can perform various tasks on your computer through a chat interface.

## Introduction

The Desktop Automator is a powerful tool that allows you to control your desktop using simple chat commands. It can open applications, browse the web, manage your files, and much more. The application features a sleek, modern chat window and can be controlled via hotkeys for quick access.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CVSAISREENIVASREDDY/desktop_automator.git
    cd desktop-automator
    ```
2.  **Create and activate a virtual environment:**
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **On macOS and Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your environment:**
    * Create a `.env` file in the root directory.
    * Add your Gemini API key to the `.env` file:
        ```
        GEMINI_API_KEY=your_api_key
        ```
5.  **Run the application:**
    ```bash
    python main.py
    ```

## Features

* Chat-based control of your desktop.
* Support for hotkeys to toggle the chat window.
* Extensible toolset for various automation tasks.
* Modern and user-friendly interface.