#!/bin/bash
##for check
dir=$1
cd $1/rpm

SPEC="$2.spec"
sed -i  "s/^Release:.*$/Release: "$4"/" $SPEC
sed -i  "s/^Version:.*$/Version: "$3"/" $SPEC


/usr/local/bin/rpm_create -p /home/admin/lz_auto_rpm -v $3 -r $4 $2.spec
