# Blender · 火柴人（可绑骨维护）

日期：2026-08-14  
原因：只烘 PNG 时，软件里没有骨架、不能点选动画、也不能拉线改姿势。改为 **Armature + 部件绑骨 + Action**。

## 现在用这个工程

`C:\Users\yehai\Documents\SpineProjects\stickman-combo\stickman_rig.blend`

- 骨骼物体：`StickRig`（选中它再改动画）
- 部件：`StickPart_*`（头/身/四肢/剑，已经绑在对应骨头上）
- 旧蜡笔 `Stickman` 已隐藏，当参考，不要当主工程

## 点选动画（两种，都是软件自带能力）

### A. 侧栏按钮（我加的小插件，因为软件没有「角色动画一键切换」）

1. 3D 视图按 **N**
2. 找到标签 **Stickman**
3. 点：待机 / 走路 / 跳跃 / 攻击 / 冲刺 / 滑铲 / 格挡 / 攀爬 / 受击
4. 按 **空格** 播放

插件文件：`%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\stickman_anim_switch.py`  
偏好设置里应已勾选 **Stickman Anim Switch**。

### B. 不用插件（Blender 自带 Action）

1. 右键点物体列表里的 **StickRig**（不要点摄像机 Cam2D）
2. 底部时间轴左边下拉：把 **Dope Sheet** 改成 **Action Editor（动作编辑器）**
3. 中间动作名字下拉：选 `idle` `walk` `jump` `attack` `dash` `slide` `block` `climb` `hurt`

你截图里摄像机属性的「动画 → 新建」，是给 **相机** 做动画用的，不是角色。角色动画在骨骼 `StickRig` 上。

## 自己改姿势

1. 选中 `StickRig` → 左上角模式改成 **姿势模式（Pose）**
2. 点灰骨头拖旋转（2D 主要转 Y 轴；肩、髋、头都能拉）
3. 时间轴上插入关键帧（选中骨头按 **I** → 旋转/位置）
4. 改完 **Ctrl+S** 保存

## 比例（2026-08-14，按 8 头身）

绘画常用标准：全身 **8 个头高**（[人体比例](https://en.wikipedia.org/wiki/Body_proportions)）。

| 位置 | 从头顶往下 |
|------|------------|
| 头顶～下巴 | 第 1 头 |
| 肩膀 | 约 1.3 头处 |
| 肘 = 肚脐 | 第 3 头 |
| 腕 = 髋/裤腰 | 第 4 头（全身一半） |
| 膝 | 第 6 头 |
| 脚底 | 第 8 头 |

胳膊从身体**顶角**长出，腿从**底角**长出，剑从手腕长出。冲刺仍不压扁。

## 外形（2026-08-14 晚，v4）

网上生成这种角色，大家常用这套词（你以后跟我说、跟别的 AI 说，都可以直接复制）：

**英文（给图像 AI / 搜参考图）**

> minimalist 2D stickman, large circular head sitting directly on the torso, **no neck**, capsule / pill limbs, **rounded joint balls** at shoulder elbow hip knee wrist, rubber-hose animation style, angry simple face (thick V-brows, big dot eyes, frown V-mouth), dual swords in hands, clean vector, high contrast black on white

**人话对照**

| 你感觉到的问题 | 他们用的词 | 意思 |
|---|---|---|
| 没有表情 / 脸太小 | angry simple face, V-brows, dot eyes | 圆脑袋上画明显五官 |
| 不要脖子 | no neck, head sitting on torso | 头直接搁在身体顶上 |
| 手脚连接太僵 | capsule / pill limbs, ball joints, rubber hose | 胶囊胳膊 + 关节圆球，不要方块铰链 |

Blender 里对应改动：删了脖子方块；头压进身体；四肢改胶囊并在肩肘髋膝腕加圆球；骨头开了 **Bendy Bones**（弯折时会弯，不是死折）。

- **冲刺 Dash**：身体不压扁，侧身跨步冲出去（对应游戏 `Dash`）。

## 外形（2026-08-14 晚，v5 双刀）

人还是自己的绑骨（能点动画、能拉骨头）。难看的黑疙瘩手脚和木棍武器换掉了：

- **手脚**：白填充 + 黑描边（不再整块涂黑）
- **身体**：细黑线火柴人（参考 [RGS_Dev CC0 2D stick figure](https://rgsdev.itch.io/animated-stick-figure-character-2d-free-cc0)，itch 要自己点一次 $0 下载 `.blend`）
- **武器**：[Poly Haven Antique Katana](https://polyhaven.com/a/antique_katana_01)（CC0 太刀），左右手各一把，双刀流。文件在 `templates/katana/`

OpenGameArt 的 [Creomoto StickMan](https://opengameart.org/content/creomotos-stick-man-fixed-up) 也下了（CC0），但是 3D 方块人，不像 2D 火柴人，所以没用它当身体。

`...\spritesheet\stickman_spritesheet.png`

以后姿势改满意了，再重新渲表。

## 规则

Cursor 规则：`prefer-native-tools-maintainability`（先用软件骨架/动作，没有的再写小插件；交付必须能点选、能拉骨）。

遥控仍用侧栏 **BlenderMCP**。旧蜡笔工程 `stickman_slash.blend` 仅作备份。
