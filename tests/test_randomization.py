
import unittest

from src.randomization import randomize, get_degrees


class TestRandomization(unittest.TestCase):

    def setUp(self):
        self.edges = {
            (1, 2), (2, 3), (3, 4),
            (4, 1), (1, 3), (2, 4)
        }

    def test_degree_preservation(self):
        original_degrees = get_degrees(self.edges)

        result = randomize(self.edges, 100, 9685)

        self.assertEqual(original_degrees, get_degrees(result))

    def test_edge_count_preservation(self):
        result = randomize(self.edges, 100, 9685)

        self.assertEqual(len(self.edges), len(result))

    def test_no_self_loops(self):
        result = randomize(self.edges, 100, 9685)

        for source, target in result:
            self.assertNotEqual(source, target)

    def test_reproducibility(self):
        first = randomize(self.edges, 100, 9685)
        second = randomize(self.edges, 100, 9685)

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
