import unittest
from usecase.encryption import EncryptionUsecase

class TestEncryptionUsecase(unittest.TestCase):
    def test_init_usecase(self):
        private_key = "pk"
        usecase = EncryptionUsecase(private_key)

    def test_can_encrypt_list_of_message(self):
        private_key = "pk"
        usecase = EncryptionUsecase(private_key)
        message = ["msg1","msg2","msg3"]
        result = usecase.encrypt(message)
        self.assertTrue(len(result) == 3)

    def test_can_decrypt_list_of_message(self):
        private_key = "pk"
        usecase = EncryptionUsecase(private_key)
        message = ["msg1", "msg2", "msg3"]
        result = usecase.decrypt(usecase.encrypt(message))
        self.assertTrue(len(result) == 3)

    def test_decrypt_and_encrypt_correct(self):
        private_key = "pk"
        usecase = EncryptionUsecase(private_key)
        message = ["msg1", "msg2", "msg3"]
        result = usecase.decrypt(usecase.encrypt(message))
        self.assertTrue(len(result) == 3)
        for i,r in enumerate(result):
            self.assertEqual(r,message[i])