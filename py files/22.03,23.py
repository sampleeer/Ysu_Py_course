from dataclasses import dataclass, InitVar
from typing import Optional
from enum import Enum


class TransportType(Enum):
    BUS = 1
    TAXIBUS = 2
    TROLLEYBUS = 3
    TRAM = 4
    RIVER_BUS = 5
    METRO = 6
    HELICOPTER = 7
    RICKSHAW = 8


@dataclass
class Route:
    transport_type: TransportType
    route_id: str
    start_point: str
    end_point: str


# Создается имутабельный класс - константный
@dataclass(frozen=True)
class Freeze:
    transport_type: TransportType
    route_id: str
    start_point: str
    end_point: str


@dataclass
class PublicVehicle:
    capacity: int
    transport_type: str
    vehicle_id: str
    owner_company: str
    is_benefit_available: bool = True
    current_rout: Optional[Route] = None
    license_plate: Optional[Route] = None

    def assign_rout(self, new_rout: Route):
        if self.transport_type == new_rout.transport_type:
            self.current_rout = new_rout
        else:
            print("Can't assign this route")

    def __post_init__(self):
        if self.transport_type == TransportType.TAXIBUS:
            self.is_benefit_available = False


# public_vehiclel = PublicVehicle(50, TransportType.BUS, '123',
# 'SuperTransport Ltd.', license_plate='A001AA76')

