"""Test fixtures."""
from builtins import super

import pytest
from napalm_base.test import conftest as parent_conftest
from napalm_base.test.double import BaseTestDouble

from napalm_ibm import IBMDriver as OriginalDriver


@pytest.fixture(scope='class')
def set_device_parameters(request):
    """Set up the class."""
    def fin():
        request.cls.device.close()
    request.addfinalizer(fin)

    request.cls.driver = OriginalDriver
    request.cls.patched_driver = PatchedDriver
    request.cls.vendor = 'ibm'
    parent_conftest.set_device_parameters(request)


def pytest_generate_tests(metafunc):
    """Generate test cases dynamically."""
    parent_conftest.pytest_generate_tests(metafunc, __file__)


class PatchedDriver(OriginalDriver):
    """Patched IBM Driver."""
    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        super().__init__(hostname, username, password, timeout, optional_args)
        self.patched_attrs = ['bnc']
        self.bnc = FakeDevice()

    def open(self):
        pass

    def close(self):
        pass


class FakeDevice(BaseTestDouble):
    """Device test double."""

    def open(self):
        pass

    def close(self):
        pass
