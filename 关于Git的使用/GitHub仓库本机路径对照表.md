# GitHub 仓库本机路径对照表

用途：忘记某个 GitHub 项目在电脑哪个文件夹时，先来这里查。

总目录约定：以后新项目优先放进

`C:\Users\yehai\Projects\`

相关：[[Git和GitHub建立联系]] · [[Git和Obsidian建立联系]]

---

## 对照表

| GitHub 仓库                                                                                         | 本机路径                                         | 备注                |
| ------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------- |
| [Robert0825-ai/Obsidian](https://github.com/Robert0825-ai/Obsidian)                               | `D:\Godot-2D-study-word\Godot-2D`            | Obsidian 笔记库      |
| [Robert0825-ai/Robert0825-ai.github.io](https://github.com/Robert0825-ai/Robert0825-ai.github.io) | `C:\Users\yehai\Documents\newfiles\godot-2d` | 游戏开发分享 / Godot 项目 |
| `Robert0825-ai/-`                                                                                 | （待补充）                                        | 还不清楚本机在哪          |

> 有新仓库，或搬家到 `Projects` 后，记得改这张表。

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
