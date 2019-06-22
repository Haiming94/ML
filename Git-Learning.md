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

