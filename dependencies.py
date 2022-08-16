def clear_clipboard():
    import subprocess
    subprocess.Popen(['CleanClipboard.exe'])

def show_text(text):
    import os
    cwd = os.getcwd()
    direct = os.path.join(cwd, "CommandlineTextBox.exe")
    import subprocess 
    subprocess.run(["CommandlineTextBox.exe", text])