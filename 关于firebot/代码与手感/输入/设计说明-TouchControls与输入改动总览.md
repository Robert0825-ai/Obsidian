# 设计说明：TouchControls 与输入相关改动总览

> 工程：`C:\Users\yehai\Documents\firebot`  
> 日期：2026-08-11  
> 读者：未来的自己（想搞懂「师傅到底改了啥、为什么」）  
> 代码逐段细讲：[[详细代码解释-圆形摇杆与虚拟键]]  
> 原理（PC/手机/Unity）：[[输入-PC与手机同一套动作]]  
> 键位表：[[按键绑定]]  
> 手游手感：[[手游操作-滑铲冲刺闪避常见做法]]  
> 约定：本文「设计」**默认包含代码改动与解释**；代码以 Markdown 原文保存（不用截图堆代码）。规则：`firebot-design-and-code-notes`

你在编辑器里选中的 `TouchControls`（挂着 `touch_controls.gd`、类型是 `CanvasLayer`）就是本文主角。

---

## 〇、本文包含什么（以后「设计思路」都按这个打包）

| 块          | 有没有                      |
| ---------- | ------------------------ |
| 为什么这样设计    | ✅ §二                     |
| 怎么创建 / 场景树 | ✅ §三                     |
| 改了哪些文件     | ✅ §四                     |
| 数据流        | ✅ §五                     |
| 核心代码（摘要级）  | ✅ §九（下面补）                |
| 逐段细讲       | ✅ 另文 [[详细代码解释-圆形摇杆与虚拟键]] |

---

## 一、一句话总览

**没有给手机另写一套「走路/跳跃脚本」。**  
而是加了一层屏幕 UI（`TouchControls`）：手指点/拖时，向引擎**注入和键盘相同的动作名**（`Jump`、`Dash`、`Left`…）。  
玩家脚本（`sword_player` / `fighter_player`）继续只听动作名。

---

## 二、设计思路（为什么要这样）

### 2.1 目标

| 目标            | 做法                                |
| ------------- | --------------------------------- |
| 以后上手机         | 现在就有可点的虚拟操作                       |
| PC 还能玩、还能测手游键 | 开发期 `show_on_pc_for_test` 在电脑上也显示 |
| 玩家脚本不因平台分裂    | **一套动作名**，两套设备                    |
| 像市面手游         | 左圆形摇杆，右跳/攻/冲/滑                    |

### 2.2 三层模型（背这个）

```text
第1层 动作名（暗号）     Left Jump Dash Slide Climb Down …
第2层 谁触发暗号？       PC 键盘 InputMap ｜ 手机 TouchControls
第3层 玩家脚本           只问 is_action_pressed("Jump") 等
```

### 2.3 为什么单独做一个 `TouchControls`，不写进玩家脚本？

| 若写进玩家脚本 | 问题 |
|----------------|------|
| `sword_player` 里画按钮 | 每个角色都要复制一份 UI；换枪兵/战斗机又抄一遍 |
| 和移动逻辑缠在一起 | 调按钮位置时容易改坏跳跃/冲刺 |

| 做成独立场景再实例化 | 好处 |
|----------------------|------|
| `Scene/ui/touch_controls.tscn` | **一处做好，多关卡拖进去** |
| 与角色解耦 | 玩家只负责「听到 Jump」；UI 只负责「发出 Jump」 |
| `CanvasLayer` | 屏幕固定一层，**镜头移动按钮不跟着跑掉** |

### 2.4 为什么根节点是 `CanvasLayer`？

你在检查器里看到的：

- 类型：`CanvasLayer`  
- 脚本：`touch_controls.gd`  
- `layer = 100`（比较靠上，盖在游戏画面上）

**人话：**  
`Node2D` 角色在「世界坐标」里走；UI 要钉在「屏幕角落」。  
`CanvasLayer` = 专门盖在屏幕上的一层玻璃纸，相机怎么拖，左下摇杆、右下按钮都还在屏幕上。

### 2.5 左手 / 右手怎么分？

```text
左手（去哪）     圆形摇杆：←→走，↑爬(Climb)，↓下爬(Down)
右手（干什么）   跳 / 攻 / 冲 / 滑
```

- **冲 = 闪避**（少一颗键，许多手游如此）  
- **滑 = 独立键**（不靠摇杆斜下组合，避免误触）  
- PC 仍可：键盘方向 + 物理键 S；或 Ctrl=`Slide`

---

## 三、TouchControls 是怎么「创建」出来的？

不是神秘插件，就是普通 Godot 场景 + 两个脚本。

### 3.1 新建了哪些文件？

