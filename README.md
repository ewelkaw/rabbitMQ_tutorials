# RabbitMQ_tutorials

Tutorials done just for trening from https://www.rabbitmq.com/getstarted.html

# Instalation
```bash
$ brew update
$ brew install rabbitmq
```

To see what queues RabbitMQ has and how many messages are in them:
```bash
sudo rabbitmqctl list_queues
```

To use scripts:
```bash
python -m pip install pika --upgrade
```

1. hello_world usage
```bash
$ python hello_world/hello_world_receive.py
$ python hello_world/hello_world_send.py
```

2. work_queues usage
```bash
# add two workes
$ python work_queues/worker.py 
$ python work_queues/worker.py 

# add some tasks
$ python work_queues/new_task.py First message.
$ python work_queues/new_task.py Second message..
$ python work_queues/new_task.py Third message...
$ python work_queues/new_task.py Fourth message....
$ python work_queues/new_task.py Fifth message.....
```