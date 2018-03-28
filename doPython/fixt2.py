# trying fixtures
import logging
import pytest
pytest_plugins = ["rough.fixt1"]

# This fixture will be called once per class, sicen its a class-scoped fixture
@pytest.mark.usefixtures('printStartAndEndOfRegressCmd')
# This fixture will be called once per testcase, since its a function-scoped fixture
@pytest.mark.usefixtures('printStartAndEndOfTest')
# session-scope fixture
@pytest.mark.usefixtures('setBaseRegressParams')
class TestRegress(object):
	def test_sccg(self):
		print('  ~ ~ ~ running test_sccg  ~ ~ ~ ')

	def test_pgw(self):
		print('  ~ ~ ~ running test_pgw  ~ ~ ~ ')

	def test_sgw(self):
		print('  ~ ~ ~ running test_sgw  ~ ~ ~ ')