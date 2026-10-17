# test_oscillatornote.py
"""
Tests for OscillatorNote module.
"""

import unittest
from oscillatornote import OscillatorNote

class TestOscillatorNote(unittest.TestCase):
    """Test cases for OscillatorNote class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OscillatorNote()
        self.assertIsInstance(instance, OscillatorNote)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OscillatorNote()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
