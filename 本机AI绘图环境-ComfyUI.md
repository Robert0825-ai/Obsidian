# 本机 AI 绘图环境（ComfyUI）

用途：提醒自己 **2026-08-08** 已经在这台电脑装好了本地 AI 出图环境；以后做立绘、封面、表情参考时可以用，不必再怀疑「我有没有这条件」。  
相关：[[GitHub仓库本机路径对照表]] · [[游戏开发推荐网站]] · [[温柔小管家]]

> 一句话：有 **RTX 3060 Laptop 6GB** + 已装好的 **ComfyUI + CUDA 版 PyTorch**，能跑二次元文生图。

---

## 它在哪

| 项目 | 内容 |
|------|------|
| ComfyUI 本机路径 | `C:\Users\yehai\Projects\ComfyUI` |
| 启动方式 | 双击 `启动ComfyUI.bat`，或见下方命令 |
| 网页界面 | http://127.0.0.1:8188 |
| 上游仓库 | https://github.com/comfyanonymous/ComfyUI （官方，不是我自己的 GitHub） |
| Python | 3.10；venv 使用 `--system-site-packages`，共用系统里的 PyTorch |
| PyTorch | `2.13.0+cu126`（GPU 可用，已验证 `torch.cuda.is_available() == True`） |
| 显卡 | NVIDIA GeForce RTX 3060 Laptop GPU，**6GB 显存** |
| 推荐分辨率 | 先用 **512×768** 左右；显存紧时启动脚本带 `--lowvram` |

---

## 怎么启动

```powershell
cd C:\Users\yehai\Projects\ComfyUI
.\venv\Scripts\activate
python main.py --lowvram --preview-method auto
```

或直接双击：

`C:\Users\yehai\Projects\ComfyUI\启动ComfyUI.bat`

浏览器打开：http://127.0.0.1:8188

---

## 已下载的模型 / 工作流

| 类型 | 路径 |
|------|------|
| 起步二次元模型 | `C:\Users\yehai\Projects\ComfyUI\models\checkpoints\Counterfeit-V3.0_fp16.safetensors` |
| 文生图工作流（可拖进画布） | `C:\Users\yehai\Projects\ComfyUI\user\default\workflows\文生图-Counterfeit.json` |
| 桌面副本 | `C:\Users\yehai\Desktop\文生图-Counterfeit.json` |
| 生成图片输出 | `C:\Users\yehai\Projects\ComfyUI\output\` |

说明：新版 ComfyUI 左侧「工作流」列表可能是空的，把 json **拖进黑色画布** 即可加载。

---

## pip / 下载注意（踩过的坑）

- 默认 pip 已设 **清华源**：`%APPDATA%\pip\pip.ini` → `https://pypi.tuna.tsinghua.edu.cn/simple`
- **GPU 版 PyTorch** 仍要从官方 CUDA 轮子下（如 `cu126`），清华 PyPI 不含完整 CUDA 包
- 装 torch 时务必先 `.\venv\Scripts\activate`；曾经误装到系统 Python，后来用 system-site-packages 共用
- 官方源慢/SSL 报错时：开梯子（系统代理/TUN）再装

---

## 和「角色生成器 / 精灵帧」的关系（别混）

| 工具 | 路径 | 干什么 |
|------|------|--------|
| **ComfyUI** | `C:\Users\yehai\Projects\ComfyUI` | AI **画**新图（脸可能每次略有差别） |
| **Character Creator VN** | `C:\Users\yehai\Documents\Sprit\CharacterCreator.exe` | 用现成部件 **拼**角色，表情切换更稳 |
| 已导出表情示例 | `C:\Users\yehai\Desktop\character-1786207265984\` | 11 张 PNG（`1.png`～`11.png`） |

- Character Creator / Sutemo 素材：**游戏商用通常可以**，但不要把立绘素材单独打包转卖（以 itch 页许可为准）
- 两条路可并存：游戏表情优先 Character Creator；要原创 AI 图再用 ComfyUI（以后可再学角色 LoRA）

---

## 以后可能用到的延伸

- [ ] 装 IP-Adapter / 参考图锁定（同一角色多表情更稳）
- [ ] 学角色 LoRA（方法 3：专门训「这一个角色」）
- [ ] 从 [Civitai](https://civitai.com/) 再下更合适的模型到 `models\checkpoints\`
- [ ] 用 AI 出图做 Steam 封面 / 占位立绘，再进 Godot/Unity

想继续时可以说：「打开 ComfyUI」或「继续做角色表情 / LoRA」。

---

最后更新：2026-08-09
