<?php
$redis = new Redis();
$redis->connect('localhost', 6379);//serverip port
$redis->set("test" , "Hello World");
echo $redis->get("test");
