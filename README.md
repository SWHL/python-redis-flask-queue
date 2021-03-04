#### python-redis-flask-queue
- 利用redis构建任务队列
- 代码来源：[python中利用redis构建任务队列(queue)](https://www.cnblogs.com/arkenstone/p/7813551.html)

#### 文件说明
- `task.py`: rq work进程来监听队列
- `test.py`: 模拟post和get请求
- `app.py`: 搭建flask框架

#### 运行步骤
1. ~~`python worker.py`启动`redis server`~~ 这种方式不能有效执行，目前不清楚问题在哪里？
1. `rq worker` 启动`redis server`
2. `python app.py`启动`flask`服务
3. `python test.py`发送post和get请求，打印队列中任务执行结果
