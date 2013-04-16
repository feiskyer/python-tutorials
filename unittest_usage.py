"""
    Python unittest tips:
        Method                      Checks that	            New in
        assertEqual(a, b)	        a == b
        assertNotEqual(a, b)	    a != b
        assertTrue(x)	            bool(x) is True
        assertFalse(x)	            bool(x) is False
        assertIs(a, b)	            a is b	                2.7
        assertIsNot(a, b)	        a is not b	            2.7
        assertIsNone(x)	            x is None	            2.7
        assertIsNotNone(x)	        x is not None	        2.7
        assertIn(a, b)	            a in b	                2.7
        assertNotIn(a, b)	        a not in b	            2.7
        assertIsInstance(a, b)	    isinstance(a, b)	    2.7
        assertNotIsInstance(a, b)	not isinstance(a, b)	2.7
        assertRaises(exc, fun, *args, **kwds)
        assertRaisesRegexp(exc, re, fun, *args, **kwds)
        assertAlmostEqual(a, b)
        assertNotAlmostEqual(a, b)
        assertGreater(a, b)
        assertGreaterEqual(a, b)
        assertLess(a, b)
        assertLessEqual(a, b)
        assertRegexpMatches(s, re)
        assertNotRegexpMatches(s, re)
        assertItemsEqual(a, b)
        assertDictContainsSubset(a, b)
        assertMultiLineEqual(a, b)
        assertSequenceEqual(a, b)
        assertListEqual(a, b)
        assertTupleEqual(a, b)
        assertSetEqual(a, b)
        assertDictEqual(a, b)
"""
import random
import unittest
import sys

__version__ = "3.4.2"

class TestSequenceFunctions(unittest.TestCase):
    """
       Basic example of unittest from http://docs.python.org/2/library/unittest.html
    """

    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        self.seq = None

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

    # Skipping tests
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # Skipping test on some conditions
    @unittest.skipIf(__version__ < (1, 3), "feature not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    # Skipping test on non-windows systems
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

if __name__ == '__main__':
    unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    #unittest.TextTestRunner(verbosity=2).run(suite)
