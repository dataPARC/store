from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadAtTimeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ReadAtTimeStatus_Successful: _ClassVar[ReadAtTimeStatus]
    ReadAtTimeStatus_NoValueFound: _ClassVar[ReadAtTimeStatus]
    ReadAtTimeStatus_UnknownOrInactiveTag: _ClassVar[ReadAtTimeStatus]
    ReadAtTimeStatus_DuplicateTag: _ClassVar[ReadAtTimeStatus]

class ReadRawStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ReadRawStatus_Successful: _ClassVar[ReadRawStatus]
    ReadRawStatus_NoValueFound: _ClassVar[ReadRawStatus]
    ReadRawStatus_UnknownOrInactiveTag: _ClassVar[ReadRawStatus]
    ReadRawStatus_DuplicateTag: _ClassVar[ReadRawStatus]
    ReadRawStatus_UnexpectedError: _ClassVar[ReadRawStatus]
    ReadRawStatus_InvalidDigitalTextConfiguration: _ClassVar[ReadRawStatus]
    ReadRawStatus_InvalidDateRange: _ClassVar[ReadRawStatus]

class ReadProcessedStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ReadProcessedStatus_Successful: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_NoValueFound: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_UnknownOrInactiveTag: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_DuplicateTag: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_UnexpectedError: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_InvalidDigitalTextConfiguration: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_InvalidParameterValue: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_ReadRawFailed: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_MissingAggregateConfig: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_NotSupported: _ClassVar[ReadProcessedStatus]
    ReadProcessedStatus_InvalidDateRange: _ClassVar[ReadProcessedStatus]

class ReadCountStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ReadCountStatus_Successful: _ClassVar[ReadCountStatus]
    ReadCountStatus_UnknownOrInactiveTag: _ClassVar[ReadCountStatus]
    ReadCountStatus_UnexpectedError: _ClassVar[ReadCountStatus]
    ReadCountStatus_InvalidDateRange: _ClassVar[ReadCountStatus]

class DigitalTextReturnType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DigitalTextReturnType_Numeric: _ClassVar[DigitalTextReturnType]
    DigitalTextReturnType_Text: _ClassVar[DigitalTextReturnType]
    DigitalTextReturnType_DigitalText: _ClassVar[DigitalTextReturnType]
    DigitalTextReturnType_Raw: _ClassVar[DigitalTextReturnType]

class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FileType_Day: _ClassVar[FileType]
    FileType_Month: _ClassVar[FileType]
    FileType_Year: _ClassVar[FileType]

class ResultErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ResultErrorCode_None: _ClassVar[ResultErrorCode]
    ResultErrorCode_NotFound: _ClassVar[ResultErrorCode]
    ResultErrorCode_Exception: _ClassVar[ResultErrorCode]

class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ValueType_None: _ClassVar[ValueType]
    ValueType_Object: _ClassVar[ValueType]
    ValueType_Boolean: _ClassVar[ValueType]
    ValueType_SByte: _ClassVar[ValueType]
    ValueType_Byte: _ClassVar[ValueType]
    ValueType_Int16: _ClassVar[ValueType]
    ValueType_UInt16: _ClassVar[ValueType]
    ValueType_Int32: _ClassVar[ValueType]
    ValueType_UInt32: _ClassVar[ValueType]
    ValueType_Int64: _ClassVar[ValueType]
    ValueType_UInt64: _ClassVar[ValueType]
    ValueType_Single: _ClassVar[ValueType]
    ValueType_Double: _ClassVar[ValueType]
    ValueType_Decimal: _ClassVar[ValueType]
    ValueType_DateTime: _ClassVar[ValueType]
    ValueType_String: _ClassVar[ValueType]

class DrawMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DrawMode_Regular: _ClassVar[DrawMode]
    DrawMode_Square: _ClassVar[DrawMode]
    DrawMode_SquareNoEdge: _ClassVar[DrawMode]
    DrawMode_State: _ClassVar[DrawMode]
    DrawMode_StateNoEdge: _ClassVar[DrawMode]
    DrawMode_Exception: _ClassVar[DrawMode]

class InterpolateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    InterpolateType_State: _ClassVar[InterpolateType]
    InterpolateType_Continuous: _ClassVar[InterpolateType]

class DataStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Successful: _ClassVar[DataStatus]
    PartiallySuccessful: _ClassVar[DataStatus]
    Error: _ClassVar[DataStatus]
    NotQueuedDueToGuidAlreadyExists: _ClassVar[DataStatus]

class ProcessedSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ProcessedSource_SavedAndProcessRaw: _ClassVar[ProcessedSource]
    ProcessedSource_Saved: _ClassVar[ProcessedSource]
    ProcessedSource_ProcessRaw: _ClassVar[ProcessedSource]

class AggregateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AggregateType_PlotReduction: _ClassVar[AggregateType]
    AggregateType_Interpolative: _ClassVar[AggregateType]
    AggregateType_Average: _ClassVar[AggregateType]
    AggregateType_TimeAverage: _ClassVar[AggregateType]
    AggregateType_TimeAverage2: _ClassVar[AggregateType]
    AggregateType_Total: _ClassVar[AggregateType]
    AggregateType_Total2: _ClassVar[AggregateType]
    AggregateType_Minimum: _ClassVar[AggregateType]
    AggregateType_Maximum: _ClassVar[AggregateType]
    AggregateType_MinimumActualTime: _ClassVar[AggregateType]
    AggregateType_MaximumActualTime: _ClassVar[AggregateType]
    AggregateType_Range: _ClassVar[AggregateType]
    AggregateType_Minimum2: _ClassVar[AggregateType]
    AggregateType_Maximum2: _ClassVar[AggregateType]
    AggregateType_MinimumActualTime2: _ClassVar[AggregateType]
    AggregateType_MaximumActualTime2: _ClassVar[AggregateType]
    AggregateType_Range2: _ClassVar[AggregateType]
    AggregateType_Count: _ClassVar[AggregateType]
    AggregateType_AnnotationCount: _ClassVar[AggregateType]
    AggregateType_DurationInStateZero: _ClassVar[AggregateType]
    AggregateType_DurationInStateNonZero: _ClassVar[AggregateType]
    AggregateType_NumberOfTransitions: _ClassVar[AggregateType]
    AggregateType_Start: _ClassVar[AggregateType]
    AggregateType_End: _ClassVar[AggregateType]
    AggregateType_Delta: _ClassVar[AggregateType]
    AggregateType_StartBound: _ClassVar[AggregateType]
    AggregateType_EndBound: _ClassVar[AggregateType]
    AggregateType_DeltaBounds: _ClassVar[AggregateType]
    AggregateType_DurationGood: _ClassVar[AggregateType]
    AggregateType_DurationBad: _ClassVar[AggregateType]
    AggregateType_PercentGood: _ClassVar[AggregateType]
    AggregateType_PercentBad: _ClassVar[AggregateType]
    AggregateType_WorstQuality: _ClassVar[AggregateType]
    AggregateType_WorstQuality2: _ClassVar[AggregateType]
    AggregateType_StandardDeviationPopulation: _ClassVar[AggregateType]
    AggregateType_VariancePopulation: _ClassVar[AggregateType]
    AggregateType_StandardDeviationSample: _ClassVar[AggregateType]
    AggregateType_VarianceSample: _ClassVar[AggregateType]
    AggregateType_NegativePeak: _ClassVar[AggregateType]
    AggregateType_Peak: _ClassVar[AggregateType]

class ReturnRawBoundMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ReturnRawBoundMode_NoBound: _ClassVar[ReturnRawBoundMode]
    ReturnRawBoundMode_AnyQuality: _ClassVar[ReturnRawBoundMode]
    ReturnRawBoundMode_GoodOrUncertainQuality: _ClassVar[ReturnRawBoundMode]
    ReturnRawBoundMode_GoodQuality: _ClassVar[ReturnRawBoundMode]

class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Direction_Forwards: _ClassVar[Direction]
    Direction_Backwards: _ClassVar[Direction]
ReadAtTimeStatus_Successful: ReadAtTimeStatus
ReadAtTimeStatus_NoValueFound: ReadAtTimeStatus
ReadAtTimeStatus_UnknownOrInactiveTag: ReadAtTimeStatus
ReadAtTimeStatus_DuplicateTag: ReadAtTimeStatus
ReadRawStatus_Successful: ReadRawStatus
ReadRawStatus_NoValueFound: ReadRawStatus
ReadRawStatus_UnknownOrInactiveTag: ReadRawStatus
ReadRawStatus_DuplicateTag: ReadRawStatus
ReadRawStatus_UnexpectedError: ReadRawStatus
ReadRawStatus_InvalidDigitalTextConfiguration: ReadRawStatus
ReadRawStatus_InvalidDateRange: ReadRawStatus
ReadProcessedStatus_Successful: ReadProcessedStatus
ReadProcessedStatus_NoValueFound: ReadProcessedStatus
ReadProcessedStatus_UnknownOrInactiveTag: ReadProcessedStatus
ReadProcessedStatus_DuplicateTag: ReadProcessedStatus
ReadProcessedStatus_UnexpectedError: ReadProcessedStatus
ReadProcessedStatus_InvalidDigitalTextConfiguration: ReadProcessedStatus
ReadProcessedStatus_InvalidParameterValue: ReadProcessedStatus
ReadProcessedStatus_ReadRawFailed: ReadProcessedStatus
ReadProcessedStatus_MissingAggregateConfig: ReadProcessedStatus
ReadProcessedStatus_NotSupported: ReadProcessedStatus
ReadProcessedStatus_InvalidDateRange: ReadProcessedStatus
ReadCountStatus_Successful: ReadCountStatus
ReadCountStatus_UnknownOrInactiveTag: ReadCountStatus
ReadCountStatus_UnexpectedError: ReadCountStatus
ReadCountStatus_InvalidDateRange: ReadCountStatus
DigitalTextReturnType_Numeric: DigitalTextReturnType
DigitalTextReturnType_Text: DigitalTextReturnType
DigitalTextReturnType_DigitalText: DigitalTextReturnType
DigitalTextReturnType_Raw: DigitalTextReturnType
FileType_Day: FileType
FileType_Month: FileType
FileType_Year: FileType
ResultErrorCode_None: ResultErrorCode
ResultErrorCode_NotFound: ResultErrorCode
ResultErrorCode_Exception: ResultErrorCode
ValueType_None: ValueType
ValueType_Object: ValueType
ValueType_Boolean: ValueType
ValueType_SByte: ValueType
ValueType_Byte: ValueType
ValueType_Int16: ValueType
ValueType_UInt16: ValueType
ValueType_Int32: ValueType
ValueType_UInt32: ValueType
ValueType_Int64: ValueType
ValueType_UInt64: ValueType
ValueType_Single: ValueType
ValueType_Double: ValueType
ValueType_Decimal: ValueType
ValueType_DateTime: ValueType
ValueType_String: ValueType
DrawMode_Regular: DrawMode
DrawMode_Square: DrawMode
DrawMode_SquareNoEdge: DrawMode
DrawMode_State: DrawMode
DrawMode_StateNoEdge: DrawMode
DrawMode_Exception: DrawMode
InterpolateType_State: InterpolateType
InterpolateType_Continuous: InterpolateType
Successful: DataStatus
PartiallySuccessful: DataStatus
Error: DataStatus
NotQueuedDueToGuidAlreadyExists: DataStatus
ProcessedSource_SavedAndProcessRaw: ProcessedSource
ProcessedSource_Saved: ProcessedSource
ProcessedSource_ProcessRaw: ProcessedSource
AggregateType_PlotReduction: AggregateType
AggregateType_Interpolative: AggregateType
AggregateType_Average: AggregateType
AggregateType_TimeAverage: AggregateType
AggregateType_TimeAverage2: AggregateType
AggregateType_Total: AggregateType
AggregateType_Total2: AggregateType
AggregateType_Minimum: AggregateType
AggregateType_Maximum: AggregateType
AggregateType_MinimumActualTime: AggregateType
AggregateType_MaximumActualTime: AggregateType
AggregateType_Range: AggregateType
AggregateType_Minimum2: AggregateType
AggregateType_Maximum2: AggregateType
AggregateType_MinimumActualTime2: AggregateType
AggregateType_MaximumActualTime2: AggregateType
AggregateType_Range2: AggregateType
AggregateType_Count: AggregateType
AggregateType_AnnotationCount: AggregateType
AggregateType_DurationInStateZero: AggregateType
AggregateType_DurationInStateNonZero: AggregateType
AggregateType_NumberOfTransitions: AggregateType
AggregateType_Start: AggregateType
AggregateType_End: AggregateType
AggregateType_Delta: AggregateType
AggregateType_StartBound: AggregateType
AggregateType_EndBound: AggregateType
AggregateType_DeltaBounds: AggregateType
AggregateType_DurationGood: AggregateType
AggregateType_DurationBad: AggregateType
AggregateType_PercentGood: AggregateType
AggregateType_PercentBad: AggregateType
AggregateType_WorstQuality: AggregateType
AggregateType_WorstQuality2: AggregateType
AggregateType_StandardDeviationPopulation: AggregateType
AggregateType_VariancePopulation: AggregateType
AggregateType_StandardDeviationSample: AggregateType
AggregateType_VarianceSample: AggregateType
AggregateType_NegativePeak: AggregateType
AggregateType_Peak: AggregateType
ReturnRawBoundMode_NoBound: ReturnRawBoundMode
ReturnRawBoundMode_AnyQuality: ReturnRawBoundMode
ReturnRawBoundMode_GoodOrUncertainQuality: ReturnRawBoundMode
ReturnRawBoundMode_GoodQuality: ReturnRawBoundMode
Direction_Forwards: Direction
Direction_Backwards: Direction