| 路径 | 角色 |
|------|------|
| `Scene/ui/touch_controls.tscn` | UI 场景：节点树 + 布局 |
| `Sprite/ui/touch_controls.gd` | 总控：要不要显示、右侧按钮接线 |
| `Sprite/ui/virtual_joystick.gd` | 左摇杆：画圆、拖动、注入四向 |

### 3.2 场景树长什么样？

```text
TouchControls (CanvasLayer) ← 你截图里选中的节点
└─ Root (Control，铺满屏幕，mouse_filter=忽略空白处点击)
   ├─ Hint (Label，顶栏说明文字)
   ├─ Joystick (Control + virtual_joystick.gd)
   └─ RightPad (GridContainer)
      ├─ BtnJump  → 动作 "Jump"
      ├─ BtnAttack → "Attack"
      ├─ BtnDash → "Dash"
      └─ BtnSlide → "Slide"
```

按钮勾了 **唯一名称**（`%BtnJump`），脚本里用 `%BtnJump` 找，不怕改父节点路径。

### 3.3 怎么挂到你的测试场？

在关卡场景里**实例化**（Instance）这份预制体，不是把代码复制进 `MyTest`：

| 场景 | 做法 |
|------|------|
| `Scene/test_playground.tscn` | 子节点 `TouchControls` = 实例 `touch_controls.tscn` |
| `Scene/my_test.tscn` | 同上（你截图的 `MyTest`） |

所以你在 `MyTest` 树里看到 `TouchControls`，点开脚本是 `touch_controls.gd`——对，就是这套。

### 3.4 创建步骤（若从零再做一遍）

1. 新建场景，根节点选 **CanvasLayer**，存为 `Scene/ui/touch_controls.tscn`  
2. 加子节点 `Root`（Control，全屏锚点）  
3. 左下加 `Joystick`（Control），挂 `virtual_joystick.gd`  
4. 右下加四个 `Button`，设唯一名，挂到 `touch_controls.gd` 的 `_wire_button`  
5. 在 `my_test` / `test_playground`：**实例化**该场景  
6. 检查器可勾 `Show On Pc For Test`（开发期用鼠标点着试）

---

## 四、师傅对工程做了哪些改变？（清单）

### 4.1 新增

| 项 | 说明 |
|----|------|
| `TouchControls` 整套 | 见上三节 |
| InputMap 动作 `Slide` | 专用滑铲（Ctrl / 手机「滑」） |
| InputMap 动作 `Interact` | 预留 E（互动） |
| `Attack` 增加鼠标左键 | PC 副键 |
| `Scene/main_menu.tscn` + `main_menu.gd` | 首页展示键位，进测试场 |
| 主场景改为 `main_menu.tscn` | F5 先见菜单（可改回） |

### 4.2 修改（玩家与输入逻辑）

| 文件 | 改了什么 | 为什么 |
|------|----------|--------|
| `sword_player.gd` | 滑铲认 `Slide`；方向+S 仅当**物理键** S/↓ | 摇杆斜下不再误触滑铲 |
| `sword_player.gd` | 冲刺听 `Dash`（Shift/C / 手机「冲」） | 冲=闪，一套动作 |
| 早期滑铲曾用 `Down`+方向 | 先改独立 Slide，再修物理键判断 | 对齐手游习惯 |
| `fighter_player.gd` | 注释补充默认键位；Climb/W 仍可练残影 | 师傅课练习场 |
| `test_playground` 地面 Label | 提示 PC/手机滑铲差别 | 运行时看得见 |

### 4.3 虚拟键演进（同一天内的迭代）

```text
① 左：方块 ◀▶ +「滑/S」在旁边
      → 丑，且难表达上/下爬
② 右：独立「滑」；左仍方块
      → 滑铲手感对了，左还是不像手游
③ 左：圆形摇杆（上Climb/下Down/左右）
      → 市面常见布局
④ 发现摇杆斜下误触滑铲
      → sword_player 增加 is_physical_key_pressed 限制
```

### 4.4 没改什么（刻意）

| 没动 | 原因 |
|------|------|
| 不用两套 `player_mobile.gd` | 避免维护两份移动逻辑 |
| 攀爬玩法本体（爬墙检测） | 摇杆已发 `Climb`/`Down`；墙/梯子逻辑可后做 |
| 摇杆精美贴图 | 先用 `_draw` 画圆，逻辑稳定再美化 |

---

## 五、数据怎么流？（从手指到角色）

### 5.1 点右侧「跳」

```text
手指按下 BtnJump
  → touch_controls._emit_action("Jump", true)
  → Input.parse_input_event(假的 Jump 按下)
  → sword_player / fighter：is_action_just_pressed("Jump")
  → _try_jump()
```

