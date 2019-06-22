## Git 学习

---- 2019/06/22 学习Git

## 本地库和远程库 の 交互

---- 团队内部协作
    
    项目经理 A 创建本地库 Bank-1 并将其 push 到远程库 Bank-2，而参与人 B 通过 clone 从 Bank-2 中下载内容并在本地初始化一个本地库 Bank-3，当 B 修改本地库以后，在加入 A 的团队后就可以向 Bank-2 上传他的 Bank-3 到 Bank-2.

---- 跨团队协作
    
    若 A和B 需要另一个团队的 C 帮忙，那么 A 可以 fork 一个新的远程库 Bank-4 给 C，C 可以直接 clone 远程库 Bank-4 到其电脑上建立本地库 Bank-5，经过 C 修改后，Bank-5 可以直接 push 到 Bank-4，同时，C 发出 pull request，经过 A 的审核，如果通过审核，A 发出 merge 的合并操作，此时的 Bank-4 就合并到 Bank-2，而 A和B 就可以通过 pull 到各自的 Bank。

## 本地库初始化

### Git命令行操作

---- 本地库初始化
    
    a.初始化本地库：
    
    进入对应的文件夹后，右键进入“git bash here”，命令行操作。
    
    1.为新的项目建立一个文件夹：mkdir FileName
    
    2.初始化git本地库：git init， 而后用 ls -lA 命令可以查看初始化后的效果
    
    注意：.git 目录中存放的是本地相关的子目录和文件，不要删除，也别修改
    
    b.设置签名
    
    1.形式----用户名：tom
    
    2.作用.区分不同开发人员的身份
    
    3.辨析.这里设置的前名和登录远程库（代码托管中心）的账户、密码没有任何关系
    
    4.命令.
    
        项目级别/仓库级别：尽在当前本地仓库范围有效
        
            git config user.name tom_pro
            git config user.email user@email.com
            信息保存位置：./.git/config 查看：cat .git/config            
        
        系统用户级别：登录当前操作系统的用户范围
        
            git config --global user.name tom_glb
            git config --global user.email user@email.com
            信息保存位置：~/.gitconfig 查看：ls -lA|less, cat .gitconfig(用户家目录下)
        
        优先级：就近原则，项目级别优先于系统级别，二者都有时，采用项目级别；如果只有系统用户系统级别，就以系统级别的签名为准；当两者都没有不允许
        
        注意：通常只设置系统用户级别即可。

## 添加提交和查看状态

    git status 查看当前项目信息：查看工作区、暂存区状态
    
    git add <filename.xxx> 用于添加文件，添加到暂存区，可用于提交
    
    git rm --cached <filename.xxx> 从暂存区删除文件，但是不会删除工作区的文件
    
    git commit <filename.xxx> 提交文件 filename.xxx {而后就需要输入关于文件的 信息/备注/说明}
    
    注意，如果现在直接 vim <filename.xxx> 并进行修改，而后 git status 可以看到修改了 filename.xxx 文件的内容，可以用 git add <filename.xxx> 更新文件filename.xxx，或者 git chechout --<filename.xxx> 撤销刚刚的修改，可以直接用 git commit <filename.xxx> 进行提交。
    
    git commit -m "xxx" <filename.xxx> 这样提交可以免进 vim 写文件 信息/备注/说明

## 版本的前进和后退

    git log 查看项目版本、签名、日志信息（最完整形式）
    
    git log --pretty=oneline 以简洁的方式显示
    
    git log --oneline 以最简洁的方式显示
    
    git reflog 现实日志，有很多参考价值
    
## 版本前进后退

    通过 git reflog 可以查看项目版本的版本信息，于是可以通过{索引值【推荐】、^符号、~符号}三种方式进行版本前进后退
    
    假设查看结果如下：
    xxxxxxx <HEAD -> master>HEAD@{0}:commit: insert yyyyyy edit
    xxxxxxx HEAD@{1}:commit: insert yyyyyy edit
    9a9ebe0 HEAD@{2}:commit: insert iiiiii edit
    xxxxxxx HEAD@{3}:commit: insert jjjjjj edit
    
    git reset --hard 9a9ebe0  项目前进或者后退到索引的那个版本
    
    ^符号/~符号 ---- 只能后退
    
    git --reset --hard HEAD^  后退一步
    
    git --reset --hard HEAD^^^  后退三步
    
    git --reset --hard HEAD~3 后退三步
    
## hard、soft 和 mixed 参数对比

    -- soft 参数
        
        仅仅在本地库移动 HEAD 指针

    -- mixed 参数
    
        在本地库移动 HEAD 指针
        
        重置暂存区
        
    -- hard 参数
    
        在本地库移动 HEAD 指针
        
        重置暂存区
        
        重置工作区

## 永久删除后找回

---- 已经提交本地库后删除，然后找回。删除后，工作区就没有该文件了。(git 只要提交了，文件就一直在，不会被删除， 那么通过项目版本退回，即可找回文件)

## 添加到暂存区的删除文件找回