class NullableString(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: str
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[str] = ...) -> None: ...

class NullableInt32(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: int
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[int] = ...) -> None: ...

class NullableUInt32(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: int
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[int] = ...) -> None: ...

class NullableBoolean(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: bool
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: bool = ...) -> None: ...

class NullableFloat(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: float
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[float] = ...) -> None: ...

class NullableDouble(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: float
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[float] = ...) -> None: ...

class NullableTimestamp(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: _timestamp_pb2.Timestamp
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NullableInterpolateType(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: InterpolateType
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[_Union[InterpolateType, str]] = ...) -> None: ...

class NullableAggregateConfig(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: AggregateConfig
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[_Union[AggregateConfig, _Mapping]] = ...) -> None: ...

class NullableFullyQualifiedTagName(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: FullyQualifiedTagName
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[_Union[FullyQualifiedTagName, _Mapping]] = ...) -> None: ...

class NullableException(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: Exception
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[_Union[Exception, _Mapping]] = ...) -> None: ...

class DecimalValue(_message.Message):
    __slots__ = ("units", "nanos")
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    units: int
    nanos: int
    def __init__(self, units: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class Quality(_message.Message):
    __slots__ = ("Source", "Historian")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    HISTORIAN_FIELD_NUMBER: _ClassVar[int]
    Source: bytes
    Historian: bytes
    def __init__(self, Source: _Optional[bytes] = ..., Historian: _Optional[bytes] = ...) -> None: ...

class Exception(_message.Message):
    __slots__ = ("Message", "StackTrace", "InnerException")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STACKTRACE_FIELD_NUMBER: _ClassVar[int]
    INNEREXCEPTION_FIELD_NUMBER: _ClassVar[int]
    Message: NullableString
    StackTrace: NullableString
    InnerException: NullableException
    def __init__(self, Message: _Optional[_Union[NullableString, _Mapping]] = ..., StackTrace: _Optional[_Union[NullableString, _Mapping]] = ..., InnerException: _Optional[_Union[NullableException, _Mapping]] = ...) -> None: ...

class TagIdentifier(_message.Message):
    __slots__ = ("FullyQualifiedTagName", "Guid", "Id")
    FULLYQUALIFIEDTAGNAME_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FullyQualifiedTagName: FullyQualifiedTagName
    Guid: str
    Id: int
    def __init__(self, FullyQualifiedTagName: _Optional[_Union[FullyQualifiedTagName, _Mapping]] = ..., Guid: _Optional[str] = ..., Id: _Optional[int] = ...) -> None: ...

class TagQueryIdentifier(_message.Message):
    __slots__ = ("FullyQualifiedTagName", "Guid", "Id")
    FULLYQUALIFIEDTAGNAME_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FullyQualifiedTagName: FullyQualifiedTagName
    Guid: str
    Id: int
    def __init__(self, FullyQualifiedTagName: _Optional[_Union[FullyQualifiedTagName, _Mapping]] = ..., Guid: _Optional[str] = ..., Id: _Optional[int] = ...) -> None: ...

class FullyQualifiedTagName(_message.Message):
    __slots__ = ("InterfaceGroup", "Interface", "InterfaceSet", "Tag")
    INTERFACEGROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    INTERFACESET_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    InterfaceGroup: str
    Interface: NullableString
    InterfaceSet: NullableString
    Tag: str
    def __init__(self, InterfaceGroup: _Optional[str] = ..., Interface: _Optional[_Union[NullableString, _Mapping]] = ..., InterfaceSet: _Optional[_Union[NullableString, _Mapping]] = ..., Tag: _Optional[str] = ...) -> None: ...

class HistorianPathConfigList(_message.Message):
    __slots__ = ("HistorianPathConfigs",)
    HISTORIANPATHCONFIGS_FIELD_NUMBER: _ClassVar[int]
    HistorianPathConfigs: _containers.RepeatedCompositeFieldContainer[HistorianPathConfig]
    def __init__(self, HistorianPathConfigs: _Optional[_Iterable[_Union[HistorianPathConfig, _Mapping]]] = ...) -> None: ...

class HistorianPathConfig(_message.Message):
    __slots__ = ("Id", "Name", "FullPath", "Description", "ModifiedBy", "ModifiedDateTime", "ModifiedComputer", "ModifiedComputerAddress")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULLPATH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDBY_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDDATETIME_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTER_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTERADDRESS_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Name: str
    FullPath: str
    Description: NullableString
    ModifiedBy: str
    ModifiedDateTime: _timestamp_pb2.Timestamp
    ModifiedComputer: str
    ModifiedComputerAddress: str
    def __init__(self, Id: _Optional[int] = ..., Name: _Optional[str] = ..., FullPath: _Optional[str] = ..., Description: _Optional[_Union[NullableString, _Mapping]] = ..., ModifiedBy: _Optional[str] = ..., ModifiedDateTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ModifiedComputer: _Optional[str] = ..., ModifiedComputerAddress: _Optional[str] = ...) -> None: ...

class InterfaceGroupConfigList(_message.Message):
    __slots__ = ("InterfaceGroupConfigs",)
    INTERFACEGROUPCONFIGS_FIELD_NUMBER: _ClassVar[int]
    InterfaceGroupConfigs: _containers.RepeatedCompositeFieldContainer[InterfaceGroupConfig]
    def __init__(self, InterfaceGroupConfigs: _Optional[_Iterable[_Union[InterfaceGroupConfig, _Mapping]]] = ...) -> None: ...

class InterfaceGroupConfig(_message.Message):
    __slots__ = ("Id", "Name", "Guid", "HistorianPathId", "Timezone", "RemoteHost", "RemotePort", "RemoteGroupName", "Active", "ModifiedBy", "ModifiedDateTime", "ModifiedComputer", "ModifiedComputerAddress")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    HISTORIANPATHID_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    REMOTEHOST_FIELD_NUMBER: _ClassVar[int]
    REMOTEPORT_FIELD_NUMBER: _ClassVar[int]
    REMOTEGROUPNAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDBY_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDDATETIME_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTER_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTERADDRESS_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Name: str
    Guid: NullableString
    HistorianPathId: int
    Timezone: NullableString
    RemoteHost: NullableString
    RemotePort: NullableInt32
    RemoteGroupName: NullableString
    Active: bool
    ModifiedBy: str
    ModifiedDateTime: _timestamp_pb2.Timestamp
    ModifiedComputer: str
    ModifiedComputerAddress: str
    def __init__(self, Id: _Optional[int] = ..., Name: _Optional[str] = ..., Guid: _Optional[_Union[NullableString, _Mapping]] = ..., HistorianPathId: _Optional[int] = ..., Timezone: _Optional[_Union[NullableString, _Mapping]] = ..., RemoteHost: _Optional[_Union[NullableString, _Mapping]] = ..., RemotePort: _Optional[_Union[NullableInt32, _Mapping]] = ..., RemoteGroupName: _Optional[_Union[NullableString, _Mapping]] = ..., Active: bool = ..., ModifiedBy: _Optional[str] = ..., ModifiedDateTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ModifiedComputer: _Optional[str] = ..., ModifiedComputerAddress: _Optional[str] = ...) -> None: ...

class InterfaceConfigList(_message.Message):
    __slots__ = ("InterfaceConfigs",)
    INTERFACECONFIGS_FIELD_NUMBER: _ClassVar[int]
    InterfaceConfigs: _containers.RepeatedCompositeFieldContainer[InterfaceConfig]
    def __init__(self, InterfaceConfigs: _Optional[_Iterable[_Union[InterfaceConfig, _Mapping]]] = ...) -> None: ...

class InterfaceConfig(_message.Message):
    __slots__ = ("Id", "GroupId", "GroupName", "Name", "Guid", "OverrideHistorianPathId", "TimeZone", "FileType", "Active", "SendCurrentValues", "ModifiedBy", "ModifiedDateTime", "ModifiedComputer", "ModifiedComputerAddress", "AllowWrites")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDEHISTORIANPATHID_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FILETYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SENDCURRENTVALUES_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDBY_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDDATETIME_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTER_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTERADDRESS_FIELD_NUMBER: _ClassVar[int]
    ALLOWWRITES_FIELD_NUMBER: _ClassVar[int]
    Id: int
    GroupId: int
    GroupName: str
    Name: str
    Guid: NullableString
    OverrideHistorianPathId: NullableInt32
    TimeZone: NullableString
    FileType: FileType
    Active: bool
    SendCurrentValues: bool
    ModifiedBy: str
    ModifiedDateTime: _timestamp_pb2.Timestamp
    ModifiedComputer: str
    ModifiedComputerAddress: str
    AllowWrites: bool
    def __init__(self, Id: _Optional[int] = ..., GroupId: _Optional[int] = ..., GroupName: _Optional[str] = ..., Name: _Optional[str] = ..., Guid: _Optional[_Union[NullableString, _Mapping]] = ..., OverrideHistorianPathId: _Optional[_Union[NullableInt32, _Mapping]] = ..., TimeZone: _Optional[_Union[NullableString, _Mapping]] = ..., FileType: _Optional[_Union[FileType, str]] = ..., Active: bool = ..., SendCurrentValues: bool = ..., ModifiedBy: _Optional[str] = ..., ModifiedDateTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ModifiedComputer: _Optional[str] = ..., ModifiedComputerAddress: _Optional[str] = ..., AllowWrites: bool = ...) -> None: ...

class InterfaceSetConfig(_message.Message):
    __slots__ = ("Id", "Name", "GroupId", "GroupName", "Scope", "Active", "ModifiedBy", "ModifiedDateTime", "ModifiedComputer", "ModifiedComputerAddress")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDBY_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDDATETIME_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTER_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTERADDRESS_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Name: str
    GroupId: int
    GroupName: str
    Scope: int
    Active: bool
    ModifiedBy: str
    ModifiedDateTime: _timestamp_pb2.Timestamp
    ModifiedComputer: str
    ModifiedComputerAddress: str
    def __init__(self, Id: _Optional[int] = ..., Name: _Optional[str] = ..., GroupId: _Optional[int] = ..., GroupName: _Optional[str] = ..., Scope: _Optional[int] = ..., Active: bool = ..., ModifiedBy: _Optional[str] = ..., ModifiedDateTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ModifiedComputer: _Optional[str] = ..., ModifiedComputerAddress: _Optional[str] = ...) -> None: ...

class TagConfig(_message.Message):
    __slots__ = ("Id", "Name", "Guid", "Description", "DataType", "DrawMode", "InterpolateType", "Address", "InterfaceId", "InterfaceName", "Position", "Units", "MaxHistoryInterval", "UpdateInterval", "DeadbandMin", "DeadbandMax", "PlotMin", "PlotMax", "UnitMultiplier", "UnitPreAdd", "UnitPostAdd", "ArrayLength", "Historize", "CalcAggregates", "OpcServerNumber", "OpcServerGroup", "TaglistVisible", "DisplayFormatMask", "AlternativeAddress", "Deviation", "DeviationIsAbsolute", "Parameters", "ClipToDeadbandMin", "ClipToDeadbandMax", "DigitalMapId", "Active", "ModifiedBy", "ModifiedDateTime", "ModifiedComputer", "ModifiedComputerAddress", "AllowWrites", "ReadTagId")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    DRAWMODE_FIELD_NUMBER: _ClassVar[int]
    INTERPOLATETYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERFACEID_FIELD_NUMBER: _ClassVar[int]
    INTERFACENAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    MAXHISTORYINTERVAL_FIELD_NUMBER: _ClassVar[int]
    UPDATEINTERVAL_FIELD_NUMBER: _ClassVar[int]
    DEADBANDMIN_FIELD_NUMBER: _ClassVar[int]
    DEADBANDMAX_FIELD_NUMBER: _ClassVar[int]
    PLOTMIN_FIELD_NUMBER: _ClassVar[int]
    PLOTMAX_FIELD_NUMBER: _ClassVar[int]
    UNITMULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    UNITPREADD_FIELD_NUMBER: _ClassVar[int]
    UNITPOSTADD_FIELD_NUMBER: _ClassVar[int]
    ARRAYLENGTH_FIELD_NUMBER: _ClassVar[int]
    HISTORIZE_FIELD_NUMBER: _ClassVar[int]
    CALCAGGREGATES_FIELD_NUMBER: _ClassVar[int]
    OPCSERVERNUMBER_FIELD_NUMBER: _ClassVar[int]
    OPCSERVERGROUP_FIELD_NUMBER: _ClassVar[int]
    TAGLISTVISIBLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAYFORMATMASK_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVEADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEVIATION_FIELD_NUMBER: _ClassVar[int]
    DEVIATIONISABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CLIPTODEADBANDMIN_FIELD_NUMBER: _ClassVar[int]
    CLIPTODEADBANDMAX_FIELD_NUMBER: _ClassVar[int]
    DIGITALMAPID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDBY_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDDATETIME_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTER_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDCOMPUTERADDRESS_FIELD_NUMBER: _ClassVar[int]
    ALLOWWRITES_FIELD_NUMBER: _ClassVar[int]
    READTAGID_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Name: str
    Guid: NullableString
    Description: NullableString
    DataType: ValueType
    DrawMode: DrawMode
    InterpolateType: InterpolateType
    Address: NullableString
    InterfaceId: int
    InterfaceName: NullableString
    Position: int
    Units: NullableString
    MaxHistoryInterval: int
    UpdateInterval: int
    DeadbandMin: NullableFloat
    DeadbandMax: NullableFloat
    PlotMin: float
    PlotMax: float
    UnitMultiplier: NullableDouble
    UnitPreAdd: NullableDouble
    UnitPostAdd: NullableDouble
    ArrayLength: int
    Historize: bool
    CalcAggregates: bool
    OpcServerNumber: NullableString
    OpcServerGroup: NullableString
    TaglistVisible: bool
    DisplayFormatMask: NullableString
    AlternativeAddress: NullableString
    Deviation: NullableFloat
    DeviationIsAbsolute: bool
    Parameters: NullableString
    ClipToDeadbandMin: bool
    ClipToDeadbandMax: bool
    DigitalMapId: NullableInt32
    Active: bool
    ModifiedBy: str
    ModifiedDateTime: _timestamp_pb2.Timestamp
    ModifiedComputer: str
    ModifiedComputerAddress: str
    AllowWrites: bool
    ReadTagId: NullableInt32
    def __init__(self, Id: _Optional[int] = ..., Name: _Optional[str] = ..., Guid: _Optional[_Union[NullableString, _Mapping]] = ..., Description: _Optional[_Union[NullableString, _Mapping]] = ..., DataType: _Optional[_Union[ValueType, str]] = ..., DrawMode: _Optional[_Union[DrawMode, str]] = ..., InterpolateType: _Optional[_Union[InterpolateType, str]] = ..., Address: _Optional[_Union[NullableString, _Mapping]] = ..., InterfaceId: _Optional[int] = ..., InterfaceName: _Optional[_Union[NullableString, _Mapping]] = ..., Position: _Optional[int] = ..., Units: _Optional[_Union[NullableString, _Mapping]] = ..., MaxHistoryInterval: _Optional[int] = ..., UpdateInterval: _Optional[int] = ..., DeadbandMin: _Optional[_Union[NullableFloat, _Mapping]] = ..., DeadbandMax: _Optional[_Union[NullableFloat, _Mapping]] = ..., PlotMin: _Optional[float] = ..., PlotMax: _Optional[float] = ..., UnitMultiplier: _Optional[_Union[NullableDouble, _Mapping]] = ..., UnitPreAdd: _Optional[_Union[NullableDouble, _Mapping]] = ..., UnitPostAdd: _Optional[_Union[NullableDouble, _Mapping]] = ..., ArrayLength: _Optional[int] = ..., Historize: bool = ..., CalcAggregates: bool = ..., OpcServerNumber: _Optional[_Union[NullableString, _Mapping]] = ..., OpcServerGroup: _Optional[_Union[NullableString, _Mapping]] = ..., TaglistVisible: bool = ..., DisplayFormatMask: _Optional[_Union[NullableString, _Mapping]] = ..., AlternativeAddress: _Optional[_Union[NullableString, _Mapping]] = ..., Deviation: _Optional[_Union[NullableFloat, _Mapping]] = ..., DeviationIsAbsolute: bool = ..., Parameters: _Optional[_Union[NullableString, _Mapping]] = ..., ClipToDeadbandMin: bool = ..., ClipToDeadbandMax: bool = ..., DigitalMapId: _Optional[_Union[NullableInt32, _Mapping]] = ..., Active: bool = ..., ModifiedBy: _Optional[str] = ..., ModifiedDateTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ModifiedComputer: _Optional[str] = ..., ModifiedComputerAddress: _Optional[str] = ..., AllowWrites: bool = ..., ReadTagId: _Optional[_Union[NullableInt32, _Mapping]] = ...) -> None: ...

class DigtalTextValue(_message.Message):
    __slots__ = ("Text", "Numeric")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FIELD_NUMBER: _ClassVar[int]
    Text: str
    Numeric: int
    def __init__(self, Text: _Optional[str] = ..., Numeric: _Optional[int] = ...) -> None: ...

class TagDataToHistorize(_message.Message):
    __slots__ = ("TagIdentifier", "DataPoint", "WriteToHistory", "TrackingGuid")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATAPOINT_FIELD_NUMBER: _ClassVar[int]
    WRITETOHISTORY_FIELD_NUMBER: _ClassVar[int]
    TRACKINGGUID_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagQueryIdentifier
    DataPoint: DataPoint
    WriteToHistory: bool
    TrackingGuid: NullableString
    def __init__(self, TagIdentifier: _Optional[_Union[TagQueryIdentifier, _Mapping]] = ..., DataPoint: _Optional[_Union[DataPoint, _Mapping]] = ..., WriteToHistory: bool = ..., TrackingGuid: _Optional[_Union[NullableString, _Mapping]] = ...) -> None: ...

class TagDataToHistorizeList(_message.Message):
    __slots__ = ("Values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    Values: _containers.RepeatedCompositeFieldContainer[TagDataToHistorize]
    def __init__(self, Values: _Optional[_Iterable[_Union[TagDataToHistorize, _Mapping]]] = ...) -> None: ...

class ReadInterfaceResult(_message.Message):
    __slots__ = ("HasError", "ErrorCode", "Exception", "Value")
    HASERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HasError: bool
    ErrorCode: ResultErrorCode
    Exception: NullableException
    Value: InterfaceConfig
    def __init__(self, HasError: bool = ..., ErrorCode: _Optional[_Union[ResultErrorCode, str]] = ..., Exception: _Optional[_Union[NullableException, _Mapping]] = ..., Value: _Optional[_Union[InterfaceConfig, _Mapping]] = ...) -> None: ...

class ReadInterfaceSetListResult(_message.Message):
    __slots__ = ("HasError", "ErrorCode", "Exception", "Values")
    HASERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    HasError: bool
    ErrorCode: ResultErrorCode
    Exception: NullableException
    Values: _containers.RepeatedCompositeFieldContainer[InterfaceSetConfig]
    def __init__(self, HasError: bool = ..., ErrorCode: _Optional[_Union[ResultErrorCode, str]] = ..., Exception: _Optional[_Union[NullableException, _Mapping]] = ..., Values: _Optional[_Iterable[_Union[InterfaceSetConfig, _Mapping]]] = ...) -> None: ...

class ReadInterfaceSetResult(_message.Message):
    __slots__ = ("HasError", "ErrorCode", "Exception", "Value")
    HASERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HasError: bool
    ErrorCode: ResultErrorCode
    Exception: NullableException
    Value: InterfaceSetConfig
    def __init__(self, HasError: bool = ..., ErrorCode: _Optional[_Union[ResultErrorCode, str]] = ..., Exception: _Optional[_Union[NullableException, _Mapping]] = ..., Value: _Optional[_Union[InterfaceSetConfig, _Mapping]] = ...) -> None: ...

class ReadTagResult(_message.Message):
    __slots__ = ("HasError", "ErrorCode", "Exception", "Value")
    HASERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HasError: bool
    ErrorCode: ResultErrorCode
    Exception: NullableException
    Value: TagConfig
    def __init__(self, HasError: bool = ..., ErrorCode: _Optional[_Union[ResultErrorCode, str]] = ..., Exception: _Optional[_Union[NullableException, _Mapping]] = ..., Value: _Optional[_Union[TagConfig, _Mapping]] = ...) -> None: ...

class ReadTagListResult(_message.Message):
    __slots__ = ("HasError", "ErrorCode", "Exception", "Value")
    HASERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HasError: bool
    ErrorCode: ResultErrorCode
    Exception: NullableException
    Value: _containers.RepeatedCompositeFieldContainer[TagConfig]
    def __init__(self, HasError: bool = ..., ErrorCode: _Optional[_Union[ResultErrorCode, str]] = ..., Exception: _Optional[_Union[NullableException, _Mapping]] = ..., Value: _Optional[_Iterable[_Union[TagConfig, _Mapping]]] = ...) -> None: ...

class TagCurrentValue(_message.Message):
    __slots__ = ("TagIdentifier", "Data", "WriteToHistory")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    WRITETOHISTORY_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagIdentifier
    Data: DataPoint
    WriteToHistory: bool
    def __init__(self, TagIdentifier: _Optional[_Union[TagIdentifier, _Mapping]] = ..., Data: _Optional[_Union[DataPoint, _Mapping]] = ..., WriteToHistory: bool = ...) -> None: ...

class TagCurrentValues(_message.Message):
    __slots__ = ("Values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    Values: _containers.RepeatedCompositeFieldContainer[TagCurrentValue]
    def __init__(self, Values: _Optional[_Iterable[_Union[TagCurrentValue, _Mapping]]] = ...) -> None: ...

class DataPointCollection(_message.Message):
    __slots__ = ("DataPointsDouble", "DataPointsFloat", "DataPointsInt", "DataPointsUInt", "DataPointsLong", "DataPointsULong", "DataPointsDecimal", "DataPointsShort", "DataPointsUShort", "DataPointsBool", "DataPointsByte", "DataPointsSByte", "DataPointsString", "DataPointsDateTime", "DataPointsDigitalText")
    DATAPOINTSDOUBLE_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSFLOAT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSINT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSUINT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSLONG_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSULONG_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSDECIMAL_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSSHORT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSUSHORT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSBOOL_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSBYTE_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSSBYTE_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSSTRING_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSDATETIME_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSDIGITALTEXT_FIELD_NUMBER: _ClassVar[int]
    DataPointsDouble: DataPointsDouble
    DataPointsFloat: DataPointsFloat
    DataPointsInt: DataPointsInt
    DataPointsUInt: DataPointsUInt
    DataPointsLong: DataPointsLong
    DataPointsULong: DataPointsULong
    DataPointsDecimal: DataPointsDecimal
    DataPointsShort: DataPointsShort
    DataPointsUShort: DataPointsUShort
    DataPointsBool: DataPointsBool
    DataPointsByte: DataPointsByte
    DataPointsSByte: DataPointsSByte
    DataPointsString: DataPointsString
    DataPointsDateTime: DataPointsDateTime
    DataPointsDigitalText: DataPointsDigitalText
    def __init__(self, DataPointsDouble: _Optional[_Union[DataPointsDouble, _Mapping]] = ..., DataPointsFloat: _Optional[_Union[DataPointsFloat, _Mapping]] = ..., DataPointsInt: _Optional[_Union[DataPointsInt, _Mapping]] = ..., DataPointsUInt: _Optional[_Union[DataPointsUInt, _Mapping]] = ..., DataPointsLong: _Optional[_Union[DataPointsLong, _Mapping]] = ..., DataPointsULong: _Optional[_Union[DataPointsULong, _Mapping]] = ..., DataPointsDecimal: _Optional[_Union[DataPointsDecimal, _Mapping]] = ..., DataPointsShort: _Optional[_Union[DataPointsShort, _Mapping]] = ..., DataPointsUShort: _Optional[_Union[DataPointsUShort, _Mapping]] = ..., DataPointsBool: _Optional[_Union[DataPointsBool, _Mapping]] = ..., DataPointsByte: _Optional[_Union[DataPointsByte, _Mapping]] = ..., DataPointsSByte: _Optional[_Union[DataPointsSByte, _Mapping]] = ..., DataPointsString: _Optional[_Union[DataPointsString, _Mapping]] = ..., DataPointsDateTime: _Optional[_Union[DataPointsDateTime, _Mapping]] = ..., DataPointsDigitalText: _Optional[_Union[DataPointsDigitalText, _Mapping]] = ...) -> None: ...

class DataPoint(_message.Message):
    __slots__ = ("DataPointDouble", "DataPointFloat", "DataPointInt", "DataPointUInt", "DataPointLong", "DataPointULong", "DataPointDecimal", "DataPointShort", "DataPointUShort", "DataPointBool", "DataPointByte", "DataPointSByte", "DataPointString", "DataPointDateTime", "DataPointDigitalText")
    DATAPOINTDOUBLE_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTFLOAT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTINT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTUINT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTLONG_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTULONG_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTDECIMAL_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSHORT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTUSHORT_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTBOOL_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTBYTE_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSBYTE_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTSTRING_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTDATETIME_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTDIGITALTEXT_FIELD_NUMBER: _ClassVar[int]
    DataPointDouble: DataPointDouble
    DataPointFloat: DataPointFloat
    DataPointInt: DataPointInt
    DataPointUInt: DataPointUInt
    DataPointLong: DataPointLong
    DataPointULong: DataPointULong
    DataPointDecimal: DataPointDecimal
    DataPointShort: DataPointShort
    DataPointUShort: DataPointUShort
    DataPointBool: DataPointBool
    DataPointByte: DataPointByte
    DataPointSByte: DataPointSByte
    DataPointString: DataPointString
    DataPointDateTime: DataPointDateTime
    DataPointDigitalText: DataPointDigitalText
    def __init__(self, DataPointDouble: _Optional[_Union[DataPointDouble, _Mapping]] = ..., DataPointFloat: _Optional[_Union[DataPointFloat, _Mapping]] = ..., DataPointInt: _Optional[_Union[DataPointInt, _Mapping]] = ..., DataPointUInt: _Optional[_Union[DataPointUInt, _Mapping]] = ..., DataPointLong: _Optional[_Union[DataPointLong, _Mapping]] = ..., DataPointULong: _Optional[_Union[DataPointULong, _Mapping]] = ..., DataPointDecimal: _Optional[_Union[DataPointDecimal, _Mapping]] = ..., DataPointShort: _Optional[_Union[DataPointShort, _Mapping]] = ..., DataPointUShort: _Optional[_Union[DataPointUShort, _Mapping]] = ..., DataPointBool: _Optional[_Union[DataPointBool, _Mapping]] = ..., DataPointByte: _Optional[_Union[DataPointByte, _Mapping]] = ..., DataPointSByte: _Optional[_Union[DataPointSByte, _Mapping]] = ..., DataPointString: _Optional[_Union[DataPointString, _Mapping]] = ..., DataPointDateTime: _Optional[_Union[DataPointDateTime, _Mapping]] = ..., DataPointDigitalText: _Optional[_Union[DataPointDigitalText, _Mapping]] = ...) -> None: ...

class ReadRawResult(_message.Message):
    __slots__ = ("TagIdentifier", "DataPointCollection", "Status", "MaxDatapointsReached")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTCOLLECTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAXDATAPOINTSREACHED_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagIdentifier
    DataPointCollection: DataPointCollection
    Status: ReadRawStatus
    MaxDatapointsReached: bool
    def __init__(self, TagIdentifier: _Optional[_Union[TagIdentifier, _Mapping]] = ..., DataPointCollection: _Optional[_Union[DataPointCollection, _Mapping]] = ..., Status: _Optional[_Union[ReadRawStatus, str]] = ..., MaxDatapointsReached: bool = ...) -> None: ...

class StreamRawMessage(_message.Message):
    __slots__ = ("Header", "DataPoints")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    Header: StreamRawHeader
    DataPoints: DataPointCollection
    def __init__(self, Header: _Optional[_Union[StreamRawHeader, _Mapping]] = ..., DataPoints: _Optional[_Union[DataPointCollection, _Mapping]] = ...) -> None: ...

class StreamRawHeader(_message.Message):
    __slots__ = ("TagIdentifier", "Status")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagIdentifier
    Status: ReadRawStatus
    def __init__(self, TagIdentifier: _Optional[_Union[TagIdentifier, _Mapping]] = ..., Status: _Optional[_Union[ReadRawStatus, str]] = ...) -> None: ...

class StreamProcessedMessage(_message.Message):
    __slots__ = ("Header", "DataPoints")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    Header: StreamProcessedHeader
    DataPoints: DataPointCollection
    def __init__(self, Header: _Optional[_Union[StreamProcessedHeader, _Mapping]] = ..., DataPoints: _Optional[_Union[DataPointCollection, _Mapping]] = ...) -> None: ...

class StreamProcessedHeader(_message.Message):
    __slots__ = ("TagIdentifier", "Status")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagIdentifier
    Status: ReadProcessedStatus
    def __init__(self, TagIdentifier: _Optional[_Union[TagIdentifier, _Mapping]] = ..., Status: _Optional[_Union[ReadProcessedStatus, str]] = ...) -> None: ...

class ReadCountResult(_message.Message):
    __slots__ = ("TagIdentifier", "Count", "Status")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagIdentifier
    Count: int
    Status: ReadCountStatus
    def __init__(self, TagIdentifier: _Optional[_Union[TagIdentifier, _Mapping]] = ..., Count: _Optional[int] = ..., Status: _Optional[_Union[ReadCountStatus, str]] = ...) -> None: ...

class ReadAtTimeResult(_message.Message):
    __slots__ = ("TagIdentifier", "DataPointCollection", "Status")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTCOLLECTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagIdentifier
    DataPointCollection: DataPointCollection
    Status: ReadAtTimeStatus
    def __init__(self, TagIdentifier: _Optional[_Union[TagIdentifier, _Mapping]] = ..., DataPointCollection: _Optional[_Union[DataPointCollection, _Mapping]] = ..., Status: _Optional[_Union[ReadAtTimeStatus, str]] = ...) -> None: ...

class ReadProcessedResult(_message.Message):
    __slots__ = ("TagIdentifier", "DataPointCollection", "Status", "MaxDatapointsReached", "AggregateConfig")
    TAGIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTCOLLECTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAXDATAPOINTSREACHED_FIELD_NUMBER: _ClassVar[int]
    AGGREGATECONFIG_FIELD_NUMBER: _ClassVar[int]
    TagIdentifier: TagIdentifier
    DataPointCollection: DataPointCollection
    Status: ReadProcessedStatus
    MaxDatapointsReached: bool
    AggregateConfig: NullableAggregateConfig
    def __init__(self, TagIdentifier: _Optional[_Union[TagIdentifier, _Mapping]] = ..., DataPointCollection: _Optional[_Union[DataPointCollection, _Mapping]] = ..., Status: _Optional[_Union[ReadProcessedStatus, str]] = ..., MaxDatapointsReached: bool = ..., AggregateConfig: _Optional[_Union[NullableAggregateConfig, _Mapping]] = ...) -> None: ...

class DataPointsDouble(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointDouble]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointDouble, _Mapping]]] = ...) -> None: ...

