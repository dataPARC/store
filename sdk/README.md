# dataPARC.Store SDK 

A .NET library for creating clients for the dataPARC.Store historian

## Documentation

See the [docs](https://dataparc.github.io/store/sdk/docs/v2.14.0/) for full API reference.

## Prerequisites

Access to a nuget feed containing the dataPARC packages distributed with dataPARC.Store. To add a feed to a project, add the following nuget.config

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="dataparc" value="[path to nuget feed]" />
  </packageSources>
</configuration>
```

With the feed configured, add a nuget reference to dataPARC.Store.SDK

`dotnet add package dataPARC.Store.SDK`

## Examples

- [Clients](#clients)
- [Failover](#failover)
- [Authorization](#authorization)
- [Connections](#connections)
- [Historian Paths](#historian-paths)
- [Interface Groups](#interface-groups)
- [Interfaces](#interfaces)
- [Interface Sets](#interface-sets)
- [Tags](#tags)
- [Writing Data](#writing-data)
- [Deleting Data](#deleting-data)
- [Reading Current Values](#reading-current-values)
- [Reading Raw Data](#reading-raw-data)
- [Reading Processed Data](#reading-processed-data)
- [Reading Processed Data By Config](#reading-processed-data-by-config)
- [Reading Array Data](#reading-array-data)
- [Using DataPoints From Read Responses](#using-datapoints-from-read-responses)
- [Tag Publishing](#tag-publishing)

### Clients

```cs
// Create clients that have methods for calling historian functions. There are 4 client classes: ReadClient, WriteClient, ConfigurationClient, and PublishingClient. Each client can be created separately, or by using the ClientFactory.

// Create a ReadClient with a hostname, port number, and a certificate validator.
string host = "hostname";
int port = 12340;

await using var readClient = new ReadClient(host, port, CertificateValidation.AcceptAllCertificates);

// Create a WriteClient with a path to a local unix socket.
await using var writeClient = new WriteClient(host, port, CertificateValidation.AcceptAllCertificates);

// Create a ClientFactory instead of creating multiple clients at once. This takes the same args required to create clients. Then any of the available clients can be accessed as properties that lazily create the clients.
await using var clientFactory = new ClientFactory(host, port, CertificateValidation.AcceptAllCertificates);

// No need for using contexts when referencing these clients since the client factory owns them and is itself being used in a using context.
var readClient2 = clientFactory.ReadClient;
var writeClient2 = clientFactory.WriteClient;
var configClient = clientFactory.ConfigurationClient;
var pubClient = clientFactory.PublishingClient;

// Subsequent references to the ClientFactory's client properties will return the same instance.
var isSame = readClient2 == clientFactory.ReadClient; // isSame = true
```

### Failover

```cs
// Reading calls support failover to backup servers if the primary server becomes unavailable. The primary server is the first server specified in the array of servers. Reading calls include reading configurations, data, and publishing. Read calls will automatically try again on a backup server. Upon switching to a backup server, the client will wait about 3 minutes before trying to reconnect to the primary server. As many backup servers as needed can be added.

var servers = new[]
{
    ("hostname1", port), // <-- Primary server
    ("hostname2", port),
    ("hostname3", port),
}

await using var client = new ReadClient(servers, CertificateValidation.AcceptAllCertificates, avgFailoverMinutes: 3);
```

### Authorization

```cs
// When creating clients, you are required to pass in an ICertificateValidation that is used to validate the server's certificate. This can be a custom validator as long as it implements ICertificateValidation.
ICertificateValidation certVal = CertificateValidation.DefaultHttpClientHandlerValidator;
await using var readClient = new ReadClient(hostname, port, certVal);

// The other auth related parameter the clients have is an optional IAuthProvider that is used to get access tokens from a token provider. This can also be a custom provider as long as it implements IAuthProvider. This is optional since a historian might have security turned off, but is required to talk to secured historians.
var token = AuthProviderFactory.StartDeviceCodeFlow("authority", "client_id", "scope", res =>
{
    // Pass info from res to user/caller to run device code flow.
}
IAuthProvider provider = AuthProviderFactory.CreateInMemoryTokenProvider(token);
await using var writeClient = new WriteClient(hostname, port, certVal, provider);
```

### Connections

```cs
// The reading, writing, and configuration clients have a CheckConnectionAsync method that acts like a ping by trying to connect to a historian server.
await using var configClient = new ConfigurationClient(hostname, port, CertificateValidation.AcceptAllCertificates);
var connected = await configClient.CheckConnectionAsync();

// The publishing client instead has a Publishing property that indicates if tag publishing has been started. For long running operations such as tag publishing, connections might become transient in changing network conditions, but the publishing client will recover and continue working.
await using var pubClient = new PublishingClient(hostname, port, CertificateValidation.AcceptAllCertificates);
var started = pubClient.Publishing;
```

### Historian Paths

```cs
// Historian paths are a path to a location for the historian to store data, i.e. directory path, network path. etc.

// Save a new historian path.
var newPath = new HistorianPathConfig("Path1", @"C:\History") {
    Description = "The primary path for recent data",
};

await using var client = new ConfigurationClient(hostname, port, CertificateValidation.AcceptAllCertificates);

var saveRes = await client.SaveHistorianPathAsync(newPath);

// When saving configs, the saved configs are returned wrapped in a SaveResult<T>. This provides a status for the save operation, the saved values, and more.
if (saveRes.Status == SaveResultStatus.DataSaved) {
    var savedPath = saveRes.SavedValue; // Historian path saved successfully.
    var pathId = savedPath.Id; // Ids are assigned by the server upon successfully saving configs.
} else {
    // Something went wrong, check against other SaveResultStatus cases for more info. Warnings and errors that may occur when saving configs are included in the SaveResult.
}

// Read all historian paths.
var readRes = await client.GetHistorianPathsAsync();

// When reading configs, the configs are returned wrapped in a GetResult<T>. This provides a status for the read operation, the values read if successful, and more.
if (readRes.Status == GetResultStatus.Successful) {
    var paths = readRes.Value; // All historian paths read successfully.
} else {
    // Something went wrong, check against other GetResultStatus cases for more info.
}
```

### Interface Groups

```cs
// Interface groups are the top level entity in the historian. All interfaces, interface sets, and tags must belong to
// an interface group.

// Save a new interface group. A group must be tied to a historian path to use as it's default path to store data, so we need
// a historian path Id.
await using var client = new ConfigurationClient(hostname, port, CertificateValidation.AcceptAllCertificates);
var pathsRes = await client.GetHistorianPathsAsync();

// Assuming pathsRes.Status == GetResultStatus.Successful... See HistorianPaths for more on GetResults and SaveResults.
var pathId = pathsRes.Value[0].Id;

var newGroup = new InterfaceGroupConfig("Group1", pathId, TimeZoneInfo.Local.StandardName);
var saveRes1 = await client.SaveInterfaceGroupAsync(newGroup);

// Save multiple interface groups. For example only, saving the same group already saved above will fail.
List<InterfaceGroupConfig> newGroups = [newGroup];
var saveRes2 = await client.SaveInterfaceGroupsAsync(newGroups);

// Read a single interface group.
var groupQuery = new InterfaceGroupQueryIdentifier(id: 1); // You can also query groups by name or by GUID.
var readRes1 = await client.GetInterfaceGroupAsync(groupQuery);

// Read all interface groups.
var readRes2 = await client.GetInterfaceGroupsAsync();
```

### Interfaces

```cs
// Interfaces are a grouping of tags. Every tag must belong to one interface.

// Save a new interface. An interface must be tied to an interface group, so we need an interface group Id.
await using var client = new ConfigurationClient(hostname, port, CertificateValidation.AcceptAllCertificates);
var groupsRes = await client.GetInterfaceGroupsAsync();

// Assuming groupsRes.Status == GetResultStatus.Successful... See HistorianPaths for more on GetResults and SaveResults.
var groupId = groupsRes.Value[0].Id;

var newInterface = new InterfaceConfig("Interface1", groupId);
var saveRes1 = await client.SaveInterfaceAsync(newInterface);

// Save multiple interfaces. For example only, saving the same interface saved above will fail.
List<InterfaceConfig> newInterfaces = [newInterface];
var saveRes2 = await client.SaveInterfacesAsync(newInterfaces);

// Read a single interface.
var interfaceQuery = new InterfaceQueryIdentifier(id: 1); // You can also query interfaces by fully qualified name or by GUID.
var readRes1 = await client.GetInterfaceAsync(interfaceQuery);

// Read all interfaces in an interface group.
var groupQuery = new InterfaceGroupQueryIdentifier(id: 1); // You can also query groups by name or by GUID.
var readRes2 = await client.GetInterfacesByInterfaceGroupAsync(groupQuery);

// Read all interfaces in all interface groups.
var readRes3 = await client.GetInterfacesAsync();
```

### Interface Sets

```cs
// Interface sets are a grouping of interfaces within the same interface group.

// Save a new interface set. An interface set must be tied to an interface group, so we need an interface group Id.
await using var client = new ConfigurationClient(hostname, port, CertificateValidation.AcceptAllCertificates);
var groupsRes = await client.GetInterfaceGroupsAsync();

// Assuming groupsRes.Status == GetResultStatus.Successful... See HistorianPaths for more on GetResults and SaveResults.
var groupId = groupsRes.Value[0].Id;

var newInterfaceSet = new InterfaceSetConfig("Set1", groupId);
var saveRes1 = await client.SaveInterfaceSetAsync(newInterfaceSet);
var interfaceSet = saveRes1.SavedValue;

// We can then add interfaces to the interface set. We need to get the interfaces for this interface group. Some or all
// interfaces in the same interface group can be added to an interface set. One interface group can have multiple
// interface sets but each interface can only belong to one interface set.
var interfacesRes = await client.GetInterfacesByInterfaceGroupAsync(new InterfaceGroupQueryIdentifier(groupId));
var interfaces = interfacesRes.Value;
var setInterfaces = interfaces.Select(i => new InterfaceSetInterfaceConfig(i.Id, interfaceSet.Id)).ToList();

// Save the interfaces to the interface set.
var saveRes2 = await client.SaveInterfaceSetInterfacesAsync(setInterfaces);

// Save multiple interface sets. For example only, saving the same interface set saved above will fail.
List<InterfaceSetConfig> newInterfaceSets = [newInterfaceSet];
var saveRes3 = await client.SaveInterfaceSetsAsync(newInterfaceSets);

// Read a single interface set.
var interfaceSetQuery = new InterfaceSetQueryIdentifier(id: 1); // You can also query interfaces sets by fully qualified name or by GUID.
var readRes1 = await client.GetInterfaceSetAsync(interfaceSetQuery);

// Read all interface sets in an interface group.
var groupQuery = new InterfaceGroupQueryIdentifier(id: 1); // You can also query groups by name or by GUID.
var readRes2 = await client.GetInterfaceSetsByInterfaceGroupAsync(groupQuery);

// Read all interface sets in all interface groups.
var readRes3 = await client.GetInterfaceSetsAsync();
```

### Tags

```cs
// Tags are anything that has a data stream such as a sensor, calculation, etc.

// Save a new tag. A tag must be tied to an interface, so we need an interface Id.
await using var client = new ConfigurationClient(hostname, port, CertificateValidation.AcceptAllCertificates);
var interfacesRes = await client.GetInterfacesAsync();

// Assuming interfacesRes.Status == GetResultStatus.Successful... See HistorianPaths for more on GetResults and SaveResults.
var interfaceId = interfacesRes.Value[0].Id;

var newTag = new TagConfig("Tag1", dataPARC.TimeSeries.Core.Enums.ValueType.Single, interfaceId);
var saveRes1 = await client.SaveTagAsync(newTag);

// Save multiple tags. For example only, saving the same tag saved above will fail.
List<TagConfig> newTags = [newTag];
var saveRes2 = await client.SaveTagsAsync(newTags);

// Read a single tag.
var tagQuery = new TagQueryIdentifier(id: 1); // You can also query tags by fully qualified name or by GUID.
var readRes1 = await client.GetTagAsync(tagQuery);

// Read all tags in an interface. You can also read all tags in an interface set.
var readParams = new ReadTagListParameters(new InterfaceQueryIdentifier(1));
var readRes2 = await client.GetTagsAsync(readParams);
```

### Writing Data

```cs
await using var client = new WriteClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Write multiple datapoints of the same type.
TagDataPointSingle[] points =
[
    new TagDataPointSingle(1, DateTime.UtcNow, Quality.Good, true, 1.1f),
    new TagDataPointSingle(1, DateTime.UtcNow, Quality.Good, true, 1.2f),
    new TagDataPointSingle(1, DateTime.UtcNow, Quality.Good, true, 1.3f),
];

// The awaitCompletion parameter determines if the write call should wait for the data to be fully written before returning or if it should return as soon as it determines if the data can be written or not. The default is false.
var writeRes1 = await client.WriteDataPointsAsync(points, awaitCompletion: false);

// Write a single datapoint.
var writeRes2 = await client.WriteDataPointAsync(points[0]);

// Write multiple datapoints of different types. Add both the points from above and some points of a different type to a TagDataPointSet.
TagDataPointDouble[] doublePoints =
[
    new TagDataPointDouble(1, DateTime.UtcNow.AddMinutes(-3), Quality.Good, true, 2.1),
    new TagDataPointDouble(1, DateTime.UtcNow.AddMinutes(-2), Quality.Good, true, 2.2),
    new TagDataPointDouble(1, DateTime.UtcNow.AddMinutes(-1), Quality.Good, true, 2.3),
];
var pointSet = new TagDataPointSet(points);
pointSet.Add(doublePoints);

var writeRes3 = await client.WriteDataPointSetAsync(pointSet);
```

### Deleting Data

```cs
await using var client = new WriteClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Delete data at specific timestamps.
List<DateTime> timestamps =
[
    DateTime.UtcNow.AddMinutes(-3),
    DateTime.UtcNow.AddMinutes(-2),
    DateTime.UtcNow.AddMinutes(-2),
];

// The awaitCompletion parameter determines if the delete call should wait for the data to be fully deleted before returning or if it should return as soon as it determines if the data can be deleted or not. The default is false.
var deleteStatus1 = await client.DeleteDataAsync(1, timestamps, awaitCompletion: false);

// Delete data in a time range.
var deleteStatus2 = await client.DeleteDataAsync(1, DateTime.UtcNow.AddMinutes(-5), DateTime.UtcNow);
```

### Reading Current Values

```cs
await using var client = new ReadClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Read the current value for a single tag.
var readParams1 = new ReadCurrentValueParameters(new TagQueryIdentifier(1));
var readRes1 = await client.ReadCurrentValueAsync(readParams1);

if (readRes1.Status == ReadCurrentValueStatus.Successful) {
    var point = readRes1.DataPoint; // The current value for the tag with Id 1.
} else {
    // Something went wrong, check against other ReadCurrentValueStatus cases for more info.
}

// Read the current value for multiple tags.
var readRes2 = await client.ReadCurrentValuesAsync([readParams1]);
foreach (var res in readRes2) {
    // Each tag requested is returned in the same object as the singular ReadCurrentValueAsync call.
}
```

### Reading Specific Timestamps

```cs
await using var client = new ReadClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Read 1 timestamp for a single tag.
var readParams1 = new ReadAtTimeParameters(new TagQueryIdentifier(1), DateTime.UtcNow);
var readRes1 = await client.ReadAtTimeAsync(readParams1);

if (readRes1.Status == ReadAtTimeStatus.Successful) {
    // The value at the timestamp request. DataPoints is an array because multiple timestamps can be requested.
    var point = readRes1.DataPoints[0];
} else {
    // Something went wrong, check against other ReadAtTimeStatus cases for more info.
}

// Read multiple timestamps for a single tag.
var readParams2 = new ReadAtTimeParameters(new TagQueryIdentifier(1), [
    DateTime.UtcNow.AddMinutes(-5),
    DateTime.UtcNow.AddMinutes(-4),
    DateTime.UtcNow.AddMinutes(-3),
    DateTime.UtcNow.AddMinutes(-2),
    DateTime.UtcNow.AddMinutes(-1)
]);
var readRes2 = await client.ReadAtTimeAsync(readParams2);
```

### Reading Raw Data

```cs
await using var client = new ReadClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Read raw data for a single tag.
var readParams1 = new ReadRawParameters(new TagQueryIdentifier(1), DateTime.UtcNow.AddMonths(-1), DateTime.UtcNow);
var readRes1 = await client.ReadRawAsync(readParams1);

if (readRes1.Status == ReadRawStatus.Successful) {
    var points = readRes1.DataPoints; // The datapoints for the last month from the tag with Id 1.
} else {
    // Something went wrong, check against other ReadRawStatus cases for more info.
}

// Read raw data for multiple tags.
var readRes2 = await client.ReadRawBulkAsync([readParams1]);
foreach (var res in readRes2) {
    // Each tag requested is returned in the same object as the singular ReadRawAsync call.
}

// Read a count of raw data points for a single tag. This doesn't load all the data on the client and instead just returns
// a count from the server.
var readRes3 = await client.ReadRawCountAsync(readParams1);

if (readRes3.Status == ReadCountStatus.Successful) {
    var cnt = readRes3.Count; // The number of raw datapoints for the last month from the tag with Id 1.
}

// Read a specified number of datapoints either forwards or backwards from a starting timestamp for a single tag.
var readParams2 = new DirectionalReadRawParameters(new TagQueryIdentifier(1), DateTime.UtcNow, Direction.Backwards, 25);
var readRes4 = await client.DirectionalReadRawAsync(readParams2);

if (readRes4.Status == ReadRawStatus.Successful) {
    var points = readRes1.DataPoints; // The 25 most recent datapoints from the tag with Id 1.
}

// Stream raw data for a single tag. Streaming is equivalent to reading in the data it can return, but it starts returning
// data faster since the server sends data into the stream as soon as it starts reading it. It also provides more flexibility
// around client memory constraints.
var streamParams1 = new StreamRawParameters(new TagQueryIdentifier(1), DateTime.UtcNow.AddMonths(-1), DateTime.UtcNow);
var streamRes1 = await client.StreamRawAsync(streamParams1);

if (streamRes1.Status == ReadRawStatus.Successful) {
    await foreach (var points in streamRes1.StreamAsync()) {
    }
}

// Stream a specified number of datapoints either forwards or backwards from a starting timestamp for a single tag.
var streamParams2 = new DirectionalStreamRawParameters(new TagQueryIdentifier(1), DateTime.UtcNow, Direction.Backwards, 25);
var streamRes4 = await client.DirectionalStreamRawAsync(streamParams2);

if (streamRes4.Status == ReadRawStatus.Successful) {
    await foreach (var points in streamRes1.StreamAsync()) {
    }
}
```

### Reading Processed Data

```cs
await using var client = new ReadClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Read processed data for a single tag.
var readParams1 = new ReadProcessedParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow.AddMonths(-1),
    DateTime.UtcNow,
    new AggregateConfig {
        AggregateType = AggregateType.TimeAverage2,
        ProcessingInterval = TimeSpan.FromMinutes(5),
    });
var readRes1 = await client.ReadProcessedAsync(readParams1);

if (readRes1.Status == ReadProcessedStatus.Successful) {
    var points = readRes1.DataPoints; // The 5 minute time averages for the last month from the tag with Id 1.
} else {
    // Something went wrong, check against other ReadProcessedStatus cases for more info.
}

// Read processed data for multiple tags.
var readRes2 = await client.ReadProcessedBulkAsync([readParams1]);
foreach (var res in readRes2) {
    // Each tag requested is returned in the same object as the singular ReadProcessedAsync call.
}

// Read a count of processed data points for a single tag. This doesn't load all the data on the client and instead just returns
// a count from the server.
var readRes3 = await client.ReadProcessedCountAsync(readParams1);

if (readRes3.Status == ReadCountStatus.Successful) {
    var cnt = readRes3.Count; // The number of 5 minute time averages for the last month from the tag with Id 1.
}

// Read a specified number of datapoints either forwards or backwards from a starting timestamp for a single tag.
var readParams2 = new DirectionalReadProcessedParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow,
    Direction.Backwards,
    25,
    new AggregateConfig {
        AggregateType = AggregateType.TimeAverage2,
        ProcessingInterval = TimeSpan.FromMinutes(5),
    });
