# PDF合并工具使用文档

## 1. 功能描述

`merge_pdfs.py` 是一个简单实用的PDF文件合并工具，主要功能如下：

- **自动扫描目录**：从指定的 `pdf_merge` 目录中自动查找所有PDF文件
- **智能排序**：按文件名对PDF文件进行排序，确保合并顺序符合预期
- **批量合并**：将多个PDF文件合并为一个统一的PDF文档
- **进度反馈**：在合并过程中显示详细的进度信息，包括找到的文件数量和每个文件的添加状态
- **编码兼容**：支持包含中文等特殊字符的文件名处理

该工具使用 PyPDF2 库进行PDF操作，适用于日常办公场景中需要合并多个PDF文件的用户。

## 2. 使用方法

### 2.1 环境准备

在使用本工具之前，请确保已安装必要的依赖：

```bash
pip install PyPDF2
```

### 2.2 文件准备

1. **创建PDF目录**：在脚本同级目录下创建一个名为 `pdf_merge` 的文件夹
2. **放入PDF文件**：将需要合并的PDF文件放入该目录中
   - 支持任意数量的PDF文件
   - 文件名可以是中文或英文
   - 文件会按文件名自动排序后合并

### 2.3 运行脚本

在命令行中执行以下命令：

```bash
python merge_pdfs.py
```

### 2.4 配置文件说明

如果需要修改默认配置，可以编辑脚本中的以下变量：

```python
# PDF源目录（可根据需要修改）
pdf_dir = "pdf_merge"

# 输出文件名（可根据需要修改）
output_file = "merged_output.pdf"
```

## 3. 输入输出说明

### 3.1 输入说明

| 参数 | 说明 | 默认值 | 要求 |
|------|------|--------|------|
| 源目录 | 存放待合并PDF文件的目录 | `pdf_merge` | 必须存在，包含至少一个PDF文件 |
| PDF文件 | 目录中的 `.pdf` 后缀文件 | - | 支持标准PDF格式 |

**输入要求：**
- 目录必须存在且可访问
- PDF文件必须是有效的PDF格式
- 文件扩展名必须为 `.pdf`（小写）
- 建议单个PDF文件大小不超过100MB

### 3.2 输出说明

| 参数 | 说明 | 默认值 | 格式 |
|------|------|--------|------|
| 合并文件 | 合并后的PDF输出文件 | `merged_output.pdf` | 标准PDF格式 |

**输出特点：**
- 生成标准PDF文件，可在任何PDF阅读器中打开
- 保留原始PDF的页面顺序和内容
- 文件大小为所有输入文件的总和
- 覆盖同名输出文件（如果已存在）

## 4. 依赖说明

### 4.1 核心依赖

| 依赖名称 | 版本要求 | 说明 |
|----------|----------|------|
| PyPDF2 | >= 3.0.0 | PDF文件读写和处理库 |

### 4.2 系统要求

- **Python版本**：Python 3.6 或更高版本
- **操作系统**：Windows、macOS、Linux 等支持Python的系统
- **内存要求**：建议至少512MB可用内存
- **磁盘空间**：至少需要源PDF文件总大小的1.5倍空间

### 4.3 安装命令

```bash
# 使用 pip 安装依赖
pip install -r requirements.txt

# 或者单独安装PyPDF2
pip install PyPDF2

# 或者使用国内镜像源（可选）
pip install PyPDF2 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 5. 使用示例

### 5.1 基础使用示例

**目录结构：**
```
project/
├── merge_pdfs.py
└── pdf_merge/
    ├── 01_文档1.pdf
    ├── 02_文档2.pdf
    └── 03_文档3.pdf
```

**执行过程：**
```bash
$ python merge_pdfs.py
找到 3 个PDF文件: ['01_文档1.pdf', '02_文档2.pdf', '03_文档3.pdf']
已添加文件 1: b'01_\xe6\x96\x87\xe6\xa1\xa31.pdf'...
已添加文件 2: b'02_\xe6\x96\x87\xe6\xa1\xa32.pdf'...
已添加文件 3: b'03_\xe6\x96\x87\xe6\xa1\xa33.pdf'...

