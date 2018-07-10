#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '

# Source other files for more organization
source .export
source .alias

# Show neofetch output when bash is launched if it is installed
if command -v neofetch > /dev/null; then neofetch; fi
