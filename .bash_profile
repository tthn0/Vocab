# Changes the command "prompt"
export PS1="\[$(tput setaf 010)\]$ \[$(tput sgr0)\]"

# Custom Command - please modify the path to the vocab.py file accordingly
function vocab() {
  python3 ~/Downloads/Vocab/vocab.py
}

# Setting PATH for Python 3.8
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
export PATH
