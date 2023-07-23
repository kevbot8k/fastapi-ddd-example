from dataclasses import dataclass
from datetime import date
from typing import List, Optional, NewType

Quantity = NewType("Quantity", int)
Sku = NewType("Sku", str)
Reference = NewType("Reference", str)


@dataclass(frozen=True)
class OrderLine:
    orderid: Reference
    sku: Sku
    quantity: Quantity


class Batch:

    def __init__(self, reference: Reference, sku: Sku, quantity: Quantity, eta: Optional[date]) -> None:
        self.reference: Reference = reference
        self.sku: Sku = sku
        self._purchased_quantity: Quantity = quantity
        self._allocations: set[OrderLine] = set()

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity
    
    def allocate(self, line: OrderLine) -> None:
        if line not in self._allocations:
            self._purchased_quantity -= line.quantity
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    def can_allocate(self, diff_line: OrderLine) -> bool:
        return self.sku == diff_line.sku and self._purchased_quantity >= diff_line.quantity
    


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    """
    Prefer
    """
    return