# 踩坑：my_test「人没动 / 看不见地」+ `.tscn` 出现 NUL 报错

> 工程：`C:\Users\yehai\Documents\firebot`  
> 场景：`res://Scene/my_test.tscn`  
> 相关：[[Godot2D搭建步骤-从空场景到可走跳]] · [[第1课-二段跳]] · [[第2课-无敌帧]]

---

## 当时现象

1. 运行后角色像钉在画面正中，绿色块在动。  
2. 看不到完整地面，只有一块绿。  
3. 后来编辑器报错：  
   `Unicode parsing error ... Unexpected NUL character`（打开 `my_test.tscn` 时）

---

## 问题 1：为什么像「人没动」

`fighter_player.tscn` 里角色下挂了 **`Camera2D`**。  
相机跟着人走 → 人永远在画面中心 → 世界（绿块）相对往后滑。

**解决（练习用）：** 在 `my_test` 里关掉跟焦，方便看出位移。

```text
Fighter_player
└── Camera2D   → Enabled = false（仅练习场景覆盖）
```

对应场景写法（实例上覆盖子节点属性）：

```
[node name="Camera2D" parent="Fighter_player" index="1"]
enabled = false
```

正式关卡想「镜头跟着人」时，再把 **Enabled** 勾回去即可。

---

## 问题 2：为什么「看不见地面」

核心原则（和搭建笔记一致）：

| 节点 | 作用 |
|------|------|
| `StaticBody2D` + `CollisionShape2D` | 只负责碰撞，**不会自动画出来** |
| `Polygon2D` / `Sprite2D` | 只负责外观 |

当时 `my_test` 的问题：

- 碰撞盒在一边（又大又长）  
- 绿色 `Polygon2D` 位置/顶点乱，又小又偏 → 只剩「一块绿」

**解决：** 让外观多边形和碰撞一样大、同一位置（对齐 `test_playground` 的写法）。

```text
Ground (StaticBody2D) @ (0, 400)
├── CollisionShape2D   矩形 2000 × 64
└── Visual (Polygon2D) 同样范围：(-1000,-32) … (1000,32)
```

玩家放在地面上方，例如 `(0, 280)`。

---

## 问题 3：`Unexpected NUL character` 是怎么来的

### 报错含义

Godot 的 `.tscn` 必须是 **UTF-8 文本**。  
若文件被存成 **UTF-16**，每个英文字符后面会多一个 `0x00`（NUL）。  
引擎按 UTF-8 读时就会报：

> Unexpected NUL character / Unicode parsing error

### 当时怎么改坏的（方便你对照学习）

为了修相机和地面，AI **直接改写了** `Scene/my_test.tscn` 的文本内容，意图是：

1. 重摆 `Ground`：碰撞 + 对齐的绿色 `Visual`  
2. 玩家移到 `(0, 280)`  
3. 覆盖关掉 `Camera2D.enabled`

在 Windows 上，若写入工具用了 **UTF-16**（或带一堆 NUL 的编码），文件看起来还像文字，但 Godot 会解析失败。

### 正确修法

用 **UTF-8（无 BOM）** 重新保存同一份内容，并确认文件里 **没有 `0x00` 字节**。

PowerShell 示例：

```powershell
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText(
  "C:\Users\yehai\Documents\firebot\Scene\my_test.tscn",
  $你的场景文本,
  $utf8NoBom
)
```

然后在 Godot 里重新打开 / 强制重载场景。

### 以后怎么避免

- 优先在 **Godot 编辑器**里改场景节点（检查器 + 保存），少手改 `.tscn`  
- 若必须手改 / 让 AI 改：保存后若出现 NUL 报错，先查编码是不是 UTF-8  
- 可用十六进制看文件头：正常 UTF-8 开头应是 `[gd_scene` 的字节 `91,103,100,...`，中间**不该**隔一个 `0`

---

## 一句话对照

| 现象 | 真正原因 | 怎么处理 |
|------|----------|----------|
| 人钉在屏幕中间 | `Camera2D` 跟焦 | 练习关关掉；正式关可再开 |
| 看不见地 | 有碰撞无对齐外观 / 外观没对齐 | `Polygon2D` 与碰撞同大同位置 |
| NUL / Unicode 报错 | `.tscn` 被存成 UTF-16 等错误编码 | 用 UTF-8 无 BOM 重存 |

---

## 改完后你该看到什么

运行 `my_test`：

- 脚下有一条完整绿色地面  
- 按左右时，**角色在画面里移动**（相机已关）  
- 编辑器不再刷 `Unexpected NUL character`
