<?php
$redis = new Redis();
$redis->connect('192.168.169.140', 6379);//serverip port
$redis ->set("test" , "Hello World");
echo $redis ->get("test");
