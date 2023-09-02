#!/usr/bin/env bash

KATA_NAME=$1

cd src && mkdir "$KATA_NAME" && touch "$KATA_NAME/$KATA_NAME.md" "$KATA_NAME/$KATA_NAME.py" && cd ..

echo -e "def $KATA_NAME():\n\tpass" >"$KATA_NAME/$KATA_NAME.py"
echo -e "# $KATA_NAME\n\n\n## Examples" >"$KATA_NAME/$KATA_NAME.md"
