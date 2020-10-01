import binascii
import hashlib
import os

class XToolsFunc():

    @staticmethod
    def base64_method(method:str, value:str) -> str:
        value = value.replace("file:///","")
        if method == "encode":
            if os.path.isfile(value):
                input_method = "输入为文件"
                with open(value,"rb") as f:
                    data_bytes = f.read()
                result = binascii.b2a_base64(data_bytes).decode()
                return result,input_method
            else:
                input_method = "输入为文本"
                data_bytes = bytes(value,encoding="utf-8")
                result = binascii.b2a_base64(data_bytes).decode()
                return result,input_method
        elif method == "decode":
            if os.path.isfile(value):
                input_method = "输入为文件"
                with open(value,"rb") as f:
                    data_bytes = f.read()
                try:
                    result = binascii.a2b_base64(data_bytes).decode()
                    return result,input_method
                except:
                    return "Incorrect input value",input_method
            else:
                input_method = "输入为文本"
                try:
                    data_bytes = bytes(value,encoding="utf-8")
                    result = binascii.a2b_base64(data_bytes).decode()
                    return result,input_method
                except:
                    return "Incorrect input value",input_method

    @staticmethod
    def hash_method(method:str, value:str) -> str:
        value = value.replace("file:///","")
        if os.path.isfile(value):
            input_method = "输入为文件"
            with open(value,"rb") as f:
                data_bytes = f.read()
            result = eval("hashlib.{0}({1}).hexdigest()".format(method,data_bytes))
            return result,input_method
        else:
            input_method = "输入为文本"
            data_bytes = bytes(value,encoding="utf-8")
            result = eval("hashlib.{0}({1}).hexdigest()".format(method,data_bytes))
            return result,input_method