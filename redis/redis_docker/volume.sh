#!/bin/bash - 
#===============================================================================
#
#          FILE: volume.sh
# 
#         USAGE: ./volume.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: ELI
#  ORGANIZATION: 
#       CREATED: 2020年12月10日 16:07
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

mkdir docker
mkdir docker/images
mkdir docker/images/data
mkdir docker/images/data/php
mkdir docker/images/data/nginx
mkdir docker/images/data/redis
mkdir docker/images/data/php/www
mkdir docker/images/data/nginx/conf


