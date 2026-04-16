# Python 自动 Git 提交
import os

print("=== Python 自动化 Git 提交 ===")

# 执行 Git 命令（和你在终端敲的一模一样）
os.system("git status")
os.system("git add .")
os.system("git commit -m 'Python 自动化提交'")
os.system("git push origin HEAD:main")
