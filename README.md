# 蓝鲸高校项目：社团招新系统
- [一、快速开始](#一快速开始)
  - [1. 从主仓库fork代码到自己的个人仓库](#1-从主仓库fock代码到自己的个人仓库)
  - [2. git clone 自己仓库的代码到本地](#2-gitclone自己仓库的代码到本地)
  - [3. 本地开发环境搭建](#3-本地开发环境搭建)
- [二、开发须知](#二开发须知)
  - [1. 开发模式----基于PR的开发协作模式](#1-开发模式----基于PR的开发协作模式)
  - [2. 开发规范](#2-开发规范)
- [三、学习资料](#三学习资料)

# 一、快速开始

### 1. fork主仓库
![image-20210904185418586](https://github.com/TencentBlueKing/bk-training-open/raw/master/static/images/image-20210904185137806.png)

### 2. clone代码到本地
1. 在自己的电脑上新建一个空目录（目录完整路径中不要包含中文）
2. 在当前目录打开终端，执行git clone ${仓库地址}

### 3. 搭建本地运行环境
1. 首先安装项目底层依赖组件：rabbitmq、redis、python3.6.7、mysql5.7
2. 配置python虚拟环境
   1. 安装pipenv：`pip install pipenv`
   2. 在项目目录下打开终端，执行pipenv install创建虚拟环境
   3. 在pycharm/vscode等IDE中选择使用上一步创建好的虚拟环境
3. 在项目新建local_settings.py，填入以下内容:

  ```python
  # -*- coding: utf-8 -*-
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': '', #本地项目数据库名
          'USER': '',  # 本地数据库账号
          'PASSWORD': '',  # 本地数据库密码
          'HOST': 'localhost',
          'PORT': '3306',
          'TEST_CHARSET': "utf8",
          'TEST_COLLATION': "utf8_general_ci",
          'TEST': {
              'CHARSET': 'utf8',
              'COLLATION': 'utf8_general_ci',
          }
      },
  }
  
  REDIS = {
      'host': 'localhost',
      'port': 6379,
      'db': 0
  }
  STATIC_ROOT = 'staticfiles'
  ```
4. 配置项目所需最小环境变量:

   | 名称         | 值                 |
   | ------------ | ------------------ |
   | APP_ID       | 联系项目负责人获取 |
   | APP_TOKEN    | 联系项目负责人获取 |
   | BK_PAAS_HOST | 联系项目负责人获取 |

5. 配置hosts：
   
   Windows：C:\Windows\System32\drivers\etc\hosts
   MacOS：/etc/hosts

   在hosts文件中新增一项：`127.0.0.1 appdev.paas-edu.bktencent.com`

6. 安装所需依赖：

   首先cd到项目根目录下，然后执行：`pip install -r requirements.txt`

7. 执行数据库初始化命令：

   `python manage.py migrate`

8. 尝试运行项目：

   收集静态文件: `python manage.py collectstatic --noinput`
   web进程：`python manage.py runserver`
   访问地址：`appdev.paas-edu.bktencent.com:8000`
   
9. 其他常用命令：

   收集静态文件：`python manage.py collectstatic --noinput`
   celery worker：`python manage.py celery worker`
   celery beat: `python manage.py celery beat`

# 二、开发须知

### 1. 基于PR的开发模式
下面通过新功能开发和bug修复两个开发场景阐述我们的工作流，假定：

   upstream：主仓库
   origin：开发者fork出的个人仓库

##### 1 基于PR的功能开发模式：https://whimsical.com/65wnasuhWbE19oMWbjkhY9

1. 开发前拉取主仓库develop分支（git pull upstream develop）
3. 新建本地功能分支（git checkout -b feature_xxx）
4. 开发·····本地自测····
5. git commit -m （此时触发pre-commit检查）
6. git push origin feature_xxx:feature_xxx（推送本地新功能代码到fork仓库新分支）
7. New  Pull Request from fork resp to main resp( 从frok仓库提交PR、合并请求到主仓库develop分支）
8. 持续集成（github自动单元测试、代码检查）
9. Code Review（项目管理员进行代码审核）
10. Merge to develop（审核通过后由管理员合并入开发分支）
11. 发布测试
12. New Pull Request from develop to master
13. 持续集成（github自动单元测试、代码检查）
14. Merge to master（代码检查通过后合并入主分支）
15. 发布测试
16. 正式发布，功能开发完成

##### 2 基于PR的bug修复模式：

1. 开发前拉取主仓库master分支（git pull upstream master）
3. 新建本地bug修复分支（git checkout -b bugfix_xxx）
4. bug修复·····本地自测····
5. git commit -m （此时触发pre-commit检查）
6. git push origin bugfix_xxx:bugfix_xxx（推送本地bugfix_xxx分支到fork仓库的bugfix_xxx分支）
7. New Pull Request from bugfix_xxx to master（从fork仓库bugfix_xxx分支提交PR到主仓库master分支）
8. 持续集成（github自动单元测试、代码检查）
9. Code Review（项目管理员进行代码审核）
10. Merge to master（审核通过后由管理员合并入主分支）
11. 发布测试
12. 正式发布，修复完成

### 3. 开发规范

- 前端规范------[文档中心 | 蓝鲸 (tencent.com)](https://bk.tencent.com/docs/document/6.0/130/5882)

- 后端规范------[文档中心 | 蓝鲸 (tencent.com)](https://bk.tencent.com/docs/document/6.0/130/5872)

- 代码提交规范

	- 配置`pre-commit`

		`pre-commit`在git add提交之后，然后执行git commit时执行，如果脚步执行没有报错就继续提交，否则就驳回提交的操作，从而实现对代码的检查、优化代码格式等任务。

		```
		# 安装pre-commit
		pip install pre-commit
		
		# 安装git hook脚本,成功之后会在.git/hooks里生成pre-commit文件
		pre-commit install
		
		# 运行所配置的所有规则，使其起作用
		pre-commit run --all-files
		```

	- commit分类-----每次代码提交必须有备注说明，注明本次提交做了哪些修改

		`bugfix` - 线上功能 bug

		`sprintfix` - 未上线代码修改 （功能模块未上线部分 bug）

		`minor` - 不重要的修改（换行，拼写错误等）

		`feature` - 新功能说明

		```
		# 新功能：
		git add .
		git commit -m feature:xxxx
		
		# bug修复：
		git add .
		git commit -m bugfix:xxxxxxxxxxxxx

      # 功能优化：
		git add .
		git commit -m minor:xxxxxxxxxxxxx
		```


## 三、学习资料

1. 在线课程[【蓝鲸开课】2020秋季蓝鲸基础开发实战课程-学习视频教程-腾讯课堂 (qq.com)](https://ke.qq.com/course/3030664?taid=10315536490446472)
2. 文档中心[文档中心 | 蓝鲸 (tencent.com)](https://bk.tencent.com/docs/document/6.0/130/5948)
3. `django-rest-framework`[Home - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/)
4. `django 2.2`[Django 文档 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/2.2/)
5. 前端组件库[蓝鲸 MagicBox-Vue 组件库 (tencent.com)](https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/index.html#/)
6. `vue`语法[介绍 — Vue.js (vuejs.org)](https://cn.vuejs.org/v2/guide/)
