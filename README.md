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