var readRes4 = await client.DirectionalReadProcessedAsync(readParams2);

if (readRes4.Status == ReadProcessedStatus.Successful) {
    var points = readRes1.DataPoints; // The 25 most recent 5 minutes time averages from the tag with Id 1.
}

// Stream processed data for a single tag. Streaming is equivalent to reading in the data it can return, but it starts returning
// data faster since the server sends data into the stream as soon as it starts reading it. It also provides more flexibility
// around client memory constraints.
var streamParams1 = new StreamProcessedParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow.AddMonths(-1),
    DateTime.UtcNow,
    new AggregateConfig {
        AggregateType = AggregateType.TimeAverage2,
        ProcessingInterval = TimeSpan.FromMinutes(5),
    });
var streamRes1 = await client.StreamProcessedAsync(streamParams1);

if (streamRes1.Status == ReadProcessedStatus.Successful) {
    await foreach (var points in streamRes1.StreamAsync()) {
    }
}

// Stream a specified number of datapoints either forwards or backwards from a starting timestamp for a single tag.
var streamParams2 = new DirectionalStreamProcessedParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow,
    Direction.Backwards,
    25,
    new AggregateConfig {
        AggregateType = AggregateType.TimeAverage2,
        ProcessingInterval = TimeSpan.FromMinutes(5),
    });
