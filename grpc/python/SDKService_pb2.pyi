import SDKTypes_pb2 as _SDKTypes_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetInterfacesParameters(_message.Message):
    __slots__ = ("GroupName",)
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    GroupName: _SDKTypes_pb2.NullableString
    def __init__(self, GroupName: _Optional[_Union[_SDKTypes_pb2.NullableString, _Mapping]] = ...) -> None: ...

class GetInterfaceParameters(_message.Message):
    __slots__ = ("InterfaceName", "GroupName")
    INTERFACENAME_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    InterfaceName: _SDKTypes_pb2.NullableString
    GroupName: _SDKTypes_pb2.NullableString
    def __init__(self, InterfaceName: _Optional[_Union[_SDKTypes_pb2.NullableString, _Mapping]] = ..., GroupName: _Optional[_Union[_SDKTypes_pb2.NullableString, _Mapping]] = ...) -> None: ...

class GetInterfaceSetsParameters(_message.Message):
    __slots__ = ("GroupName",)
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    GroupName: _SDKTypes_pb2.NullableString
    def __init__(self, GroupName: _Optional[_Union[_SDKTypes_pb2.NullableString, _Mapping]] = ...) -> None: ...

class GetInterfaceSetParameters(_message.Message):
    __slots__ = ("InterfaceSetName", "GroupName")
    INTERFACESETNAME_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    InterfaceSetName: _SDKTypes_pb2.NullableString
    GroupName: _SDKTypes_pb2.NullableString
    def __init__(self, InterfaceSetName: _Optional[_Union[_SDKTypes_pb2.NullableString, _Mapping]] = ..., GroupName: _Optional[_Union[_SDKTypes_pb2.NullableString, _Mapping]] = ...) -> None: ...

class GetTagParameters(_message.Message):
    __slots__ = ("TagIdentifier",)
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ...) -> None: ...

