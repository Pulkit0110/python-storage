
transport inheritance structure
_______________________________

`StorageTransport` is the ABC for all transports.
- public child `StorageGrpcTransport` for sync gRPC transport (defined in `grpc.py`).
- public child `StorageGrpcAsyncIOTransport` for async gRPC transport (defined in `grpc_asyncio.py`).
- private child `_BaseStorageRestTransport` for base REST transport with inner classes `_BaseMETHOD` (defined in `rest_base.py`).
- public child `StorageRestTransport` for sync REST transport with inner classes `METHOD` derived from the parent's corresponding `_BaseMETHOD` classes (defined in `rest.py`).