var streamRes4 = await client.DirectionalStreamProcessedAsync(streamParams2);

if (streamRes4.Status == ReadProcessedStatus.Successful) {
    await foreach (var points in streamRes1.StreamAsync()) {
    }
}
```

### Reading Processed Data By Config

```cs
await using var client = new ReadClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Read processed data for a single tag using a preconfigured aggregate.
var readParams1 = new ReadProcessedByConfigParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow.AddMonths(-1),
    DateTime.UtcNow,
    "SavedAgg1");
var readRes1 = await client.ReadProcessedByConfigAsync(readParams1);

if (readRes1.Status == ReadProcessedStatus.Successful) {
    var points = readRes1.DataPoints; // The 5 minute time averages for the last month from the tag with Id 1.
} else {
    // Something went wrong, check against other ReadProcessedStatus cases for more info.
}

// Read processed data for multiple tags using preconfigured aggregates.
var readRes2 = await client.ReadProcessedBulkByConfigAsync([readParams1]);
foreach (var res in readRes2) {
    // Each tag requested is returned in the same object as the singular ReadProcessedAsync call.
}

// Read a count of processed data points for a single tag using a preconfigured aggregate. This doesn't load all the data
// on the client and instead just returns a count from the server.
var readRes3 = await client.ReadProcessedByConfigCountAsync(readParams1);

