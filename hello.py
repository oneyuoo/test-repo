import os

print("=== Python 自动分类文件 ===")

for file in os.listdir("."):
    # 如果是文件夹
    if os.path.isdir(file):
        print("📁 文件夹：" + file)
    
    # 如果是 .py 脚本
    elif file.endswith(".py"):
        print("🐍 Python 文件：" + file)
    
    # 如果是 .sh 脚本
    elif file.endswith(".sh"):
        print("⚙️  Shell 脚本：" + file)
    
    # 如果是文本文件
    elif file.endswith(".txt"):
        print("📄 文本文件：" + file)
    
    else:
        print("📎 其他文件：" + file)
