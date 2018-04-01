class testStep(object):
    def __init__(self, testStep, mmeGrp, **kwargs):
        self.testStep = testStep
        self.mmeGrp = mmeGrp
        allowed_keys = ['testStep', 'mmeGrp', 'session', 'ratType']
        self.__dict__.update((k, v) for k, v in kwargs.iteritems() if k in allowed_keys)
        for key, value in kwargs.iteritems():
            if key not in allowed_keys:
                raise ValueError("%s is not a valid variable of class testStep." % key)

    def __str__(self):
        return "TestStep : %s,\n\t on MME Grp : %s\n\t MME Session : %s\n\t RAT-Type : %s\n" % (self.testStep, self.mmeGrp, self.session, self.ratType)


    def printTestStep(self):
        print('Test Step : ', self.testStep)
        print('\t On Mme Grp : ', self.mmeGrp)

        # if hasattr(self, "session"):
        #     print('\t Mme Session : ', self.session)
        # if hasattr(self, "ratType"):
        #     print('\t RAT-Type : ', self.ratType)
        # - OR -
        for key,value in self.__dict__.iteritems():
            print('%s : ' % key, value)

# List of 'testStep' class objects
testStepsList = []

doAttach = testStep('doAttach', '1', session='session1', ratType='WLAN')
print(dir(doAttach))
print(doAttach)
testStepsList.append(doAttach)
doDetach = testStep('doDetach', '1', session='session1', ratType='WLAN')
testStepsList.append(doDetach)

doAttach = testStep('doAttach', '2', session='session2', ratType='LTE')
testStepsList.append(doAttach)
doDetach = testStep('doDetach', '2', session='session2', ratType='LTE')
testStepsList.append(doDetach)

for subTest in testStepsList:
    subTest.printTestStep()