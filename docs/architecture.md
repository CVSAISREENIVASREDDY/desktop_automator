# System Architecture

This document outlines the architecture of the Desktop Automator project.

## Overview

The Desktop Automator is built with a modular architecture that separates the user interface, core logic, and tools. This design allows for easy extension and maintenance.

### Components

1.  **GUI (Graphical User interface)**
    * **Technology**: The GUI is built using PyQt5, providing a robust and cross-platform user interface.
    * **Main Window**: The `ChatWindow` class is the main interface where users can interact with the assistant.
    * **Real-time Interaction**: The application uses `asyncio` and `qasync` to handle asynchronous operations, ensuring the GUI remains responsive while performing tasks.
2.  **Core Logic**
    * **Main Entry Point**: `main.py` is the entry point of the application, responsible for initializing the event loop and showing the main window.
    * **Asynchronous Handling**: The application leverages `asyncio` to manage long-running tasks without blocking the user interface.
3.  **Agents**
    * **God Agent**: The `god` agent is the primary decision-maker, responsible for interpreting user commands and selecting the appropriate tool.
    * **Watcher Agent**: The `watcher` agent can analyze the screen and provide descriptions, enabling more complex interactions.
4.  **Models**
    * **Generative AI**: The project uses the Gemini API to power its natural language understanding and generation capabilities.
    * **Web Model**: The `web_model` is a specialized model for extracting information from web pages, such as finding the XPath of an element.
5.  **Tools**
    * **Tool Abstraction**: Tools are organized into separate modules based on their functionality (e.g., `gui_tools`, `web_tools`, `clipboard_tools`).
    * **Extensibility**: The architecture makes it easy to add new tools by creating new functions and registering them in the `FUNCTIONS` dictionary.

### Directory Structure