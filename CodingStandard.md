- **函数名、类名等使用大驼峰命名法**，例如：  
  - class DataBase:  
  - def ParameterInput():

- **变量名使用小驼峰命名法**，例如:  
  - exercisesStorage  
  - sampleValue

- **所有名称应为实际作用的全称或缩写**，例如：  
  - `ParameterInput`缩写为`ParaIn`，用于输入命令行参数  

- **每个函数名之后须跟上函数功能的注释**
- **函数中出现的if、for等包含条件判断的代码块，如果较为复杂，应在首行注释说明该代码块的功能**
- **涉及文件读写时，文件编码默认为UTF-8**，样例代码如下：  
  - ```python
    file=open(path,'r',encoding="UTF-8")
    ```
- **出现加减乘除操作时，尽量不使用缩写**，例如：  
  - 使用a=a+1 而不是 a+=1
