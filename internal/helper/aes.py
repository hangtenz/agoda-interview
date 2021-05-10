import pyaes, pbkdf2, binascii, os, secrets


class AESCipher(object):
    key: bytes
    init_vector: int
    coding_method: str

    def __init__(self, private_key):
        password_salt = os.urandom(16)
        self.key = pbkdf2.PBKDF2(private_key, password_salt).read(32)
        self.init_vector = secrets.randbits(256)
        self.coding_method = 'unicode_escape'

    def encrypt(self,message):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.init_vector))
        ciphertext = aes.encrypt(message)

        return ciphertext.decode(self.coding_method)

    def decrypt(self,ciphertext):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.init_vector))
        decrypted = aes.decrypt(ciphertext)
        return decrypted.decode(self.coding_method)