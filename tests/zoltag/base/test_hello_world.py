import unittest

from zoltag.base.hello_world import HelloWorld


class TestHelloWorld(unittest.TestCase):

  def test_default(self) -> None:
    self.assertEqual(HelloWorld().greet(), "Hello, World!")

  def test_custom(self) -> None:
    self.assertEqual(HelloWorld().greet("Bob"), "Hello, Bob!")
