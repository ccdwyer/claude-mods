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
<!-- mods:end -->

Every mod is validated, type-checked, and tested with `claude plugin test`, and was reviewed by GPT-6-Astra and Grok 4.7 before release.
