- **函数名、类名等使用大驼峰命名法**，例如：  
  - class DataBase:  
  - def ParameterInput():

- **变量名使用小驼峰命名法**，例如:  
  - exercisesStorage  
  - sampleValue

- **所有名称应为实际作用的全称或缩写**，例如：  
ParameterInput缩写为ParaIn，用于输入命令行参数  

- **每个函数名之后须跟上函数功能的注释**
- **函数中出现的if、for等包含条件判断的代码块，如果较为复杂，应在首行注释说明该代码块的功能**
- **涉及文件读写时，文件编码默认为UTF-8**，例如：  
  - ```python
    file=open(path,'r',encoding="UTF-8")
    ```
