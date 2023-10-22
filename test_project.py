import unittest
from project.py import pack_containers, Item, Container

class TestPackContainers(unittest.TestCase):

    def test_pack_items_within_weight_limit(self):
        items = [
            Item("Item1", 10, 2, 5000),
            Item("Item2", 15, 3, 8000),
        ]
        container_capacity = 100
        unit_name = "cubic meters"
        weight_limit = 10000

        containers, _ = pack_containers(items, container_capacity, unit_name, weight_limit)

        self.assertEqual(len(containers), 1)
        # Should be packed in one container
        self.assertEqual(containers[0].weight_kg, 13000)
        # Total weight of items in the container
        self.assertTrue(containers[0].weight_kg <= weight_limit)
        # Weight should not exceed the limit

    def test_pack_items_exceeding_weight_limit(self):
        items = [
            Item("Item1", 10, 2, 5000),
            Item("Item2", 15, 3, 15000),
            # This item exceeds the weight limit
        ]
        container_capacity = 100
        unit_name = "cubic meters"
        weight_limit = 10000

        containers, _ = pack_containers(items, container_capacity, unit_name, weight_limit)

        self.assertEqual(len(containers), 2)
        # Should be packed in two containers
        self.assertEqual(containers[0].weight_kg, 5000)
        self.assertEqual(containers[1].weight_kg, 15000)
        self.assertTrue(all(container.weight_kg <= weight_limit for container in containers))

if __name__ == "__main__":
    unittest.main()