### 5.2 拖左摇杆向右

```text
手指拖动摇杆头
  → virtual_joystick._update_drag
  → Input.action_press("Right", 力度)
  → get_axis("Left","Right") > 0
  → velocity.x = 向右跑；facing = 1
```

### 5.3 点「滑」（手机正确滑铲）

```text
BtnSlide → 注入 "Slide"
  → want_slide = true
  → _start_slide() 朝 facing
```

### 5.4 摇杆推左下（不应滑铲）

```text
注入 Left + Down（力度）
  → Down 动作有了，但没有物理键 S/↓
  → want_slide 保持 false
  → 只当「左走 + 向下爬信号」，不滑铲
```

---

## 六、和你截图的对应关系

你打开的是 `MyTest`，树里有：

- `Ground`  
- `Fighter_player`  
- **`TouchControls`** ← 实例来的手机操作层  

检查器：

- Script = `touch_controls.gd`  
- **Show On Pc For Test** 勾选 → 所以在电脑上也能看见摇杆和按钮  

脚本 `_ready` 里四行 `_wire_button`：只负责**右四键**；左摇杆是子节点自己的 `virtual_joystick.gd`，不走这四行。

---

## 七、相关笔记怎么读（建议顺序）

1. **本文** — 改了啥、为什么、怎么创建（地图）  
2. [[输入-PC与手机同一套动作]] — 动作为什么能 PC/手机共用  
3. [[详细代码解释-圆形摇杆与虚拟键]] — 逐行代码（截图级）  
4. [[按键绑定]] — 键位速查  
5. [[手游操作-滑铲冲刺闪避常见做法]] — 市面手感与误触修复说明  

---

## 八、以后你自己加新关卡时

1. 打开新场景  
2. 把 `Scene/ui/touch_controls.tscn` **拖进去实例化**（或「实例化子场景」）  
3. 不要复制粘贴一整份按钮节点（改一处会漏改另一处）  
4. 新动作：先加 InputMap → 玩家脚本听动作名 → 再在 `touch_controls` 加按钮并 `_wire_button`

---

## 九、核心代码摘要（设计文里也要有代码）

> 更细的名词表/语法点见 [[详细代码解释-圆形摇杆与虚拟键]]。这里放「设计时最该记住」的几段。

### 9.1 右侧按钮：假装按下动作名

`Sprite/ui/touch_controls.gd`：

```gdscript
func _emit_action(action: StringName, pressed: bool) -> void:
	var ev := InputEventAction.new()
	ev.action = action
	ev.pressed = pressed
	ev.strength = 1.0 if pressed else 0.0
	Input.parse_input_event(ev)
```

**人话：** 做一个「Jump/Dash/Slide 被按下了」的假事件，塞进引擎；玩家脚本不用知道是手指还是键盘。

### 9.2 摇杆：上爬、下爬、左右走

`Sprite/ui/virtual_joystick.gd`：

```gdscript
func _apply_to_input(v: Vector2) -> void:
	_set_action_strength(&"Right", maxf(v.x, 0.0))
	_set_action_strength(&"Left", maxf(-v.x, 0.0))
	_set_action_strength(&"Down", maxf(v.y, 0.0))
	_set_action_strength(&"Climb", maxf(-v.y, 0.0))
```

**人话：** 控件坐标 y 向下为正 → 手指往上拖时 `v.y` 为负 → 用 `-v.y` 驱动 `Climb`。

### 9.3 滑铲：手机用 Slide；键盘方向+S 要验物理键

`Sprite/sword_player.gd`：

```gdscript
var want_slide := Input.is_action_just_pressed("Slide")
if not want_slide and Input.is_action_just_pressed("Down") and absf(axis) > 0.01:
	if Input.is_physical_key_pressed(KEY_S) or Input.is_physical_key_pressed(KEY_DOWN):
		want_slide = true
```

**人话：** 摇杆斜下也会注入 `Down`+左右，但不按真实键盘 S/↓ → 不滑铲。手机点「滑」走 `Slide`。

---

## 十、行号速查表（行｜代码｜作用）

> 约定（2026-08-11）：凡「按行号对照」的表，三列固定为 **行｜代码｜作用**。  
> 代码列用 `` `反引号` ``；多行用 `<br>`。行号以当时工程为准。

### `main_menu.gd` 第 1–34 行

