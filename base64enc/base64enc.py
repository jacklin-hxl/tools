import base64


def base64enc(filename:str) -> bytes:
    with open(filename,"rb") as f1, open("result.txt","wb") as f2:
        data = f1.read()
        result = base64.b64encode(data)
        f2.write(result)
        return result

def main():
    base64enc("test.jpg")
    
if __name__ == "__main__":
    main()