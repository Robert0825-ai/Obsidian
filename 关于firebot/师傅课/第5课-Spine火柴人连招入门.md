# 第 5 课：Spine 火柴人连招入门（双刀）

> 日期：2026-08-14  
> 工具：Spine Trial `C:\Program Files\Spine Trial\SpineTrial.exe`  
> 素材：`C:\Users\yehai\Documents\SpineProjects\stickman-combo\`  
> 说明：本课是**工具操作课**（暂无 Godot 代码）；连招先在 Spine 里能播，再谈进游戏。

## 本课目标

1. 打开 Spine，建好第一个火柴人工程  
2. 导入 **512** 图（不要用 2048）  
3. 摆一套最少骨骼  
4. 做出 **3～4 个关键帧** 的第一段挥砍（`slash_1`）  

过关：时间轴上能循环播放一记挥砍，看起来「抡出去又收回来」。

## 为什么不用 ComfyUI 了（复习一句）

AI 出帧对火柴人又慢又吃内存；Spine 是游戏连招正路：绑骨 → 关键帧 → 以后进 Godot。

---

## 手把手：从零到第一刀

### 0. 素材在哪（已帮你备好）

| 文件 | 用途 |
|------|------|
| `stickman_dual_sword_512.png` | **用这个导入** |
| `stickman_dual_sword_2048.png` | 备份，别直接进 Spine |

文件夹：`C:\Users\yehai\Documents\SpineProjects\stickman-combo\`

### 1. 打开 Spine Trial

1. 开始菜单或  
   `C:\Program Files\Spine Trial\SpineTrial.exe`  
2. 若弹出试用说明 → 知道功能有限制即可，先学流程  

### 2. 新建项目

1. **New Project**（新建）  
2. 建议：  
   - 名称：`stickman-combo`  
   - 保存到：`C:\Users\yehai\Documents\SpineProjects\stickman-combo\`  
3. 画布/导入图用 512 即可  

### 3. 导入图片（Setup 模式）

Spine 上面有模式切换，先留在 **Setup（装配）**：

1. 把 `stickman_dual_sword_512.png` 拖进 Spine，或用 Images / Import  
2. 树里应出现这张图对应的 **Slot（插槽）+ Attachment（附件）**  
3. 人话：插槽像「挂钩」，附件像「挂上去的纸片」  

### 4. 建最少骨骼（先能挥，不求完美）

目标骨架（够用就行）：

```text
root（根）
 └─ hip（胯/中心）
     ├─ torso（上身，可含头）
     ├─ arm_L → hand_L（左手，可连左刀）
     ├─ arm_R → hand_R（右手，可连右刀）
     ├─ leg_L
     └─ leg_R
```

操作习惯（不同版本文案略有差别，找不到就在左侧树 / 工具栏找 Bone）：

1. 选 **Create Bone（创建骨骼）**  
2. 从胯往上点出 `torso`，往两侧点出手臂、腿  
3. 把图片（slot）**挂到**大致对应的骨头上（拖到骨头下，或 Weight/绑定时再细调）  

**第一课偷懒版（若绑多张图太难）：**  
整张火柴人先挂在 `hip` 或 `torso` 上一根骨头上 → 先用**旋转整身 + 手臂骨**做出「砍」的感觉。  
下节课再拆部件（更像真连招）。

### 5. 切到 Animate（动画）做 `slash_1`

1. 切到 **Animate**  
2. 新建动画，命名：`slash_1`  
3. 时间轴上打关键帧（Keyframe）：

| 时间（约） | 动作（人话） |
|------------|----------------|
| 0 帧 | 站立预备（双刀架势） |
| 3～5 帧 | 手臂抬起蓄力 |
| 8～12 帧 | 刀抡到最前面（攻击判定点） |
| 16～20 帧 | 收回 / 结束  

4. 选中手臂或 `torso` 骨头 → 改 **Rotation（旋转）** → 自动或手动记下关键帧  
5. 点播放 ▶，看是否「抡出去又收回」  

### 6. 保存

- `Ctrl+S` 存项目（会有 `.spine` 文件）  
- 先**不要急着导出进 Godot**（下节课再做）

---

## 详细「面板」解释（本课无 GDScript）

### 1）Setup vs Animate

| 模式 | 干什么 |
|------|--------|
| Setup | 拼人：图挂哪、骨头怎么长 |
| Animate | 演戏：骨头在时间轴上怎么转 |

人话：Setup 做偶，Animate 拉线让偶动。

### 2）Bone / Slot / Attachment

| 词 | 人话 |
|----|------|
| Bone | 骨头，转它，图跟着转 |
| Slot | 挂钩位置（一层） |
| Attachment | 挂上去的那张图 |

### 3）关键帧

改旋转/位移后在时间轴上留下的「姿势书签」。中间帧 Spine 会帮你补间（Tween）。

### 4）为什么坚持 512

2048 在 AI 里已证明会拖垮内存；Spine 里也没必要用那么大预览图。

---

## 行号速查表（操作对照｜步骤｜作用）

本课无代码行号，用步骤表：

| 步骤 | 操作 | 作用 |
|------|------|------|
| 1 | 打开 Spine Trial | 进入编辑器 |
| 2 | 新建并保存到 `SpineProjects\stickman-combo` | 工程落地 |
| 3 | 导入 `stickman_dual_sword_512.png` | 有可视角色 |
| 4 | Setup 建 `root→hip→臂腿` | 有可转的骨头 |
| 5 | Animate 建 `slash_1` 打 3～4 关键帧 | 第一刀连招胚子 |
| 6 | 播放检查 | 确认能循环挥砍 |

---

## 过关标准

- [ ] 工程保存在 `SpineProjects\stickman-combo`  
- [ ] 用的是 **512** 图  
- [ ] 至少有动画 `slash_1`  
- [ ] 播放时能看出挥砍（不是完全静止）  

## 下节预告

- 把图拆成：身 / 左臂 / 右臂 / 两把刀（连招更好看）  
- `slash_2` 接段  
- 以后：导出 + Godot Spine 插件  

## 问答记录

（上课时追加）

- 2026-08-14：弃用 ComfyUI 路线 1；本课开始 Spine 路线 2。  