---- 文件已经添加到暂存区，但是没有提交，文件被删除。此时，通过 git reset --hard HEAD 即可恢复文件

## 比较文件

---- 带文件名 <filename.xxx> 比较

    git diff <filename.xxx> 和暂存区文件比较,

    git diff HEAD <filename.xxx> 和本地库最新版本文件比较，

    git diff HEAD^ <filename.xxx> 和历史版本比较，
    
    
---- 不带文件名比较，与多个文件比较

    git diff HEAD 与当前工作区的所有文件比较
    
## 分支操作

    除了master分支还可以创建分支： 
    
    git branch -v 查看分支
    
    git branch [branchname] 创建分支
    
    git checkout [branchname] 切换分支
    
    合并分支(用于将最新修改的版本合并到 master 分支上，增加新内容)
        
        1.切换到master分支：git checkout master
        
        2.执行 merge 操作：git merge [branchname]
    
    解决冲突（合并中产生冲突：两个版本在同一个位置都有修改，系统无法确定保留哪一个文件，此时需要手动合并）
    
        通过 git merge [branchname] 会在合并的文件内部产生特殊符号以表示冲突，需要人为进行操作(编辑文件，删除特殊符号并修改好)。
        
        人为修改结束后，用 git add <filename.xx> 更新暂存区文件，但进一步提交必须用 git commit -m "xxx"（注意不带文件名）
    
## Hash 算法

---- Hash 是一个加密算法。
    
    1.不管数据的数据量多大，输入同一个Hash算法，得到的加密长度固定；
    2.Hash算法和输入确定下，输出可以确定；
    3.Hash算法确定，输入有变化，输出一定有变化，且一般变化很大；
    4.Hash算法不可逆。
    
## Git保存版本机制

---- 基于快照的方式保存不同版本的文件，每个文件都会

Git 分支管理的本质是创建和移动指针，针对没有更新的内容，直接用指针移动。
    
## 创建远程库

---- 远程库的名字和本地库不一定要完全一样，但一般设置一样，便于项目管理。

New repository --> 填写仓库名(完善描述、私有/公开、创建一个README用于初始化库[为了避免和本地冲突，一般不创建])

## 在本地创建远程库地址别名

复制远程库的 http 地址： https://github.com/Prime-Number/ML.git

查看本地库已有的远程库：git remote -v

添加远程库：git remote add [别名] [http地址] 例如：git remote add origin https://github.com/Prime-Number/ML.git

## 本地库文件推送到远程库

推送：git push [别名] [版本] 例如：git push origin master

## 克隆远程库

---- B 需要获取远程库到本地，使用 clone 操作

git clone [http地址] 例如：git clone https://github.com/Prime-Number/ML.git
    
    完整地克隆远程库到本地
    
    创建 [别名 origin] 远程地址别名
    
    初始化本地库
    
## 邀请团队成员

---- B 在本地修改了本地库，拟将本地库提交到远程库，需要 A 邀请 B 进入团队。

在 github 上进行操作：

    1.A 进入在线代码库 --> Settings --> Collaborators --> {输入拟邀请用户的 github 账号，点击 Add collaborator} --> {通过其他方式将 http地址 发送给 B}
    
    2.B 进入 A 给的 http地址，并选择 Accept invitation(成为团队成员)
    
    成为团队成员后，就可以 push 文件。
    
## 远程库修改的拉取操作

---- B 上传文件后，A 需要将文件拉取（pull）下来。

拉取(pull)有两个操作：fetch + merge
    
    A: git fetch [远程库地址别名 origin] [远程分支名] 例如：git fetch origin master {此时只是下载文件，并不会修改本地文件。}
    
    A: git merge [远程库地址别名 origin/远程分支名] 例如：git merge origin master
    
    或者直接用 pull 操作{一般用于修改很小，不会产生冲突的情况}：git pull origin master
    
## 协同开发时的冲突

---- 当 A 和 B 同时对 <filename.xxx> 进行了修改，并先后推送到远程库。{此时先推送的成功，后推送的失败.}

解决办法：

    1.下载先上传的版本 version-1：git pull origin master
    
    2.修改冲突，再次提交新的版本 version-2.{注意，解决冲突后 commit 不能带文件名}

## 跨团队操作

---- 邀请 C 来参与项目。

    1.C 去访问远程仓库（通过 http 地址），并点击右上角的 Fork 按钮 {注意，是以 C 的身份去点击}
    
    2.Fork 结束后，C 有一个完全一样的远程库（fork from A）
    
    3.C 可以对这个项目可以进行 clone，push 等操作.{本地修改，推送到远程}
    
    4.C 进入 C 的远程库 --> Pull request --> {填写 pull 申请}
    
    5.A 进入远程仓库 --> Pull request --> {获取 C 的请求，可以回信交流（而 C 也可以同样在线沟通）} --> Commits {查看 C 的提交}, Files changed {查看具体修改的文件} （对代码进行审核）--> {如果可以接受，回到 Pull request 点击 "Merge pull request" 合并代码}
    
