import redis

conn = redis.Redis('127.0.0.1', 6379)
conn.set("a", "a")
