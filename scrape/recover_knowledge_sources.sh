#!/usr/bin/env bash
# Recover local knowledge-sources/ to commit 22c08b4 after rebase collision.
#
# Run from the chaoyuan root, NOT from inside knowledge-sources/:
#   bash /mnt/d/vincenjiang/AI学习/chaoyuan/scrape/recover_knowledge_sources.sh
#
set -euo pipefail

KS=/mnt/d/vincenjiang/AI学习/chaoyuan/knowledge-sources
cd "$KS"

# 1. clean lock if any
rm -f .git/index.lock .git/HEAD.lock

# 2. discard README mod + remove untracked SRC dirs that rebase left
git checkout -- README.md
rm -rf SRC-001 SRC-002 SRC-003 SRC-014 SRC-016 SRC-038 SRC-039

# 3. confirm we are at the right commit
echo "before reset:"
git log --oneline -3
echo

# 4. reset to local HEAD with full tree (22c08b4 holds 5000+ files)
git reset --hard 22c08b4

echo
echo "after reset:"
git log --oneline -3
echo
echo "SRC dir count: $(ls -d SRC-* 2>/dev/null | wc -l)"

# 5. push (use force-with-lease so concurrent changes abort)
git push origin 22c08b4:main --force-with-lease