class ReadCurrentValueParameters(_message.Message):
    __slots__ = ("TagIdentifiers", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifiers: _SDKTypes_pb2.TagQueryIdentifier
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifiers: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class ReadCurrentValuesParameters(_message.Message):
    __slots__ = ("Parameters",)
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    Parameters: _containers.RepeatedCompositeFieldContainer[ReadCurrentValueParameters]
    def __init__(self, Parameters: _Optional[_Iterable[_Union[ReadCurrentValueParameters, _Mapping]]] = ...) -> None: ...

class ReadRawParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "EndTime", "ReturnStartBounds", "ReturnEndBounds", "DigitalTextReturnType", "DoNotApplyUnitConversion", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    RETURNSTARTBOUNDS_FIELD_NUMBER: _ClassVar[int]
    RETURNENDBOUNDS_FIELD_NUMBER: _ClassVar[int]
    DIGITALTEXTRETURNTYPE_FIELD_NUMBER: _ClassVar[int]
    DONOTAPPLYUNITCONVERSION_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    EndTime: _timestamp_pb2.Timestamp
    ReturnStartBounds: _SDKTypes_pb2.ReturnRawBoundMode
    ReturnEndBounds: _SDKTypes_pb2.ReturnRawBoundMode
    DigitalTextReturnType: _SDKTypes_pb2.DigitalTextReturnType
    DoNotApplyUnitConversion: bool
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., EndTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ReturnStartBounds: _Optional[_Union[_SDKTypes_pb2.ReturnRawBoundMode, str]] = ..., ReturnEndBounds: _Optional[_Union[_SDKTypes_pb2.ReturnRawBoundMode, str]] = ..., DigitalTextReturnType: _Optional[_Union[_SDKTypes_pb2.DigitalTextReturnType, str]] = ..., DoNotApplyUnitConversion: bool = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class StreamRawParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "EndTime", "ReturnStartBounds", "ReturnEndBounds", "DigitalTextReturnType", "DoNotApplyUnitConversion", "ChunkSize", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    RETURNSTARTBOUNDS_FIELD_NUMBER: _ClassVar[int]
    RETURNENDBOUNDS_FIELD_NUMBER: _ClassVar[int]
    DIGITALTEXTRETURNTYPE_FIELD_NUMBER: _ClassVar[int]
    DONOTAPPLYUNITCONVERSION_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    EndTime: _timestamp_pb2.Timestamp
    ReturnStartBounds: _SDKTypes_pb2.ReturnRawBoundMode
    ReturnEndBounds: _SDKTypes_pb2.ReturnRawBoundMode
    DigitalTextReturnType: _SDKTypes_pb2.DigitalTextReturnType
    DoNotApplyUnitConversion: bool
    ChunkSize: int
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., EndTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ReturnStartBounds: _Optional[_Union[_SDKTypes_pb2.ReturnRawBoundMode, str]] = ..., ReturnEndBounds: _Optional[_Union[_SDKTypes_pb2.ReturnRawBoundMode, str]] = ..., DigitalTextReturnType: _Optional[_Union[_SDKTypes_pb2.DigitalTextReturnType, str]] = ..., DoNotApplyUnitConversion: bool = ..., ChunkSize: _Optional[int] = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class DirectionalStreamRawParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "Direction", "NumberOfPoints", "ReturnStartBounds", "DigitalTextReturnType", "DoNotApplyUnitConversion", "ChunkSize", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFPOINTS_FIELD_NUMBER: _ClassVar[int]
    RETURNSTARTBOUNDS_FIELD_NUMBER: _ClassVar[int]
    DIGITALTEXTRETURNTYPE_FIELD_NUMBER: _ClassVar[int]
    DONOTAPPLYUNITCONVERSION_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    Direction: _SDKTypes_pb2.Direction
    NumberOfPoints: int
    ReturnStartBounds: _SDKTypes_pb2.ReturnRawBoundMode
    DigitalTextReturnType: _SDKTypes_pb2.DigitalTextReturnType
    DoNotApplyUnitConversion: bool
    ChunkSize: int
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Direction: _Optional[_Union[_SDKTypes_pb2.Direction, str]] = ..., NumberOfPoints: _Optional[int] = ..., ReturnStartBounds: _Optional[_Union[_SDKTypes_pb2.ReturnRawBoundMode, str]] = ..., DigitalTextReturnType: _Optional[_Union[_SDKTypes_pb2.DigitalTextReturnType, str]] = ..., DoNotApplyUnitConversion: bool = ..., ChunkSize: _Optional[int] = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class ReadProcessedParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "EndTime", "ReturnBounds", "ProcessedSource", "DigitalTextReturnType", "AggregateConfig", "ReturnPartialIntervals", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    RETURNBOUNDS_FIELD_NUMBER: _ClassVar[int]
    PROCESSEDSOURCE_FIELD_NUMBER: _ClassVar[int]
    DIGITALTEXTRETURNTYPE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATECONFIG_FIELD_NUMBER: _ClassVar[int]
    RETURNPARTIALINTERVALS_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    EndTime: _timestamp_pb2.Timestamp
    ReturnBounds: bool
    ProcessedSource: _SDKTypes_pb2.ProcessedSource
    DigitalTextReturnType: _SDKTypes_pb2.DigitalTextReturnType
    AggregateConfig: _SDKTypes_pb2.AggregateConfig
    ReturnPartialIntervals: bool
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., EndTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ReturnBounds: bool = ..., ProcessedSource: _Optional[_Union[_SDKTypes_pb2.ProcessedSource, str]] = ..., DigitalTextReturnType: _Optional[_Union[_SDKTypes_pb2.DigitalTextReturnType, str]] = ..., AggregateConfig: _Optional[_Union[_SDKTypes_pb2.AggregateConfig, _Mapping]] = ..., ReturnPartialIntervals: bool = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class ReadProcessedByConfigParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "EndTime", "ReturnBounds", "AggregateConfigName", "ProcessRaw", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    RETURNBOUNDS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATECONFIGNAME_FIELD_NUMBER: _ClassVar[int]
    PROCESSRAW_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    EndTime: _timestamp_pb2.Timestamp
    ReturnBounds: bool
    AggregateConfigName: str
    ProcessRaw: bool
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., EndTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ReturnBounds: bool = ..., AggregateConfigName: _Optional[str] = ..., ProcessRaw: bool = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class StreamProcessedParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "EndTime", "ReturnBounds", "ProcessedSource", "DigitalTextReturnType", "ReturnPartialIntervals", "AggregateConfig", "ChunkSize", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    RETURNBOUNDS_FIELD_NUMBER: _ClassVar[int]
    PROCESSEDSOURCE_FIELD_NUMBER: _ClassVar[int]
    DIGITALTEXTRETURNTYPE_FIELD_NUMBER: _ClassVar[int]
    RETURNPARTIALINTERVALS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATECONFIG_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    EndTime: _timestamp_pb2.Timestamp
    ReturnBounds: bool
    ProcessedSource: _SDKTypes_pb2.ProcessedSource
    DigitalTextReturnType: _SDKTypes_pb2.DigitalTextReturnType
    ReturnPartialIntervals: bool
    AggregateConfig: _SDKTypes_pb2.AggregateConfig
    ChunkSize: int
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., EndTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ReturnBounds: bool = ..., ProcessedSource: _Optional[_Union[_SDKTypes_pb2.ProcessedSource, str]] = ..., DigitalTextReturnType: _Optional[_Union[_SDKTypes_pb2.DigitalTextReturnType, str]] = ..., ReturnPartialIntervals: bool = ..., AggregateConfig: _Optional[_Union[_SDKTypes_pb2.AggregateConfig, _Mapping]] = ..., ChunkSize: _Optional[int] = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class DirectionalStreamProcessedParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "Direction", "NumberOfPoints", "AggregateConfig", "ReturnBounds", "ReturnPartialIntervals", "ProcessedSource", "DigitalTextReturnType", "ChunkSize", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFPOINTS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATECONFIG_FIELD_NUMBER: _ClassVar[int]
    RETURNBOUNDS_FIELD_NUMBER: _ClassVar[int]
    RETURNPARTIALINTERVALS_FIELD_NUMBER: _ClassVar[int]
    PROCESSEDSOURCE_FIELD_NUMBER: _ClassVar[int]
    DIGITALTEXTRETURNTYPE_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    Direction: _SDKTypes_pb2.Direction
    NumberOfPoints: int
    AggregateConfig: _SDKTypes_pb2.AggregateConfig
    ReturnBounds: bool
    ReturnPartialIntervals: bool
    ProcessedSource: _SDKTypes_pb2.ProcessedSource
    DigitalTextReturnType: _SDKTypes_pb2.DigitalTextReturnType
    ChunkSize: int
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Direction: _Optional[_Union[_SDKTypes_pb2.Direction, str]] = ..., NumberOfPoints: _Optional[int] = ..., AggregateConfig: _Optional[_Union[_SDKTypes_pb2.AggregateConfig, _Mapping]] = ..., ReturnBounds: bool = ..., ReturnPartialIntervals: bool = ..., ProcessedSource: _Optional[_Union[_SDKTypes_pb2.ProcessedSource, str]] = ..., DigitalTextReturnType: _Optional[_Union[_SDKTypes_pb2.DigitalTextReturnType, str]] = ..., ChunkSize: _Optional[int] = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class StreamProcessedByConfigParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "EndTime", "ReturnBounds", "AggregateConfigName", "ProcessRaw", "ChunkSize", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    RETURNBOUNDS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATECONFIGNAME_FIELD_NUMBER: _ClassVar[int]
    PROCESSRAW_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    EndTime: _timestamp_pb2.Timestamp
    ReturnBounds: bool
    AggregateConfigName: str
    ProcessRaw: bool
    ChunkSize: int
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., EndTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ReturnBounds: bool = ..., AggregateConfigName: _Optional[str] = ..., ProcessRaw: bool = ..., ChunkSize: _Optional[int] = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class DirectionalStreamProcessedByConfigParameters(_message.Message):
    __slots__ = ("TagIdentifier", "StartTime", "Direction", "NumberOfPoints", "AggregateConfigName", "ReturnBounds", "ProcessRaw", "ChunkSize", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFPOINTS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATECONFIGNAME_FIELD_NUMBER: _ClassVar[int]
    RETURNBOUNDS_FIELD_NUMBER: _ClassVar[int]
    PROCESSRAW_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    StartTime: _timestamp_pb2.Timestamp
    Direction: _SDKTypes_pb2.Direction
    NumberOfPoints: int
    AggregateConfigName: str
    ReturnBounds: bool
    ProcessRaw: bool
    ChunkSize: int
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., StartTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Direction: _Optional[_Union[_SDKTypes_pb2.Direction, str]] = ..., NumberOfPoints: _Optional[int] = ..., AggregateConfigName: _Optional[str] = ..., ReturnBounds: bool = ..., ProcessRaw: bool = ..., ChunkSize: _Optional[int] = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...

class ReadAtTimeParameters(_message.Message):
    __slots__ = ("TagIdentifier", "Timestamps", "UseSimpleBounds", "ArrayStartIndex", "ArrayLength")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    USESIMPLEBOUNDS_FIELD_NUMBER: _ClassVar[int]
    ARRAYSTARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: _SDKTypes_pb2.TagQueryIdentifier
    Timestamps: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    UseSimpleBounds: bool
    ArrayStartIndex: _SDKTypes_pb2.NullableInt32
    ArrayLength: _SDKTypes_pb2.NullableInt32
    def __init__(self, TagIdentifier: _Optional[_Union[_SDKTypes_pb2.TagQueryIdentifier, _Mapping]] = ..., Timestamps: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ..., UseSimpleBounds: bool = ..., ArrayStartIndex: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ..., ArrayLength: _Optional[_Union[_SDKTypes_pb2.NullableInt32, _Mapping]] = ...) -> None: ...
