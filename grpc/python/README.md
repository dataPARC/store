# dataPARC.Store Python gRPC Client

An example python client that uses protobuf files to connect to the gRPC endpoints on the dataPARC.Store historian.

## Prerequisites

See [https://grpc.io/docs/languages/python/](https://grpc.io/docs/languages/python/) for more info.

## Getting Started

1. Add python packages

   ```bash
   $ pip install grpcio grpcio-tools
   ```

2. Generate stubs from protobuf files. Given a directory structure like so:

   ```
   |- protos
      |- historian protobuf files...
      |- ...
      |- ...
   ```

   ```bash
   $ python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/*.proto
   ```

3. Certificates

   dataPARC.Store accepts HTTPS requests only, HTTP is not supported. This requires that secure channels must be used, insecure channels implicitly make HTTP requests. So the client must have access to the server's certificate.

## Example

```python
import datetime as dt
import ssl
from PublishingTypes_pb2 import (
    PublishingDataMode,
    StartTagPublishingRequest,
    TagPublishingRequests,
)
import grpc
import SDKService_pb2
import SDKService_pb2_grpc
import PublishingService_pb2_grpc
import SDKTypes_pb2
import google.protobuf.empty_pb2 as empty_pb2
from google.protobuf.duration_pb2 import Duration
from google.protobuf.timestamp_pb2 import Timestamp


def main():
    cert = ssl.get_server_certificate((host_name, port_number))
    creds = grpc.ssl_channel_credentials(cert.encode())

    with grpc.secure_channel(f"{host_name}:{port_number}", creds) as channel:
        tag = SDKTypes_pb2.TagQueryIdentifier(Id=144)

        service = SDKService_pb2_grpc.SDKServiceStub(channel)

        # Read all interfaces
        interfaces = service.GetInterfaces(empty_pb2.Empty())
        for interface in interfaces.InterfaceConfigs:
            print(interface)

        # Read raw data for a tag
        start = Timestamp()
        start.FromDatetime(dt.datetime.now(dt.timezone.utc) - dt.timedelta(seconds=5))
        end = Timestamp()
        end.FromDatetime(dt.datetime.now(dt.timezone.utc))
        params = SDKService_pb2.StreamRawParameters(
            TagIdentifier=tag,
            StartTime=start,
            EndTime=end,
        )
        for msg in service.StreamRawData(params):
            print(msg)

        # Subscribe to raw data for a tag
        publisher = PublishingService_pb2_grpc.PublishingServiceStub(channel)
        duration = Duration(seconds=1)

        def requests():
            yield TagPublishingRequests(
                StartTagPublishingRequest=StartTagPublishingRequest(
                    TagIdentifier=tag,
                    PublishingInterval=duration,
                    PublishingDataMode=PublishingDataMode.PublishingDataMode_All,
                )
            )

        stream = publisher.TagPublishing(requests())
        for res in stream:
            print(res)


if __name__ == "__main__":
    main()
```