class DataPointsFloat(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointFloat]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointFloat, _Mapping]]] = ...) -> None: ...

class DataPointsInt(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointInt]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointInt, _Mapping]]] = ...) -> None: ...

class DataPointsUInt(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointUInt]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointUInt, _Mapping]]] = ...) -> None: ...

class DataPointsLong(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointLong]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointLong, _Mapping]]] = ...) -> None: ...

class DataPointsULong(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointULong]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointULong, _Mapping]]] = ...) -> None: ...

class DataPointsDecimal(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointDecimal]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointDecimal, _Mapping]]] = ...) -> None: ...

class DataPointsShort(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointShort]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointShort, _Mapping]]] = ...) -> None: ...

class DataPointsUShort(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointUShort]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointUShort, _Mapping]]] = ...) -> None: ...

class DataPointsBool(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointBool]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointBool, _Mapping]]] = ...) -> None: ...

class DataPointsByte(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointByte]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointByte, _Mapping]]] = ...) -> None: ...

class DataPointsSByte(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointSByte]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointSByte, _Mapping]]] = ...) -> None: ...

class DataPointsString(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointString]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointString, _Mapping]]] = ...) -> None: ...

class DataPointsDateTime(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointDateTime]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointDateTime, _Mapping]]] = ...) -> None: ...

