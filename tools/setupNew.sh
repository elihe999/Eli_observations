#!/bin/bash - 
#===============================================================================
#
#          FILE: setupNew.sh
# 
#         USAGE: ./setupNew.sh 
# 
#   DESCRIPTION: for debian/ubuntu
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: eli
#  ORGANIZATION: 
#       CREATED: 20201210 15:34
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

echo "------------------Start-------------------"
sudo apt update -y
sudo apt upgrade -y
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt install openssh-server docker-ce -y
sudo /etc/init.d/ssh stop
sudo /etc/init.d/ssh start
