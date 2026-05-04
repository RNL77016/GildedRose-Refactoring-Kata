# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class TestGildedRose(unittest.TestCase):

    def test_normal_item_quality_decreases_by_1_before_sell_date(self):
        items = [Item("Normal Item", sell_in=10, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_normal_item_quality_decreases_by_2_after_sell_date(self):
        items = [Item("Normal Item", sell_in=0, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 18)
        self.assertEqual(items[0].sell_in, -1)

    def test_quality_never_goes_below_zero(self):
        items = [Item("Normal Item", sell_in=5, quality=0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_normal_item_quality_decreases_by_1_when_quality_is_1_before_sell_date(self):
        items = [Item("Normal Item", sell_in=5, quality=1)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_normal_item_quality_decreases_by_2_when_quality_is_1_after_sell_date(self):
        items = [Item("Normal Item", sell_in=0, quality=1)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item_degrades_twice_as_fast_before_sell_date(self):
        items = [Item("Conjured Mana Cake", sell_in=5, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 18)

    def test_conjured_item_degrades_four_times_after_sell_date(self):
        items = [Item("Conjured Mana Cake", sell_in=0, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 16)

    def test_conjured_quality_never_below_zero(self):
        items = [Item("Conjured Mana Cake", sell_in=5, quality=1)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_increases_quality_over_time(self):
        items = [Item("Aged Brie", sell_in=5, quality=10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 11)
        self.assertEqual(items[0].sell_in, 4)

    def test_aged_brie_increases_quality_twice_as_fast_after_sell_date(self):
        items = [Item("Aged Brie", sell_in=0, quality=10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 12)
        self.assertEqual(items[0].sell_in, -1)

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", sell_in=5, quality=50)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_aged_brie_quality_does_not_exceed_50_after_sell_date(self):
        items = [Item("Aged Brie", sell_in=0, quality=49)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_aged_brie_quality_does_not_exceed_50_when_at_50_after_sell_date(self):
        items = [Item("Aged Brie", sell_in=0, quality=50)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_sulfuras_never_changes_with_positive_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 10)

    def test_backstage_pass_quality_increases_by_1_when_sell_in_greater_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 14)

    def test_backstage_pass_quality_increases_by_2_when_sell_in_between_6_and_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 22)
        self.assertEqual(items[0].sell_in, 9)

    def test_backstage_pass_quality_increases_by_3_when_sell_in_between_1_and_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 23)
        self.assertEqual(items[0].sell_in, 4)

    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_backstage_pass_quality_increases_but_not_above_50_when_sell_in_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_backstage_pass_quality_increases_but_not_above_50_when_sell_in_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=48)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)


if __name__ == '__main__':
    unittest.main()
