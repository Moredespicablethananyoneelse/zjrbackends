##项目文档
https://docs.djangoproject.com/en/5.1/intro/

##创建虚拟环境
[zjr@VM-24-5-centos getting_started_django]$ mkdir .virtualenvs

"当前路径是README所在的路径"
python3.12 -m venv .virtualenvs/getting_started_django


##激活虚拟环境
source .virtualenvs/getting_started_django/bin/activate



##下载django到虚拟环境
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ python -m pip install Django
Collecting Django
  Obtaining dependency information for Django from https://files.pythonhosted.org/packages/a3/b8/f205f2b8c44c6cdc555c4f56bbe85ceef7f67c0cf1caa8abe078bb7e32bd/Django-5.1.2-py3-none-any.whl.metadata
  Using cached Django-5.1.2-py3-none-any.whl.metadata (4.2 kB)
Collecting asgiref<4,>=3.8.1 (from Django)
  Obtaining dependency information for asgiref<4,>=3.8.1 from https://files.pythonhosted.org/packages/39/e3/893e8757be2612e6c266d9bb58ad2e3651524b5b40cf56761e985a28b13e/asgiref-3.8.1-py3-none-any.whl.metadata
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django)
  Obtaining dependency information for sqlparse>=0.3.1 from https://files.pythonhosted.org/packages/5d/a5/b2860373aa8de1e626b2bdfdd6df4355f0565b47e51f7d0c54fe70faf8fe/sqlparse-0.5.1-py3-none-any.whl.metadata
  Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Downloading Django-5.1.2-py3-none-any.whl (8.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 13.9 kB/s eta 0:00:00
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
Installing collected packages: sqlparse, asgiref, Django
Successfully installed Django-5.1.2 asgiref-3.8.1 sqlparse-0.5.1

[notice] A new release of pip is available: 23.2.1 -> 24.2
[notice] To update, run: pip install --upgrade pip
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$



#查看当前版本（参考文档https://docs.djangoproject.com/en/5.1/intro/tutorial01/）
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ python -m django --version
5.1.2

#继续回来安装django项目相关模块，因为前几天调研了其他模块的内容,中断了前面的文档的描述，所以我们从切换到django项目gettingstarteddjango开始
## 安装psycopg (version psycopg 3)
[zjr@VM-24-5-centos ~]$ cd getting_started_django/
[zjr@VM-24-5-centos getting_started_django]$ ls
README.md  tutorial.md
### 激活虚拟环境 ,即执行source .virtualenvs/gettingstarteddjango/bin/activate
[zjr@VM-24-5-centos getting_started_django]$ source .
./            ../           .virtualenvs/ 
[zjr@VM-24-5-centos getting_started_django]$ source .virtualenvs/getting_started_django/
bin/        include/    lib/        lib64/      pyvenv.cfg  
[zjr@VM-24-5-centos getting_started_django]$ source .virtualenvs/getting_started_django/bin/activate
###激活虚拟环境后，查看django版本是否为上述安装的5.1.2版本
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ 
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ python -m django --version
5.1.2
###升级pip工具
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ pip install --upgrade pip
Requirement already satisfied: pip in ./.virtualenvs/getting_started_django/lib64/python3.12/site-packages (23.2.1)
Collecting pip
  Obtaining dependency information for pip from https://files.pythonhosted.org/packages/ef/7d/500c9ad20238fcfcb4cb9243eede163594d7020ce87bd9610c9e02771876/pip-24.3.1-py3-none-any.whl.metadata
  Using cached pip-24.3.1-py3-none-any.whl.metadata (3.7 kB)
Using cached pip-24.3.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.2.1
    Uninstalling pip-23.2.1:
      Successfully uninstalled pip-23.2.1
Successfully installed pip-24.3.1
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ 
###安装psycopg有三种方式，参见文档https://www.psycopg.org/psycopg3/docs/basic/install.html
###我们使用运行效率最高的pip install "psycopg[c]"命令安装。这种方式需要服务器上提前安装好c编译器，c编译器的安装可以参见总结的其他文档
###安装成功
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ pip install "psycopg[c]"
Collecting psycopg[c]
  Downloading psycopg-3.2.3-py3-none-any.whl.metadata (4.3 kB)
Collecting typing-extensions>=4.6 (from psycopg[c])
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting psycopg-c==3.2.3 (from psycopg[c])
  Downloading psycopg_c-3.2.3.tar.gz (598 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 598.9/598.9 kB 159.5 kB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Downloading psycopg-3.2.3-py3-none-any.whl (197 kB)
Building wheels for collected packages: psycopg-c
  Building wheel for psycopg-c (pyproject.toml) ... done
  Created wheel for psycopg-c: filename=psycopg_c-3.2.3-cp312-cp312-linux_x86_64.whl size=2296018 sha256=bc4c810cc9a4d83349d98168f55e7dec39bc7965b00c3589e205358562f63645
  Stored in directory: /home/zjr/.cache/pip/wheels/ef/2e/f8/cc5fcf314723a870f6b55e9ae64de79883ed337261c09e6e70
Successfully built psycopg-c
Installing collected packages: typing-extensions, psycopg-c, psycopg
Successfully installed psycopg-3.2.3 psycopg-c-3.2.3 typing-extensions-4.12.2
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$

###编写脚本程序，测试psycopg是否可以正常链接已经安装好的postgres数据库，测试脚本参见https://www.psycopg.org/psycopg3/docs/basic/usage.html
###将以上脚本保存在名为test-psycopg3.py的文件中，然后执行python test-psycopg3.py
###注意执行python test-psycopg3.py需要激活上文中的虚拟环境,如下所示命令提示符中提示现在使用的虚拟环境是(gettingstarteddjango)
###(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ python test-psycopg3.py
 
##安装链接池（缓存django和数据库之间创建的链接）

