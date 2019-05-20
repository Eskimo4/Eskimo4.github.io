# Redis学习总结

## 一、常用命令

### 1、字符串
key和value的形式。

如果value可以被解释为十进制整数或者浮点数，redis会感知到并允许进行INCR和DECR操作。对不存在的或者空的key/value的操作会自动创建并设value初始值为0.

命令 | 描述
-|-
INCR key | 将value值加1  
DECR key | 将value值减1
INCRBY key amount | 将value值加整数amount
DECRBY key amount | 将value值减整数amount
INCRBYFLOAT key amount | 将value值加浮点数amount

还可以处理子串和二进制形式的操作。

命令 | 描述
-|-
APPEND key str | 将str追加到value末尾
GETRANGE key start end | 获取value中[start,end]下标内的子串
SETRANGE key offset str | 设置value的下标offset后为str
GETBIT key offset | 获取value的下标offset的二进制位值（将value视为二进制串）
SETBIT key offset bit | 设置value的下标offset的二进制位为bit（同上）
BITOP operation dest-key key [key...] | 对一个或多个key进行二进制运算，结果存到dest-key中，operation包括AND、OR、XOR、NOT

### 2、列表
key和有序列表[value,value,...]的形式。

命令|描述
-|-
RPUSH key value [value...] | 向列表右端推入一个或多个值
LPUSH key value [value...] | 向列表左端推入一个或多个值
RPOP key | 从列表右端取出一个值并返回
LPOP key | 从列表左端取出一个值并返回
LINDEX key index | 返回列表中下标为index的值
LRANGE key start end | 返回列表中下标在[start,end]范围内的所有值
LTRIM key start end | 裁剪列表，保留下标在[start,end]范围内的所有值

还可以执行阻塞式的弹出和在列表之间移动元素的操作。

命令|描述
-|-
BLPOP key [key...] timeout | 从第一个非空列表中弹出最左端的值，如没有则等待，timeout为超时时间
BRPOP key [key...] timeout | 从第一个非空列表中弹出最右端的值，如没有则等待，timeout为超时时间
RPOPLPUSH src-key des-key | 从src-key的列表的右端弹出一个值，并添加到des-key的左端
LPOPRPUSH src-key des-key | 从src-key的列表的左端弹出一个值，并添加到des-key的右端

### 3、集合
key和无序set的形式。

命令|描述
-|-
SADD key item [item...] | 将一个或多个item值添加到set中，返回成功添加的个数
SREM key item [item...] | 将一个或多个item值从set中删除，返回成功删除的个数
SISMEMBER key item | 判断item是否在set中
SCARD key | 返回set中元素的数量
SMEMBERS key | 返回set中所有元素
SRANDMEMBER key [count] | 随机返回set中一个或多个元素；count为正数时，元素不会重复；count为负数时，元素可能重复
SPOP key | 随机的移除set中的一个元素并返回
SMOVE src-key des-key item | 如果item在src-key中，则将item从src-key移动到des-key中，返回1；否则，返回0

多个集合之间的操作，差集、交集、并集。

命令|描述
-|-
SDIFF key [key...] | 返回在第一个集合中存在，但在后续的集合中都不存在的元素
SDIFFSTORE des-key key [key...] | 将在第一个集合中存在，但在后续的集合中都不存在的元素存储到des-key中
SINTER key [key...] | 返回在所有的集合中都存在的元素
SINTERSTORE des-key key [key...] | 将在所有的集合中都存在的元素存储到des-key中
SUNION key [key...] | 返回去除重复后的所有的集合中的元素
SUNIONSTORE des-key key [key...] | 将去除重复后的所有的集合中的元素存储到des-key中

### 4、散列
hkey和多个[key,value]对的形式。

命令|描述
-|-
HMGET hkey key [key...] | 从散列中获取一个或多个key的value值
HMSET hkey key value [key value...] | 设置散列中的一个或多个key的value值
HDEL hkey key [key...] | 从散列中删除一个或多个key/value对，返回成功删除的数量
HLEN hkey | 返回散列中包含的key/value对的数量
HEXISTS hkey key | 判断key是否存在于散列中
HKEYS hkey | 返回散列中所有的key
HVALS hkey | 返回散列中所有的value
HGETALL hkey | 返回散列中所有的key/value对
HINCRBY hkey key amount | 将散列中key的value值加上整数amount
HINCRBYFLOAT hkey key amout | 将散列中key的value值加上浮点数amount

### 5、有序集合zset
key和多个[member,score]的形式。

zset中默认按照分值从小到大排序。

