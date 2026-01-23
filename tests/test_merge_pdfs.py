import unittest
import os
import tempfile
import sys

# 将项目根目录添加到Python路径中，以便导入merge_pdfs模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 延迟导入，避免在PyPDF2不可用时出错
try:
    from merge_pdfs import merge_pdfs, get_pdf_files
    PY_PDF_AVAILABLE = True
except ImportError:
    PY_PDF_AVAILABLE = False

class TestMergePdfs(unittest.TestCase):
    
    def setUp(self):
        """在每个测试方法之前运行，设置测试环境"""
        if not PY_PDF_AVAILABLE:
            self.skipTest("PyPDF2 not available")
            
        # 创建临时目录用于测试
        self.test_dir = tempfile.mkdtemp()
        self.pdf_dir = os.path.join(self.test_dir, "pdf_merge")
        os.makedirs(self.pdf_dir)
        
        # 创建一些简单的测试PDF文件
        self.create_test_pdf(os.path.join(self.pdf_dir, "test1.pdf"))
        self.create_test_pdf(os.path.join(self.pdf_dir, "test2.pdf"))
        self.create_test_pdf(os.path.join(self.pdf_dir, "test3.pdf"))
        
        # 设置输出文件路径
        self.output_file = os.path.join(self.test_dir, "merged_output.pdf")
        
    def tearDown(self):
        """在每个测试方法之后运行，清理测试环境"""
        if not PY_PDF_AVAILABLE:
            return
            
        # 清理创建的文件和目录
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
            
        for file in os.listdir(self.pdf_dir):
            os.remove(os.path.join(self.pdf_dir, file))
        os.rmdir(self.pdf_dir)
        os.rmdir(self.test_dir)
    
    def create_test_pdf(self, filename):
        """创建一个简单的测试PDF文件"""
        try:
            from PyPDF2 import PdfWriter, PageObject
            writer = PdfWriter()
            
            # 创建一个空白页面
            page = PageObject.create_blank_page(width=612, height=792)  # 标准信纸尺寸
            writer.add_page(page)
            
            with open(filename, "wb") as output_stream:
                writer.write(output_stream)
        except ImportError:
            # 如果PyPDF2不可用，则创建一个简单的PDF文件占位符
            with open(filename, "wb") as f:
                # 创建一个最小的PDF文件头
                f.write(b"%PDF-1.4\n")
                f.write(b"1 0 obj\n")
                f.write(b"<< /Type /Catalog /Pages 2 0 R >>\n")
                f.write(b"endobj\n")
                f.write(b"xref\n")
                f.write(b"trailer\n")
                f.write(b"<< /Root 1 0 R >>\n")
                f.write(b"%%EOF\n")
    
    def test_pdf_files_discovery(self):
        """测试是否能正确发现目录中的PDF文件"""
        # 测试get_pdf_files函数
        pdf_files = get_pdf_files(self.pdf_dir)
        self.assertEqual(len(pdf_files), 3)
        self.assertEqual(pdf_files, ["test1.pdf", "test2.pdf", "test3.pdf"])
    
    def test_merge_pdfs_functionality(self):
        """测试PDF合并功能"""
        # 保存当前工作目录
        original_cwd = os.getcwd()
        
        try:
            # 切换到测试目录
            os.chdir(self.test_dir)
            
            # 执行合并操作
            count, files = merge_pdfs(self.pdf_dir, self.output_file)
            
            # 验证返回值
            self.assertEqual(count, 3)
            self.assertEqual(files, ["test1.pdf", "test2.pdf", "test3.pdf"])
            
            # 验证输出文件是否存在
            self.assertTrue(os.path.exists(self.output_file))
            
        except Exception as e:
            # 如果PyPDF2不可用或其他错误，跳过测试
            if "PyPDF2" in str(e) or "pypdf" in str(e).lower():
                self.skipTest("PyPDF2 not available")
            else:
                raise
        finally:
            # 恢复原来的工作目录
            os.chdir(original_cwd)

    def test_empty_directory_handling(self):
        """测试空目录的处理"""
        if not PY_PDF_AVAILABLE:
            self.skipTest("PyPDF2 not available")
            
        # 创建一个空的PDF目录
        empty_dir = os.path.join(self.test_dir, "empty_pdf_dir")
        os.makedirs(empty_dir)
        
        # 保存当前工作目录
        original_cwd = os.getcwd()
        
        try:
            # 切换到测试目录
            os.chdir(self.test_dir)
            
            # 执行合并操作
            count, files = merge_pdfs(empty_dir, self.output_file)
            
            # 验证返回值
            self.assertEqual(count, 0)
            self.assertEqual(files, [])
            
            # 验证输出文件是否存在
            self.assertTrue(os.path.exists(self.output_file))
            
        except Exception as e:
            # 如果PyPDF2不可用或其他错误，跳过测试
            if "PyPDF2" in str(e) or "pypdf" in str(e).lower():
                self.skipTest("PyPDF2 not available")
            else:
                raise
        finally:
            # 恢复原来的工作目录
            os.chdir(original_cwd)
            
            # 清理
            if os.path.exists(self.output_file):
                os.remove(self.output_file)
            os.rmdir(empty_dir)

if __name__ == '__main__':
    unittest.main()