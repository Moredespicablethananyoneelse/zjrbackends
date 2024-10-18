参考文献
https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_using_database_servers/using-postgresql_configuring-and-using-database-servers#installing-postgresql_using-postgresql

0：简介
  PostgreSQL server是一款建立在sql语言基础上的开源，稳定，可扩展性强的数据库服务。

1：安装PostgreSQL
   RHEL9（本机使用的是Centos-Stream-9）提供的该数据库的PostgreSQL 13版本。所以可以很简单的使用RPM安装

   安装过程：
   切换到root用户
   [zjr@VM-24-5-centos ~]$ su - root
   Password:
   Last login: Thu Oct 17 19:17:16 CST 2024 on pts/2


   给账户zjr赋予sudo权限
   [root@VM-24-5-centos ~]# usermod -aG wheel zjr
   [root@VM-24-5-centos ~]#
   
   切换到zjr账户 
   [root@VM-24-5-centos ~]# su - zjr
   Last login: Thu Oct 17 21:50:57 CST 2024 from 223.104.41.205 on pts/0
   
   安装postgresql-server 注意我们此处安装的是PostgreSql 16不是默认的PostgreSql 13(使用dnf install postgresql-server安装13）.

   [zjr@VM-24-5-centos ~]$  dnf module install postgresql:16/server
Error: This command has to be run with superuser privileges (under the root user on most systems).
[zjr@VM-24-5-centos ~]$ sudo dnf module install postgresql:16/server
Last metadata expiration check: 1:37:02 ago on Thu 17 Oct 2024 08:57:24 PM CST.
Dependencies resolved.
=====================================================================================================================================
 Package                              Architecture        Version                                       Repository              Size
=====================================================================================================================================
Installing group/module packages:
 postgresql-server                    x86_64              16.4-2.module_el9+1109+d821d6e7               appstream              7.0 M
Installing dependencies:
 libicu                               x86_64              67.1-9.el9                                    baseos                 9.6 M
 postgresql                           x86_64              16.4-2.module_el9+1109+d821d6e7               appstream              1.9 M
 postgresql-private-libs              x86_64              16.4-2.module_el9+1109+d821d6e7               appstream              144 k
Installing module profiles:
 postgresql/server
Enabling module streams:
 postgresql                                               16

Transaction Summary
=====================================================================================================================================
Install  4 Packages

Total download size: 19 M
Installed size: 70 M
Is this ok [y/N]: y
Downloading Packages:
(1/4): postgresql-private-libs-16.4-2.module_el9+1109+d821d6e7.x86_64.rpm                            594 kB/s | 144 kB     00:00
(2/4): postgresql-16.4-2.module_el9+1109+d821d6e7.x86_64.rpm                                         4.1 MB/s | 1.9 MB     00:00
(3/4): libicu-67.1-9.el9.x86_64.rpm                                                                   17 MB/s | 9.6 MB     00:00
(4/4): postgresql-server-16.4-2.module_el9+1109+d821d6e7.x86_64.rpm                                  8.3 MB/s | 7.0 MB     00:00
-------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                 22 MB/s |  19 MB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                             1/1
  Installing       : postgresql-private-libs-16.4-2.module_el9+1109+d821d6e7.x86_64                                              1/4
  Installing       : postgresql-16.4-2.module_el9+1109+d821d6e7.x86_64                                                           2/4
  Installing       : libicu-67.1-9.el9.x86_64                                                                                    3/4
  Running scriptlet: postgresql-server-16.4-2.module_el9+1109+d821d6e7.x86_64                                                    4/4
  Installing       : postgresql-server-16.4-2.module_el9+1109+d821d6e7.x86_64                                                    4/4
  Running scriptlet: postgresql-server-16.4-2.module_el9+1109+d821d6e7.x86_64                                                    4/4
  Verifying        : postgresql-16.4-2.module_el9+1109+d821d6e7.x86_64                                                           1/4
  Verifying        : postgresql-private-libs-16.4-2.module_el9+1109+d821d6e7.x86_64                                              2/4
  Verifying        : postgresql-server-16.4-2.module_el9+1109+d821d6e7.x86_64                                                    3/4
  Verifying        : libicu-67.1-9.el9.x86_64                                                                                    4/4

Installed:
  libicu-67.1-9.el9.x86_64                                             postgresql-16.4-2.module_el9+1109+d821d6e7.x86_64
  postgresql-private-libs-16.4-2.module_el9+1109+d821d6e7.x86_64       postgresql-server-16.4-2.module_el9+1109+d821d6e7.x86_64

Complete!
[zjr@VM-24-5-centos ~]$


初始化数据库集群
[zjr@VM-24-5-centos zjrbackends]$ sudo postgresql-setup --initdb
[sudo] password for zjr:
 * Initializing database in '/var/lib/pgsql/data'
 * Initialized, logs are in /var/lib/pgsql/initdb_postgresql.log
[zjr@VM-24-5-centos zjrbackends]$



修改配置文件postgresql.conf中的
#password_encryption = md5              # md5 or scram-sha-256
为
password_encryption = scram-sha-256
方法如下：
[zjr@VM-24-5-centos ~]$ sudo ls /var/lib/pgsql/data/postgresql.conf
/var/lib/pgsql/data/postgresql.conf
[zjr@VM-24-5-centos ~]$ sudo vim /var/lib/pgsql/data/postgresql.conf
[zjr@VM-24-5-centos ~]$

修改配置文件/var/lib/pgsql/data/pg_hba.conf中host    all             all             127.0.0.1/32            ident
为host    all             all             127.0.0.1/32            scram-sha-256
[zjr@VM-24-5-centos ~]$ sudo vim /var/lib/pgsql/data/pg_hba.conf


启动服务器
[zjr@VM-24-5-centos ~]$ sudo systemctl start postgresql.service
检查服务器是否启动成功
[zjr@VM-24-5-centos ~]$ sudo systemctl status postgresql
● postgresql.service - PostgreSQL database server
     Loaded: loaded (/usr/lib/systemd/system/postgresql.service; disabled; vendor preset: disabled)
     Active: active (running) since Thu 2024-10-17 23:00:54 CST; 1min 19s ago
    Process: 150057 ExecStartPre=/usr/libexec/postgresql-check-db-dir postgresql (code=exited, status=0/SUCCESS)
   Main PID: 150059 (postgres)
      Tasks: 7 (limit: 10715)
     Memory: 19.3M
        CPU: 80ms
     CGroup: /system.slice/postgresql.service
             ├─150059 /usr/bin/postgres -D /var/lib/pgsql/data
             ├─150060 "postgres: logger " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             ├─150061 "postgres: checkpointer " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             ├─150062 "postgres: background writer " "" "" "" "" "" "" "" "" "" "" "" ""
             ├─150064 "postgres: walwriter " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             ├─150065 "postgres: autovacuum launcher " "" "" "" "" "" "" "" "" "" ""
             └─150066 "postgres: logical replication launcher " ""

Oct 17 23:00:54 VM-24-5-centos systemd[1]: Starting PostgreSQL database server...
Oct 17 23:00:54 VM-24-5-centos postgres[150059]: 2024-10-17 23:00:54.916 CST [150059] LOG:  redirecting log output to l>
Oct 17 23:00:54 VM-24-5-centos postgres[150059]: 2024-10-17 23:00:54.916 CST [150059] HINT:  Future log output will app>
Oct 17 23:00:54 VM-24-5-centos systemd[1]: Started PostgreSQL database server.


切换到系统用户postgres

[zjr@VM-24-5-centos ~]$ sudo su - postgres
[postgres@VM-24-5-centos ~]$


启动postgresql交互式命令终端
[zjr@VM-24-5-centos ~]$ sudo su - postgres
[postgres@VM-24-5-centos ~]$ psql
psql (16.4)
Type "help" for help.

postgres=#

获取当前的链接信息
postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
postgres=#



创建用户zjr 密码123456 ，赋予zjr 权限createrole 和createdb
postgres=# create user zjr with password '123456' createrole createdb;
CREATE ROLE
postgres=#
现在zjr这个用户可以执行日常的数据库管理工作，比如创建数据库和管理用户索引


退出数据库交互终端
postgres=# \q
[postgres@VM-24-5-centos ~]$



退出当前操作系统用户postgres
[postgres@VM-24-5-centos ~]$ logout
[zjr@VM-24-5-centos ~]$

使用zjr这个数据库用户登录postgresql终端，指定hostname，链接默认的数据库postgres(部署时默认创建的）
[zjr@VM-24-5-centos zjrbackends]$ psql -U zjr -h 127.0.0.1 -d postgres
Password for user zjr:
psql (16.4)
Type "help" for help.

postgres=>


创建数据库zjr20241017
postgres=> create database zjr20241017
postgres-> ;
CREATE DATABASE
postgres=>



退出当前postgres的终端
postgres=> \q

使用数据库用户zjr登录数据库
[zjr@VM-24-5-centos zjrbackends]$ psql -U zjr -h 127.0.0.1 -d zjr20241017
Password for user zjr:
psql (16.4)
Type "help" for help.

zjr20241017=>

显示链接信息
zjr20241017=> \conninfo
You are connected to database "zjr20241017" as user "zjr" on host "127.0.0.1" at port "5432".
zjr20241017=>


/*******
https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_using_database_servers/using-postgresql_configuring-and-using-database-servers#proc_configuring-tls-encryption-on-a-postgresql-server_using-postgresql
其中的Example 4.4. Initializing, creating, and connecting to a PostgreSQL database using TLS encryption有个grant某个数据库权限给某个用户的过程。但是Example 4.1. Initializing, creating, and connecting to a PostgreSQL database没有。两个例子不同的是：后者创建的用户具有createdb权限，同时后者的数据库的创建者就是这个创建的用户，所以不需要额外授权

********/
