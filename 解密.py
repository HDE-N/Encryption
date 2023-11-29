import base64
import time

def base64_decode(data):
    """
    使用Base64解碼字符串
    """
    decoded_data = base64.b64decode(data).decode('UTF-8')
    return decoded_data

print('測試用，無須Key...')
time.sleep(1)

a = input('請輸入密文檔案名: ')
b = input('請輸入解密後之檔案名: ')

with open(a, 'r', encoding='utf-8') as k:
    file=k.read()

while 1:
    try:
        file=base64_decode(file)
    except:
        break
with open(b, 'w', encoding='utf-8') as k:
    k.write(file)

print('解密完成~')

time.sleep(10)