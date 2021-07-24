#!/data/data/com.termux/files/usr/bin/env python3
import sys
import webbrowser
import functions

REPO_LINK = "https://github.com/ZeroKun265/custom-bash-echo-generator"

help     = False
start    = False
finished = False
while not finished:
     print("Welcome to custom echo generstor v1.0.0")
     menu = True
     while menu:
          instr = input("Help:   H/h/help\nQuit:   Q/q/quit\nStart:  S/s/start\n\n")
          if instr in ["H", "h", "help"]:
              help = True
              menu = False
          if instr in ["Q", "q", "quit"]:
              print("\n\n")
              exit()
          if instr in ["S", "s", "start"]:
              start = True
              menu  = False
     
     #help loop:
     while help:
          print("Custom Echo Generator help section:\n")
          print("You will be adding pieces of text as components\nThe program will ask you to add a piece of text, then any styling(example: bold) and then a color")
          print("The program won't detect errors in what you type(if you say red instead of RED) so make sure it's right")
          print("For more info check the Github's Repo\n\n")
          instr2 = input("Github:  G/g/github\nBack:    B/b/back\n\n")
          if instr2 in ["G", "g", "github"]:
              print(f"Trying to open '{REPO_LINK}'\nIf nothing happens then the enviroment variable BROWSER is not available, just copy the link by hand")
          if instr2 in ["B",  "b", "back"]:
              help  = False
              menu = True
     #start loop:
     while start:
          print("not yet available")
          exit()
