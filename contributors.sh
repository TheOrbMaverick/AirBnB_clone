#!/usr/bin/env bash

set -e

ROOTDIR="$(git rev-parse --show-toplevel)"

# see also ".mailmap" for how email addresses and names are deduplicated
git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf > "${ROOTDIR}/AUTHORS"

echo "Contributors list generated and saved to ${ROOTDIR}/AUTHORS."
