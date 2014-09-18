#%define-自定义自己的的宏，使用方式为%{variable}

%define __os_install_post /usr/lib/rpm/brp-compress
%define __key_version 0.0.1

# 包的名称 不能含有空白字符，比如空格、Tab和回车等
# <公司名>-<产品线>-[子系统]-[模块] 的架构来定义包名，中间分隔线可以使中划线”-”也可以是下划线”_” 
Name: pkgname

# 版本由三位或四位构成：主版本(主产品号).次版本号.功能号[.小修改号]，如：0.6.7，或0.6.7.1 
Version: 0.0.1

# Release:发布号，如果使用版本控制工具，可以采用提交码
Release: 1

# 包的分类
Group: Productivity/Networking/API

# 摘要包含一行介绍包的文字，不要超过50个字符
Summary: Auto Rpm

# 包许可证 
License: Commercial

# 硬件无关时：
BuildArch: noarch

# 包的关联关系，如果没有包的依赖关系，no
AutoReqProv:no

# 运行/安装依赖 包名 [{>=|<=|>|<|=} 版本号],可以多个
# Requires: rpm >= 4.0.0
# Requires: rpm >= 4.0.0

# 详细的介绍，描述支持少量的格式化，空行用于分割段落，以空白开头（比如空格或者Tab）的行通常会以等宽字体显示
%description
Generating specific directory structure for rpm-create

# 安装前的准备
%prep
cd $OLDPWD/.. && make dist

# 编译过程
# %build
#../configure ----prefix=%{_sysconfdir}/httpd .......


# 安装步骤， 注意%{_prefix}前的.不能省略，代表当前目录，当前操作是在.rpm的目录中进行的，并非是绝对路径
%install
cp -rf $OLDPWD/../_dist/* .%{_prefix}

# 用到的新的目录都需要创建
#mkdir -p .%{_prefix}/../../../usr/local/bin
#cp .%{_prefix}/lz_rpm_init .%{_prefix}/../../../usr/local/bin/

# 安装的文件，在卸载的时候会删除掉，尽量少用*替换符，避免在卸载的时候删错文件，此时需要绝对路径，因为文件已经在安装的时候拷贝到相应的绝对路径中
%files
%defattr(755,admin,admin)
%{_prefix}

# 安装完成时执行
%post

# 变更记录
%changelog
