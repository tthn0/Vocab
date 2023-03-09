# Silences the deprecation warning
export BASH_SILENCE_DEPRECATION_WARNING=1

# Changes the command "prompt"
export PS1="\[$(tput setaf 010)\]$ \[$(tput sgr0)\]"

# Displays quote
echo never $(tput setaf 10)mind$(tput sgr0) $(tput setaf 172)perfection$(tput sgr0), $(tput setaf 14)focus$(tput sgr0) $(tput setaf 11)on$(tput sgr0) progress.
echo

# Runs the vocab.py script. Change the path accordingly
python3 ~/path/to/Vocab/vocab.py
