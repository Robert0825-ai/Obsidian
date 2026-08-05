目标：让 Obsidian 里的笔记文件夹，能用 Git 管理，并上传到 GitHub 分享或备份。

相关笔记：[[Git和GitHub建立联系]]  
（请先确保那篇里的「电脑 ↔ GitHub」已经能连通。）

---

## 先搞懂在干什么

Obsidian 的「仓库」其实就是电脑上的一个普通文件夹。  
建立联系的意思是：

1. 在 GitHub 网站上建一个空仓库（网上的家）
2. 在本地这个文件夹里启用 Git（本地的家）
3. 把两者绑在一起，再把笔记推上去

> 下面的代码**不是编译代码**。  
> 请打开 **PowerShell**（或 Git Bash / Cursor 终端），进入你的笔记文件夹后，一条条执行。

### 命令在哪里输入？

1. 按 `Win` 键，搜索并打开 **Windows PowerShell**
2. 用 `cd` 命令进入你的 Obsidian 文件夹（见下文）
3. 再输入 `git ...` 相关命令

---

## 一、在 GitHub 网页新建仓库

用浏览器打开 GitHub，新建一个仓库。小白可以这样选：

| 选项 | 建议 | 原因 |
|------|------|------|
| Repository name | 自己起名，例如 `Obsidian` | 这是网上仓库的名字 |
| Public / Private | 想分享就 Public；只自己看就 Private | 公开后别人能打开链接看 |
| Add README | **关掉** | 本地已有笔记时，空仓库更好推 |
| Add .gitignore | **No** | 本地自己建更清楚 |
| License | **No** | 入门阶段可不加 |

点 **Create repository** 后，仓库就建好了。  
网页上会看到提示命令——**先不用急着照抄**，按本文顺序做更不容易乱。

![[Pasted image 20260805145722.png]]

你会用到一个远程地址（二选一，推荐 SSH）：

```text
SSH：  git@github.com:你的用户名/仓库名.git
HTTPS：https://github.com/你的用户名/仓库名.git
```

把其中的 `你的用户名`、`仓库名` 换成你自己的即可。

---

## 二、从零开始：完整操作（推荐照着做）

适合：这个文件夹**还没有**做过 `git init`，也**还没有**绑定过远程。

### 第 0 步：进入你的 Obsidian 文件夹

把路径换成你自己的笔记文件夹路径：

```powershell
cd 你的Obsidian文件夹路径
```

**这行是什么意思？**

- `cd` = change directory，进入某个文件夹
- 后面必须是你电脑上真实存在的路径

例（仅作格式参考，请改成你自己的）：

```powershell
cd D:\某个文件夹\我的笔记库
```

可用下面命令确认当前在哪个目录：

```powershell
pwd
```

---

### 第 1 步：初始化 Git

```powershell
git init
```

**这行是什么意思？**  
在当前文件夹创建一个隐藏的 `.git` 目录，表示「从现在开始，这个文件夹由 Git 管理」。

成功时大致会看到：`Initialized empty Git repository...`

![[Pasted image 20260805150328.png]]

---

### 第 2 步：添加忽略列表 `.gitignore`

Obsidian 有些文件只是窗口布局，经常变，同步上去容易打架。建议忽略它们。

在 PowerShell 里**整行复制**下面这一条（不要用 `@"` 那种多行写法，容易粘贴报错）：

```powershell
Set-Content -Encoding utf8 .gitignore ".obsidian/workspace.json`n.obsidian/workspaces.json`n.obsidian/workspace-mobile.json"
```

**这行是什么意思？**

