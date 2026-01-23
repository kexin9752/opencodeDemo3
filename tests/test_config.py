"""
测试配置文件
"""

import os
import tempfile

# 测试数据目录
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")

# 创建测试目录的函数
def create_test_directory():
    """创建测试目录结构"""
    test_dir = tempfile.mkdtemp()
    pdf_dir = os.path.join(test_dir, "pdf_merge")
    os.makedirs(pdf_dir)
    return test_dir, pdf_dir

# 清理测试目录的函数
def cleanup_test_directory(test_dir):
    """清理测试目录"""
    import shutil
    shutil.rmtree(test_dir, ignore_errors=True)