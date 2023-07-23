from dataclasses import dataclass
from datetime import date
from typing import List, Optional, NewType

Quantity = NewType("Quantity", int)
Sku = NewType("Sku", str)
Reference = NewType("Reference", str)

class OutOfStock(Exception):
    pass

@dataclass(frozen=True)
class OrderLine:
    orderid: Reference
    sku: Sku
    quantity: Quantity


class Batch:

    def __init__(self, reference: Reference, sku: Sku, quantity: Quantity, eta: Optional[date]) -> None:
        self.reference: Reference = reference
        self.sku: Sku = sku
        self.eta = eta
        self._purchased_quantity: Quantity = quantity
        self._allocations: set[OrderLine] = set()

    def __repr__(self) -> str:
        return f"<Batch {self.reference}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self) -> int:
        return hash(self.reference)

    def __gt__(self, other) -> bool:
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity
    
    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine) -> None:
        if line in self._allocations:
            self._allocations.remove(line)

    def can_allocate(self, diff_line: OrderLine) -> bool:
        return self.sku == diff_line.sku and self.available_quantity >= diff_line.quantity
    


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    """
    Prefer
    """
    try:
        target_batch = next(batch for batch in sorted(batches) if batch.can_allocate(line))
        target_batch.allocate(line)
        return target_batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")