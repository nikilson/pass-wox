def clear_clipboard(sec = 45):
    from time import sleep
    from ctypes import windll
    sleep(sec)
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

def show_text(text):
    import os
    cwd = os.getcwd()
    direct = os.path.join(cwd, "CommandlineTextBox.exe")
    import subprocess 
    subprocess.run(["CommandlineTextBox.exe", text])