if (readRes3.Status == ReadCountStatus.Successful) {
    var cnt = readRes3.Count; // The number of 5 minute time averages for the last month from the tag with Id 1.
}

// Read a specified number of datapoints either forwards or backwards from a starting timestamp for a single tag using a
// preconfigured aggregate.
var readParams2 = new DirectionalReadProcessedByConfigParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow,
    Direction.Backwards,
    25,
    "SavedAgg1");
var readRes4 = await client.DirectionalReadProcessedByConfigAsync(readParams2);

if (readRes4.Status == ReadProcessedStatus.Successful) {
    var points = readRes1.DataPoints; // The 25 most recent 5 minutes time averages from the tag with Id 1.
}

// Stream processed data for a single tag using a preconfigured aggregate. Streaming is equivalent to reading in the data it
// can return, but it starts returning data faster since the server sends data into the stream as soon as it starts reading
// it. It also provides more flexibility around client memory constraints.
var streamParams1 = new StreamProcessedByConfigParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow.AddMonths(-1),
    DateTime.UtcNow,
    "SavedAgg1");
var streamRes1 = await client.StreamProcessedByConfigAsync(streamParams1);

if (streamRes1.Status == ReadProcessedStatus.Successful) {
    await foreach (var points in streamRes1.StreamAsync()) {
    }
}

