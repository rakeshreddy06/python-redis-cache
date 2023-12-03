from redis import StrictRedis
from redis_cache import RedisCache
client = StrictRedis(host="localhost", decode_responses=True)
cache = RedisCache(redis_client=client)
@cache.cache()
def my_func(arg1, arg2):
    result = arg1**arg2
    print(arg2, result)
# Use the function
my_func(80, 90)
# Call it again with the same arguments and it will use cache
my_func(80, 91)
my_func(80, 92)
my_func(80, 90)
my_func(80, 93)
my_func(80, 94)
my_func(80, 95)
my_func(80, 90)
my_func(80, 91)
my_func(80, 96)
my_func(80, 92)
my_func(80, 96)

# Invalidate a single value
my_func.invalidate(80, 90)
my_func.invalidate(80, 91)
my_func.invalidate(80, 92)
my_func.invalidate(80, 93)
my_func.invalidate(80, 94)
my_func.invalidate(80, 95)
# Invalidate all values for function
my_func.invalidate_all()