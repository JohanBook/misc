#!/bin/bash
# Configure an Ubuntu Python server
# run using <host name><admin password>

# Install security updates
apt update -y && apt upgrade -y

# Set host name
hostnamectl set-hostname $1
# set hostname in /etc/hosts

# Create limited user account
adduser admin -p $2
adduser admin sudo

# Setup ssh

# Setup firewall
apt install ufw
ufw default allow outoing
ufw default deny incoming
ufw allow ssh
ufw enable

# Install python
apt install python3-pip -y
apt install python3-venv -y
