# Description
- UPDATED 6/2/2020: Please read the important notes! If you cloned/downloaded before 6/2, I have updated this repository. Instead of using hyper-init to run commands, I just put them in .bash_profile
- Displays a new vocabulary word everyday in your terminal using python. I assume you found this on r/Python, know about python, and how to use it in your OS. I also assume you know how to use the shell your computer is running. If you have questions that aren't related to anything OS specific, feel free to ask. My reddit is https://www.reddit.com/user/ImportantDesk

# Important Notes
- If you just want the Python script, just look at vocab.py and be on your merry way. If you're interested in the Hyper configuration or Bash stuff, keep reading.
- I made this on Mac OS running Bash terminal; If you're on Windows, I'm not sure if I can help troubleshoot.
- I use a terminal called Hyper (https://hyper.is).
- The new Mac OS Catalina uses Zsh instead of Bash, but I switched back to Bash using Hyper (in the config file, it is on line 108). Please change this accordingly as there are instructions in the file.
- On Catalina, switching back to Bash gives an ugly message everytime a new terminal window opens, so I configured .bash_profile to remove the message. If you never got the message in the first place, you can remove lines 1-3 on the .bash_profile
- The code in .bash_profile is commented. Please look thru and make changes if needed (change the path on the 'vocab' command in the .bash_profile according to where you clone/download)
- On lines 155-157 of the .hyper.js file, those are the plugins I prefer.
- On lines 158-161 of the .juper.js file, I left cool plugins for you guys to check out, but I don't use them atm

# Files
- .hyper.js - My Hyper config file
- .bash_profile - My bash configuration
- vocab.py - The python file to scrape dictionary.com for the word of the day

# Requirements
- pip install requests
- pip install bs4

# FAQ
- Q: How do you get your terminal to look like that? A: I use a terminal called Hyper with a theme called 'hyperterm-material'
