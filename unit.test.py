import unittest
import random

from revised import generate_ids


class TestGenerateIds(unittest.TestCase):

    def test_generate_ids(self):
        # Test matrix: generate random values for n and length
        test_cases = [{'n': random.randint(1, 1000), 'length': random.randint(1, 100)} for _ in range(5)]

        for case in test_cases:
            n = case['n']
            length = case['length']
            with self.subTest(f'n={n}, length={length}'):
                # Generate IDs
                ids = list(generate_ids(n, length=length))

                # Check that there are n IDs
                self.assertEqual(len(ids), n)

                # Check that each ID is a string
                for id in ids:
                    self.assertIsInstance(id, str)

                # Check that each ID is the correct length
                for id in ids:
                    self.assertEqual(len(id), length)

                # Check that each ID contains only alphanumeric characters
                for id in ids:
                    self.assertTrue(id.isalnum())


if __name__ == '__main__':
    unittest.main()
