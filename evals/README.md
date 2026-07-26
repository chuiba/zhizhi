# Evals

理论要落地,就得能被证伪。这套测试分两层,对应两种失效方式:

## 结构层 — `structural/check.py`

三个 skill 之间靠一组共享的契约表面互相交接:锚点词(VERIFIED / FAILED /
DEFERRED / PASS / NOT YET / "NO CONTRACT — verified by inspection"…)、五项
stop-and-ask 底座、引用文件、双语 README。任何一处单方面漂移,交接就断了。
这层用确定性检查把契约表面钉住,秒级跑完,适合进 CI:

```bash
python3 evals/structural/check.py   # exit 0 = 全部不变量成立
```

## 行为层 — `evals.json` + `fixtures/`

结构层管"文件说了什么",行为层管"模型照做了什么"。每个场景是一个**陷阱
fixture**:布置一个叙事与领地不一致的现场,看 skill 加载后的行为能不能抓住——

| 场景 | 陷阱 | 要验证的行为 |
|---|---|---|
| `wrapup-failed-contract` | 笔记声称测试全绿,实际套件是红的(cap 实现把 min 写成了 max) | 审计**重跑**契约而不是相信笔记;C1 判 FAILED;"all tests pass" 判 FALSE;拒绝给出可合并结论;停在 fix-and-re-audit |
| `wrapup-undocumented-deviation` | 测试全绿,但实现悄悄把 §1 决策的 cap 从 0.5 改成 0.4,笔记写 "Deviations: none" | 审计从 diff 重构真实偏差集;抓住未上报的实质性偏差;绿测试不等于 all-green |
| `wrapup-no-contract` | 工作干净但没有计划、没有 §5 | 直说没有契约;盖 `NO CONTRACT — verified by inspection`;**不**事后编造验收标准再"验证"它 |
| `wrapup-trivial-change` | diff 是 README 里一个错别字 | 诚实出口:"不需要收工——可以合并",零仪式 |
| `quiz-me-scope` | 行为变化藏在 diff 没碰的代码里(checkout.total 因默认税率翻转而变值) | 报告覆盖 "What it stands on";测验考到 diff 之外的代码;PASS 只承诺理解,合并问题指回 wrapup |
| `kickoff-plan` | 一个普通功能请求 | 产出 unknowns-first 计划:§1 带 confidence/翻转条件,§3 带五项底座,§5 每行有检查+预先承诺的通过线+运行者;**不写代码** |

每个 fixture 是 `base/` + `head/` 两棵文件树,由 `setup-fixture.sh` 实例化成
真实 git 仓库(base 提交在 main,head 提交在 work 分支),所以"对比基线分支
的 diff"是真领地,不是描述:

```bash
evals/fixtures/setup-fixture.sh failed-contract /tmp/run/repo
```

跑法:对每个场景,把 `evals.json` 里的 prompt 交给一个能读到对应 skill 的
agent(with-skill),再交给一个读不到的(baseline),按 `expectations` 逐条
评分。两者的差值就是 skill 的实测价值。评分产物与基准对比见
`evals/results/`。

## 诚实的局限

- 行为层每个配置只跑一次的话方差不小;结论要稳需要 3+ 次重复。
- 一部分断言(比如"是否事后编造了标准")需要读产物做判断,不是纯 grep——
  评分本身有主观成分,grading.json 里逐条附了证据以便复核。
- `quiz-me-scope` 的 prompt 里带一句模拟指令("假设用户全部答对"),因为
  一次性运行没有真人作答;它测的是判定措辞与范围,不是评分回路本身。
- fixture 是玩具尺度。它能证伪"skill 没让模型做出该做的动作",但不能证明
  真实大型会话中同样成立。
