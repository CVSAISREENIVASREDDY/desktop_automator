
# Desktop Automator

This project is a desktop assistant that can perform various tasks on your computer through a chat interface.

## Introduction

The Desktop Automator is a powerful tool that allows you to control your desktop using simple chat commands. It can open applications, browse the web, manage your files, and much more. The application features a sleek, modern chat window and can be controlled via hotkeys for quick access.

## System Architecture

The Desktop Automator is built with a modular architecture that separates the user interface, core logic, and tools. This design allows for easy extension and maintenance.

```
[User] -> [GUI (chat.py)] -> [Agent (god.py)] -> [Model (god_model.py)] -> [Tools]
   ^                                                                         |
   |-------------------------------------------------------------------------|
```

### Components

1.  **GUI (Graphical User Interface)**
    *   **File:** `gui/chat.py`
    *   **Technology:** The GUI is built using PyQt5, providing a robust and cross-platform user interface.
    *   **Main Window:** The `ChatWindow` class is the main interface where users can interact with the assistant.
    *   **Real-time Interaction:** The application uses `asyncio` and `qasync` to handle asynchronous operations, ensuring the GUI remains responsive while performing tasks.

2.  **Core Logic**
    *   **Main Entry Point:** `main.py` is the entry point of the application, responsible for initializing the event loop and showing the main window.
    *   **Asynchronous Handling:** The application leverages `asyncio` to manage long-running tasks without blocking the user interface.

3.  **Agents**
    *   **God Agent (`agents/god.py`):** The `god` agent is the primary decision-maker, responsible for interpreting user commands and selecting the appropriate tool. It receives prompts from the GUI and passes them to the `god_model`.
    *   **Watcher Agent (`agents/watcher.py`):** The `watcher` agent can analyze the screen and provide descriptions, enabling more complex interactions. It uses the `watcher_model` to describe the screen's contents.

4.  **Models**
    *   **God Model (`models/god_model.py`):** This model is the core of the assistant's intelligence. It uses the Gemini API to understand user prompts and decide which tool to use. It receives the user's prompt and a list of available tools, and returns the name of the tool to execute and the arguments to use.
    *   **Watcher Model (`models/watcher_model.py`):** This model is used by the `watcher` agent to describe the contents of the screen. It takes a screenshot of the screen and uses the Gemini API to generate a description.
    *   **Web Model (`models/web_model.py`):** The `web_model` is a specialized model for extracting information from web pages, such as finding the XPath of an element.

5.  **Tools**
    *   **Tool Abstraction:** Tools are organized into separate modules based on their functionality (e.g., `gui_tools`, `web_tools`, `clipboard_tools`).
    *   **Extensibility:** The architecture makes it easy to add new tools by creating new functions and registering them in the `FUNCTIONS` dictionary in `tools/all_tools.py`.
    *   **Available Tools:**
        *   `clipboard_tools.py`: `get_clipboard_text`, `set_clipboard_text`, `get_selected_text`
        *   `gui_tools.py`: `press_key`, `close_tab`, `close_window`, `take_screenshot`, `press_shortcut`, `send_message_or_text`
        *   `music_tools.py`: `play_song`, `control_music`
        *   `selenium_tools.py`: A suite of tools for browser automation, including `launch_browser`, `navigate_current_tab`, `click_element_by_description`, and more.
        *   `utility_tools.py`: `get_current_datetime`, `open_apps`, `open_file`, `open_folder`, `execute_command`
        *   `web_tools.py`: `open_url`, `search_web`

### Flowchart

```
+-----------------+      +-----------------+      +----------------+      +--------------------+
|   User Input    |----->|   GUI (PyQt5)   |----->|  God Agent     |----->| God Model (Gemini) |
+-----------------+      +-----------------+      |(agents/god.py) |      |(models/god_model.py)|
                               ^  |                +----------------+      +--------------------+
                               |  |                                             |
                               |  v                                             v
+-----------------+      +-----------------+      +----------------+      +--------------------+
| Watcher Agent   |<-----| Watcher Model   |      | Tool Execution |<-----|   Tool Selection   |
|(agents/watcher.py)|    |(models/watcher.py)|    +----------------+      +--------------------+
+-----------------+      +-----------------+
```

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CVSAISREENIVASREDDY/desktop_automator.git
    cd desktop-automator
    ```
2.  **Create and activate a virtual environment:**
    *   **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **On macOS and Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your environment:**
    *   Create a `.env` file in the root directory.
    *   Add your Gemini API key to the `.env` file:
        ```
        GEMINI_API_KEY=your_api_key
        ```
5.  **Run the application:**
    ```bash
    python main.py
    ```

## Features

*   Chat-based control of your desktop.
*   Support for hotkeys to toggle the chat window.
*   Extensible toolset for various automation tasks.
*   Modern and user-friendly interface.