- `Set-Content`：写入文件内容
- `.gitignore`：生成/覆盖这个忽略名单文件
- 引号里三行路径：告诉 Git 不要跟踪这些布局文件
- `` `n ``：在 PowerShell 里表示换行

写入后可检查：

```powershell
Get-Content .gitignore
```

应能看到：

```text
.obsidian/workspace.json
.obsidian/workspaces.json
.obsidian/workspace-mobile.json
```

也可以不用命令，直接在 Obsidian / 记事本里新建名为 `.gitignore` 的文件，把上面三行粘贴进去保存。
---

### 第 3 步：把文件交给 Git，并做第一次提交

```powershell
git add .
git commit -m "初始化 Obsidian 仓库"
git branch -M main
```

**逐行意思：**

| 命令 | 意思 |
|------|------|
| `git add .` | 把当前文件夹里该跟踪的文件，全部放进「待提交清单」（`.` 表示当前目录） |
| `git commit -m "..."` | 拍一张快照保存下来；引号里是这次提交的说明文字 |
| `git branch -M main` | 把当前分支命名为 `main`（GitHub 现在常用这个名字） |

---

### 第 4 步：绑定 GitHub 上的仓库

```powershell
git remote add origin git@github.com:你的用户名/仓库名.git
```

**这行是什么意思？**

- `git remote add`：添加一个远程地址
- `origin`：这个远程的昵称（以后推送时常用这个名字）
- 后面那串：GitHub 仓库的 SSH 地址

检查有没有绑成功：

```powershell
git remote -v
```

**这行是什么意思？**  
列出已经绑定的远程地址。能看到 `github.com` 就对了。

> 如果提示 remote origin already exists，说明之前绑过了。  
> 可先查看：`git remote -v`  
> 若地址不对，可删掉重加：
>
> ```powershell
> git remote remove origin
> git remote add origin git@github.com:你的用户名/仓库名.git
> ```

---

### 第 5 步：推送到 GitHub

```powershell
git push -u origin main
```

**这行是什么意思？**

- `git push`：把本地提交上传到网上
- `origin`：上传到昵称叫 origin 的那个远程
- `main`：上传 main 这个分支
- `-u`：记住这条对应关系，以后有时只需输入 `git push`

完成后，用浏览器打开你的 GitHub 仓库页面，能看到笔记文件，就成功了。

---

## 三、如果你已经做了一部分，从哪里继续？

不用从头再来，看你卡在哪一步：

| 你已经做过 | 下一步做什么 |
|------------|--------------|
| 只在 GitHub 建好了空仓库 | 从上面「第 0 步」开始 |
| 已 `git init`，还没 `remote` | 从第 2 或第 3 步继续，再到第 4、5 步 |
| 已 `git init` 且已 `remote add` | 做第 2、3 步（若还没提交），然后直接第 5 步 `git push` |
| 已经能在 GitHub 看到文件 | 平时只需「日常同步」 |

自检命令：

```powershell
Test-Path .git
git remote -v
git status
```

| 命令 | 用来看什么 |
|------|------------|
| `Test-Path .git` | 有没有初始化过（`True` = 有） |
| `git remote -v` | 有没有绑定 GitHub |
| `git status` | 当前有没有未提交的改动 |

---

## 四、以后日常怎么同步

在 Obsidian 里改完笔记后，打开 PowerShell，先 `cd` 进同一个文件夹，再执行：

```powershell
git add .
git commit -m "更新笔记"
git push
```

**意思简述：**

1. 把改动放入待提交清单  
2. 保存一版说明为「更新笔记」的快照  
3. 上传到 GitHub  

如果另一台电脑也要拿最新版：

```powershell
git pull
```

**这行是什么意思？**  
从 GitHub 把最新内容拉到本地。

---

## 五、可选：用 Obsidian 插件自动同步

命令行先跑通以后，可以在 Obsidian 里装插件，少敲命令。

1. Obsidian → **设置** → **社区插件**
2. 关闭 **安全模式**
3. **浏览** → 搜索 `Obsidian Git`
4. **安装** → **启用**

可在插件设置里打开：

- 自动 commit
- 自动 push
- 启动时 pull

注意：插件不能代替前面的绑定。  
仍需要这个文件夹已经是 Git 仓库，并且 `origin` 已指向 GitHub。

---

## 六、和「Obsidian 官方同步」有什么不同？

| | Git + GitHub | Obsidian Sync（官方） |
|--|--------------|------------------------|
| 钱 | 一般免费 | 要订阅 |
| 怎么同步 | 你提交/推送时同步 | 官方自动同步 |
| 分享 | Public 仓库可给人看链接 | 主要是自己多设备 |

不买官方 Sync，也可以用 GitHub 备份和分享。

另外：推到 GitHub 后，别人通常是在仓库页面看 Markdown 文件；  
这还**不是**自动生成一个独立漂亮网站。若以后想做成网站，可以再学 GitHub Pages 等方法。

---

## 七、常见问题

**Q：要打开什么软件来「编译」这些代码？**  
A：不用编译。打开 **PowerShell**，进入笔记文件夹后执行命令即可。

**Q：GitHub 新建仓库页面要选 HTTPS 还是 SSH？**  
A：如果你已按 [[Git和GitHub建立联系]] 配好 SSH，选 **SSH**。  
本地绑定也用 `git@github.com:...` 这种地址。

**Q：GitHub 页面上两段示例命令选哪个？**  
A：

- 「create a new repository on the command line」：适合从零新建，还会生成 README；**本地已有笔记时不太适合照抄**
- 「push an existing repository...」：适合本地**已经是** Git 仓库时；若你还没 `git init`，不能只复制那几行

更稳妥：按本文「从零开始」顺序做。

**Q：push 失败怎么办？**  
A：先确认 `ssh -T git@github.com` 能成功；再检查 `git remote -v` 地址是否写对。

**Q：密码、验证码能不能放进笔记再推上去？**  
A：不要。尤其是 Public 仓库，等于公开给所有人。

---

## 八、小白操作清单

- [ ] 已能打开 PowerShell，并 `cd` 进笔记文件夹
- [ ] GitHub 上已新建仓库（本地有内容时不要勾 README）
- [ ] `git init`
- [ ] 创建 `.gitignore`
- [ ] `git add .` 和 `git commit`
- [ ] `git branch -M main`
- [ ] `git remote add origin ...`
- [ ] `git push -u origin main`
- [ ] 浏览器打开 GitHub，能看到笔记文件
- [ ] （可选）安装 Obsidian Git 插件
