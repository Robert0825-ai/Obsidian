# 输入原理：PC 键盘 vs 手机虚拟键（兼 Unity）

> 工程：`C:\Users\yehai\Documents\firebot`  
> 默认键位表：[[按键绑定]]  
> Cursor 规则：`firebot-input-defaults`  
> GDD：[[游戏设定：]] §8.4  
> 来源：2026-08-11 问答（师傅讲解「你是怎么做到的 / 要不要像电脑那样绑键 / Unity 呢」）  
> 相关代码：`Sprite/ui/touch_controls.gd` · `Sprite/ui/virtual_joystick.gd` · `Scene/ui/touch_controls.tscn`  
> 手游手感：[[手游操作-滑铲冲刺闪避常见做法]]  
> **详细代码解释（为什么改 + 逐段讲解）：** [[详细代码解释-圆形摇杆与虚拟键]]  
> **设计总览（TouchControls 怎么来的、改动清单）：** [[设计说明-TouchControls与输入改动总览]]---

## 结论（先看这三句）

1. **手机不用像电脑那样，在「输入映射」里再绑一套物理键。** 手机没有 A、空格。  
2. **手机做的是：** 屏幕按钮被点 → 告诉引擎「动作名 `Jump` / `Dash` 被按下了」。  
3. **玩家脚本只认动作名**，不认「是键盘还是手指」。Godot 和 Unity 都是这个哲学。

---

## 一、工程里其实有三层

```text
第1层：动作名（大家共用的暗号）
        Left / Jump / Dash / Down …

第2层：谁来触发这个暗号？
        PC：键盘（在输入映射里绑 A、空格、Shift…）
        手机：屏幕按钮（代码里注入同名动作）

第3层：玩家脚本
        只问：Jump 按了吗？  →  不管手指还是键盘
```

| 问题 | 答案 |
|------|------|
| 手机要像电脑那样再绑一遍键吗？ | **不用**（也绑不了「手机键盘 A」这种东西） |
| 那手机靠什么？ | 靠 UI 按钮 + 几行代码，把 `Jump` 等动作「按下去 / 松开」 |
| 输入映射还要吗？ | **还要**——至少 PC 要用；动作名也要在工程里存在，脚本和虚拟键才有共同暗号 |

可以记：

> **输入映射 = PC 的接线板；虚拟键脚本 = 手机的接线板；中间插头都叫 `Jump`。**

---

## 二、人话对照表

| | PC | 手机 |
|--|----|------|
| 硬件 | 键盘 | 手指点屏幕 |
| 工程里 | InputMap 把 A/空格绑到动作名 | 虚拟键 **注入** 同名动作 |
| 玩家脚本 | `is_action_pressed("Dash")` | **同一句代码**，不用写两套 |

---

## 三、firebot 里具体怎么做的（摘要）

> **完整「为什么改 + 逐段代码」见：** [[详细代码解释-圆形摇杆与虚拟键]]  
> 下面只留地图级摘要，避免和详解笔记重复过时。

### 3.1 场景结构（2026-08-11）

文件：`Scene/ui/touch_controls.tscn`（已挂 `test_playground`、`my_test`）

```text
左：圆形摇杆 virtual_joystick.gd
    ←→ 走；↑ Climb（爬）；↓ Down（向下爬）
右：跳 / 攻 / 冲 / 滑 按钮 → Jump / Attack / Dash / Slide
```

### 3.2 两种注入方式（都是同一套动作名）

| 控件 | 怎么注入 | 适合 |
|------|----------|------|
| 右按钮 | `InputEventAction` + `parse_input_event` | 点一下（跳、冲、滑） |
| 左摇杆 | `Input.action_press` / `action_release`（带力度） | 按住推（走、爬） |

玩家脚本仍然：`Input.is_action_just_pressed("Jump")` 等，不区分手指或键盘。

### 3.3 滑铲

- 手机：右手「滑」→ `Slide`  
- PC：方向+S，或 Ctrl→`Slide`  
- 详见详解笔记 §C。

---

## 四、和「电脑那种绑定」哪里像、哪里不像

| | PC 输入映射 | 手机虚拟键 |
|--|-------------|------------|
| 目的 | 让物理键对应动作名 | 让屏幕钮对应动作名 |
| 在哪设置 | 项目设置 → 输入映射 | `touch_controls` 场景 + 脚本 |
| 要不要动作名存在 | 要 | 要（名字必须和脚本一致） |
| 玩家移动脚本 | `is_action_pressed("Left")` | **同一句** |

所以：  
- **像：** 都是「某设备 → 动作名」。  
- **不像：** 手机不是再填一张「键位表」，而是 UI + 代码注入。

---

## 五、Unity 怎么对应？

思路几乎一样，只是名字不同：

| 概念 | Godot | Unity（常见） |
|------|-------|----------------|
| 动作名 | InputMap：`Jump` | 旧 Input Manager；或 **Input System** 的 Action（如 `Jump`） |
| 玩家脚本该听谁 | `Input.is_action_just_pressed("Jump")` | 如 `actions["Jump"].WasPressedThisFrame()` |
| 手机虚拟键 | 按钮 → `InputEventAction` / 注入动作 | 按钮 `OnPointerDown` → **触发同一个 Action** |
| 要不要为手机再写一套移动 | 不推荐 | 同样不推荐 |

Unity 两种做法：

1. **好做法（和 firebot 现在一样）：** UI 按钮 → 触发 Input Action「Jump」→ 角色只听 Action。  
2. **凑合做法：** 按钮直接 `player.Jump()`——能跑，但和键盘变成两套路，以后难维护。

新项目更推荐 Unity **Input System + UI 绑到 Action**；老教程里的 `Input.GetKey(KeyCode.Space)` 再另写一套触屏，容易分裂成两套逻辑。

---

## 六、自己在编辑器里怎么核对

1. 打开 `Scene/ui/touch_controls.tscn` → 看有哪些按钮  
2. 打开 `Sprite/ui/touch_controls.gd` → 看 `_wire_button(..., "Jump")` 等（手机版绑定表）  
3. 打开「项目 → 项目设置 → 输入映射」→ 看 PC 键盘绑到哪些动作名  
4. 打开 `sword_player.gd` → 搜 `is_action_`：应只有动作名，没有 `KEY_A` 之类

---

## 七、和本库其它笔记的关系

- 键位清单、滑铲组合、虚拟键表：[[按键绑定]]  
- **圆形摇杆 + 虚拟键：为什么改、逐段代码：** [[详细代码解释-圆形摇杆与虚拟键]]  
- 手游滑/冲/闪手感：[[手游操作-滑铲冲刺闪避常见做法]]  
- 产品层输入策略：[[游戏设定：]] §8.4  
- 冲刺/滑铲玩法课：[[师傅课/第4课-冲刺位移与冷却]]  

---

## 问答记录

### Q：你是怎么做到的？手机要在 Godot 里像电脑那样绑键吗？Unity 呢？（2026-08-11）

见上文全文。摘要：手机不绑键盘；虚拟键注入同名动作；Unity 用 Input Action 同一哲学。
