# redis/docker

## master slave

> wget http://download.redis.io/releases/redis-5.0.7.tar.gz

## create

```
cd /redis/masterandslave
docker build -t redis5asm .
```
## connect

1. Run server on both continer

> \> SLAVEOF 192.160.1.150 6379
