#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试运行脚本
"""

import subprocess
import sys
import os

def install_dependencies():
    """安装项目依赖"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("依赖安装成功!")
        return True
    except subprocess.CalledProcessError:
        print("依赖安装失败，请手动安装PyPDF2: pip install PyPDF2")
        return False

def run_tests():
    """运行单元测试"""
    try:
        # 运行测试
        result = subprocess.run([sys.executable, "-m", "unittest", "discover", "tests", "-v"], 
                              capture_output=True, text=True)
        
        print("测试输出:")
        print(result.stdout)
        
        if result.stderr:
            print("测试错误:")
            print(result.stderr)
            
        print(f"测试完成，退出码: {result.returncode}")
        return result.returncode == 0
    except Exception as e:
        print(f"运行测试时出错: {e}")
        return False

def main():
    """主函数"""
    print("PDF合并工具单元测试运行器")
    print("=" * 30)
    
    # 安装依赖
    print("正在安装依赖...")
    if not install_dependencies():
        return False
    
    # 运行测试
    print("\n正在运行测试...")
    success = run_tests()
    
    if success:
        print("\n所有测试通过!")
    else:
        print("\n部分测试失败!")
    
    return success

if __name__ == "__main__":
    sys.exit(0 if main() else 1)