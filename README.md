# Description
Displays a new vocabulary word everyday in your terminal using python. I assume you found this on r/Python, know about python, and how to use it in your OS. I also assume you know how to use the shell your computer is running. If you have questions that aren't related to anything OS specific, feel free to ask. 

# Important Notes
- If you just want the Python script, just look at vocab.py and be on your merry way. If you're interested in the Hyper config or Bash stuff, keep reading.
- I made this on Mac OS running Bash terminal; If you're on Windows, I'm not sure if I can help troubleshoot.
- I use a terminal called Hyper (https://hyper.is).
- The new Mac OS Catalina uses Zsh instead of Bash, but I switched back to Bash using Hyper (in the config file, it is on line 108). Please change this accordingly as there are instructions in the file.
- On Catalina, switching back to Bash gives an ugly message everytime a new terminal window opens, so I configured my Hyper terminal to clear the screen everytime a new window opens (line 149).
- On line 150 of the config file, the command outputs the quote 'never mind perfection, focus on progress.' in color. I'm not sure if it works on other shells, but works fine on Bash.
- On line 151 of the config file, it prints a new line
- On line 152 of the config file, it calls my custom Bash command that will run the Python script
- I only configured by .bash_profile (not .bashrc) to have the custom 'vocab' command and to change the command "prompt"
- Please change the path on the 'vocab' command in the .bash_profile according to where you clone/download

# Files
- .hyper.js - The Hyper config file
- .bash_profile - My bash configuration
- vocab.py - The python file to scrape dictionary.com for the word of the day

# Requirements
- pip install requests
- pip install bs4

# FAQ
- Coming soon
