参考文献
https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/installing_and_using_dynamic_programming_languages/assembly_installing-and-using-python_installing-and-using-dynamic-programming-languages#assembly_installing-and-using-python_installing-and-using-dynamic-programming-languages


在RHEL 9中，Python3.9是默认的python是实现。从RHEL9.2，Python 3.11以python3.11包套件出现,
在RHEL 9.4中 Python 3.12以python3.12的包套件出现


0:安装Python 3.12
[zjr@VM-24-5-centos ~]$ sudo dnf install python3.12
[sudo] password for zjr:
Last metadata expiration check: 0:49:48 ago on Fri 18 Oct 2024 11:08:02 AM CST.
Dependencies resolved.
========================================================================================================================
 Package                             Architecture          Version                       Repository                Size
========================================================================================================================
Installing:
 python3.12                          x86_64                3.12.6-1.el9                  appstream                 27 k
Installing dependencies:
 libnsl2                             x86_64                2.0.0-1.el9                   appstream                 31 k
 mpdecimal                           x86_64                2.5.1-3.el9                   appstream                 86 k
 python3.12-libs                     x86_64                3.12.6-1.el9                  appstream                9.7 M
 python3.12-pip-wheel                noarch                23.2.1-4.el9                  appstream                1.5 M

Transaction Summary
========================================================================================================================
Install  5 Packages

Total download size: 11 M
Installed size: 44 M
Is this ok [y/N]: y
Downloading Packages:
(1/5): libnsl2-2.0.0-1.el9.x86_64.rpm                                                   222 kB/s |  31 kB     00:00
(2/5): python3.12-3.12.6-1.el9.x86_64.rpm                                               174 kB/s |  27 kB     00:00
(3/5): mpdecimal-2.5.1-3.el9.x86_64.rpm                                                 359 kB/s |  86 kB     00:00
(4/5): python3.12-libs-3.12.6-1.el9.x86_64.rpm                                           15 MB/s | 9.7 MB     00:00
(5/5): python3.12-pip-wheel-23.2.1-4.el9.noarch.rpm                                     1.9 MB/s | 1.5 MB     00:00
------------------------------------------------------------------------------------------------------------------------
Total                                                                                    12 MB/s |  11 MB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                1/1
  Installing       : python3.12-pip-wheel-23.2.1-4.el9.noarch                                                       1/5
  Installing       : mpdecimal-2.5.1-3.el9.x86_64                                                                   2/5
  Installing       : libnsl2-2.0.0-1.el9.x86_64                                                                     3/5
  Installing       : python3.12-3.12.6-1.el9.x86_64                                                                 4/5
  Installing       : python3.12-libs-3.12.6-1.el9.x86_64                                                                         5/5
  Running scriptlet: python3.12-libs-3.12.6-1.el9.x86_64                                                                         5/5
  Verifying        : libnsl2-2.0.0-1.el9.x86_64                                                                                  1/5
  Verifying        : mpdecimal-2.5.1-3.el9.x86_64                                                                                2/5
  Verifying        : python3.12-3.12.6-1.el9.x86_64                                                                              3/5
  Verifying        : python3.12-libs-3.12.6-1.el9.x86_64                                                                         4/5
  Verifying        : python3.12-pip-wheel-23.2.1-4.el9.noarch                                                                    5/5

Installed:
  libnsl2-2.0.0-1.el9.x86_64                  mpdecimal-2.5.1-3.el9.x86_64                     python3.12-3.12.6-1.el9.x86_64
  python3.12-libs-3.12.6-1.el9.x86_64         python3.12-pip-wheel-23.2.1-4.el9.noarch

Complete!
[zjr@VM-24-5-centos ~]$

1：安装pip3.12

[zjr@VM-24-5-centos ~]$ sudo dnf install python3.12-pip
Last metadata expiration check: 0:51:15 ago on Fri 18 Oct 2024 11:08:02 AM CST.
Dependencies resolved.
=====================================================================================================================================
 Package                                 Architecture             Version                          Repository                   Size
=====================================================================================================================================
Installing:
 python3.12-pip                          noarch                   23.2.1-4.el9                     appstream                   3.2 M
Installing weak dependencies:
 python3.12-setuptools                   noarch                   68.2.2-4.el9                     appstream                   1.6 M

Transaction Summary
=====================================================================================================================================
Install  2 Packages

Total download size: 4.8 M
Installed size: 21 M
Is this ok [y/N]: y
Downloading Packages:
(1/2): python3.12-setuptools-68.2.2-4.el9.noarch.rpm                                                 3.3 MB/s | 1.6 MB     00:00
(2/2): python3.12-pip-23.2.1-4.el9.noarch.rpm                                                        4.8 MB/s | 3.2 MB     00:00
-------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                7.1 MB/s | 4.8 MB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                             1/1
  Installing       : python3.12-setuptools-68.2.2-4.el9.noarch                                                                   1/2
  Installing       : python3.12-pip-23.2.1-4.el9.noarch                                                                          2/2
  Running scriptlet: python3.12-pip-23.2.1-4.el9.noarch                                                                          2/2
  Verifying        : python3.12-pip-23.2.1-4.el9.noarch                                                                          1/2
  Verifying        : python3.12-setuptools-68.2.2-4.el9.noarch                                                                   2/2

Installed:
  python3.12-pip-23.2.1-4.el9.noarch                            python3.12-setuptools-68.2.2-4.el9.noarch

Complete!
[zjr@VM-24-5-centos ~]$


注意使用python3.12的时候要使用下面的形式
python3.12
python3.12 -m venv --help
python3.12 -m pip install package
pip3.12 install package

不能直接使用python，因为python在centos-stream 9中是python3.9的软连接.而且这个软连接不能修改成指向python3.12(我修改过，再执行dnf命令就报错了，因为dnf的某些python脚本报错找不到某些module，因为dnf找这些module的时候是按照python3.9的相关路径找的，现在让他按照3.12路径找相关的module，很多module不在了，或者修改了路径，或者名称不叫原来的名字了，比如加上了版本号）