class DataPointsDigitalText(_message.Message):
    __slots__ = ("DataPoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    DataPoints: _containers.RepeatedCompositeFieldContainer[DataPointDigitalText]
    def __init__(self, DataPoints: _Optional[_Iterable[_Union[DataPointDigitalText, _Mapping]]] = ...) -> None: ...

class DataPointDouble(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[float]] = ...) -> None: ...

class DataPointFloat(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[float]] = ...) -> None: ...

class DataPointInt(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[int]] = ...) -> None: ...

class DataPointUInt(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[int]] = ...) -> None: ...

class DataPointLong(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[int]] = ...) -> None: ...

class DataPointULong(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[int]] = ...) -> None: ...

class DataPointDecimal(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedCompositeFieldContainer[DecimalValue]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[_Union[DecimalValue, _Mapping]]] = ...) -> None: ...

class DataPointShort(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[int]] = ...) -> None: ...

class DataPointUShort(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[int]] = ...) -> None: ...

class DataPointBool(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[bool]] = ...) -> None: ...

class DataPointByte(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[bytes]] = ...) -> None: ...

class DataPointSByte(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[bytes]] = ...) -> None: ...

class DataPointString(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedCompositeFieldContainer[NullableString]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[_Union[NullableString, _Mapping]]] = ...) -> None: ...

