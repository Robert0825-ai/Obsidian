# 02 · 技术设计（TDD）

作者角色：技术总监  
引擎：**Godot 4.x**（与本机 firebot 同代，当前 4.7 特征集；Demo 写 `4.7` + `Mobile` 以便安卓）

## 1. 目标

- 一份工程，导出 **Windows** 与 **Android**  
- 输入：InputMap 动作名，PC 与触屏注入同一套  
- 2D：`CharacterBody2D` + `AnimatedSprite2D`（Demo 只有 2 张姿势，不是走跑表）

## 2. 目录（2026-08-24）

独立 Demo `C:\Users\yehai\Projects\night-knight\` **已删**。切片暂住 firebot：

```
C:\Users\yehai\Documents\firebot\
  scenes/cemetery_stitch.tscn      # 四区环境原型
  scenes/mv_night_knight/          # 36 房布局实验
  assets/cemetery/                 # 墓园件
  assets/cemetery_knight/          # 拆件实验（白袍不是锁）
```

故事与终皮仍属黑夜骑士。有可玩切片、炭盔锁图进引擎后再分仓。拍板 [[13-拍板锁-2026-08-24]]。

## 3. 显示

- 逻辑分辨率 1280×720，`canvas_items` + `expand`  
- 像素精灵：`texture_filter = nearest`  
- 相机：跟着骑士，死区小，不要晃到恶心

## 4. 物理

- 重力约 980  
- 走速约 180–220（比猫测试略慢，人不是四脚窜）  
- 跳约 -400  
- 攻击：短 Timer，期间可轻微锁水平或保持惯性（Demo 保持惯性，不锁死）

## 5. 资源

- PNG 必须 **透明底** 进 Sprite。灰底 `#888888` 只存在生成/看图阶段，导入前用脚本扣。  
- 导入：`filter_nearest`，mipmaps 关

## 6. 安卓

- 导出模板以后再下；Demo 先在 PC 用鼠标点虚拟键验证逻辑  
- 刘海：虚拟键贴安全区下沿，不要挡住脚  
- 返回键 = `Pause`（完整版）

## 7. 不做（技术债清单）

- 联网、存档云、Steam 成就  
- Shader 刀光（有需求再加另层 Sprite）  
- 自动寻路

## 8. 验收命令（有 Godot 可执行文件时）

```
godot --path C:\Users\yehai\Documents\firebot --headless --import
godot --path C:\Users\yehai\Documents\firebot --quit-after 2
```

无红字 `Failed loading resource` 才叫能交。独立 `night-knight` 路径已作废。
