# -*- coding: utf-8 -*-
import os
import re
import subprocess 
from wox import Wox

class UnixPassMenu(Wox):

    # query is default function to receive realtime keystrokes from wox launcher
    def query(self, query):
        results = []
        usr = os.path.expanduser('~')
        pass_dir = os.path.join(usr, '.password-store')
        password_files = [passwd_file for passwd_file in os.listdir(pass_dir) if not passwd_file.startswith('.')]
        # password_files = ["hi", "bye", "hellow"]
        rexp = re.compile(query)
        password_files = list(filter(rexp.match, password_files))
        for passwd in password_files:
            results.append({
                "Title": "{}".format(passwd[:-4]),
                "SubTitle": "Key Word: {}".format(query),
                # "IcoPath":"Images/app.png",
                "ContextData": "ctxData",
                "JsonRPCAction": {
                    'method': 'take_action',
                    'parameters': ["{}".format(passwd), "{}".format(pass_dir)],
                    'dontHideAfterAction': False
                }
            })
        return results

    # context_menu is default function called for ContextData where `data = ctxData`
    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format("Show Full Message"),
            "IcoPath":"Images/app.png"
        })
        return results

    def take_action(self, filename, pass_dir):
        # Choose what to trigger on pressing enter on the result.
        # use SomeArgument to do something with data sent by parameters.
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        filename = os.path.join(pass_dir, filename)
        file = open(filename, "rb")
        cipher = file.read()
        file.close()
        keyid_file = os.path.join(pass_dir, ".gpg-id")
        idfile = open(keyid_file, "r")
        keyid = idfile.read()
        idfile.close()
        output = subprocess.check_output(["gpg", "-u", keyid, "-d", "{}".format(filename)], startupinfo=si)
        subprocess.run("clip.exe", universal_newlines=True, input=output.decode(), startupinfo=si)
        # os.system("echo {} | clip.exe".format(content))

        return None

if __name__ == "__main__":
    UnixPassMenu()
