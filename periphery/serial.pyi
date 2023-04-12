from types import TracebackType

class SerialError(IOError): ...

class Serial:
    def __init__(
        self,
        devpath: str,
        baudrate: int,
        databits: int = ...,
        parity: str = ...,
        stopbits: int = ...,
        xonxoff: bool = ...,
        rtscts: bool = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> Serial: ...  # noqa: Y034
    def __exit__(self, t: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def read(self, length: int, timeout: float | None = ...) -> bytes: ...
    def write(self, data: bytes | bytearray | list[int]) -> int: ...
    def poll(self, timeout: float | None = ...) -> bool: ...
    def flush(self) -> None: ...
    def input_waiting(self) -> int: ...
    def output_waiting(self) -> int: ...
    def close(self) -> None: ...
    @property
    def fd(self) -> int: ...
    @property
    def devpath(self) -> str: ...
    baudrate: int
    databits: int
    parity: str
    stopbits: int
    xonxoff: bool
    rtscts: bool
    vmin: int
    vtime: float
