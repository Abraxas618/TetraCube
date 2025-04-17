
import os
import unittest
from post_quantum_crypto import pq_hash, generate_entropy_key

class TestPostQuantumCrypto(unittest.TestCase):
    def test_pq_hash_output_length(self):
        hashed = pq_hash("test", "salt")
        self.assertEqual(len(hashed), 64)

    def test_entropy_key_length(self):
        key = generate_entropy_key(64)
        self.assertEqual(len(key), 64)

if __name__ == "__main__":
    unittest.main()
