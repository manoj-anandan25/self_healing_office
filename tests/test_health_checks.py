import unittest
from monitoring.ping_check import ping_host
from monitoring.dns_check import dns_lookup
from monitoring.traceroute_check import traceroute_host

class TestHealthChecks(unittest.TestCase):
    def test_ping(self):
        result = ping_host("8.8.8.8")
        self.assertIsNotNone(result)

    def test_dns(self):
        result = dns_lookup("google.com")
        self.assertIsNotNone(result)

    def test_traceroute(self):
        result = traceroute_host("8.8.8.8")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()