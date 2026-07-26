<div align="center">

# zhizhi（知之）

**「知之为知之，不知为不知，是知也。」**

—— 《论语·为政》

<br/>

开工 `kickoff` &nbsp;·&nbsp; 收工 `wrapup` &nbsp;·&nbsp; 不放心 `quiz-me`

三个命令，在代价变大之前，让你"是知也"。

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-4B8BBE)](https://agentskills.io)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-D97757)](#claude-code)
[![Codex CLI](https://img.shields.io/badge/Codex_CLI-supported-10A37F)](#openai-codex-cli)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](./LICENSE)

[English](./README.md) · **中文**

</div>

---

## 两千年前的答案，和今天的问题

孔子给"智"下过一个定义：知道自己知道什么，也知道自己不知道什么。

和 AI 结对干活时，这句话变成了一个工程问题。你的提示词是一张**地图**，代码库——连同
它的历史、惯例、写了一半的适配器——才是**疆域**。两者不一致的地方，Agent 只能靠猜；
而它猜的每一处，都是你"不知，而不自知"的地方。你委托的工作越多，它猜得越多。

把孔子的两句拆开，再往下推两层，正好是这套工具要对付的四种状态：

| 状态 | 对应 | 谁来解决 |
|---|---|---|
| **知之为知之** | 你写进提示词里的东西 | 已经解决了 |
| **不知为不知** | 你知道还没想清楚的问题 | 访谈你，一次一个问题 |
| **知，而不自知** | "看到才知道要什么" | 出几个原型让你挑 |
| **不知，而不自知** | 完全没想到的坑 | 替你扫盲区 |
| **不知，而以为知** | 你当作事实的、其实是错的 | 前提挑战，逐条证伪 |

最后一种正是孔子那句话真正批评的状态——"强不知以为知"。原文的四象限默认你的
"已知"都是对的，但最贵的事故恰恰来自错误的确信，所以我们给它补了一个专门的技巧。

但这里有个悖论：**最需要发现盲区的人，恰恰是不知道自己有盲区的人。** 你永远不会
想到"我现在处于'知而不自知'状态，该跑对应的技巧了"。

所以这套工具不要求你背任何分类法，它只对应**三个你真切感知得到的时刻**。

## 三个时刻

### 🔍 `kickoff` —— "我要开始干活了"

先诊断你的 unknowns，然后**只跑被触发的技巧**——不熟的领域先做盲区简报；"看到才
知道要什么"就出几个一次性原型；有悬而未决的决策就一次一个问题地访谈你；有参考实现
就提炼语义清单——最后落成一份 5 分钟能审完的计划，计划末尾是一份**验收契约**：
检查、预先承诺的及格线、谁来跑，在实现开始前就锁定。

```text
你：    /kickoff 加 SSO——这个应用的 auth 模块我从来没碰过

Agent： 两个信号触发了：陌生领域、未决决策。
        先对 src/auth 做盲区扫描……

        · 有一个写了一半的 OIDC 适配器（PR #142，已弃）——复用还是重写？
        · 会话存在签名 cookie 里，装不下 SSO token，这里需要你做决定。
        · 一个你不知道该问的问题：三条登录流程里，SSO 替换哪一条？

        接下来访谈你——一次一个问题，先问影响架构的。
```

如果什么信号都没触发，它会直说 **"没有值得挖的 unknowns——直接实现吧"**，然后让开。
kickoff 是诊断，不是仪式。

### 📦 `wrapup` —— "活干完了"

先**审计**：重跑计划里的验收契约，把 diff 对照计划重构出真实的偏差集、与实现笔记
对账——没被坦白的偏差是被检测出来的，不是靠自觉。然后把成果打包成 demo 开头的
buy-in 文档，把亲手跑 demo 的步骤和最值得深看的两三处抽查点交给你；再就真实发生的
改动（包括 diff 看不到的既有代码路径）出题考你。**契约全绿且测验通过，才建议合并**；
最后把这轮的意外发现沉淀进永久上下文。

### 🎯 `quiz-me` —— "我不确定自己看懂了这次改动"

单独的测验：讲解、出题、严格打分。明确给出 **PASS——你理解了这次改动** 或
**NOT YET——以下主题没过**。

"不知为不知"——没看懂就承认没看懂，这正是测验存在的意义。从不放水，所以 PASS
值得信任——但 PASS 只回答"理解"这一轴；改动本身对不对，是 wrapup 审计的问题。

## 循环

```mermaid
flowchart LR
    K["🔍 kickoff 开工"] --> P["unknowns 优先的计划<br/><i>+ 验收契约</i>"]
    P --> I["实现<br/><i>新会话，偏差自动记录</i>"]
    I --> W["📦 wrapup 收工<br/><i>审计 → 打包 → 测验</i>"]
    W -. "学到的沉淀进<br/>CLAUDE.md / AGENTS.md" .-> K
```

这一轮学到的，就是下一轮的地图。不知的越来越少，知的越来越实——**是知也**。

## 里面是什么

Thariq 的
[*A Field Guide to Fable: Finding Your Unknowns*](https://x.com/trq212/article/2073100352921215386)
里的八种技巧全都在——外加框架在逻辑上必然要求的两种。**前提挑战**：四象限默认
你的"已知"是对的，而最贵的失败恰恰来自错误的确信，所以 kickoff 会逐条证伪你
当作事实的东西。以及它的镜像——**验证审计**：实现完成后，错误确信的风险转移到了
实现者身上，所以 wrapup 用同样的标准证伪实现自己的断言——对着 diff 和运行系统验，
从不对着它自己讲的故事验。

全部技巧作为 Agent 的内部工具箱（每个 skill 的 `references/`）按需加载。你永远
不需要叫出它们的名字：

| 你说…… | kickoff 会拿出 |
|---|---|
| "这块代码我从来没碰过" | 盲区扫描 |
| "会话肯定存在 Redis 里，没别人调这个接口" | 前提挑战 |
| "给我看几个方向，我看到才知道要什么" | 头脑风暴 + 一次性原型 |
| "不确定这事到底可不可行" | 可行性探针 |
| "还有些事我没想好" | 一次一个问题的访谈 |
| "照着这个库做一个" | 参考实现语义提炼 |
| "好了，可以开始建了" | unknowns 优先的计划 + 实现笔记 |

<details>
<summary><b>展开看完整工具箱</b></summary>
<br/>

| 技巧 | 阶段 | 做什么 | 文档 |
|---|---|---|---|
| 盲区扫描 | 实现前 | 探索你不熟的领域，汇报你不知道该问的问题、坑、既有方案、以及"好"的标准 | [blindspot.md](./skills/kickoff/references/blindspot.md) |
| 前提挑战 | 实现前 | 把你和 Agent 当作事实的断言全部拎出来，逐条对着疆域验证：CONFIRMED / FALSE / UNVERIFIABLE，每条附证据 | [challenge.md](./skills/kickoff/references/challenge.md) |
| 头脑风暴 + 原型 | 实现前 | 5–10 个方案按"最便宜→最激进"排序，或 3–4 个风格迥异的单文件 HTML 原型；你的反应被沉淀成明确的判断标准 | [brainstorm.md](./skills/kickoff/references/brainstorm.md) |
| 可行性探针 | 实现前 | 最小实验拿到带测量证据的 yes/no；及格线在跑实验**之前**定好，防止事后合理化 | [brainstorm.md](./skills/kickoff/references/brainstorm.md)（Mode C） |
| 访谈 | 实现前 | 一次一个问题，先问影响架构最大的，每题附推荐默认值；产出可直接粘贴的决策日志 | [interview.md](./skills/kickoff/references/interview.md) |
| 参考实现提炼 | 实现前 | 读参考的真实源码，先产出"保留/改造/舍弃"语义清单，再动手写代码 | [use-reference.md](./skills/kickoff/references/use-reference.md) |
| unknowns 优先的计划 | 实现前 | 最可能被改的决策放最前（附置信度和"什么会推翻它"），机械性工作沉底 | [plan.md](./skills/kickoff/references/plan.md) |
| 实现笔记 | 实现中 | 边干边记决策、偏差和意外；偏差累积到第 3 条或前提被推翻时，触发中途重诊而不是继续给破产的计划打补丁 | [impl-notes.md](./skills/kickoff/references/impl-notes.md) |
| 验证审计 | 实现后 | 重跑计划的验收契约，从 diff 重构真实偏差集并与笔记对账，逐条评判实现自己的断言——对准实现者的前提挑战 | [audit.md](./skills/wrapup/references/audit.md) |
| 提案文档 | 实现后 | demo 开头的 buy-in 文档，评审者还没开口就先回答他们的疑问 | [pitch.md](./skills/wrapup/references/pitch.md) |
| 理解测验 | 实现后 | 报告覆盖 diff 看不到的部分，然后严格打分的测验——合并判定的"理解"轴 | [quiz.md](./skills/wrapup/references/quiz.md) |

</details>

wrapup 收的是两个环，不是一个：把这轮的意外沉淀进永久上下文（更好的地图），再回头
问"哪道屏障本该抓住这个——没触发的 kickoff 技巧？没写进契约的检查？为什么漏了"
（更好的画图方法）。

## 安装

#### Claude Code

```
/plugin marketplace add lusipad/zhizhi
/plugin install zhizhi@zhizhi
```

#### OpenAI Codex CLI

```sh
git clone https://github.com/lusipad/zhizhi.git
cd zhizhi && ./install.sh --codex
```

Windows：`.\install.ps1 -Codex`

#### 通用安装器（Claude Code + Codex + Cursor 等）

```sh
npx skills add lusipad/zhizhi
```

#### 手动安装

每个 skill 就是一个含 `SKILL.md` 的普通文件夹。把 `skills/` 下任意文件夹复制到你的
Agent skills 目录即可（`~/.claude/skills/`、`~/.codex/skills/`……）。

### 三条常驻规则

有两件事没人会记得主动触发：干活途中记实现笔记，以及合并前做检查。规则只有一份正本——
[`rules/unknowns-rules.md`](./rules/unknowns-rules.md)——按每种宿主的原生形态送达，
没有会漂移的拷贝：

| 宿主 | 规则如何生效 |
|---|---|
| Claude Code（插件） | **自动**——SessionStart hook 注入（sh 与 PowerShell 均可用；不想要就禁用插件） |
| Claude Code / Codex（克隆仓库） | `./install.sh --rules <项目>` 追加到 `CLAUDE.md` / `AGENTS.md`（幂等） |
| Cursor | 同一条命令在项目有 `.cursor/` 时生成 `.cursor/rules/zhizhi-unknowns.mdc` |
| Windsurf | 同一条命令在项目有 `.windsurf/` 时生成 `.windsurf/rules/zhizhi-unknowns.md` |
| `npx skills` / 其他宿主 | 手动复制那三行 |

Windows：`.\install.ps1 -Rules D:\your\project`。

## 多语言

指令正文保持英文（模型遵循度最高），但每个 skill 都明确要求：面向用户的输出——简报、
提问、测验、判定——**必须用你正在说的语言**。任何语言都能通过语义匹配触发；中文触发词
（开工 / 收工 / 考考我）已内置在 description 里。

## 设计原则

- **按时刻划分，不按分类法划分。** 人人都能感知"要开始了"和"干完了"，但没人能察觉
  自己"知而不自知"。命令对应前者，后者交给 Agent。
- **渐进式披露。** 3 个入口，技巧作为参考文档按需读取——不用时不占上下文。
- **天生可移植。** Frontmatter 只有 `name` + `description`（开放的
  [Agent Skills](https://agentskills.io) 格式），正文不含任何特定 Agent 的工具名。
- **不知为不知。** "直接实现吧"和 "NOT YET" 是一等公民的结论，不是失败——诚实的
  出口本身就是这套工具的核心主张。
- **作者永远不当裁判。** 计划在结果存在之前就锁定及格线；实现者记录证据但从不给
  证据打分；审计重跑检查而不是信任日志；"理解"（PASS）永远不与"正确"（契约计数）
  混为一谈。边界按**所有权**划——意图、价值权衡、不可逆操作、安全面、对外承诺，
  任何信任水平都停下来问人——而不按能力划，因为能力每次模型发版都在漂移。
- **叙事不是证据。** 会话讲述的"我做了什么"是地图。判定来自重跑命令和阅读 diff
  ——疆域——且每个"它能跑"的断言都要引用看得见的凭证。

### 诚实的局限（对自己也一样）

- skill 只能指示、不能强制——这里的一切都是君子协定。设计押注的是让诚实成为最省力
  的路径：重跑一条列好的命令，比伪造它更省力。
- 契约的双份留痕防的是漂移，不是对手——控制磁盘的会话可以把两份都改掉。
- 同会话的自审不可能"盲"；诚实的是 "(self-audited)" 这个标签本身。宿主提供第二个
  模型或子代理时就用它们——但 AI 验证者与 AI 实现者同源，相关的盲区无论如何都在。
- 按项目积累的信任账本——随记录放宽仪式——是 future work。

## 致谢与许可

理念来自 [Thariq (@trq212)](https://x.com/trq212) 的
[*A Field Guide to Fable: Finding Your Unknowns*](https://x.com/trq212/article/2073100352921215386)，
以及《论语·为政》。MIT——见 [LICENSE](./LICENSE)。
