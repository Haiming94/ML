## Git 学习

---- 2019/06/22 学习Git

## 本地库和远程库 の 交互

---- 团队内部协作
    
    项目经理 A 创建本地库 Bank-1 并将其 push 到远程库 Bank-2，而参与人 B 通过 clone 从 Bank-2 中下载内容并在本地初始化一个本地库 Bank-3，当 B 修改本地库以后，在加入 A 的团队后就可以向 Bank-2 上传他的 Bank-3 到 Bank-2.

---- 跨团队协作
    
    若 A和B 需要另一个团队的 C 帮忙，那么 A 可以 fork 一个新的远程库 Bank-4 给 C，C 可以直接 clone 远程库 Bank-4 到其电脑上建立本地库 Bank-5，经过 C 修改后，Bank-5 可以直接 push 到 Bank-4，同时，C 发出 pull request，经过 A 的审核，如果通过审核，A 发出 merge 的合并操作，此时的 Bank-4 就合并到 Bank-2，而 A和B 就可以通过 pull 到各自的 Bank。

## 
