# 单元测试说明

## 测试结构

- `test_merge_pdfs.py`: 包含对PDF合并功能的单元测试

## 运行测试

### 方法1: 使用unittest模块直接运行
```bash
python -m unittest tests.test_merge_pdfs
```

### 方法2: 运行所有测试
```bash
python -m unittest discover tests
```

### 方法3: 详细输出模式
```bash
python -m unittest -v tests.test_merge_pdfs
```

## 测试内容

1. **test_pdf_files_discovery**: 测试能否正确发现目录中的PDF文件
2. **test_merge_pdfs_functionality**: 测试PDF合并功能是否正常工作
3. **test_empty_directory_handling**: 测试空目录的处理情况

## 依赖

确保安装了所需的依赖包：
```bash
pip install PyPDF2
```