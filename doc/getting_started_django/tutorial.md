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
###将以上脚本保存在名为test_psycopg3.py的文件中，然后执行python test_psycopg3.py
###修改过的test_psycopg3.py的内容，参见同路径下的同名文件
###注意执行python test-psycopg3.py需要激活上文中的虚拟环境,如下所示命令提示符中提示现在使用的虚拟环境是(gettingstarteddjango)
###(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ python test_psycopg3.py 


##安装链接池（缓存django和数据库之间创建的链接）
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ pip install "psycopg[pool]"
Requirement already satisfied: psycopg[pool] in ./.virtualenvs/getting_started_django/lib64/python3.12/site-packages (3.2.3)
Requirement already satisfied: typing-extensions>=4.6 in ./.virtualenvs/getting_started_django/lib64/python3.12/site-packages (from psycopg[pool]) (4.12.2)
Collecting psycopg-pool (from psycopg[pool])
  Downloading psycopg_pool-3.2.4-py3-none-any.whl.metadata (2.6 kB)
Downloading psycopg_pool-3.2.4-py3-none-any.whl (38 kB)
Installing collected packages: psycopg-pool
Successfully installed psycopg-pool-3.2.4
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$



#创建djangotutorial项目
##项目所在路径及其中现有文件情况
[O(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ ls
README.md  tutorial.md
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ pwd
/home/zjr/getting_started_django
##创建djangotutorial项目路径
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ mkdir djangotutorial
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ ls
djangotutorial  README.md  tutorial.md
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ ls djangotutorial/
##在djangotutorial路径下生成django项目脚手架
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ django-admin startproject mysite djangotutorial
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ ls 
djangotutorial  README.md  tutorial.md
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ ls djangotutorial/
manage.py  mysite
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ 

##安装tree命令
[zjr@VM-24-5-centos ~]$ sudo dnf install tree
[sudo] password for zjr: 
Repository baseos is listed more than once in the configuration
Repository baseos-source is listed more than once in the configuration
Repository appstream is listed more than once in the configuration
Repository appstream-source is listed more than once in the configuration
Repository rt is listed more than once in the configuration
Repository rt-source is listed more than once in the configuration
Repository resilientstorage is listed more than once in the configuration
Repository resilientstorage-source is listed more than once in the configuration
Last metadata expiration check: 1:05:10 ago on Sun 01 Dec 2024 08:44:41 AM CST.
Dependencies resolved.
======================================================================================================================================================================
 Package                             Architecture                          Version                                        Repository                             Size
======================================================================================================================================================================
Installing:
 tree                                x86_64                                1.8.0-10.el9                                   baseos                                 56 k

Transaction Summary
======================================================================================================================================================================
Install  1 Package

Total download size: 56 k
Installed size: 113 k
Is this ok [y/N]: y
Downloading Packages:
tree-1.8.0-10.el9.x86_64.rpm                                                                                                          309 kB/s |  56 kB     00:00    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                 305 kB/s |  56 kB     00:00     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                              1/1 
  Installing       : tree-1.8.0-10.el9.x86_64                                                                                                                     1/1 
  Running scriptlet: tree-1.8.0-10.el9.x86_64                                                                                                                     1/1 
  Verifying        : tree-1.8.0-10.el9.x86_64                                                                                                                     1/1 

Installed:
  tree-1.8.0-10.el9.x86_64                                                                                                                                            

Complete!
[zjr@VM-24-5-centos ~]$ 

## 显示djangotutorial当前目录树结构
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ tree djangotutorial/
djangotutorial/
├── manage.py
└── mysite
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

1 directory, 6 files
##检查脚手架是否可以正常使用
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 01, 2024 - 02:03:57
Django version 5.1.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[01/Dec/2024 02:04:05] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[01/Dec/2024 02:04:06] "GET /favicon.ico HTTP/1.1" 404 2208

##创建好django 项目后，开始创建django app
###切换路径
(getting_started_django) [zjr@VM-24-5-centos getting_started_django]$ cd djangotutorial/
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ ls
db.sqlite3  manage.py  mysite
###在manage.py所在的路径中创建polls 问卷调查app
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$  python manage.py startapp polls
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ tree .
.
├── db.sqlite3
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

4 directories, 18 files
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$



##查看polls  app的结构
[zjr@VM-24-5-centos djangotutorial]$ tree polls
polls
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files
[zjr@VM-24-5-centos djangotutorial]$ 

## 为polls编写简单的views
polls/views.py

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

## 在polls路径下创建urls.py文件polls/urls.py，并在其中编写如下代码
### 注意创建的polls文件下，默认是没有urls.py文件的
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
]
## polls文件夹下的路径结构为
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py

## 配置整个django项目路径mysite下的urls.py，即： mysite/urls.py

from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

## 启动django的开发服务器
python manage.py runserver

## 访问 http://localhost:8000/polls/
###注意访问http://localhost:8000会报错（这个报错是正常的，官方文档对这有描述）
Using the URLconf defined in mysite.urls, Django tried these URL patterns, in this order:
polls/
admin/
The empty path didn’t match any of these.

看不到第一次执行python manage.py runserver了。
The install worked successfully! Congratulations!
View release notes for Django 5.1
You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.

###需要注意的是，此时，我们并没有将polls这个app放进mysite的INSTALL_APP里，只是将修改了polls/views.py, polls/urls.py和mysite/urls.py三个文件，就可以通过浏览器访问polls/views.py这个视图了,zhe'gs

**********
Writing your first Django app, part 2
##链接数据库,修改mysite/settings.py

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}
    
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "zjr20241017",
        "USER": "zjr",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "OPTIONS": {
            "pool": True,
        }
    }
}
### 迁移django内建的app
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ 

