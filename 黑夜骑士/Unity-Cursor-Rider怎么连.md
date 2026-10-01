# Unity · Cursor · Rider 怎么连

日期：2026-08-16  
工程：`C:\Users\yehai\Documents\Hello Knight\My project`

三件东西各管一块，**不要互相代替**：

| 软件 | 干什么 | 怎么连 |
|------|--------|--------|
| **Unity** | 游戏本体：场景、精灵、按 Play | 开着这个工程 |
| **Cursor** | 跟助手说话；经 MCP 指挥 Unity | `mcp.json` 里的 `unityMCP` → `http://localhost:8080/mcp` |
| **Rider** | 写/调试 C#（断点、重构） | Unity 里把外部脚本编辑器设成 Rider |

口诀：**Unity 是舞台，Cursor 是导演，Rider 是编剧。**  
Cursor 不经过 Rider；Rider 也不需要 MCP。双击 `.cs` 从 Unity 跳到 Rider 即可。

---

## 已经替你改过的

1. 工程 `Packages/manifest.json` 加了包：`com.coplaydev.unity-mcp`（git `#v10.1.2`）
2. Cursor 用户 MCP 加了：`unityMCP` → `http://localhost:8080/mcp`

你本机已有 `uv`（Godot MCP 在用），向导一般能找到。

Rider 安装位置：`C:\Program Files\JetBrains\JetBrains Rider 2024.1.7\bin\rider64.exe`

---

## 你要在 Unity 里点的（助手点不到菜单）

1. 切回 Unity，等 Package Manager 把 MCP 包拉下来（第一次要联网）。
2. 菜单 **Window → MCP for Unity**。若弹出向导：确认 Python / uv 是绿的 → Done → 勾 Cursor → Configure。
3. 状态要变成 **Connected**。没有的话点 Start。
4. **Edit → Preferences → External Tools → External Script Editor** 选 **Rider**（或 Browse 到 `...\JetBrains Rider 2024.1.7\bin\rider64.exe`）。
5. 回 Cursor：**Settings → MCP**，看 `unityMCP` 是不是绿的。若刚改过 `mcp.json`，可能要开关一次 MCP 或重开这一侧聊天。

测通：在 Cursor 里说「在当前场景放三个立方体，红蓝黄」。场景里出现才算连上。

---

## 不要

- 不要用 Rider 当 Unity MCP 客户端（它不是这条线）。
- 不要关 Unity 只开 Cursor：桥断了，助手就控不了编辑器。
- 不要把《空洞骑士》拆包当这个空工程的素材。

相关：[[Hello-Knight素材分布]]
