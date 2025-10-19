import pyautogui as pg
import pyperclip
import subprocess
import os
import fnmatch

def write_code(code: str) -> dict:
    """
    types the given code into the active text field
    Args:
        code (str): the code to type
    """
    for line in code.split("\n"):
        pg.hotkey("home")
        pyperclip.copy(line)
        pg.hotkey("ctrl", "v")
        pg.press("enter")
    return {"message": "done"}

def write_text(text: str) -> dict:
    """
    types the given text into the active text field
    Args:
        text (str): the text to type
    """
    pyperclip.copy(text)
    pg.hotkey("ctrl", "v")
    return {"message": "done"}


def press_shortcut(shortcut):
    pg.hotkey(*shortcut)


def update_files_list():
    directories = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Downloads"),
        os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Videos"),
        os.path.join(os.path.expanduser("~"), "Pictures"),
        os.path.join(os.path.expanduser("~"), "Music"),
    ]
    skip_patterns = [
        "*/.git/*",
        "*/.vscode/*",
        "*/__pycache__/*",
        "*/node_modules/*",
        "*/venv/*",
        "*/.venv/*",
        "*/envi/*",
        "*/Music/*",
        "*/Python-3.10.18/*"
    ]

    with open("files.txt", "w", encoding="utf-8") as f:
        for directory in directories:
            for root, _, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    if not any(fnmatch.fnmatch(filepath, pattern) for pattern in skip_patterns):
                        try:
                            f.write(filepath + "\n")
                        except UnicodeEncodeError:
                            print(f"Skipping file with encoding issues: {filepath}")


def get_files_list():
    update_files_list()
    with open("files.txt", "r", encoding="utf-8") as f:
        return f.read()


def run_command(command):
    try:
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {"output": output.stdout, "error": output.stderr}
    except Exception as e:
        return {"error": str(e)}


def take_screenshot():
    pg.screenshot("screenshot.png")
