#!/bin/bash
# Configure an Ubuntu Python server

# Install security updates
apt update -y && apt upgrade -y

# Set host name
hostnamectl set-hostname <host-name>
# set hostname in /etc/hosts

# Create limited user account
adduser admin # also password
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
