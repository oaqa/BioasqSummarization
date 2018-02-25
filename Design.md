# BioASQ Summarization Design Notes

## Project Structure

TBD

## RabbitMQ

1. Starting the RabbitMQ server
1. The RabbitMQ management console

### Getting the IP address for the RabbitMQ server.

The services are configured to look for a RabbitMQ server on *localhost*. This is fine for development and testing

```
docker network inspect bridge
```

```json
"Containers": {
    "61b390c1f1643c0ed5aeb3791b3ef00d70f8cf0d63c09d3f8c1feb2dbf176172": {
        "Name": "rabbit",
        "EndpointID": "4f056e9f757f3b940039c9988c731581a0e6ceec09dcb16d63db18b5c300c09f",
        "MacAddress": "02:42:ac:11:00:02",
        "IPv4Address": "172.17.0.2/16",
        "IPv6Address": ""
    }
}
```

## The Data Model

TDB

## The Task Class

1. Provides a Logger for subclasses to use.
1. Provides methods for starting, stopping, and joining (waiting for) the service thread.
1. Provides two abstract methods subclasses can override:
  1. `perform(self, input_string)`<br/>Called whenever a message arrives for the service.
  1. `command(self, input_string)`<br/>Called when a *command* message arrives for the service. The `input` parameter will contain the command that was sent to the service.

## Building Docker Images

TBD

## The Services

| Module | Message Queue |
|---|---|
| Expander | expand.none |
| | expand.umls |
| Ranker | mmr.core |
| | mmr.soft |
| | mmr.hard |
| Tiler | tiler.concat |
| | tiler.fusion |
| Order | order.majority |
| | order.cluster |
| | order.kmeans |

## Running The Services

TBD

