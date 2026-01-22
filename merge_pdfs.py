from PyPDF2 import PdfWriter, PdfReader
import os

pdf_dir = "pdf_merge"
output_file = "merged_output.pdf"

pdf_files = sorted([f for f in os.listdir(pdf_dir) if f.endswith(".pdf")])
print(f"找到 {len(pdf_files)} 个PDF文件: {pdf_files}")

merger = PdfWriter()

for i, pdf in enumerate(pdf_files):
    pdf_path = os.path.join(pdf_dir, pdf)
    merger.append(PdfReader(pdf_path))
    print(f"已添加文件 {i + 1}: {pdf.encode('utf-8')[:50]}...")

merger.write(output_file)
merger.close()

print(f"\n合并完成！输出文件: {output_file}")
