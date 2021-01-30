from enum import Enum


class ProductStatus(str, Enum):
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