// Stream a specified number of datapoints either forwards or backwards from a starting timestamp for a single tag using a
// preconfigured aggregate.
var streamParams2 = new DirectionalStreamProcessedByConfigParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow,
    Direction.Backwards,
    25,
    "SavedAgg1");
var streamRes4 = await client.DirectionalStreamProcessedByConfigAsync(streamParams2);

if (streamRes4.Status == ReadProcessedStatus.Successful) {
    await foreach (var points in streamRes1.StreamAsync()) {
    }
}
```

### Reading Array Data

```cs
// All read call support 2 additional parameters for slicing array tags: arrayStartIndex and arrayLength.

await using var client = new ReadClient(hostname, port, CertificateValidation.AcceptAllCertificates);

var readParams = new ReadRawParameters(
    new TagQueryIdentifier(1),
    DateTime.UtcNow.AddMonths(-1),
    DateTime.UtcNow,
    arrayStartIndex: 2,
    arrayLength: 3);
var readRes = await client.ReadRawAsync(readParams);

// The datapoints returned will be slices of the shape [2..5] from the array datapoints.
var points = readRes.DataPoints;
```

### Using DataPoints From Read Responses

```cs
// All read calls return datapoints in 1 of 2 types: DataPoints or IDataPoint
//      DataPoints: an array of 1 of multiple types of datapoints, i.e. one of DataPointSingle[], DataPointByte[], etc.
//      IDataPoint: 1 of datapoint types, i.e. one of DataPointSingle, DataPointByte, etc.

