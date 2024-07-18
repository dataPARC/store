# dataPARC.Store Python gRPC Client

## Prerequisites

See [https://grpc.io/docs/languages/python/](https://grpc.io/docs/languages/python/) for more info.

## Getting Started

1. Add python packages

   `$ pip install grpcio grpcio-tools`

2. Generate stubs from protobuf files. Given a directory structure like so:

   ```
   |- protos
      |- google
      |   |- api
      |      |- annotations.proto
      |      |- http.proto
      |- historian protobuf files...
      |- ...
      |- ...
   ```

   `$ python -m grpc_tools.protoc -I ./protos -I ./protos/google/api --python_out=. --pyi_out=. --grpc_python_out=. ./protos/*.proto ./protos/google/api/*.proto`

3. Certificates

   dataPARC.Store accepts HTTPS requests only, HTTP is not supported. This requires that secure channels must be used, insecure channels implicitly make HTTP requests. So the client must have access to the server's certificate.

## Example

```python
import datetime as dt
import ssl
import grpc
import SDKService_pb2
import SDKService_pb2_grpc
import SDKTypes_pb2
import google.protobuf.empty_pb2 as empty_pb2
from google.protobuf.timestamp_pb2 import Timestamp


def main():
    cert = ssl.get_server_certificate((host_name, port_number))
    creds = grpc.ssl_channel_credentials(cert.encode())

    with grpc.secure_channel(f"{host_name}:{port_number}", creds) as channel:
        service = SDKService_pb2_grpc.SDKServiceStub(channel)

        # Read all interfaces
        interfaces = service.GetInterfaces(empty_pb2.Empty())
        for interface in interfaces.InterfaceConfigs:
            print(interface)

        # Read raw data for a tag
        start = Timestamp()
        start.FromDatetime(
            dt.datetime.now(dt.timezone.utc) - dt.timedelta(seconds=5)
        )
        end = Timestamp()
        end.FromDatetime(dt.datetime.now(dt.timezone.utc))
        params = SDKService_pb2.StreamRawParameters(
            TagIdentifier=SDKTypes_pb2.TagQueryIdentifier(Id=144),
            StartTime=start,
            EndTime=end,
        )
        for msg in service.StreamRawData(params):
            print(msg)


if __name__ == "__main__":
    main()
```
