# COVID-19-screening-report-Ocr
 核酸检测证明截图检视辅助工具
## 简介

一张一张检视核酸检测结果证明效率低下，手动重命名截图文件效率低下，故基于`python`的`easyocr`库实现自动检视与重命名。

|    pack | version |
| ------: | ------- |
|  python | 3.9     |
| easyocr | 1.4.2   |
| xlwings | 0.27.5  |

## 功能

- 根据截图自动提取最新检测信息（检测时间与检测结果）
- 重命名截图文件
- 生成`list.xlxs`

## 使用方法

1. 将检测对象集合的学号与姓名填入`list.xlxs`，ocr的结果将与之比对
2. 将截图放入`img`文件夹下
3. 运行`main.py`