合并完成！输出文件: merged_output.pdf
```

**结果：**
- 生成 `merged_output.pdf` 文件
- 包含3个文档的所有页面
- 页面顺序按文件名排序

### 5.2 实际应用场景

#### 场景一：合并会议资料

假设您有多个会议的PDF资料需要合并：

```
pdf_merge/
├── 01_会议议程.pdf
├── 02_主题演讲.pdf
├── 03_讨论纪要.pdf
└── 04_附录材料.pdf
```

运行脚本后，这些文件将按顺序合并为一个完整的会议资料包。

#### 场景二：合并报告章节

```
pdf_merge/
├── 第1章_概述.pdf
├── 第2章_分析方法.pdf
├── 第3章_结果展示.pdf
└── 第4章_结论建议.pdf
```

合并后形成完整的分析报告。

### 5.3 批量操作示例

如果您经常需要合并PDF，可以创建批处理文件：

**Windows (merge.bat):**
```batch
@echo off
python merge_pdfs.py
pause
```

**Linux/Mac (merge.sh):**
```bash
#!/bin/bash
python merge_pdfs.py
```

### 5.4 进阶使用：自定义目录

如果需要从不同目录合并PDF，可以修改脚本：

```python
import sys

# 使用命令行参数指定目录
if len(sys.argv) > 1:
    pdf_dir = sys.argv[1]
else:
    pdf_dir = "pdf_merge"

if len(sys.argv) > 2:
    output_file = sys.argv[2]
else:
    output_file = "merged_output.pdf"
```

使用时：
```bash
python merge_pdfs.py /path/to/pdfs output.pdf
```

## 6. 常见问题

### Q1: 提示 "FileNotFoundError: [Errno 2] No such file or directory: 'pdf_merge'"？

**解决方法：** 确保 `pdf_merge` 目录存在，且目录名称完全匹配（包括大小写）。

### Q2: 合并后的文件打不开？

**可能原因：**
1. 源PDF文件已损坏
2. 源PDF文件是加密的
3. PyPDF2版本过旧

**解决方法：**
- 检查源PDF文件是否正常
- 更新PyPDF2：`pip install --upgrade PyPDF2`
- 使用其他工具验证源文件

### Q3: 文件名包含中文时出现乱码？

**解决方法：** 当前脚本已支持中文文件名，如果仍有问题，检查系统编码设置。

### Q4: 如何控制合并顺序？

**说明：** 脚本使用 `sorted()` 函数按文件名排序。如需自定义顺序：
1. 重命名文件使用数字前缀（如 `01_xxx.pdf`）
2. 或者修改代码使用自定义排序逻辑

## 7. 注意事项

1. **文件备份**：建议在合并前备份原始PDF文件
2. **磁盘空间**：确保有足够的磁盘空间存储输出文件
3. **文件权限**：确保对源目录和目标目录有读写权限
4. **大文件处理**：处理大型PDF文件时可能需要较长时间，请耐心等待
5. **编码问题**：尽量使用UTF-8编码的文件名，避免特殊字符

## 8. 单元测试

本项目包含了针对PDF合并功能的单元测试，确保代码质量和功能正确性。

### 8.1 测试结构

测试代码位于 `tests/` 目录下：
- `test_merge_pdfs.py`: 主要的测试文件，包含对PDF合并功能的测试
- `README.md`: 测试运行说明

### 8.2 运行测试

有两种方式运行测试：

#### 方法1: 使用测试运行脚本（推荐）
```bash
python run_tests.py
```

#### 方法2: 手动运行测试
```bash
# 运行所有测试
python -m unittest discover tests

# 运行特定测试文件
python -m unittest tests.test_merge_pdfs

# 详细输出模式
python -m unittest -v tests.test_merge_pdfs
```

### 8.3 测试内容

当前测试覆盖以下功能：
1. PDF文件发现功能
2. PDF合并核心功能
3. 空目录处理情况

### 8.4 测试依赖

测试需要安装PyPDF2库：
```bash
pip install PyPDF2
```

## 9. 扩展建议

如果如果您需要更高级的功能，可以考虑：

- 添加错误处理机制
- 支持PDF拆分功能
- 添加PDF压缩选项
- 支持密码保护的PDF
- 添加图形界面（GUI）

---

**作者信息：** 本工具由 AI 生成，仅供学习和办公使用。

**更新日期：** 2026年1月23日