// To use DataPoints, first mock up some datapoint returned from a read call:
DataPoints datapoints = new[] {
    new DataPointSingle(DateTime.UtcNow.AddMinutes(-3), Quality.Good, true, 1.3f),
    new DataPointSingle(DateTime.UtcNow.AddMinutes(-2), Quality.Good, true, 1.2f),
    new DataPointSingle(DateTime.UtcNow.AddMinutes(-1), Quality.Good, true, 1.1f),
};


// When you know the type of datapoints returned, you can grab them by property. This is best case in terms of performance.
DataPointSingle[] datapointSingles = datapoints.DataPointSingles;

// When you don't know the type, such as in a function that operates over any type of datapoints, you can pass in a func
// for every type. This is how the Count property is implemented on DataPoints.
var cnt = datapoints.Match(
    dpBools => dpBools.Length,
    dpBytes => dpBytes.Length,
    dpSBytes => dpSBytes.Length,
    dpDateTimes => dpDateTimes.Length,
    dpDecimals => dpDecimals.Length,
    dpDigTexts => dpDigTexts.Length,
    dpDoubles => dpDoubles.Length,
    dpSingles => dpSingles.Length,
    dpInt16s => dpInt16s.Length,
    dpInt32s => dpInt32s.Length,
    dpInt64s => dpInt64s.Length,
    dpUInt16s => dpUInt16s.Length,
    dpUInt32s => dpUInt32s.Length,
    dpUInt64s => dpUInt64s.Length,
    dpStrings => dpStrings.Length,
    dpBoolArrs => dpBoolArrs.Length,
    dpByteArrs => dpByteArrs.Length,
    dpSByteArrs => dpSByteArrs.Length,
    dpDateTimeArrs => dpDateTimeArrs.Length,
    dpDecimalArrs => dpDecimalArrs.Length,
    dpDoubleArrs => dpDoubleArrs.Length,
    dpSingleArrs => dpSingleArrs.Length,
    dpInt16Arrs => dpInt16Arrs.Length,
    dpInt32Arrs => dpInt32Arrs.Length,
    dpInt64Arrs => dpInt64Arrs.Length,
    dpUInt16Arrs => dpUInt16Arrs.Length,
    dpUInt32Arrs => dpUInt32Arrs.Length,
    dpUInt64Arrs => dpUInt64Arrs.Length,
    dpStringArrs => dpStringArrs.Length);

