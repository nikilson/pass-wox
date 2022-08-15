import os
import re
import subprocess

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
subprocess.run("Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Hello World')")