| 行 | 代码 | 作用 |
|----|------|------|
| 4–5 | `const PLAYGROUND := "res://Scene/test_playground.tscn"`<br>`const MY_TEST := "res://Scene/my_test.tscn"` | 两个场景路径常量 |
| 8–10 | `if has_node("%KeysLabel"):`<br>`$"%KeysLabel".text = _keys_text()` | 启动时填键位说明文字 |
| 13–27 | `func _keys_text() -> String:`<br>`return "\n".join([ ... ])` | `_keys_text()` 拼 PC/手机键位说明 |
| 29–34 | `func _on_play_pressed()` → `change_scene_to_file(PLAYGROUND)`<br>`func _on_practice_pressed()` → `MY_TEST` | 按钮：进剑士场 / 进 my_test |

### `touch_controls.gd` 第 1–51 行

| 行 | 代码 | 作用 |
|----|------|------|
| 1 | `extends CanvasLayer` | 钉在屏幕层，不跟镜头跑 |
| 5 | `@export var show_on_pc_for_test: bool = true` | 开发期电脑也显示虚拟键 |
| 7 | `@onready var _root: Control = $Root` | 整层 UI 根节点 |
| 10–15 | `_root.visible = _should_show()`<br>`_wire_button(%BtnJump, "Jump")` … Slide | 显示判断 + 右四键接线 |
| 18–26 | `OS.has_feature("android")` 等 | 非测试时仅手机/触屏显示 |
| 29–35 | `button_down.connect(...bind(action))` + `mouse_exited` 松开 | 按下/松开接线；防卡键 |
| 46–51 | `InputEventAction.new()` … `Input.parse_input_event(ev)` | 注入假动作事件给玩家脚本听 |

### `virtual_joystick.gd` 关键行

| 行 | 代码 | 作用 |
|----|------|------|
| 5–7 | `deadzone` / `base_radius` / `knob_radius` | 死区与圆盘尺寸 |
| 18–21 | `mouse_filter = STOP`；`resized.connect(queue_redraw)` | 接住触点；尺寸变重画 |
| 24–25 | `_exit_tree` → `_release_all()` | 换场景防方向卡死 |
| 28–52 | `_gui_input` 触屏/鼠标 | 开始拖、拖动、结束拖 |
| 69–84 | `_update_drag`：夹长度、死区、映射 | 算方向向量并输出 |
| 96–101 | `Right/Left/Down/Climb` + `maxf` | 右/左/下爬/上爬 |
| 104–108 | `Input.action_press` / `action_release` | 按住推的持续输入 |
| 117–129 | `_draw` 画圆与十字 | 市面常见圆形摇杆外观 |

### `sword_player.gd` 滑铲/冲刺（约 100–114 行）

| 行 | 代码 | 作用 |
|----|------|------|
| 103 | `want_slide := Input.is_action_just_pressed("Slide")` | 手机「滑」/ Ctrl |
| 104–106 | `Down` + 左右轴 + `is_physical_key_pressed(KEY_S/DOWN)` | 仅键盘方向+S；摇杆斜下不误触 |
| 107–109 | `is_on_floor()` 且冷却好 → `_start_slide()` | 真正开滑铲 |
| 112–114 | `is_action_just_pressed("Dash")` → `_start_dash()` | 冲刺兼闪避 |

### 场景挂载

| 文件 | 代码/位置 | 作用 |
|------|-----------|------|
| `test_playground.tscn` ~4、63 | `ext_resource ... touch_controls.tscn` + 子节点实例 | 剑士场挂虚拟键 |
| `my_test.tscn` ~5、28 | 同上 | 师傅课练习场挂虚拟键 |
| `project.godot` ~14 | `run/main_scene="res://Scene/main_menu.tscn"` | F5 先进首页 |

---

## 问答记录

### Q：想知道对代码做了哪些改变、为什么要 TouchControls、怎么创建的、设计思路；并写入 Obsidian（2026-08-11）

见本文全文。细代码见 [[详细代码解释-圆形摇杆与虚拟键]]。

### Q：设计思路要含代码；写笔记后聊天也要讲；代码用 Markdown 还是截图？（2026-08-11）

**约定已写入规则** `firebot-design-and-code-notes` + 教法画像：

- 「设计思路」= 原因 + 改动清单 + 详细代码解释（聊天 + Obsidian）  
- **代码用 Markdown 代码块**（省空间、可搜索、好改）；截图只偶尔示意 UI  
- 写入 Obsidian 后，**当次聊天也要讲一遍**，不能只丢链接  

### Q：行号表要在「行」和「作用」中间加「代码」列；其它课也要（2026-08-11）

已定格式：**\| 行 \| 代码 \| 作用 \|**（见上文 §十）。  
师傅课第 1–4 课的 `## 详细代码解释` 末尾已补「行号速查表」。规则已更新。  
