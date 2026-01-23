# PDF文件合并工具
# 导入PyPDF2库中的PdfWriter和PdfReader类，用于处理PDF文件
# 导入os模块，用于处理文件路径和目录操作
from PyPDF2 import PdfWriter, PdfReader
import os

def merge_pdfs(pdf_dir="pdf_merge", output_file="merged_output.pdf"):
    """
    合并指定目录下的所有PDF文件
    
    Args:
        pdf_dir (str): 包含PDF文件的目录路径，默认为"pdf_merge"
        output_file (str): 输出文件名，默认为"merged_output.pdf"
    
    Returns:
        tuple: (成功合并的文件数, 合并的文件列表)
    """
    # 获取指定目录下所有以.pdf结尾的文件，并按文件名排序
    pdf_files = sorted([f for f in os.listdir(pdf_dir) if f.endswith(".pdf")])
    print(f"找到 {len(pdf_files)} 个PDF文件: {pdf_files}")

    # 创建PdfWriter对象，用于合并PDF文件
    merger = PdfWriter()

    # 遍历所有PDF文件并逐个合并
    for i, pdf in enumerate(pdf_files):
        # 构建PDF文件的完整路径
        pdf_path = os.path.join(pdf_dir, pdf)
        # 将当前PDF文件添加到合并器中
        merger.append(PdfReader(pdf_path))
        # 打印进度信息，显示已添加的文件名（限制长度以避免过长）
        print(f"已添加文件 {i + 1}: {pdf.encode('utf-8')[:50]}...")

    # 将合并后的PDF写入输出文件
    merger.write(output_file)
    # 关闭合并器，释放资源
    merger.close()

    print(f"\n合并完成！输出文件: {output_file}")
    return len(pdf_files), pdf_files

def get_pdf_files(pdf_dir="pdf_merge"):
    """
    获取指定目录下所有PDF文件
    
    Args:
        pdf_dir (str): 包含PDF文件的目录路径，默认为"pdf_merge"
    
    Returns:
        list: PDF文件列表
    """
    return sorted([f for f in os.listdir(pdf_dir) if f.endswith(".pdf")])

if __name__ == "__main__":
    # 当直接运行此脚本时执行合并操作
    merge_pdfs()
