import enum
from typing import Any, NamedTuple

from ._common import (
    NIC_DUPLEX_FULL as NIC_DUPLEX_FULL,
    NIC_DUPLEX_HALF as NIC_DUPLEX_HALF,
    NIC_DUPLEX_UNKNOWN as NIC_DUPLEX_UNKNOWN,
    AccessDenied as AccessDenied,
    NoSuchProcess as NoSuchProcess,
    ZombieProcess as ZombieProcess,
    isfile_strict as isfile_strict,
    parse_environ_block as parse_environ_block,
    path_exists_strict as path_exists_strict,
    supports_ipv6 as supports_ipv6,
    usage_percent as usage_percent,
)

__extra__all__: Any
POWER_SUPPLY_PATH: str
HAS_PROC_IO_PRIORITY: Any
HAS_CPU_AFFINITY: Any
CLOCK_TICKS: Any
PAGESIZE: Any
BOOT_TIME: Any
LITTLE_ENDIAN: Any
DISK_SECTOR_SIZE: int
AF_LINK: Any
AddressFamily: Any
IOPRIO_CLASS_NONE: int
IOPRIO_CLASS_RT: int
IOPRIO_CLASS_BE: int
IOPRIO_CLASS_IDLE: int

class IOPriority(enum.IntEnum):
    IOPRIO_CLASS_NONE: int
    IOPRIO_CLASS_RT: int
    IOPRIO_CLASS_BE: int
    IOPRIO_CLASS_IDLE: int

PROC_STATUSES: Any
TCP_STATUSES: Any

class svmem(NamedTuple):
    total: Any
    available: Any
    percent: Any
    used: Any
    free: Any
    active: Any
    inactive: Any
    buffers: Any
    cached: Any
    shared: Any
    slab: Any

class sdiskio(NamedTuple):
    read_count: Any
    write_count: Any
    read_bytes: Any
    write_bytes: Any
    read_time: Any
    write_time: Any
    read_merged_count: Any
    write_merged_count: Any
    busy_time: Any

class popenfile(NamedTuple):
    path: Any
    fd: Any
    position: Any
    mode: Any
    flags: Any

class pmem(NamedTuple):
    rss: Any
    vms: Any
    shared: Any
    text: Any
    lib: Any
    data: Any
    dirty: Any

pfullmem: Any

class pmmap_grouped(NamedTuple):
    path: Any
    rss: Any
    size: Any
    pss: Any
    shared_clean: Any
    shared_dirty: Any
    private_clean: Any
    private_dirty: Any
    referenced: Any
    anonymous: Any
    swap: Any

pmmap_ext: Any

class pio(NamedTuple):
    read_count: Any
    write_count: Any
    read_bytes: Any
    write_bytes: Any
    read_chars: Any
    write_chars: Any

class pcputimes(NamedTuple):
    user: Any
    system: Any
    children_user: Any
    children_system: Any
    iowait: Any

def readlink(path): ...
def file_flags_to_mode(flags): ...
def is_storage_device(name): ...
def set_scputimes_ntuple(procfs_path) -> None: ...

scputimes: Any
prlimit: Any

def calculate_avail_vmem(mems): ...
def virtual_memory() -> svmem: ...
def swap_memory(): ...
def cpu_times(): ...
def per_cpu_times(): ...
def cpu_count_logical(): ...
def cpu_count_cores() -> int | None: ...
def cpu_stats(): ...
def cpu_freq(): ...

net_if_addrs: Any

class _Ipv6UnsupportedError(Exception): ...

class Connections:
    tmap: Any
    def __init__(self) -> None: ...
    def get_proc_inodes(self, pid): ...
    def get_all_inodes(self): ...
    @staticmethod
    def decode_address(addr, family): ...
    @staticmethod
    def process_inet(file, family, type_, inodes, filter_pid: Any | None = ...) -> None: ...
    @staticmethod
    def process_unix(file, family, inodes, filter_pid: Any | None = ...) -> None: ...
    def retrieve(self, kind, pid: Any | None = ...): ...

def net_connections(kind: str = ...): ...
def net_io_counters(): ...
def net_if_stats(): ...

disk_usage: Any

def disk_io_counters(perdisk: bool = ...): ...
def disk_partitions(all: bool = ...): ...
def sensors_temperatures(): ...
def sensors_fans(): ...
def sensors_battery(): ...
def users(): ...
def boot_time(): ...
def pids(): ...
def pid_exists(pid): ...
def ppid_map(): ...
def wrap_exceptions(fun): ...

class Process:
    pid: Any
    def __init__(self, pid) -> None: ...
    def oneshot_enter(self) -> None: ...
    def oneshot_exit(self) -> None: ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def environ(self): ...
    def terminal(self): ...
    def io_counters(self): ...
    def cpu_times(self): ...
    def cpu_num(self): ...
    def wait(self, timeout: Any | None = ...): ...
    def create_time(self): ...
    def memory_info(self): ...
    def memory_full_info(self): ...
    def memory_maps(self): ...
    def cwd(self): ...
    def num_ctx_switches(self, _ctxsw_re=...): ...
    def num_threads(self, _num_threads_re=...): ...
    def threads(self): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def cpu_affinity_get(self): ...
    def cpu_affinity_set(self, cpus) -> None: ...
    def ionice_get(self): ...
    def ionice_set(self, ioclass, value): ...
    def rlimit(self, resource_, limits: Any | None = ...): ...
    def status(self): ...
    def open_files(self): ...
    def connections(self, kind: str = ...): ...
    def num_fds(self): ...
    def ppid(self): ...
    def uids(self, _uids_re=...): ...
    def gids(self, _gids_re=...): ...
