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
| [loop-breaker](https://github.com/ccdwyer/loop-breaker) | Stops the agent repeating the same failing command or undoing its own edits, and shows a stuck meter above the prompt | `/plugin install loop-breaker@ccdwyer-mods` |
| [review-ghost](https://github.com/ccdwyer/review-ghost) | Attaches a file's unresolved GitHub PR review threads to the model's Read and Edit results, so review comments get fixed in the file it is already touching | `/plugin install review-ghost@ccdwyer-mods` |
<!-- mods:end -->

Every mod is validated, type-checked, and tested with `claude plugin test`, and was reviewed by GPT-6-Astra and Grok 4.7 before release.
