from calendar import timegm
from datetime import datetime, timedelta
from typing import Any, Dict
import jwt
from flask import current_app


class JwtToken:
    def __init__(self, data: Dict[str, Any]):
        self._now = datetime.now()
        self._data = data

    def _get_token(self, time_delta: timedelta) -> str:
        self._data.update({
            "exp": timegm((self._now + time_delta).timetuple())
        })
        return jwt.encode(self._data, current_app.config['SECRET_KEY'], algorithm="HS256")

    @property
    def refresh_token(self) -> str:
        return self._get_token(time_delta=timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS']))

    @property
    def access_token(self) -> str:
        return self._get_token(time_delta=timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES']))

    def get_tokens(self) -> Dict[str, str]:
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
        }

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
