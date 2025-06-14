import json
import keyboard
import subprocess

# Load hotkeys and messages
with open('messages.json', 'r') as f:
    hotkeys = json.load(f)

def send_chat(message):
    # Run AHK script with the message as argument
    subprocess.Popen([r'your path to autoHotKey.exe', 'send_chat.ahk', message])

# Register all hotkeys
for combo, msg in hotkeys.items():
    keyboard.add_hotkey(combo, send_chat, args=(msg,))
    print(f"Hotkey {combo} registered for message: {msg}")

print("Running. Press ESC to quit.")
keyboard.wait('esc')