# What

auto-rpm -> Generate all the files used for creating a rpm

## Why

如果你想要创建一个rpm软件安装包，又不想编写spec文件，那么就请安装auto-rpm

## How

* 首先进入项目文件夹，查看文件结构，会发现这些文件就是为打一个rpm包准备的
* sh test-rpm.sh 执行这个命令会打出auto-rpm的软件安装包，在rpm文件夹下
* 安装生成的rpm包 rpm -ivh auto-rpm-build
* 然后执行lz_init_rpm -h 会有具体的使用方式

## TODO


