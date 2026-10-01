# 游戏开发 GitHub 学习仓库

日期：2026-08-17  
用途：卡住时查、以后翻；**不要当成新课表从头学完。**  
相关：[[游戏开发推荐网站]] · [[师傅课/README]] · [[现在下一步]]

> 借鉴结构和写法可以；不要把别人的整作美术、音乐、关卡当自己的上架内容。

今晚仍以 firebot 测试场为准（`C:\Users\yehai\Documents\firebot`，F5）。这些仓库是路标，不是下一关要通的副本。

---

## 1. gonglei007/GameDevMind（中文）

- 仓库：https://github.com/gonglei007/GameDevMind  
- 是什么：游戏开发技术图谱。

**怎么用：** 卡住时当词典查。搜「存档 / 状态机 / 关卡」这类词，看行业里通常把一块系统拆成什么。  
**不要：** 把图谱上每一个节点都学一遍。

---

## 2. miloyip/game-programmer

- 仓库：https://github.com/miloyip/game-programmer  
- 是什么：很经典的游戏程序员学习路线。

**怎么用：** 先收藏。内容偏底层、很长。  
**不要现在：** 顺着它去学线性代数、引擎内核。那是以后的事，会把第一款猫拖死。

---

## 3. munificent/game-programming-patterns

- 仓库：https://github.com/munificent/game-programming-patterns  
- 配套免费书：https://gameprogrammingpatterns.com  

**先看这几章（少返工）：**

| 模式 | 人话 | 和 Godot 的关系 |
|------|------|-----------------|
| State / 状态机 | 走、跳、冲各是一种状态，不要用一堆 `if` 缠死 | 以后玩家动作多了再用 |
| Component / 组件 | 能力拆成小块，不要一个脚本包打世界 | 场景树本身就偏这个 |
| Command / 命令（输入） | 「按下」变成一条指令，键盘和手机可发同一条 | 我们已在用动作名 `Dash` `Jump` |
| Observer / 观察者 | 一件事发生了，别人来听 | Godot 里就是 **信号（signal）** |

**对你最有用的一句：** 不要把玩家脚本写成「上帝脚本」（一个文件管移动、UI、存档、对话、战斗）。测试场现在还小，够用；以后加系统时按这块拆。

---

## 4. gdquest-demos/godot-design-patterns

- 仓库：https://github.com/gdquest-demos/godot-design-patterns  
- 是什么：上面那些模式在 Godot / GDScript 里的现成工程。

**怎么用：** 比纯理论更适合你。打开工程看状态机是怎么挂到节点上的。  
配套文章（可先看状态机）：https://www.gdquest.com/tutorial/godot/design-patterns/finite-state-machine/

---

## 5. godotengine/godot-demo-projects

- 仓库：https://github.com/godotengine/godot-demo-projects  
- 是什么：Godot 官方示例工程。

**怎么用（拆别人的，比看「注意事项」文章更值）：**

- 场景怎么分  
- 2D 角色怎么做  
- 游戏怎么暂停  
- 关卡怎么切换  

我们测试场的 Esc 暂停，以后对照这里的暂停示例即可。

---

## 补充：只想练 GDScript 语法时

- 仓库：https://github.com/GDQuest/learn-gdscript  
- 浏览器里练变量、函数、循环。  
- 这是练语法，**不是**做完整游戏。做游戏仍回 firebot 测试场。

---

## 资源大清单（只收藏）

- 仓库：https://github.com/dawdle-deer/awesome-learn-gamedev  
- 学习资料合集。需要时再搜，不要从头刷完。

---

## 和当前 firebot 怎么配

| 你现在在做的 | 对应上面哪条 |
|--------------|--------------|
| 测试场、动作名、Esc 暂停 | 官方 demo 的暂停 / 2D 角色 |
| 键盘和手机同一套输入 | 书里的 Command；我们已在用动作名 |
| 以后玩家脚本太长 | 状态机 + 组件；先看 GDQuest 的 Godot 实现 |
| 卡住不知行业怎么拆系统 | GameDevMind 查词，不学整张图 |
| 觉得自己数学/引擎不够 | miloyip 先别开，做完第一座林子再说 |

最后更新：2026-08-17
