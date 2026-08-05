目标：让你的电脑能认出 GitHub，以后才能把文件「推」上去。

相关笔记：[[Git和Obsidian建立联系]] · [[GitHub仓库本机路径对照表]]

忘记某个仓库在电脑哪个文件夹时，先打开：[[GitHub仓库本机路径对照表]]

---

## 先搞懂这几个词

| 名称 | 是什么 | 可以怎么理解 |
|------|--------|--------------|
| Git | 装在电脑上的软件 | 负责记「改了什么、哪一版」 |
| GitHub | 网站 | 把你的文件放在网上，方便备份和分享 |
| 仓库（repository） | 一个项目文件夹 | 本地有一份，GitHub 上也可以有一份 |
| 终端 / PowerShell | 黑窗口 / 蓝窗口 | **用来输入命令的地方**，不是编译器 |

> 下面这些代码**不是拿去编译的**。  
> 它们是「命令」：打开 PowerShell，复制粘贴进去，按回车执行。

---

## 一、命令要在哪里输入？

在 Windows 上，常用这个：

1. 按键盘 `Win` 键
2. 搜索 **PowerShell** 或 **Windows PowerShell**
3. 打开它
4. 看到类似 `PS C:\Users\...>` 的提示符，就可以输入命令了

也可以用：

- **Git Bash**（安装 Git 时一般会带上）
- Cursor / VS Code 下面的 **终端** 面板

本文以 **PowerShell** 为例。

---

## 二、准备条件

