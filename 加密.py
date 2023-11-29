import base64

def base64_encode(data):
    """
    使用Base64編碼字符串
    """
    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return encoded_data

a = input('請輸入檔案名: ')
b = input('請輸入加密後的檔案名: ')
s = int(input('請輸入欲加密的次數: '))

with open(a, 'r', encoding='utf-8') as k:
    file=k.read()

for i in range(s):
    file = base64_encode(file)

with open(b, 'w', encoding='utf-8') as k:
    k.write(file)

print('加密完成~')