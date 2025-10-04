import PyInstaller.__main__
import os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'pdf_password_crack.py',
    '--onefile',
    '--console',
    '--name=PDF密码去除工具',
    '--icon=NONE',  # 如果有图标文件，可以替换为图标路径
    # '--add-data=README.md;.',  # 如果需要添加额外文件
])
