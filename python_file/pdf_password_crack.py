# #去除polyu 的pdf的密码,在最后的batch_remove_password 填写路径，分别是：‘要转换的文件夹位置’，‘输出文件夹位置’，‘已知的密码’
# #如果想转换单个文件，用remove_pdf_password，‘要转换的文件位置’，‘输出文件位置’，‘已知的密码’

# import os
# import PyPDF2

# def remove_pdf_password(input_path, output_path, password=None):
#     """
#     移除PDF文件的密码保护
    
#     参数:
#         input_path: 输入的PDF文件路径
#         output_path: 输出的PDF文件路径
#         password: PDF的密码(如果有)
#     """
#     if not os.path.exists(input_path):
#         print(f"错误：文件 '{input_path}' 不存在。")
#         return False
        
#     try:
#         with open(input_path, 'rb') as file:
#             # 创建PDF阅读器对象
#             pdf_reader = PyPDF2.PdfReader(file)
            
#             # 检查文档是否加密
#             if pdf_reader.is_encrypted:
#                 # 尝试使用密码解密
#                 if password:
#                     decrypt_result = pdf_reader.decrypt(password)
#                     if not decrypt_result:
#                         print("密码错误，解密失败。")
#                         return False
#                 else:
#                     # 尝试空密码解密
#                     pdf_reader.decrypt("")
                
#                 # 创建PDF写入器对象
#                 pdf_writer = PyPDF2.PdfWriter()
                
#                 # 复制每一页内容到新文档
#                 for page in pdf_reader.pages:
#                     pdf_writer.add_page(page)
                
#                 # 保存新文档
#                 with open(output_path, 'wb') as output_file:
#                     pdf_writer.write(output_file)
                
#                 print("密码移除成功！")
#                 return True
#             else:
#                 print("文档未加密，无需移除密码。")
#                 return False
                
#     except Exception as e:
#         print(f"处理过程中发生错误：{e}")
#         return False

# def batch_remove_password(input_folder, output_folder, password=None):
#     """
#     批量移除PDF文件的密码保护
#     """
#     # 确保输出文件夹存在
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # 遍历输入文件夹中的所有PDF文件
#     for filename in os.listdir(input_folder):
#         if filename.lower().endswith('.pdf'):
#             input_path = os.path.join(input_folder, filename)
#             output_path = os.path.join(output_folder, filename)
            
#             print(f"处理文件: {filename}")
#             success = remove_pdf_password(input_path, output_path, password)
            
#             if success:
#                 print(f"成功处理: {filename}")
#             else:
#                 print(f"处理失败: {filename}")

# # 使用
# batch_remove_password(r"D:\polyu\energy\ori\week2", r"D:\polyu\energy\no_password", "EVWLiu")


#----------------------------打包程序测试---------------------------------------------------


import os
import PyPDF2
import sys
from pathlib import Path

def remove_pdf_password(input_path, output_path, password):
    """
    去除单个PDF文件的密码
    """
    try:
        with open(input_path, 'rb') as input_file:
            reader = PyPDF2.PdfReader(input_file)
            if reader.is_encrypted:
                if not reader.decrypt(password):
                    print(f"密码错误: {input_path}")
                    return False
            
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            
            # 确保输出目录存在
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
                
        print(f"成功处理: {input_path} -> {output_path}")
        return True
    except Exception as e:
        print(f"处理失败 {input_path}: {str(e)}")
        return False

def process_pdf_file(input_file, output_path, password):
    """
    处理单个PDF文件
    """
    return remove_pdf_password(input_file, output_path, password)

def process_pdf_folder(input_folder, output_folder, password):
    """
    处理文件夹中的所有PDF文件
    """
    # 确保输出目录存在
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except PermissionError:
            print(f"错误: 没有权限创建输出目录 {output_folder}")
            return 0, 0
    
    success_count = 0
    total_count = 0
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            total_count += 1
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            if remove_pdf_password(input_path, output_path, password):
                success_count += 1
    
    print(f"处理完成: 成功 {success_count}/{total_count} 个文件")
    return success_count, total_count

def validate_path(path, is_file=False):
    """验证路径是否存在并有相应权限"""
    if not os.path.exists(path):
        return False, "路径不存在"
    
    if is_file and not os.path.isfile(path):
        return False, "不是有效的文件"
    
    if not is_file and not os.path.isdir(path):
        return False, "不是有效的文件夹"
    
    # 检查读取权限
    if not os.access(path, os.R_OK):
        return False, "没有读取权限"
    
    return True, ""

def get_valid_path(prompt, is_file=False):
    """获取有效的路径输入"""
    while True:
        path = input(prompt).strip().strip('"')
        if not path:
            print("错误: 路径不能为空")
            continue
        
        # 处理相对路径
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        
        valid, message = validate_path(path, is_file)
        if valid:
            return path
        else:
            print(f"错误: {message}，请重新输入")

def get_output_path(input_path, is_file=False):
    """获取输出路径"""
    while True:
        output_path = input("请输入输出路径: ").strip().strip('"')
        if not output_path:
            print("错误: 输出路径不能为空")
            continue
        
        # 处理相对路径
        if not os.path.isabs(output_path):
            output_path = os.path.abspath(output_path)
        
        # 检查输出目录的写入权限
        if is_file:
            output_dir = os.path.dirname(output_path)
            if not output_dir:  # 如果只有文件名
                output_dir = "."
        else:
            output_dir = output_path
        
        # 检查输出目录是否存在，如果不存在则尝试创建
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
                return output_path
            except PermissionError:
                print(f"错误: 没有权限创建输出目录 {output_dir}")
                continue
            except Exception as e:
                print(f"错误: 创建目录失败: {str(e)}")
                continue
        
        # 检查写入权限
        if not os.access(output_dir, os.W_OK):
            print(f"错误: 没有写入权限 {output_dir}")
            print("请尝试选择其他有写入权限的目录")
            continue
        
        return output_path

def main():
    print("=" * 50)
    print("PDF密码去除工具")
    print("=" * 50)
    
    # 选择处理模式
    while True:
        print("\n请选择处理模式:")
        print("1. 处理单个PDF文件")
        print("2. 处理文件夹中的所有PDF文件")
        choice = input("请输入选项 (1 或 2): ").strip()
        
        if choice in ['1', '2']:
            break
        else:
            print("无效选项，请重新选择")
    
    # 获取输入路径
    if choice == '1':
        input_path = get_valid_path("请输入PDF文件路径: ", is_file=True)
    else:
        input_path = get_valid_path("请输入文件夹路径: ", is_file=False)
    
    # 获取输出路径
    output_path = get_output_path(input_path, is_file=(choice == '1'))
    
    # 获取密码
    password = input("请输入PDF密码: ").strip()
    
    print("\n开始处理...")
    print("-" * 30)
    
    # 执行处理
    if choice == '1':
        success = process_pdf_file(input_path, output_path, password)
        if success:
            print("\n文件处理成功!")
        else:
            print("\n文件处理失败!")
    else:
        success_count, total_count = process_pdf_folder(input_path, output_path, password)
        if total_count > 0:
            print(f"\n文件夹处理完成: 成功 {success_count}/{total_count} 个文件")
        else:
            print("\n未找到PDF文件")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n用户中断程序")
    except Exception as e:
        print(f"\n程序发生错误: {str(e)}")
    finally:
        input("\n按Enter键退出...")