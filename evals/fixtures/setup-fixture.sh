#!/usr/bin/env bash
# Instantiate a fixture as a real git repository.
#
#   setup-fixture.sh <fixture-name> <target-dir>
#
# The fixture's base/ tree becomes the main branch; if a head/ tree exists it
# becomes a `work` branch (head/ holds the full desired state, not an overlay).
# The behavioral evals run the skills against these repos so that "the diff
# against the base branch" is real territory, not a description of one.
set -euo pipefail

fixture_dir="$(cd "$(dirname "$0")/$1" && pwd)"
mkdir -p "$2"
target="$(cd "$2" && pwd)"

cp -r "$fixture_dir/base/." "$target/"
cd "$target"
git init -q -b main
git config user.email fixture@zhizhi.local
git config user.name "Fixture Setup"
git add -A
git commit -qm "base"

if [ -d "$fixture_dir/head" ]; then
  git switch -qc work
  find . -mindepth 1 -maxdepth 1 -not -name .git -exec rm -rf {} +
  cp -r "$fixture_dir/head/." .
  git add -A
  git commit -qm "implementation"
fi
