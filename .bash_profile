# Changes the command "prompt"
export PS1="\[$(tput setaf 010)\]$ \[$(tput sgr0)\]"
# $(tput setaf 046) # Blue

# source ~/Documents/Programming/Bash/custom_commands.sh

function vocab() {
  python3 ~/Documents/Programming/Python/Projects/Vocab/vocab.py
}

# Setting PATH for Python 3.8
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
export PATH