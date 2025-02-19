# 进制转换工具
一个基于 PySide6 和 QtFluentWidgets 开发的现代化进制转换工具，支持二进制、八进制、十进制和十六进制之间的相互转换。

## 功能特点

- 支持多种进制转换：
  - 二进制 (Binary)
  - 八进制 (Octal)
  - 十进制 (Decimal)
  - 十六进制 (Hexadecimal)
- 实时转换，输入即可看到结果
- 现代化的 Fluent Design 界面
- 支持深色/浅色主题自动切换
- 支持高分辨率显示
- 结果可选择复制

## 安装说明

1. 确保已安装 Python 3.7 或更高版本
2. 安装依赖包：
```bash
pip install PySide6
pip install PyQt-Fluent-Widgets
```

## 使用方法

1. 运行程序：
```bash
python main.py
 ```

2. 在输入框中输入要转换的数值
3. 从下拉菜单选择输入数值的进制
4. 程序会自动显示其他进制的对应值
5. 点击结果可以选择并复制

## 开发环境
- Python 3.7+
- PySide6
- PyQt-Fluent-Widgets

## 注意事项

- 输入数值必须符合所选择的进制规则
  - 二进制：只能输入 0 和 1
  - 八进制：只能输入 0-7 的数字
  - 十进制：只能输入 0-9 的数字
  - 十六进制：可以输入 0-9 的数字和 A-F 的字母

  