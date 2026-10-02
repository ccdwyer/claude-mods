# ccdwyer-mods

19 [Claude Code mods](https://claude.dev/blog/getting-started-with-claude-code-mods/): plugins of function hooks that change what Claude Code does and draw UI inside it. Each mod lives in its own repo; this repo is the marketplace that lists them all.

## Install

All of them (needs the `claude` CLI on your PATH):

```sh
curl -fsSL https://raw.githubusercontent.com/ccdwyer/claude-mods/main/install.sh | sh
```

Or from inside Claude Code, add the marketplace once, then install whichever mods you want (commands are under each mod below):

```
/plugin marketplace add ccdwyer/claude-mods
/plugin install <mod>@ccdwyer-mods
/reload-plugins
```

## Contents

- **Guardrails:** [Loop Breaker](#loop-breaker) · [Assertion Guardian](#assertion-guardian) · [Secret Sentry](#secret-sentry) · [Dependency Bouncer](#dependency-bouncer) · [Quarantine](#quarantine) · [Budget Governor](#budget-governor)
- **Feedback loops:** [Red Squiggle](#red-squiggle) · [Proof Decay](#proof-decay) · [Review Ghost](#review-ghost) · [Redbox Relay](#redbox-relay)
- **Workflow:** [Inline Tribunal](#inline-tribunal) · [Stack Traffic Control](#stack-traffic-control)
- **Visuals:** [Boot Sequence](#boot-sequence) · [Diff Seismograph](#diff-seismograph) · [Departure Board](#departure-board) · [Transit Map](#transit-map) · [Fault Lacquer](#fault-lacquer)
- **Fun:** [Context Dungeon](#context-dungeon) · [Speedrun Splits](#speedrun-splits)

## Guardrails

### Loop Breaker

Notices when the agent keeps running the same failing command or flips an edit back and forth, refuses the next identical try, and shows a stuck meter above the prompt. A real code change or a different error resets it, so normal fix-and-retest work is never blocked.

![Loop Breaker demo](https://github.com/ccdwyer/loop-breaker/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/loop-breaker.mp4) · [Screenshot](https://github.com/ccdwyer/loop-breaker/raw/main/media/03-refused.png) · [Repo](https://github.com/ccdwyer/loop-breaker)

```
/plugin install loop-breaker@ccdwyer-mods
```

### Assertion Guardian

Refuses edits that weaken tests to fake a green run: changed expected values, looser matchers, deleted assertions, `.skip`/`.only`, swallowed failures, bulk snapshot updates. You can allow a specific change once.

![Assertion Guardian demo](https://github.com/ccdwyer/assertion-guardian/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/assertion-guardian.mp4) · [Screenshot](https://github.com/ccdwyer/assertion-guardian/raw/main/media/02-refused.png) · [Repo](https://github.com/ccdwyer/assertion-guardian)

```
/plugin install assertion-guardian@ccdwyer-mods
```

### Secret Sentry

Redacts credentials in prompts and tool output before the model sees them, and refuses writes or shell commands that would put a key into a tracked file.

![Secret Sentry demo](https://github.com/ccdwyer/secret-sentry/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/secret-sentry.mp4) · [Screenshot](https://github.com/ccdwyer/secret-sentry/raw/main/media/02-write-refused.png) · [Repo](https://github.com/ccdwyer/secret-sentry)

```
/plugin install secret-sentry@ccdwyer-mods
```

### Dependency Bouncer

Checks packages against the npm and PyPI registries before they install. It blocks made-up names, typosquats and brand-new packages with install scripts, and flags dependencies you already have something for.

![Dependency Bouncer demo](https://github.com/ccdwyer/dependency-bouncer/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/dependency-bouncer.mp4) · [Screenshot](https://github.com/ccdwyer/dependency-bouncer/raw/main/media/02-blocked.png) · [Repo](https://github.com/ccdwyer/dependency-bouncer)

```
/plugin install dependency-bouncer@ccdwyer-mods
```

### Quarantine

Wraps untrusted tool output (web pages, MCP results, vendored files, fetched PR and issue text) in an "untrusted content" fence and defangs lines that read like instructions, so prompt injections arrive as data.

![Quarantine demo](https://github.com/ccdwyer/quarantine/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/quarantine.mp4) · [Screenshot](https://github.com/ccdwyer/quarantine/raw/main/media/02-defanged.png) · [Repo](https://github.com/ccdwyer/quarantine)

```
/plugin install quarantine@ccdwyer-mods
```

### Budget Governor

Enforces session and daily spend caps. It shows a gauge above the prompt, tells the model to wrap up at 80%, and refuses new prompts at the cap until you raise it.

![Budget Governor demo](https://github.com/ccdwyer/budget-governor/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/budget-governor.mp4) · [Screenshot](https://github.com/ccdwyer/budget-governor/raw/main/media/03-refused.png) · [Repo](https://github.com/ccdwyer/budget-governor)

```
/plugin install budget-governor@ccdwyer-mods
```

## Feedback loops

### Red Squiggle

Runs your project's own tsc, eslint and ruff right after each edit and attaches only the new errors to that edit's result, so the model fixes them on the same step.

![Red Squiggle demo](https://github.com/ccdwyer/red-squiggle/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/red-squiggle.mp4) · [Screenshot](https://github.com/ccdwyer/red-squiggle/raw/main/media/02-diagnostics.png) · [Repo](https://github.com/ccdwyer/red-squiggle)

```
/plugin install red-squiggle@ccdwyer-mods
```

### Proof Decay

Tracks whether "tests passed" is still true. Later edits turn results stale on a board above the prompt, and Oathkeeper refuses commit messages that claim checks pass when they aren't current.

![Proof Decay demo](https://github.com/ccdwyer/proof-decay/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/proof-decay.mp4) · [Screenshot](https://github.com/ccdwyer/proof-decay/raw/main/media/02-stale.png) · [Repo](https://github.com/ccdwyer/proof-decay)

```
/plugin install proof-decay@ccdwyer-mods
```

### Review Ghost

When the agent reads or edits a file on a branch with an open PR, it attaches that file's unresolved GitHub review threads. `/ghost` lists them all.

![Review Ghost demo](https://github.com/ccdwyer/review-ghost/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/review-ghost.mp4) · [Screenshot](https://github.com/ccdwyer/review-ghost/raw/main/media/02-threads-attached.png) · [Repo](https://github.com/ccdwyer/review-ghost)

```
/plugin install review-ghost@ccdwyer-mods
```

### Redbox Relay

For React Native: attaches fresh simulator and emulator errors to your next prompt, and warns when an edit to native code needs `pod install` and a native rebuild.

![Redbox Relay demo](https://github.com/ccdwyer/redbox-relay/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/redbox-relay.mp4) · [Screenshot](https://github.com/ccdwyer/redbox-relay/raw/main/media/02-rebuild-warning.png) · [Repo](https://github.com/ccdwyer/redbox-relay)

```
/plugin install redbox-relay@ccdwyer-mods
```

## Workflow

### Inline Tribunal

A `second_opinion` tool and a `/tribunal` command that send your diff to Codex and Grok in locked-down, read-only sandboxes and show both verdicts side by side.

![Inline Tribunal demo](https://github.com/ccdwyer/inline-tribunal/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/inline-tribunal.mp4) · [Screenshot](https://github.com/ccdwyer/inline-tribunal/raw/main/media/02-pane.png) · [Repo](https://github.com/ccdwyer/inline-tribunal)

```
/plugin install inline-tribunal@ccdwyer-mods
```

### Stack Traffic Control

A departure board for `gh stack` stacked PRs (`/stack`), plus a guard that refuses force-pushes, rebases and PR base changes on stacked branches and points to the right `gh stack` command.

![Stack Traffic Control demo](https://github.com/ccdwyer/stack-traffic-control/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/stack-traffic-control.mp4) · [Screenshot](https://github.com/ccdwyer/stack-traffic-control/raw/main/media/02-board.png) · [Repo](https://github.com/ccdwyer/stack-traffic-control)

```
/plugin install stack-traffic-control@ccdwyer-mods
```

## Visuals

### Boot Sequence

A BIOS-style POST screen when a session starts that runs real checks (git, toolchains, simulators, dev-server ports, disk, context) and types each one out as `[ OK ]`, `[WARN]` or `[FAIL]`. `/boot` replays it.

*Demo recording coming soon.* · [Repo](https://github.com/ccdwyer/boot-sequence)

```
/plugin install boot-sequence@ccdwyer-mods
```

### Diff Seismograph

A live braille seismograph of lines added and removed above the prompt, with `QUAKE M5.2` alerts on big edits. `/quake` adds a heat treemap of the repo, glowing where this session changed code.

*Demo recording coming soon.* · [Repo](https://github.com/ccdwyer/diff-seismograph)

```
/plugin install diff-seismograph@ccdwyer-mods
```

### Departure Board

A Solari split-flap board in amber that cascades flap by flap as Claude's tasks go from BOARDING to DEPARTED, DELAYED or CANCELLED. A mini board sits above the prompt and `/board` opens it fullscreen.

*Demo recording coming soon.* · [Repo](https://github.com/ccdwyer/departure-board)

```
/plugin install departure-board@ccdwyer-mods
```

### Transit Map

`/metro` shows your git history as a Vignelli subway map: branches are coloured lines, commits are stations, merges are interchanges, and your working tree is a train with one car per uncommitted file.

*Demo recording coming soon.* · [Repo](https://github.com/ccdwyer/transit-map)

```
/plugin install transit-map@ccdwyer-mods
```

### Fault Lacquer

Kintsugi for your session: each failing operation cracks its lacquer tile, and when it later succeeds the cracks fill with animated gold seams. `/kintsugi` shows the wall.

*Demo recording coming soon.* · [Repo](https://github.com/ccdwyer/fault-lacquer)

```
/plugin install fault-lacquer@ccdwyer-mods
```

## Fun

### Context Dungeon

A roguelike pane driven by your real session: context is HP, failing tests spawn monsters named after the error, green runs land the killing blow, and commits open treasure chests.

![Context Dungeon demo](https://github.com/ccdwyer/context-dungeon/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/context-dungeon.mp4) · [Screenshot](https://github.com/ccdwyer/context-dungeon/raw/main/media/02-monster.png) · [Repo](https://github.com/ccdwyer/context-dungeon)

```
/plugin install context-dungeon@ccdwyer-mods
```

### Speedrun Splits

A LiveSplit-style timer above the prompt. It splits automatically from recon to first edit to test to green to commit or PR, and keeps personal bests and gold segments for each repo.

![Speedrun Splits demo](https://github.com/ccdwyer/speedrun-splits/raw/main/media/demo.gif)

[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/speedrun-splits.mp4) · [Screenshot](https://github.com/ccdwyer/speedrun-splits/raw/main/media/02-live-deltas.png) · [Repo](https://github.com/ccdwyer/speedrun-splits)

```
/plugin install speedrun-splits@ccdwyer-mods
```

---

Every mod is validated, type-checked and tested with `claude plugin test`, and went through review rounds with GPT-6-Astra and Grok 4.7. Each repo's README lists what it does not cover.