## 为polls创建models，编辑polls/models.py

```
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
```
## 将polls这个app加入到django项目，编辑mysite/settings.py
 
```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
### 注意，在mysite/settings.py不需要import polls这样的命令，就可以直接在INSTALLED_APP里直接添加

## 将polls加入到django项目后，才可以使用django提供的命令进行polls 的数据库的迁移
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    + Create model Question
    + Create model Choice
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ 

## 查看即将进行的polls的迁移产生的sql语句
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ python manage.py sqlmigrate polls 0001
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "question_text" varchar(200) NOT NULL, "pub_date" timestamp with time zone NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL);
ALTER TABLE "polls_choice" ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id" FOREIGN KEY ("question_id") REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ 



## 迁移
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ 


## Creating an admin user
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ python manage.py createsuperuser
Username (leave blank to use 'zjr'): 
Email address: donotblieveit@outlook.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ 
## 启动django开发服务器
(getting_started_django) [zjr@VM-24-5-centos djangotutorial]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 01, 2024 - 04:56:24
Django version 5.1.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[01/Dec/2024 04:56:28] "GET / HTTP/1.1" 200 12068
[01/Dec/2024 04:56:38] "GET /admin/ HTTP/1.1" 302 0
[01/Dec/2024 04:56:38] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4160
[01/Dec/2024 04:56:43] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[01/Dec/2024 04:56:44] "GET /admin/ HTTP/1.1" 200 5850
[01/Dec/2024 04:56:44] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 441
[01/Dec/2024 04:56:44] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[01/Dec/2024 04:56:44] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380

## 访问 http://127.0.0.1:8000/admin/
我们可以看到admin管理界面现在管理了User和Group两个model

## 将polls的model纳入admin管理，修改polls/admin.py
from django.contrib import admin

# Register your models here.

from .models import Question
admin.site.register(Question)


## 再次访问http://127.0.0.1:8000/admin/
现在可以看到poll的Question已经被admin接管了


## Writing your first Django app, part 3
### 在 polls/views.py中增加以下几个view。在此前已经自Writing your first Django app, part1 已经添加index这个view，所以这次不用,
### 而且在Writing your first Django app,part1中在mysite的全局urls.py中include了polls/urls
```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```


### 在polls中的urls文件即polls/urls.py中添加如下内容。而mysite/urls.py先前已经include了polls.urls,所以这次不用改
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
## 此时可以访问http://127.0.0.1:8000/polls/5/vote, http://127.0.0.1:8000/polls/5/results, http://127.0.0.1:8000/polls/5/,http://127.0.0.1:8000/polls/
## 依次调用的时vote， results， detail,index 这几个view。

###view 做两件事，返回HttpRessponse和 Http404，剩下的其他做什么都行,比如读取数据库数据，调用django的模板系统，生成pdf文件，xml文件，调用任何python 库等等。
## django只要修返回HttpResponse护着Http404

## 修改index 这个view干点实际的事情,比如查询数据库，然后显示poll的前5条
```
 from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```
#
## 在view中使用django的模板系统
### 在默认的配置文件中DjangoTemplates 配置的 APP_DIRS 被设置成了 True，
##所以DjangoTemplates会在INSTALLED_APPS指定的各个app路径下找templates子路径
## 为index生成的模板应该放在polls/templates/polls/index.html里
## 这是因为app_directories template loader加载模板的机制决定的
###你可以在django项目中使用 polls/index.html，引用这个模板,在view里引用，如下文的index这个view
## 在文件polls/templates/polls/index.html编写如下内容
```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

## 我们在index视图中使用上面的模板
### 我们更新下polls/views.py中的index这个view
```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
###上面index使用template的方式有简写方法，但是我们本地不用深究。如有需要参考django的官网的Writing your first Django App, part3
## 我们再尝试下在view中抛出异常。
## 修改polls/views.py的detail这个view
```
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```
## 上面这个view也有简写模式，这里不继续讨论
## 创建polls/tempaltes/polls/detail.html编写如下模板文件
```
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

## 删除模板中的url硬编码
# 修改polls/urls.py，添加app_name属性
```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
##这样就name="detail"的url地址添加了命名空间polls，这样就能区分开mysite这个项目的其他app中也叫detail链接
## 而path中detail这个链接名称可以用在模板系统中，用来去除硬编码的url链接
## 比如polls/tempaltes/polls/index.html可以使用如下方式引用detail这个view的url

```
      <li><a href="/polls/{{question.id}}/">{{ question.question_text }}</a></li>
```
 ## 可以修改成下面的方式
```
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
