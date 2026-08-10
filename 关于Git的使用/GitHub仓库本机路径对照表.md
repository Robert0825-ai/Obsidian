# GitHub 仓库本机路径对照表

用途：忘记某个 GitHub 项目在电脑哪个文件夹时，先来这里查。

总目录约定：以后新项目优先放进

`C:\Users\yehai\Projects\`

相关：[[Git和GitHub建立联系]] · [[Git和Obsidian建立联系]] · [[我的个人网站]] · [[温柔小管家]] · [[本机AI绘图环境-ComfyUI]]

---

## 对照表

| GitHub 仓库 | 本机路径 | 备注 |
|-------------|----------|------|
| [Robert0825-ai/Obsidian](https://github.com/Robert0825-ai/Obsidian) | `D:\Godot-2D-study-word\Godot-2D` | Obsidian 笔记库 |
| [Robert0825-ai/Robert0825-ai.github.io](https://github.com/Robert0825-ai/Robert0825-ai.github.io) | `C:\Users\yehai\Documents\newfiles\godot-2d` | 个人网站源码仓库（GitHub Pages） |
| `Robert0825-ai/-` | （待补充） | 还不清楚本机在哪 |
| [Robert0825-ai/gentle-butler](https://github.com/Robert0825-ai/gentle-butler)（[[温柔小管家]]） | `C:\Users\yehai\Projects\gentle-butler` | C# WPF；运行见该笔记 |
| [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)（[[本机AI绘图环境-ComfyUI]]） | `C:\Users\yehai\Projects\ComfyUI` | 本地 AI 出图；官方仓库 clone，非我的 GitHub 账号 |

### 本机工具（不一定是我的 GitHub 仓库）

| 工具 | 本机路径 | 备注 |
|------|----------|------|
| Character Creator VN | `C:\Users\yehai\Documents\Sprit\CharacterCreator.exe` | 拼立绘/导出表情；说明见 [[本机AI绘图环境-ComfyUI]] |
| 表情导出示例 | `C:\Users\yehai\Desktop\character-1786207265984\` | 11 张 PNG |

> 有新仓库，或搬家到 `Projects` 后，记得改这张表。

---

## 重要：个人网站链接（别和代码仓库搞混）

你已经有一个 **GitHub 免费个人网站**（二级域名）：

| 用途 | 链接 | 别人点开看到什么 |
|------|------|------------------|
| **给人看的网站**（发视频、自我介绍用这个） | https://Robert0825-ai.github.io | 网站页面（像博客/作品页那种界面） |
| **看源码的仓库**（开发、改文件用这个） | https://github.com/Robert0825-ai/Robert0825-ai.github.io | GitHub 代码/文件列表界面 |

记住口诀：

- 给别人、放视频简介 → 发 **不带** `github.com` 的：`https://Robert0825-ai.github.io`
- 自己改代码、看提交 → 打开仓库页或本机文件夹 `C:\Users\yehai\Documents\newfiles\godot-2d`

更完整的说明见：[[我的个人网站]]

---

## 更新某个仓库时怎么做

1. 在上表找到本机路径  
2. 打开 PowerShell：

```powershell
cd 这里换成表里的本机路径
git add .
git commit -m "更新说明"
git push
```

更新个人网站内容：改的是本机 `godot-2d` 文件夹，push 成功后，过一会儿刷新 https://Robert0825-ai.github.io 查看。

---

## 找不到旧路径时

1. 先看本篇对照表  
2. 再看总目录：`C:\Users\yehai\Projects\`  
3. 还是没有，可重新 clone 到总目录（注意：旧文件夹里没推送的改动不会自动过来）：

```powershell
cd C:\Users\yehai\Projects
git clone git@github.com:你的用户名/仓库名.git
```

4. clone 成功后，把新路径写回上面的对照表  

---

## 小约定（给我自己看的）

- 新 clone / 新项目：默认放进 `C:\Users\yehai\Projects\`
- 旧项目可以暂时留在原地，但路径要记在这张表里
- 搬家前先确认没有未提交的重要改动；搬家后更新本表，并检查 Obsidian / Godot 是否还指向正确文件夹
