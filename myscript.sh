#!/bin/bash

echo "=== 自动 Git 提交脚本 ==="

# 1. 查看当前改动
git status

# 2. 全部添加
git add .

# 3. 自动提交（备注可以自己改）
git commit -m "自动化提交：Shell 脚本练习"

# 4. 推送到远程
git push origin HEAD:main