#!/bin/sh
# Install ccdwyer-mods into Claude Code.
#   All mods:      curl -fsSL https://raw.githubusercontent.com/ccdwyer/claude-mods/main/install.sh | sh
#   Pick some:     curl -fsSL https://raw.githubusercontent.com/ccdwyer/claude-mods/main/install.sh | sh -s -- loop-breaker quarantine
set -e
MODS="review-ghost assertion-guardian budget-governor secret-sentry context-dungeon red-squiggle dependency-bouncer loop-breaker inline-tribunal speedrun-splits stack-traffic-control redbox-relay proof-decay quarantine boot-sequence diff-seismograph departure-board transit-map fault-lacquer netrunner-hud mirror-pane codebase-galaxy netrunner-trace"
command -v claude >/dev/null 2>&1 || { echo "claude (Claude Code CLI) not found on PATH" >&2; exit 1; }
[ "$#" -gt 0 ] && MODS="$*"
claude plugin marketplace add ccdwyer/claude-mods >/dev/null 2>&1 || claude plugin marketplace update ccdwyer-mods >/dev/null
for mod in $MODS; do
  case " review-ghost assertion-guardian budget-governor secret-sentry context-dungeon red-squiggle dependency-bouncer loop-breaker inline-tribunal speedrun-splits stack-traffic-control redbox-relay proof-decay quarantine boot-sequence diff-seismograph departure-board transit-map fault-lacquer netrunner-hud mirror-pane codebase-galaxy netrunner-trace " in *" $mod "*) ;; *) echo "unknown mod: $mod" >&2; exit 1 ;; esac
  if claude plugin install "$mod@ccdwyer-mods" >/dev/null 2>&1; then echo "installed $mod"; else echo "failed: $mod" >&2; fi
done
echo "Done. Run /reload-plugins in an open Claude Code session, or start a new one."
