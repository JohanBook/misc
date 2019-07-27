#!/bin/bash
# Configure an Ubuntu Python server
# run using <host name><admin password>

# Install security updates
apt update -y && apt upgrade -y

# Install postgress
apt install -qy postgresql postgresql-contrib
