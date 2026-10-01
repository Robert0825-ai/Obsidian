# 交给 Opus 5 · 走跑循环（Grok 没把握）

日期：2026-08-16  
写给人：Opus 5（出图 / 改帧）  
写稿人：Cursor Grok 4.6（已承认走跑循环没把握，且犯过「假交替」）  
游戏：黑夜骑士（Blackout Knight），工程 `C:\Users\yehai\Projects\night-knight`  
Look-dev：`C:\Users\yehai\Documents\SpineProjects\stickman-combo\pixel-knight\`

**请先打开本文再动手。** 不要接着 Grok 的走跑成品当终皮，除非你自己逐帧看过「哪只脚在前」。

---

## 1. 任务（只做这些）

做出能循环的：

1. **走路 8 帧**（两帧一拍、4 个姿势）  
2. **跑步 6 帧**（两帧一拍、3 个姿势）

角色是红缨黑骑士，侧面朝右，灰底 `#888888`。人和剑的大小锁在待机图。

做完必须：

- 浏览器循环能看出左右脚在换  
- `python audit_walk_run.py` 出 `AUDIT_OK`（含：至少 2 帧 `lead=far`）  
- 成品腿是炭黑盔甲，没有青/黄/蓝

不要做：走跑进 Godot Demo（用户没签字）；不要改 firebot 猫；不要自动跑 `slice_and_animate.py`。

---

## 2. 为什么交给你

Grok 对「灰底单骑士静帧、攻击分镜」有把握。  
对**走跑循环**没把握。已经交过一版，用户一眼看穿：

> 每一帧都是同一只脚在前，右脚在后，没有交替过。

Grok 当时用量「脚底宽窄」当检查。步子开合了，脚没换。检查空转。

后来走路 5、6 帧用脚本示意图重画，检测器报 `far`。**仍须你用人眼看循环**，不要信脚本一句。跑步检测仍是 0 帧 `far`，当作失败。

---

## 3. 锁死外观（不准改）

锁图（人和剑的尺子）：

`C:\Users\yehai\Documents\SpineProjects\stickman-combo\pixel-knight\unsliced\idle\01.png`

| 要 | 不要 |
|----|------|
| 炭黑盔甲、深灰黑披风、只有缨是绯红、银剑 | 红/蓝披风、灰白缨、青黄腿 |
| 侧面朝右，头在画面右边 | 最后一帧镜像朝左 |
| 灰底 `#888888` | 黑底白底 |
| 同一只人、同一把剑 | 某一帧整个人缩小 |

体量数字（`knight_scale.py`）：盔甲像素约 183000（82%～118%）；缨宽约 208（70%～140%）；银剑像素约 3250（白虚影帧跳过）。

禁区全文：同目录 `NEVER_AGAIN.md`。

---

## 4. 走跑分镜（面向右）

靠近镜头 = **近腿 = 角色右腿**（画面里更完整、高光更多）。  
远处 = **远腿 = 角色左腿**（略暗、略被挡）。

### 走路 8 帧

| 帧 | 姿势 | 近腿（右） | 远腿（左） | 检测器应报 |
|----|------|------------|------------|------------|
| 01–02 | 右脚接触 | **在前、踩地** | 在后 | `near` |
| 03–04 | 路过 | 收到身下 | 从后向前摆 | 近或 unknown |
| 05–06 | **左脚接触** | 在后 | **在前、踩地**（画面最右边那只脚是远腿） | **`far`** |
| 07–08 | 路过回去 | 从后向前摆 | 收到身下 | 近或 unknown |

相邻两帧几乎同一姿势，只挪一点。两帧才换脚。

### 跑步 6 帧

更前倾、步子更开，**不要缩成一团**。

| 帧 | 姿势 | 应报 |
|----|------|------|
| 01–02 | 右接触（近腿前） | `near` |
| 03–04 | 路过 | 近或 unknown |
| 05–06 | **左接触（远腿前）** | **`far`** |

口诀：**画面最右边那只脚，有一半接触帧必须是远处的左脚。**  
8 帧走路若有 6 帧都是近腿在前，作废。

---

## 5. 生成时不要再犯的（Grok 刚犯过）

1. **不要**把「右脚在前」的上一帧当参考去画「左脚在前」。模型会照抄同一只脚。左接触只准参考：待机锁 + **脚本画的**青黄示意图（或你已确认的 `far` 帧）。  
2. **不要**让模型生成青黄示意图。它会把青腿画到后面。用：

```
python draw_leg_diagrams.py
```

产出在 Cursor assets：`walk_diag_LEFT_script.png`（青脚必须在画面右边）、`walk_diag_RIGHT_script.png`。  
3. 示意图只借姿势。成品腿必须炭黑。扫一遍：除红缨外不准大块高饱和青/黄。  
4. **不要**用量包围盒高度、不要只用量脚距宽窄。脚距开合 ≠ 左右交替。  
5. 一张一张画，同一循环的相邻帧不要并行生成。  
6. 剑尖完整，右边留灰空。一帧一张图。