1. 电脑已安装 [Git](https://git-scm.com/)
2. 浏览器能登录 [GitHub](https://github.com)
3. 打开 PowerShell，输入下面这行，能看到版本号：

```powershell
git --version
```

**这行是什么意思？**  
问电脑：「Git 装好了吗？是哪个版本？」

---

## 三、告诉 Git「你是谁」（只做一次）

在 PowerShell 里输入（把引号里的内容换成你的）：

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

**这两行是什么意思？**

- `git config`：设置 Git 的配置
- `--global`：对这台电脑全局生效（以后每个项目都用）
- `user.name` / `user.email`：提交记录上显示的名字和邮箱

查看有没有设好：

```powershell
git config --global user.name
git config --global user.email
```

会分别打印出你刚设的名字和邮箱。

---

## 四、两种连 GitHub 的方式（选一种）

| 方式 | 远程地址长什么样 | 小白建议 |
|------|------------------|----------|
| SSH（推荐） | `git@github.com:用户名/仓库名.git` | 长期用，设一次较省事 |
| HTTPS | `https://github.com/用户名/仓库名.git` | 偶尔用，可能要反复登录 |

下面教 **SSH**。

---

## 五、用 SSH 把电脑和 GitHub 连起来

可以把它想成：给你的电脑配一把「钥匙」，GitHub 认这把钥匙后，才允许你上传。

### 1. 看看有没有现成的钥匙

在 PowerShell 输入：

```powershell
Test-Path $env:USERPROFILE\.ssh\id_ed25519.pub
```

**这行是什么意思？**

- `Test-Path`：检查某个文件在不在
- `$env:USERPROFILE\.ssh\id_ed25519.pub`：你用户目录下的公钥文件路径

结果：

- 显示 `True`：已有钥匙，跳到第 3 步
- 显示 `False`：还没有，做第 2 步

### 2. 生成钥匙

```powershell
ssh-keygen -t ed25519 -C "你的邮箱"
```

**这行是什么意思？**

- `ssh-keygen`：生成 SSH 密钥的工具
- `-t ed25519`：密钥类型
- `-C "你的邮箱"`：备注，方便以后辨认

一路按回车即可。  
会得到两个文件：

- `id_ed25519`：私钥（**不要发给别人**）
- `id_ed25519.pub`：公钥（要粘贴到 GitHub）

### 3. 把公钥放到 GitHub

先在 PowerShell 显示公钥内容：

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

**这行是什么意思？**  
把公钥文件内容打印出来，方便你复制。

然后在浏览器：

1. 打开 GitHub 并登录
2. 右上角头像 → **Settings**
3. 左侧 **SSH and GPG keys**
4. **New SSH key**
5. Title 随便写，例如 `我的电脑`
6. Key 里粘贴刚才复制的整行内容 → 保存

### 4. 测试能不能连上

```powershell
ssh -T git@github.com
```

**这行是什么意思？**  
试着用 SSH 连一下 GitHub，看认不认你的钥匙。

第一次可能问是否继续，输入 `yes` 回车。  
成功时大致会看到：

```text
Hi 你的用户名! You've successfully authenticated...
```

看到类似这句话，就说明：**电脑和 GitHub 已经建立联系了。**

### 5.（可选）有些网络连不上时

如果上一步失败，可能是网络拦了默认端口。  
可在用户目录下的 `.ssh\config` 文件里写：

```text
Host github.com
    HostName ssh.github.com
    Port 443
    User git
```

写好后再试一次 `ssh -T git@github.com`。

---

## 六、这一步完成了，还缺什么？

到这里只是：

> 电脑「有资格」访问你的 GitHub 账号

还没有把某个具体文件夹同步上去。  
要把笔记/项目真正传到 GitHub，请看：[[Git和Obsidian建立联系]]

那篇会告诉你：

1. 在 GitHub 网页新建仓库
2. 在本地文件夹里执行 `git init`、提交、推送
3. 每条命令是什么意思
4. **以后怎么更新** GitHub 上已有的内容

---

## 七、第一次推上去之后，怎么更新 GitHub？

第一次 `git push` 成功后，GitHub 上已经有一份内容了。  
你在电脑上又改了文件，**不会自动出现在 GitHub**，需要再「提交 + 推送」一次。

### 在哪里操作？

还是打开 **PowerShell**（不是编译器），先进入那个已经绑定过的文件夹：

```powershell
cd 你的本地文件夹路径
```

### 更新时固定做这三步

```powershell
git add .
git commit -m "更新说明，可自己改这句话"
git push
```

**逐行意思：**

| 命令 | 意思 |
|------|------|
| `git add .` | 把这次改过的文件，全部放进待提交清单 |
| `git commit -m "..."` | 在本地保存一版；引号里写这次改了什么 |
| `git push` | 把本地新版本上传到 GitHub |

完成后，用浏览器刷新你的 GitHub 仓库页面，就能看到最新文件。

### 常见提示

| 终端显示 | 含义 | 你要做什么 |
|----------|------|------------|
| `nothing to commit, working tree clean` | 没有新改动 | 不用 push；先在软件里保存文件再试 |
| 正常出现 commit 记录后 `git push` 成功 | 更新完成 | 去网页刷新查看 |
| `failed to push` 之类错误 | 上传失败 | 检查网络 / SSH，或先 `git pull` 再 `git push` |

### 和其他电脑同步时

如果另一台电脑也改过，并推到了 GitHub，你这台要先拉再改：

```powershell
git pull
```

**这行是什么意思？**  
从 GitHub 把网上最新版下载到本地，避免两边内容打架。

> 若主要是 Obsidian 笔记库，更完整的日常流程见：[[Git和Obsidian建立联系#四、以后日常怎么更新 GitHub 上的库]]

---

## 八、HTTPS 备选（不用 SSH 时）

绑定远程时可以用这种地址：

```powershell
git remote add origin https://github.com/你的用户名/仓库名.git
```

推送时 GitHub 可能要求登录。  
现在通常不能用账号密码，而要用 **Personal Access Token（个人访问令牌）** 当作密码。

小白更建议优先用 SSH。

---

## 九、常见问题

**Q：这些命令要在哪个软件里编译？**  
A：不用编译。打开 **PowerShell**（或 Git Bash / Cursor 终端）输入即可。

**Q：关联成功了，但以后 push 失败？**  
A：先再跑一次 `ssh -T git@github.com`；再检查远程地址里的用户名、仓库名是否写对。

**Q：换电脑怎么办？**  
A：新电脑要重新配置 Git 用户信息，并重新生成/导入 SSH 钥匙，再加到 GitHub。

**Q：公开仓库和私有仓库？**  
A：Public = 任何人能看；Private = 只有你（和你邀请的人）能看。按你是否想分享来选。

**Q：改完文件，GitHub 网页怎么还是旧的？**  
A：本地改动不会自动上传。需要再执行 `git add` → `git commit` → `git push`，然后刷新网页。
