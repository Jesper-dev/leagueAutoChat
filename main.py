import os
import json
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox
import keyboard
# Get the folder where the EXE was launched from
BASE_DIR = os.getcwd()

# Load messages
with open(os.path.join(BASE_DIR, 'messages.json'), 'r') as f:
    hotkeys = json.load(f)

# Send chat messages
def send_chat(message):
    try:
        ahk_path = r'your path to autohotkey.exe'
        ahk_file = os.path.join(BASE_DIR, 'send_chat.ahk')
        subprocess.Popen([ahk_path, ahk_file, message])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send message:\n{e}")

# Set up hotkeys
def register_hotkeys():
    for key_combo, message in hotkeys.items():
        keyboard.add_hotkey(key_combo, lambda m=message: send_chat(m))

# Run hotkeys in a background thread so GUI doesn't freeze
def start_hotkey_thread():
    thread = threading.Thread(target=register_hotkeys, daemon=True)
    thread.start()

# Build UI
root = tk.Tk()
root.title("Lague auto chat")

tk.Label(root, text="Click to send messages in chat").pack(pady=10)

for key, msg in hotkeys.items():
    btn = tk.Button(root, text=f"{key.upper()}: {msg}", width=40, command=lambda m=msg: send_chat(m))
    btn.pack(pady=5)

tk.Label(root, text="Make sure that League is focused.").pack(pady=10)

# Start hotkey detection
start_hotkey_thread()

root.mainloop()