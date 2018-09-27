# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import inventory


def register():
    Pool.register(
        inventory.InventoryLine,
        module='stock_inventory_expected_quantity', type_='model')