// When you don't know the type, you can also pass in an action for every type. This is like Match but doesn't return anything.
datapoints.Switch(
    dpBools => Console.WriteLine(dpBools.Length),
    dpBytes => Console.WriteLine(dpBytes.Length),
    dpSBytes => Console.WriteLine(dpSBytes.Length),
    dpDateTimes => Console.WriteLine(dpDateTimes.Length),
    dpDecimals => Console.WriteLine(dpDecimals.Length),
    dpDigTexts => Console.WriteLine(dpDigTexts.Length),
    dpDoubles => Console.WriteLine(dpDoubles.Length),
    dpSingles => Console.WriteLine(dpSingles.Length),
    dpInt16s => Console.WriteLine(dpInt16s.Length),
    dpInt32s => Console.WriteLine(dpInt32s.Length),
    dpInt64s => Console.WriteLine(dpInt64s.Length),
    dpUInt16s => Console.WriteLine(dpUInt16s.Length),
    dpUInt32s => Console.WriteLine(dpUInt32s.Length),
    dpUInt64s => Console.WriteLine(dpUInt64s.Length),
    dpStrings => Console.WriteLine(dpStrings.Length),
    dpBoolArrs => Console.WriteLine(dpBoolArrs.Length),
    dpByteArrs => Console.WriteLine(dpByteArrs.Length),
    dpSByteArrs => Console.WriteLine(dpSByteArrs.Length),
    dpDateTimeArrs => Console.WriteLine(dpDateTimeArrs.Length),
    dpDecimalArrs => Console.WriteLine(dpDecimalArrs.Length),
    dpDoubleArrs => Console.WriteLine(dpDoubleArrs.Length),
    dpSingleArrs => Console.WriteLine(dpSingleArrs.Length),
    dpInt16Arrs => Console.WriteLine(dpInt16Arrs.Length),
    dpInt32Arrs => Console.WriteLine(dpInt32Arrs.Length),
    dpInt64Arrs => Console.WriteLine(dpInt64Arrs.Length),
    dpUInt16Arrs => Console.WriteLine(dpUInt16Arrs.Length),
    dpUInt32Arrs => Console.WriteLine(dpUInt32Arrs.Length),
    dpUInt64Arrs => Console.WriteLine(dpUInt64Arrs.Length),
    dpStringArrs => Console.WriteLine(dpStringArrs.Length));

