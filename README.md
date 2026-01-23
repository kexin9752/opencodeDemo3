# PDF合并工具

一个简单易用的PDF文件合并工具，可以将多个PDF文件按顺序合并成一个PDF文件。

## 功能特性

- 自动扫描指定目录中的所有PDF文件
- 按文件名字母顺序排序后合并
- 支持中文文件名
- 显示合并进度和结果
- 轻量级，易于使用

## 安装依赖

```bash
pip install -r requirements.txt
```

或者直接安装PyPDF2：

```bash
pip install PyPDF2
```

## 使用方法

1. 在项目目录下创建一个名为 `pdf_merge` 的文件夹
2. 将需要合并的PDF文件放入该文件夹中
3. 运行合并脚本：

```bash
python merge_pdfs.py
```

4. 合并完成后，将在项目目录下生成 `merged_output.pdf` 文件

## 配置说明

可以通过修改 `merge_pdfs.py` 中的参数来自定义行为：

```python
# PDF源目录（可根据需要修改）
pdf_dir = "pdf_merge"

# 输出文件名（可根据需要修改）
output_file = "merged_output.pdf"
```

## 使用示例

目录结构：
```
project/
├── merge_pdfs.py
└── pdf_merge/
    ├── 01_文档1.pdf
    ├── 02_文档2.pdf
    └── 03_文档3.pdf
```

执行合并：
```bash
$ python merge_pdfs.py
找到 3 个PDF文件: ['01_文档1.pdf', '02_文档2.pdf', '03_文档3.pdf']
已添加文件 1: b'01_\xe6\x96\x87\xe6\xa1\xa31.pdf'...
已添加文件 2: b'02_\xe6\x96\x87\xe6\xa1\xa32.pdf'...
已添加文件 3: b'03_\xe6\x96\x87\xe6\xa1\xa33.pdf'...

合并完成！输出文件: merged_output.pdf
```

## 运行测试

项目包含了单元测试，可以通过以下方式运行：

### 使用测试运行脚本（推荐）
```bash
python run_tests.py
```

### 手动运行测试
```bash
# 运行所有测试
python -m unittest discover tests

# 运行特定测试文件
python -m unittest tests.test_merge_pdfs

# 详细输出模式
python -m unittest -v tests.test_merge_pdfs
```

## 系统要求

- Python 3.6 或更高版本
- PyPDF2 >= 3.0.0

## 注意事项

1. 确保 `pdf_merge` 目录存在且包含至少一个PDF文件
2. 合并过程会覆盖已存在的输出文件
3. 大文件合并可能需要较长时间，请耐心等待

## 许可证

本项目仅供学习和办公使用。