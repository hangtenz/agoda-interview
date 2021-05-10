import unittest
from helper.aes import AESCipher


class TestAESCipher(unittest.TestCase):
    def test_create_aes(self):
        private_key = "test key"
        aes = AESCipher(private_key)

    # can encrypt with use tool and get cipher text
    def test_can_encrypt(self):
        private_key = "test key"
        aes = AESCipher(private_key)
        text = "test text"
        cipher_text = aes.encrypt(text)
        self.assertTrue(type(cipher_text) is str)

    #after decrypt messge was encrypt get back same result
    def test_decrypt(self):
        private_key = "test key"
        aes = AESCipher(private_key)
        text = "test text"
        cipher_text = aes.encrypt(text)
        res_text = aes.decrypt(cipher_text)
        self.assertTrue(type(res_text) is str)
        self.assertEqual(text,res_text)