class DataPointDateTime(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class DataPointDigitalText(_message.Message):
    __slots__ = ("Timestamp", "Quality", "Value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Timestamp: _timestamp_pb2.Timestamp
    Quality: Quality
    Value: _containers.RepeatedCompositeFieldContainer[DigtalTextValue]
    def __init__(self, Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Quality: _Optional[_Union[Quality, _Mapping]] = ..., Value: _Optional[_Iterable[_Union[DigtalTextValue, _Mapping]]] = ...) -> None: ...

class AggregateConfig(_message.Message):
    __slots__ = ("AggregateType", "ProcessingInterval", "AlignmentOrigin", "InterpolateType", "TreatUncertainAsBad", "UseUtcTimeForInterval")
    AGGREGATETYPE_FIELD_NUMBER: _ClassVar[int]
    PROCESSINGINTERVAL_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENTORIGIN_FIELD_NUMBER: _ClassVar[int]
    INTERPOLATETYPE_FIELD_NUMBER: _ClassVar[int]
    TREATUNCERTAINASBAD_FIELD_NUMBER: _ClassVar[int]
    USEUTCTIMEFORINTERVAL_FIELD_NUMBER: _ClassVar[int]
    AggregateType: AggregateType
    ProcessingInterval: _duration_pb2.Duration
    AlignmentOrigin: _timestamp_pb2.Timestamp
    InterpolateType: NullableInterpolateType
    TreatUncertainAsBad: bool
    UseUtcTimeForInterval: bool
    def __init__(self, AggregateType: _Optional[_Union[AggregateType, str]] = ..., ProcessingInterval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., AlignmentOrigin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., InterpolateType: _Optional[_Union[NullableInterpolateType, _Mapping]] = ..., TreatUncertainAsBad: bool = ..., UseUtcTimeForInterval: bool = ...) -> None: ...

class HealthReportResult(_message.Message):
    __slots__ = ("HistorianInstanceId", "Timestamp", "HealthStatResults", "HealthCheckResults")
    HISTORIANINSTANCEID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HEALTHSTATRESULTS_FIELD_NUMBER: _ClassVar[int]
    HEALTHCHECKRESULTS_FIELD_NUMBER: _ClassVar[int]
    HistorianInstanceId: str
    Timestamp: _timestamp_pb2.Timestamp
    HealthStatResults: str
    HealthCheckResults: str
    def __init__(self, HistorianInstanceId: _Optional[str] = ..., Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., HealthStatResults: _Optional[str] = ..., HealthCheckResults: _Optional[str] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("Status", "NumPointsReceived", "NumCurrValuePoints", "NumFailedPoints", "ExceptionMessages")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUMPOINTSRECEIVED_FIELD_NUMBER: _ClassVar[int]
    NUMCURRVALUEPOINTS_FIELD_NUMBER: _ClassVar[int]
    NUMFAILEDPOINTS_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONMESSAGES_FIELD_NUMBER: _ClassVar[int]
    Status: DataStatus
    NumPointsReceived: int
    NumCurrValuePoints: int
    NumFailedPoints: int
    ExceptionMessages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, Status: _Optional[_Union[DataStatus, str]] = ..., NumPointsReceived: _Optional[int] = ..., NumCurrValuePoints: _Optional[int] = ..., NumFailedPoints: _Optional[int] = ..., ExceptionMessages: _Optional[_Iterable[str]] = ...) -> None: ...
