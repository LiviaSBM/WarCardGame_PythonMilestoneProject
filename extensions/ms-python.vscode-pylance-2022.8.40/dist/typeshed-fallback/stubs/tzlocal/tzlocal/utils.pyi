import sys

import pytz

if sys.version_info >= (3, 9):
    import zoneinfo

    class ZoneInfoNotFoundError(pytz.UnknownTimeZoneError, zoneinfo.ZoneInfoNotFoundError): ...

else:
    class ZoneInfoNotFoundError(pytz.UnknownTimeZoneError): ...

def get_system_offset(): ...
def get_tz_offset(tz): ...
def assert_tz_offset(tz) -> None: ...
