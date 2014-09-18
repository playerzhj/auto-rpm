#!/bin/bash

# 打包调用程序，如果该文件存在，abs系统会调用此文件进行rpm的打包。程序根据传的参数自动替换spec文件中的release,version变量的值

# $1 spec文件所在的目录
# $2 spec文件名称，与申请的包名一致
# $3 版本号version
# $4 release号

cd $1/rpm

SPEC="$2.spec"
#sed -i  "s/^Release:.*$/Release: "$5"/" $SPEC
#sed -i  "s/^Version:.*$/Version: "$4"/" $SPEC

# 开始打包，默认安装在/home/admin/$2目录下，请根据实际安装路径修改
./rpm_create -p /home/admin/$2 -v $3 -r $4 $2.spec
