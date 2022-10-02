#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/10/22, 6:50 AM

from typing import AsyncIterable
import aioredis


async def init_redis(
    host: str, port: int, password: str
) -> AsyncIterable[aioredis.Redis]:
    """
    READ ME: https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html
    :param host:
    :param port:
    :param password:
    :return:
    """
    pool = aioredis.ConnectionPool.from_url(f"redis://{host}:{port}", password=password)
    try:
        yield aioredis.Redis(connection_pool=pool)
    finally:
        await pool.disconnect()
