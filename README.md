# tools
该仓库的tools应用于数据处理

## hashenc
+ 用于计算文件的hash值

+ 修改hash算法名称和目标文件名称（大小写敏感），输出的hash值保存在result.txt中。
    ```python
    def main():
        hashenc("sha384","test.txt")
    ```
+ 目前支持算法的有:  
{'sha3_384', 'sha512', 'sha256', 'blake2b', 'blake2s', 'shake_256', 'sha384', 'sha224', 'sha3_224', 'sha1', 'sha3_256', 'md5', 'sha3_512', 'shake_128'}

## base64enc  
+ 用于base64编码文件内容
+ 修改目标文件名称，输出base64编码值保存在result.txt中。
    ```python
    def main():
        base64enc("test.jpg")
    ```  

## Xtools
+ 集成base64编解码和Hash算法，面向用户的GUI应用
+ 选择编码类型和编码方法对数据进行相应操作,支持输入内容支持文件和文本内容，支持文件拖动输入区域。