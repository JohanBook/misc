#!/bin/bash
# Configure an Ubuntu Python server
# run using <host name><admin password>

# Install security updates
apt update -y && apt upgrade -y

apt install -y postgres
