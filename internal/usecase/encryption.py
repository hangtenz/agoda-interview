from internal.helper.aes import AESCipher


class EncryptionUsecase(object):
    aes_tool:AESCipher

    def __init__(self,private_key):
        self.aes_tool = AESCipher(private_key)

    def encrypt(self,list_message):
        res = []
        for message in list_message:
            res.append(self.aes_tool.encrypt(message))
        return res

    def decrypt(self,list_message):
        res = []
        for message in list_message:
            res.append(self.aes_tool.decrypt(message))
        return res