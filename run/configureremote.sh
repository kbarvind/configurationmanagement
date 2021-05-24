#!/bin/bash


if [[ -z $1 ]]
then
   echo "usage: $0 <ip>"
   exit 1
fi

IP=$1

echo "connecting ip ${IP}"

boxconfig install -h ${IP} -u root


