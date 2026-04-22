import os

print("=== 智能版 Python Git 自动提交 ===")

# 先检查是不是 Git 仓库
if os.path.isdir(".git"):
    print("✅ 检测到 Git 仓库，开始检查工作区状态")
    
    # 先获取 git 状态，判断有没有内容要提交
    status_result = os.popen("git status --porcelain").read()
    
    if status_result.strip() != "":
        # 有改动才执行提交推送
        os.system("git add .")
        os.system("git commit -m 'Python 智能自动提交'")
        os.system("git push origin HEAD:main")
        print("✅ 全部提交推送完成！")
    else:
        print("ℹ️  工作区干净无改动，无需提交")

else:
    print("❌ 当前不是 Git 仓库，无法提交")