---

## 6. 现成文件（请打开看，不要盲信）

循环预览（本机若还开着 8769）：

- 走路：`http://127.0.0.1:8769/walk_v2/watch.html`  
- 跑步：`http://127.0.0.1:8769/run_v2/watch.html`  
- 攻击（已可用，不要重做）：`http://127.0.0.1:8769/attack_v2/watch.html`

磁盘：

| 路径 | 是什么 |
|------|--------|
| `unsliced/idle/01.png` | 锁图 |
| `unsliced/walk_v2/01.png` … `08.png` | Grok 试稿。01–02 近腿前；05–06 检测器报 far，**请你看循环确认** |
| `unsliced/walk_v2/_bad_same_foot_05.png` | 旧错帧：一直近腿前。检查必须仍判 `near` |
| `unsliced/run_v2/` | Grok 试稿。**检测 0 帧 far，当失败** |
| `unsliced/attack_v2/` | 攻击五帧，已过体量。不要当走跑参考（姿势不同） |

工作目录：`C:\Users\yehai\Documents\SpineProjects\stickman-combo\pixel-knight\`

验收命令：

```
python audit_knight_frames.py
python audit_walk_run.py
```

走跑必须先看到 `FIXTURE_SAME_FOOT_OK near`，再看到至少 2 个 `lead=far`，最后 `AUDIT_OK`。  
若旧错帧 `_bad_same_foot_05.png` 被判成 `far`，检测器坏了，不要交。

新帧请写到 `unsliced/walk_v2/`、`unsliced/run_v2/`（可覆盖 Grok 试稿）。对齐脚本：`build_walk_run_v2.py`。源生成图现放在 Cursor `assets/nk_walk_*.png`、`nk_run_*.png`。

看循环用浏览器 `watch.html`，不要指望 Cursor 里 GIF 会动。

---

## 7. 交回用户时怎么说

用人话告诉他：第几帧是右脚接触、第几帧是左脚接触。打开循环页给他看。没过 `AUDIT_OK`、或你自己看循环仍是同一只脚，不要说「这个也不错」。

没让进游戏就不要换进 `night-knight` 的 `SpriteFrames`。

---

## 8. 复制给 Opus 5（英文，省 token）

把下面整段贴进 Opus 5，并附上：`unsliced/idle/01.png`、脚本示意图 `walk_diag_LEFT_script.png`（青脚在画面右边）、`unsliced/walk_v2/01.png`、错例 `unsliced/walk_v2/_bad_same_foot_05.png`。

```
You are doing pixel look-dev for Blackout Knight. Grok already failed the walk/run cycles (same lead foot every frame). Do NOT treat Grok’s walk_v2/run_v2 as final unless you eyeball which foot is in front.

TASK ONLY: 8-frame walk (2 frames per pose, 4 poses) + 6-frame run (2 frames per pose, 3 poses). Side view FACING RIGHT, head on the right. BG always #888888. Charcoal armor, dark gray-black cape, crimson plume ONLY, silver sword. Same character/weapon size as the attached idle lock. Full sword tip every frame; leave gray space to the right of the tip. One PNG per frame. Finished legs MUST be charcoal armor — no cyan/yellow/blue.

Facing right: NEAR leg = character’s RIGHT (more complete, more highlight). FAR leg = character’s LEFT (slightly darker/occluded).

WALK: 01–02 right contact (near forward, lead=near); 03–04 passing; 05–06 LEFT contact (far foot is the rightmost planted foot, lead=far); 07–08 passing back. Adjacent frames almost identical; change feet every TWO frames. If 6/8 frames are near-forward, scrap it.

RUN: more lean, longer stride, do NOT squash into a ball. 01–02 near contact; 03–04 passing; 05–06 far/left contact. Need ≥2 frames lead=far.

DO NOT: use a near-forward previous frame as the ref when drawing left-foot-forward (the model copies the same foot). For left contact, ref ONLY the idle lock + the SCRIPT cyan/yellow diagram (cyan foot must be on the RIGHT of the image) or a frame you already verified as far. Do NOT generate the diagram with an image model. Do NOT use foot-span open/close or bbox height as “alternation.” Generate frames sequentially, never parallel for adjacent cycle frames. Do not put walk/run into the Godot Demo or firebot cat. Do not run slice_and_animate.py. Attack 5-frames are done — do not redo.

Work dir: C:\Users\yehai\Documents\SpineProjects\stickman-combo\pixel-knight\
Write new frames to unsliced/walk_v2/ and unsliced/run_v2/. Align with build_walk_run_v2.py. Preview loops in browser watch.html (Cursor GIFs freeze).

PASS: python audit_walk_run.py shows FIXTURE_SAME_FOOT_OK near on _bad_same_foot_05.png, at least 2 lead=far, then AUDIT_OK. If the bad fixture is scored far, the detector is broken — do not ship. Also python audit_knight_frames.py. Tell the user in plain language which frames are right-contact vs left-contact. If the loop still looks like one foot, do not say it is good enough.
```
