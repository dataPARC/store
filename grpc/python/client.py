import datetime as dt
import ssl
import grpc
import SDKService_pb2
import SDKService_pb2_grpc
import SDKTypes_pb2
import google.protobuf.empty_pb2 as empty_pb2
from google.protobuf.timestamp_pb2 import Timestamp


def main():
    cert = ssl.get_server_certificate(("localhost", 12341))
    creds = grpc.ssl_channel_credentials(cert.encode())

    with grpc.secure_channel("localhost:12341", creds) as channel:
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
            TagIdentifier=SDKTypes_pb2.TagQueryIdentifier(Id=144),
            StartTime=start,
            EndTime=end,
        )
        for msg in service.StreamRawData(params):
            print(msg)


if __name__ == "__main__":
    main()
