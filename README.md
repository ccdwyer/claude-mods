# ccdwyer-mods

Claude Code mods: plugins of function hooks that change what Claude Code does and draw UI inside it. Each mod lives in its own repo; this repo is the marketplace that lists them all.

## Install

```
/plugin marketplace add ccdwyer/claude-mods
/plugin install <mod>@ccdwyer-mods
/reload-plugins
```

## Mods

<!-- mods:start -->
| Mod | What it does | Install |
|---|---|---|
| [review-ghost](https://github.com/ccdwyer/review-ghost) | Attaches a file's unresolved GitHub PR review threads to the model's Read and Edit results, so review comments get fixed in the file it is already touching | `/plugin install review-ghost@ccdwyer-mods` |
| [assertion-guardian](https://github.com/ccdwyer/assertion-guardian) | Blocks edits that weaken tests to fake a green run: removed or loosened assertions, added skips, deleted cases, swallowed errors, snapshot rewrites | `/plugin install assertion-guardian@ccdwyer-mods` |
| [budget-governor](https://github.com/ccdwyer/budget-governor) | Enforces session and daily spend caps: a live gauge above the prompt, a wrap-up nudge at 80%, and new prompts refused at the cap | `/plugin install budget-governor@ccdwyer-mods` |
| [secret-sentry](https://github.com/ccdwyer/secret-sentry) | Two-way secret scrubbing: redacts credentials before the model sees them and blocks writing them into tracked files or shell commands | `/plugin install secret-sentry@ccdwyer-mods` |
| [context-dungeon](https://github.com/ccdwyer/context-dungeon) | A roguelike pane played by your real session: context is HP, errors spawn monsters, green tests slay them, commits open chests, PRs are floor bosses | `/plugin install context-dungeon@ccdwyer-mods` |
| [red-squiggle](https://github.com/ccdwyer/red-squiggle) | Type-checks and lints the file Claude just edited and puts the errors in that same tool result | `/plugin install red-squiggle@ccdwyer-mods` |
| [dependency-bouncer](https://github.com/ccdwyer/dependency-bouncer) | Vets npm and PyPI packages before they install: blocks hallucinated, typosquatted and brand-new install-script packages, flags risky ones | `/plugin install dependency-bouncer@ccdwyer-mods` |
| [loop-breaker](https://github.com/ccdwyer/loop-breaker) | Stops the agent repeating the same failing command or undoing its own edits, and shows a stuck meter above the prompt | `/plugin install loop-breaker@ccdwyer-mods` |
| [inline-tribunal](https://github.com/ccdwyer/inline-tribunal) | A second_opinion tool and /tribunal command: your diff is reviewed by Codex and Grok side by side, read-only, inside the session | `/plugin install inline-tribunal@ccdwyer-mods` |
| [speedrun-splits](https://github.com/ccdwyer/speedrun-splits) | A LiveSplit-style timer above the prompt that auto-splits on recon, first edit, tests, green, commit and PR, with personal bests and gold segments | `/plugin install speedrun-splits@ccdwyer-mods` |
| [stack-traffic-control](https://github.com/ccdwyer/stack-traffic-control) | A departure board for gh stack: live stack pane, a one-line status above the prompt, and raw force-pushes, rebases and PR base edits on stacked branches redirected to gh stack | `/plugin install stack-traffic-control@ccdwyer-mods` |
| [redbox-relay](https://github.com/ccdwyer/redbox-relay) | Attaches fresh React Native redboxes and native crash logs from running simulators and emulators to your prompt, and warns when an edit needs a native rebuild | `/plugin install redbox-relay@ccdwyer-mods` |
| [proof-decay](https://github.com/ccdwyer/proof-decay) | Tracks which test, typecheck, lint and build results are still true after later edits, and stops commit messages that claim checks which are stale | `/plugin install proof-decay@ccdwyer-mods` |
| [quarantine](https://github.com/ccdwyer/quarantine) | Wraps web, MCP and third-party tool output as untrusted data and defangs prompt-injection lines before the model reads them | `/plugin install quarantine@ccdwyer-mods` |
<!-- mods:end -->

## Demos

### [Loop Breaker](https://github.com/ccdwyer/loop-breaker)

Stops the agent repeating the same failing command or undoing its own edits, and shows a stuck meter above the prompt.

![Loop Breaker demo](https://github.com/ccdwyer/loop-breaker/raw/main/media/demo.gif)

`/plugin install loop-breaker@ccdwyer-mods`

### [Red Squiggle](https://github.com/ccdwyer/red-squiggle)

Type-checks and lints the file Claude just edited and puts the errors in that same tool result.

![Red Squiggle demo](https://github.com/ccdwyer/red-squiggle/raw/main/media/demo.gif)

`/plugin install red-squiggle@ccdwyer-mods`

### [Review Ghost](https://github.com/ccdwyer/review-ghost)

Attaches a file's unresolved GitHub PR review threads to the model's Read and Edit results, so review comments get fixed in the file it is already touching.

![Review Ghost demo](https://github.com/ccdwyer/review-ghost/raw/main/media/demo.gif)

`/plugin install review-ghost@ccdwyer-mods`

### [Secret Sentry](https://github.com/ccdwyer/secret-sentry)

Two-way secret scrubbing: redacts credentials before the model sees them and blocks writing them into tracked files or shell commands.

![Secret Sentry demo](https://github.com/ccdwyer/secret-sentry/raw/main/media/demo.gif)

`/plugin install secret-sentry@ccdwyer-mods`

### [Assertion Guardian](https://github.com/ccdwyer/assertion-guardian)

Blocks edits that weaken tests to fake a green run: removed or loosened assertions, added skips, deleted cases, swallowed errors, snapshot rewrites.

![Assertion Guardian demo](https://github.com/ccdwyer/assertion-guardian/raw/main/media/demo.gif)

`/plugin install assertion-guardian@ccdwyer-mods`

### [Redbox Relay](https://github.com/ccdwyer/redbox-relay)

Attaches fresh React Native redboxes and native crash logs from running simulators and emulators to your prompt, and warns when an edit needs a native rebuild.

![Redbox Relay demo](https://github.com/ccdwyer/redbox-relay/raw/main/media/demo.gif)

`/plugin install redbox-relay@ccdwyer-mods`

### [Stack Traffic Control](https://github.com/ccdwyer/stack-traffic-control)

A departure board for gh stack: live stack pane, a one-line status above the prompt, and raw force-pushes, rebases and PR base edits on stacked branches redirected to gh stack.

![Stack Traffic Control demo](https://github.com/ccdwyer/stack-traffic-control/raw/main/media/demo.gif)

`/plugin install stack-traffic-control@ccdwyer-mods`

### [Inline Tribunal](https://github.com/ccdwyer/inline-tribunal)

A second_opinion tool and /tribunal command: your diff is reviewed by Codex and Grok side by side, read-only, inside the session.

![Inline Tribunal demo](https://github.com/ccdwyer/inline-tribunal/raw/main/media/demo.gif)

`/plugin install inline-tribunal@ccdwyer-mods`

### [Budget Governor](https://github.com/ccdwyer/budget-governor)

Enforces session and daily spend caps: a live gauge above the prompt, a wrap-up nudge at 80%, and new prompts refused at the cap.

![Budget Governor demo](https://github.com/ccdwyer/budget-governor/raw/main/media/demo.gif)

`/plugin install budget-governor@ccdwyer-mods`

### [Proof Decay](https://github.com/ccdwyer/proof-decay)

Tracks which test, typecheck, lint and build results are still true after later edits, and stops commit messages that claim checks which are stale.

![Proof Decay demo](https://github.com/ccdwyer/proof-decay/raw/main/media/demo.gif)

`/plugin install proof-decay@ccdwyer-mods`

### [Dependency Bouncer](https://github.com/ccdwyer/dependency-bouncer)

Vets npm and PyPI packages before they install: blocks hallucinated, typosquatted and brand-new install-script packages, flags risky ones.

![Dependency Bouncer demo](https://github.com/ccdwyer/dependency-bouncer/raw/main/media/demo.gif)

`/plugin install dependency-bouncer@ccdwyer-mods`

### [Context Dungeon](https://github.com/ccdwyer/context-dungeon)

A roguelike pane played by your real session: context is HP, errors spawn monsters, green tests slay them, commits open chests, PRs are floor bosses.

![Context Dungeon demo](https://github.com/ccdwyer/context-dungeon/raw/main/media/demo.gif)

`/plugin install context-dungeon@ccdwyer-mods`

### [Speedrun Splits](https://github.com/ccdwyer/speedrun-splits)

A LiveSplit-style timer above the prompt that auto-splits on recon, first edit, tests, green, commit and PR, with personal bests and gold segments.

![Speedrun Splits demo](https://github.com/ccdwyer/speedrun-splits/raw/main/media/demo.gif)

`/plugin install speedrun-splits@ccdwyer-mods`

### [Quarantine](https://github.com/ccdwyer/quarantine)

Wraps web, MCP and third-party tool output as untrusted data and defangs prompt-injection lines before the model reads them.

![Quarantine demo](https://github.com/ccdwyer/quarantine/raw/main/media/demo.gif)

`/plugin install quarantine@ccdwyer-mods`

Every mod is validated, type-checked, and tested with `claude plugin test`, and was reviewed by GPT-6-Astra and Grok 4.7 before release.
