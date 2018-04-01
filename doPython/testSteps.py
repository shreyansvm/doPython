class testStep(object):
    def __init__(self, testStep, mmeGrp):
        self.testStep = testStep
        self.mmeGrp   = mmeGrp

    def printTestStep(self):
        print('Test Step : ', self.testStep)
        print('\t On Mme Grp : ', self.mmeGrp)

'''
MmeSeqFile is derived class of testStep class
'''
class MmeSeqFile(testStep):
    def __init__(self):
        self.mmeGrp = testStep.mmeGrp



A = testStep('doAttach', '1')
A.printTestStep()

B = testStep('doDetach', '1')
B.printTestStep()