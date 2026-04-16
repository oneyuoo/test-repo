#!/bin/bash
echo "=== 自动 Git 提交 ==="
git status
git add .
git commit -m "auto commit"
git push origin HEAD:main