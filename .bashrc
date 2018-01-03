# Standard commands
alias clr=clear
alias cls=clear
alias ls='ls -1 --color=always --sort=extension'

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."

# Make things look nice

# Directories: Pink
LS_COLORS=$LS_COLORS:'di=1;35:' ; export LS_COLORS

# Text documents: Green
LS_COLORS=$LS_COLORS:'*.pdf=0;92:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.doc=0;92:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.docx=0;92:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.txt=0;92:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.odt=0;92:' ; export LS_COLORS

# Images: Cyan
LS_COLORS=$LS_COLORS:'*.png=0;96:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.eps=0;96:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.jpg=0;96:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.JPG=0;96:' ; export LS_COLORS

# LaTeX:
LS_COLORS=$LS_COLORS:'*.tex=0;33:' ; export LS_COLORS	

# Zip File: Red

# Code : Yellow
LS_COLORS=$LS_COLORS:'*.py=0;93:' ; export LS_COLORS	
LS_COLORS=$LS_COLORS:'*.java=0;93:' ; export LS_COLORS	
LS_COLORS=$LS_COLORS:'*.cpp=0;93:' ; export LS_COLORS	
LS_COLORS=$LS_COLORS:'*.cc=0;93:' ; export LS_COLORS	
LS_COLORS=$LS_COLORS:'*.cpp=0;93:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.m=0;93:' ; export LS_COLORS

# Data Files :
LS_COLORS=$LS_COLORS:'*.mat=0;97:' ; export LS_COLORS
LS_COLORS=$LS_COLORS:'*.dat=0;97:' ; export LS_COLORS

# Extract comand
extract () {
   if [ -f $1 ] ; then
       case $1 in
           *.tar.bz2)   tar xvjf $1    ;;
           *.tar.gz)    tar xvzf $1    ;;
           *.bz2)       bunzip2 $1     ;;
           *.rar)       unrar x $1       ;;
           *.gz)        gunzip $1      ;;
           *.tar)       tar xvf $1     ;;
           *.tbz2)      tar xvjf $1    ;;
           *.tgz)       tar xvzf $1    ;;
           *.zip)       unzip $1       ;;
           *.Z)         uncompress $1  ;;
           *.7z)        7z x $1        ;;
           *)           echo "Error: Unable to extract '$1'..." ;;
       esac
   else
       echo "Error: '$1' is not a valid file"
   fi
 }

# Start it
# setterm -bfreq 0
ls