命令|描述
-|-
ZADD key score member [score member...] | 在zset中添加一个或多个成员及其分值
ZREM key member [member...] | 删除zset中的一个或多个成员
ZCARD key | 返回zset中的成员数量
ZINCRBY key amount member | 将member的分值加上amount
ZCOUNT key min max | 返回分值在[min,max]之间的成员数量
ZRANK key member | 返回member在zset中的排名（序号从0开始）
ZSCORE key member | 返回member的分值
ZRANGE key start end [WITHSCORES] | 返回zset中排名在[start,end]之间的成员，可以选择是否带上分值
ZRANGEBYSCORE key min max [WITHSCORES] | 返回zset中分值在[min,max]之间的成员，可以选择是否带上分值

还有一些倒序的操作。

命令|描述
-|-
ZREVRANK key member | 返回member在zset中的排名（从大到小排序）
ZREVRANGE key start end [WITHSCORES] | 返回zset中排名在[start,end]之间的成员，可以选择是否带上分值（从大到小排序）
ZREVRANGEBYSCORE key max min [WITHSCORES] | 返回zset中分值在[max,min]之间的成员，可以选择是否带上分值（从大到小排序）

一些删除的操作。

命令|描述
-|-
ZREMRANGEBYRANK key start end | 删除zset中排名在[start,end]之间的成员
ZREMRANGEBYSCORE key min max | 删除zset中分值在[min,max]之间的成员

还有一些交集、并集操作。

命令|描述
-|-
ZINTERSCORE des-key key-count key [key...] | 对一个或多个key执行交集运算，结果存到des-key中
ZUNIONSCORE des-key key-count key [key...] | 对一个或多个key执行并集运算，结果存到des-key中

### 6、发布订阅

redis支持发布和订阅功能，PUBLISH、SUBSCRIBE等命令，不过貌似很少有人用。另外再介绍专业的消息中间件，如支持MQTT协议的mosquitto等。

### 7、其他命令

排序SORT、事务相关（MULTI、EXEC）

命令|描述
-|-
SORT src-key [BY pattern] [GET pattern [GET pattern ...]] [ASC\|DESC] [ALPHA] [STORE des-key] | 对列表、集合和有序集合进行排序，返回或存储结果。ALPHA表示根据字符串排序，AEC升序，DESC降序。
MULTI和EXEC | 创建事务，在MULTI和EXEC之间的命令会按序一起执行

设置过期时间，过期命令只能针对key，即只能为整个键设置过期时间，而不能为键里的单个元素设置。

命令|描述
-|-
PERSIST key | 移除键的过期时间
TTL key | 查看键的过期时间，单位为秒
EXPIRE key seconds | 设置键在指定时间后过期时间，单位为秒
EXPIREAT key timestamp |  设置键在给定时间戳时过期，单位为秒
PTTL key | 查看键的过期时间，单位为毫秒
PEXPIRE key milliseconds | 设置键在指定时间后过期时间，单位为毫秒
PEXPIREAT key timestamp |  设置键在给定时间戳时过期，单位为毫秒

## 二、持久化和复制

### 1、持久化

redis有两种持久化方式，分别是快照rdb和只追加文件aof。

redis进行快照的时机：
* BGSAVE命令，非阻塞，redis会fork一个子进程写快照文件
* SAVE命令，阻塞，redis主进程写快照文件
* 按照save配置项自动触发BGSAVE
* SHUTDOWN时，redis执行SAVE
* 当有从连接到主时，主redis进行一次BGSAVE


快照的相关配置：

配置项|描述
-|-
save 60 1000 | 在60s内有1000次写入时进行快照
rdbcompression yes | 对快照文件进行压缩
dbfilename dump.rdb | 指定快照文件名
dir ./ | 指定rdb文件和aof文件的存放目录


aof相关配置：

配置项|描述
-|-
appendonly yes | 开启aof持久化
appendfsync everysec | 每秒同步一次aof文件，可选择的还有：always（每次写入时同步），no（让系统决定何时同步）
auto-aof-rewrite-percentage 100 | 当aof文件的大小增长了100%时，进行重写（也可以通过BGREWRITEAOF命令触发重写）
auto-aof-rewrite-min-size 64mb | 指定aof文件大小的最小值

### 2、复制

redis可以配置一主多从的集群，主可读可写，从只读。主从之间在初次连接时，将主的数据复制到从中，然后主redis后面的每次写命令都同步到从redis。

从redis的配置如下：

配置项|描述
-|-
slaveof host port | 设置主的ip地址和端口
slaveof no one | 取消主

也可以对从redis执行slaveof命令进而达到相同的效果。