// Finally, since each datapoint type implements IDataPoint, you can get an array of IDataPoint from all datapoints
// contained in a DataPoints instance. This is least ideal when working with DataPoints since every datapoint contained is
// boxed upon being referenced as an IDataPoint.
// Since DataPoints implements IEnumerable<IDataPoint>, spreading it into a collection expression, calling ToArray, or
// calling ToList on it will transform it into a collection of IDataPoint(s).
IDataPoint[] idatapoints1 = [.. datapoints];
IDataPoint[] idatapoints2 = datapoints.ToArray();
List<IDataPoint> idatapoints3 = datapoints.ToList();
```

### Tag Publishing

```cs
await using var client = new PublishingClient(hostname, port, CertificateValidation.AcceptAllCertificates);

// Setup a callback to run if the client connection to the server changes state. There are other callbacks for first
// connection and disconnection as well.
client.OnReconnected = async () => {
    Console.WriteLine("Reconnected!");
    await Task.Delay(1000); // This callback is a Func<Task> so async code can run here.
};

// Setup a callback to run when tag data is published. This will be called by the publishing client when it receives published
// tag data from the server.
static async ValueTask OnPublish(TagPublishingResult result) {
    Console.WriteLine($"{result.DataPoints.Count} points received");
    await Task.Delay(1000); // This callback returns a ValueTask so async code can run here.
}

// Subscribe to a single tag. Here's where we pass in our on publish callback.
var startParams1 = new StartTagPublishingParameters(new TagQueryIdentifier(1), TimeSpan.FromSeconds(5));
var startRes1 = await client.StartPublishingAsync(startParams1, OnPublish);

// Subscribe to multiple tags. Resub to the same tag for example.
List<(StartTagPublishingParameters, Func<TagPublishingResult, ValueTask>)> startParams2 =
[
    (new StartTagPublishingParameters(new TagQueryIdentifier(2), TimeSpan.FromSeconds(5)), OnPublish),
    (new StartTagPublishingParameters(new TagQueryIdentifier(3), TimeSpan.FromSeconds(5)), OnPublish),
];
var startRes2 = await client.StartPublishingAsync(startParams2);

// Change the publishing interval of an active subscription. You can also pass in multiple Ids.
var id = startRes1.ClientTagId;
var changeIntRes = await client.ChangePublishingIntervalAsync(id, TimeSpan.FromSeconds(3));

// Stop publishing for a single tag. You can also pass in multiple Ids.
var stopRes1 = await client.StopPublishingAsync(id);

// Or stop publishing for all tags.
await client.StopPublishingAsync();
```
