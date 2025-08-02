# Desktop Automator

This project is a desktop assistant that can perform various tasks on your computer through a chat interface.

## Introduction

The Desktop Automator is a powerful tool that allows you to control your desktop using simple chat commands. It can open applications, browse the web, manage your files, and much more. The application features a sleek, modern chat window and can be controlled via hotkeys for quick access.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/desktop-automator.git](https://github.com/your-username/desktop-automator.git)
    cd desktop-automator
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your environment:**
    * Create a `.env` file in the root directory.
    * Add your Gemini API key to the `.env` file:
        ```
        GEMINI_API_KEY=your_api_key
        ```
4.  **Run the application:**
    ```bash
    python main.py
    ```

## Features

* Chat-based control of your desktop.
* Support for hotkeys to toggle the chat window.
* Extensible toolset for various automation tasks.
* Modern and user-friendly interface.