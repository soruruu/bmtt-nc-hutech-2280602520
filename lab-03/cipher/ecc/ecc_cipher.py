import ecdsa, os

# Tạo thư mục lưu khóa nếu chưa tồn tại
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()  # Tạo khóa riêng tư
        vk = sk.get_verifying_key()       # Tạo khóa công khai tương ứng

        with open('cipher/ecc/keys/privatekey.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('cipher/ecc/keys/publickey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/privatekey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('cipher/ecc/keys/publickey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def encrypt(self, message, key):
        # Ký thông điệp bằng khóa riêng tư (SigningKey)
        return key.sign(message.encode('utf-8'))

    def decrypt(self, message, signature, key):
        # Xác minh chữ ký bằng khóa công khai (VerifyingKey)
        try:
            return key.verify(signature, message.encode('utf-8'))
        except ecdsa.BadSignatureError:
            return False
