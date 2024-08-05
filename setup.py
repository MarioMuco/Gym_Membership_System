import sys
from cx_Freeze import setup, Executable

# Increase the recursion limit
sys.setrecursionlimit(5000)

# For .exe file conversion
build_exe_options = {
    "packages": [
        "customtkinter",
        "cv2",
        "datetime",
        "matplotlib",
        "numpy",
        "PIL",
        "qrcode",
        "random",
        "requests",
        "sqlite3",
        "string",
        "tkcalendar",
        "tkinter"
    ],
    "includes": ["tkinter", "tkcalendar"],
    "include_files": [
        ("SQLite db", "SQLite db"),
        ("templates", "templates"),
        ("requirements.txt", "requirements.txt"),
        ("setup.txt", "setup.txt"),
    ],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this option if you want to hide the console window

# Path to your icon file
icon_path = "logo.ico"

executables = [Executable("gym.py", base=base, icon=icon_path)]

setup(
    name="Palestrafy",
    version="1.1",
    description="Management Software",
    options={"build_exe": build_exe_options},
    executables=executables,
)
