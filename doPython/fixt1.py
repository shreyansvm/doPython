# Trying fixtures
import pytest

# session-scope fixture
@pytest.fixture(scope="session")
def setBaseRegressParams():
	regressCmdSessParams = {
	 'testbed': 'mvltevm08',
     'forcePcapCollection': 'true'
	}
	print(' ---------- Inside setBaseRegressParams, scope : function ---------- ')
	# yield
	# print(' ---------- End of suite ----------')
	return regressCmdSessParams

@pytest.fixture(scope="class")
def verifyIfRegressSubmittedOnTestbed():
	print('\n ######## ######## ######## Verifying whether regression was successfully submitted on the testbed ######## ######## ######## ')

@pytest.fixture(scope="class")
def imageAndCvsTag():
	print('\n -useimages 10.0/latest_s ')
	print(' -cvs_tag 10_0_current ')

# class-scoped fixture
@pytest.fixture(scope="class")
def printStartAndEndOfRegressCmd(imageAndCvsTag):
	print('\n ######## ######## ######## Firing a regression ######## ######## ######## ')
	yield 
	print('\n ######## ######## ######## Done with firing of regression ######## ######## ######## ')
	verifyIfRegressSubmittedOnTestbed()

# function-scoped fixture
@pytest.fixture()
def printStartAndEndOfTest(setBaseRegressParams):
	print('\n +++++++ +++++++ Start of testcase +++++++ +++++++ ')
	print('\t\t testbed ',setBaseRegressParams['testbed'])
	print('\t\t forcePcapCollection ',setBaseRegressParams['forcePcapCollection'])
	yield 
	print('\n +++++++ +++++++ End of testcase +++++++ +++++++ ')