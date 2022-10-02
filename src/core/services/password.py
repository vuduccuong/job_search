#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/1/22, 5:33 PM
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordService:
    @staticmethod
    def get_password_hash(password):
        return bcrypt_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return bcrypt_context.verify(plain_password, hashed_password)
