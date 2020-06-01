# Description
Displays a new vocabulary word everyday in your terminal. Please read everything before asking questions.

# Important Notes
- If you just want the Python script, just look at vocab.py and be on your merry way. If you're interested in the Hyper config or Bash stuff, keep reading.
- I made this on Mac OS running Bash terminal; If you're on Windows, I'm not sure if I can hep troubleshoot.
- I use a terminal called Hyper (https://hyper.is).
- The new Mac OS Catalina uses Zsh instead of Bash, but I switched back to Bash using Hyper (in the config file, it is on line 108). Please change this accordingly as there are instructions in the file.
- On Catalina, switching back to Bash gives an ugly message everytime a new terminal window opens, so I configured my Hyper terminal to clear the screen everytime a new window opens (line 149).
- On line 150 of the config file, the command outputs the quote 'never mind perfection, focus on progress.' in color. I'm not sure if it works on other shells, but works fine on Bash.
- On line 151, it prints a new line
- On line 152, it calls my custom Bash command that will run the Python script
- I only configured by .bash_profile (not .bashrc) to have the custom 'vocab' command and to change the command "prompt"

# Files
- .hyper.js - the Hyper config file
- vocab.py - the python file to scrape dictionary.com for the word of the day
- .bash_profile - my bash configuration

# Requirements
pip install requests
pip install bs4

# FAQ
- Coming soon
