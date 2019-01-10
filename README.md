# headerpy
headerpy
step0 在环境变量中添加别名
```
alias header=‘python abspath/header_V2.py ’
```
step1 更新环境变量
```
source ~/.bash_profile
```
使用案例1
```
header file tab 

header test.txt 
header test.txt t
header test.txt ,
header test.txt s
```
使用案例2
```
cat test.txt | header - 
cat test.txt | header - t 
cat test.txt | header - 
```
