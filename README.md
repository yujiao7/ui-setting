# 一、版本发布
## 1. 安装twine
```
pip install twine
```
## 2. 本地打包
```
python setup.py sdist  
```
## 3. 发布版本
```
pip install twine
twine upload dist/guoya-tools-1.2.1.tar.gz
```