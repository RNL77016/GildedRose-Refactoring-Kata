# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"


class ItemUpdater:
    """Base class for updating items using Template Method pattern."""

    def update(self, item):
        """Template method that defines the update algorithm."""
        self._update_sell_in(item)
        self._update_quality(item)

    def _update_sell_in(self, item):
        """Hook method for updating sell_in. Can be overridden by subclasses."""
        item.sell_in -= 1

    def _update_quality(self, item):
        """Hook method for updating quality. Can be overridden by subclasses."""
        # Default behavior for normal items
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class NormalItemUpdater(ItemUpdater):
    """Updater for normal items."""
    pass  # Uses default behavior from ItemUpdater


class AgedBrieUpdater(ItemUpdater):
    """Updater for Aged Brie items."""

    def _update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassUpdater(ItemUpdater):
    """Updater for Backstage passes."""

    def _update_quality(self, item):
        if item.quality >= 50:
            return

        item.quality += 1

        if item.sell_in < 11 and item.quality < 50:
            item.quality += 1

        if item.sell_in < 6 and item.quality < 50:
            item.quality += 1

        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(ItemUpdater):
    """Updater for Sulfuras items - never changes."""

    def _update_sell_in(self, item):
        pass  # Sulfuras sell_in never changes

    def _update_quality(self, item):
        pass  # Sulfuras quality never changes


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self._updaters = {
            AGED_BRIE: AgedBrieUpdater(),
            BACKSTAGE_PASSES: BackstagePassUpdater(),
            SULFURAS: SulfurasUpdater(),
        }

    def update_quality(self):
        for item in self.items:
            updater = self._updaters.get(item.name, NormalItemUpdater())
            updater.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
