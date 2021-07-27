#!/usr/bin/env python3
import sys
import webbrowser
import functions

REPO_LINK = "https://github.com/ZeroKun265/custom-bash-echo-generator"
echo_command = ""
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
          print("Any typo in the color/stylenwill be ignored, only recognized keywords will actually be used")
          print("For more info check the Github's Repo\n\n")
          print("Colors and style may be interpreted differently on different terminals")
          instr2 = input("Github:  G/g/github\nBack:    B/b/back\n\n")
          if instr2 in ["G", "g", "github"]:
              print(f"Trying to open '{REPO_LINK}'\nIf nothing happens then the enviroment variable BROWSER is not available, just copy the link by hand")
          if instr2 in ["B",  "b", "back"]:
              help  = False
              menu = True
     #start loop:
     components = []
     while start:
          component = []
          text = input("Insert some text, you'll later pick color and style:\n")
          print(f"Now select colors and styling for {text}\n(not inserting any color or style means it will stary as default)")
          print("Here are the available colors and styles")
          functions.print_colors()
          functions.print_highlights()
          getting_style = True
          styles = []
          while getting_style:
               print("To add a color or style, input its name, input L/l/list to see again the list of styles and colors\nInput Q/q/quit to stopp adding styles")
               print(f"Current styles: {styles}")
               style = input("\n")
               if style in ["L", "l", "list"]:
                   functions.print_colors()
                   functions.print_highlights()
               elif style in ["Q", "q", "quit"]:
                   getting_style = False
               else:
                   styles.append(style)
          component.append(text)
          component.append(styles)
          component.append(functions.generate_escapes(component[1]))
          print(f"Here is the component you created: {component[0:2]}")
          while True:
               keep = input("You want to keep the component? [Y/N]")
               if keep in ["Y", "y", "yes"]:
                    components.append(component)
                    break
               elif keep in ["N", "n", "no"]:
                    print("Discarded component")
                    break
               else:
                    print("Unrecognized character, try again\n")
          while True:
               more = input("Do you want to stop and get your echo command?[Y/N]")
               if more in ["Y", "y", "yes"]:
                    start = False
                    help = False
                    finished = True
                    echo_command = functions.generate_echo(components)
                    break
               elif more in ["N", "n", "no"]:
                    break
               else:
                    print("Unrecognized character\n")


print("Here is your echo command:\n")
print(echo_command)

print("And here is a preview of it")
preview = echo_command[9:-1]
preview = preview.encode("latin-1", "backslashreplace").decode("unicode_escape")
print(preview)
