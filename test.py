import os
import re
import subprocess
from time import sleep
from dependencies import clear_clipboard
from dependencies import show_text
import multiprocessing
import threading
usr = os.path.expanduser('~')
pass_dir = os.path.join(usr, '.password-store')
password_files = [passwd_file for passwd_file in os.listdir(pass_dir) if not passwd_file.startswith('.')]
print(password_files)
r = re.compile("ud")
newlist = list(filter(r.match, password_files)) # Read Note below
print(newlist)
filename = os.path.join(pass_dir, newlist[0])
file = open(os.path.join(pass_dir, newlist[0]), "rb")
cipher = file.read()
file.close()
keyid_file = os.path.join(pass_dir, '.gpg-id')
idfile = open(keyid_file, "r")
keyid = idfile.read()
idfile.close()
output = subprocess.check_output(["gpg", "-u", keyid, "-d", "{}".format(filename)]).decode()
print(output)
subprocess.run("clip.exe", universal_newlines=True, input=output[:output.find("\n")])
thred2 = multiprocessing.Process(target = show_text, args = (output[output.find('\n')+1:],))
thred = multiprocessing.Process(target = clear_clipboard)
# thred.daemon = True
if __name__ == '__main__':
    thred.start()
    thred2.start()

# thred.join()
print(thred.is_alive())
if __name__ == '__main__':
    thred.terminate()
print(thred.is_alive())
# sleep(5)
# if __name__ == '__main__':
#     thred2.terminate()