from account.models import UserCredentials
from common.utils.redis import RedisUtils


class UserCredentialService:
    def __init__(self):
        self.redis = RedisUtils()

    @staticmethod
    def get_otp_key(user_id):
        return f"otp:{user_id}"

    def generate_otp(self, user_id):
        pass

    def validate_otp(self, user_id, otp):
        # validate otp from redis
        key = self.get_otp_key(user_id=user_id)
        otp_from_redis = self.redis.get_value_from_key(key=key)
        if otp != otp_from_redis:
            return False
        UserCredentials.mark_verify(user_id=user_id)
        return True
