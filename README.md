# Git 和 GitHub 练习仓库

用一个简单的 Python 待办清单练习 Git 的提交、分支，以及在 GitHub 上查看改动和合并分支。

## 项目文件

- `main.py`：命令行待办清单。
- `.gitignore`：让 Git 忽略虚拟环境、Python 缓存和 PyCharm 配置。
- `README.md`：你正在阅读的项目说明和练习指南。

## 运行程序

在 Windows PowerShell 中进入项目目录。程序使用 Python 3.9 或以上版本，无需安装第三方库。

```powershell
Set-Location 'E:\codex_coding\git-practice'
python main.py
```

每输入一条待办事项就按一次 Enter。输入空行后，程序会显示本次清单并退出。

## 第一次练习：在本地做一次提交

1. 从 `main` 创建练习分支。已有本地仓库可以直接进入目录，无需重新初始化或克隆。

   ```powershell
   git switch main
   git pull --ff-only origin main
   git switch -c practice/first-change
   ```

2. 用编辑器打开 `main.py`，把 `今日待办：` 改成 `我的待办：`，保存，然后运行以下命令。

   ```powershell
   python main.py
   git status
   git diff -- main.py
   git add main.py
   git diff --staged
   git commit -m "更新待办清单标题"
   git log --oneline -3
   ```

   `git add` 选中下次要提交的文件内容，`git commit` 将它记录到本地历史。如果 `git status` 提示干净，说明本地没有待提交的改动。

3. 把练习分支上传到 GitHub。首次推送如果弹出登录页面，按提示授权。

   ```powershell
   git push -u origin practice/first-change
   ```

## 在 GitHub 上查看和合并改动

1. 打开 [仓库主页](https://github.com/fermi004/git-practice)。在 **Code** 页用分支下拉菜单切到 `practice/first-change`，然后点开 `main.py`，确认能看到新标题。
2. 打开 **Pull requests → New pull request**。设 `base: main`，`compare: practice/first-change`。PR（拉取请求）是一个可以查看差异、讨论并合并改动的页面。在 **Files changed** 检查修改。
3. 创建 PR 后，确认改动是自己想要的，再在 PR 页面按提示合并。
4. 回到 PowerShell，将 GitHub 上已合并的内容拉回本地 `main`。

   ```powershell
   git switch main
   git pull --ff-only origin main
   git status -sb
   ```

## 常用入口

- **Code**：浏览文件、切换分支、查看提交历史。在新电脑上，可以从 **Code → HTTPS** 复制地址并使用 `git clone` 下载仓库。
- **Pull requests**：查看和合并分支改动。
- **Issues**：记录待办、功能想法或问题。

这个仓库是公开的。提交前用 `git status` 和 `git diff --staged` 查看将要提交的内容，避免上传密码、访问令牌和未公开的数据。更多操作可参考 [GitHub 官方入门练习](https://docs.github.com/en/get-started/using-github/hello-world)。
