import hashlib

hash_available =  hashlib.algorithms_guaranteed

def hashenc(hash_method:str, filename:str) -> str:
    if hash_method in hash_available:
        with open(filename,"rb") as f1,open("result.txt","wb") as f2:
            data = f1.read()
            file_md5 = eval("hashlib.{hash_method}({data}).hexdigest()".format(hash_method=hash_method,data=data))
            f2.write(file_md5.encode())
            return file_md5
    else:
        raise Exception("{hash_method} is not supported")

def main():
    hashenc("sha384","test.txt")

if __name__ == "__main__":
    main()
