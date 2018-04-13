import threading
import time
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('loggerInfo.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

mmeGroups = []

'''
Decorator function to return a unique command for each testStep
    and respective comment as well
'''
def testStepToCmdMap(func):
    def func_wrapper(*args, **kwargs):
        mmeObj, testStep = func(*args, **kwargs)

        ''' Return format : stepComment + stepCommand '''

        if testStep == 'doAttach':
            return '# Attach IMSIs in group %s\n' % format(mmeObj.mmeGrp) + \
                   'proc attach group %s\n' % format(mmeObj.mmeGrp)

        elif testStep == 'doDetach':
            return '# Detach IMSIs in group %s\n' % format(mmeObj.mmeGrp) + \
                   'proc detach group %s\n' % format(mmeObj.mmeGrp)

        elif testStep == 'idle':
            return '# Move all IMSIs in group %s to IDLE state\n' % format(mmeObj.mmeGrp) + \
                   'idle group %s\n' % format(mmeObj.mmeGrp)

        elif testStep == 'active':
            return '# Move all IMSIs in group %s to ACTIVE state\n' % format(mmeObj.mmeGrp) + \
                   'active group %s\n' % format(mmeObj.mmeGrp)

        elif testStep == 'mbCmd':
            return '# Send MBCMD for all IMSIs in group %s\n' % format(mmeObj.mmeGrp) + \
                   'mbcmd group %s\n' % format(mmeObj.mmeGrp)

        else:
            logger.info('UNKNOWN CMD received %s on MME Grp : %s , SpawnId : %s\n' % (testStep, mmeObj.mmeGrp, mmeObj.spawnId))
            return '# unknown command on group %s\n' % format(mmeObj.mmeGrp) + \
                   'unknown command on group %s\n' % format(mmeObj.mmeGrp)
    return func_wrapper

'''
MME Class
'''
class MmeExp(object):
    def __init__(self, **kwargs):
        allowed_keys = ['mmeGrp', 'spawnId']
        self.__dict__.update((k, v) for k, v in kwargs.iteritems() if k in allowed_keys)
        for key, value in kwargs.iteritems():
            if key not in allowed_keys:
                logger.error("%s is not a valid variable of class MmeExp." % key)
                raise ValueError("%s is not a valid variable of class MmeExp." % key)
        self.mmeSeqFile = "mmeGrp" + self.mmeGrp + "CmdSeq.txt"
        self.mmeSeqFileObj = open(self.mmeSeqFile,'w')

        # IMSI Range : 123456789010000 , 123456789020000 ..
        self.mmeImsiRange = int("1234567890" + self.mmeGrp + "0000")
        self.cfgFile = 'mmeCfg.file'
        self.logFile = 'mmeLog.file'

    def returnMmeGrpId(self):
        return self.mmeGrp

    def __str__(self):
        # TODO : As more variables are added, update the return string
        return "MME Grp : %s,\n\t on SpawnId : %s\n\t IMSI range : %s\n" % (self.mmeGrp, self.spawnId, self.mmeImsiRange)

    def setProfileParams(self):
        print(' -- Set mme group / profile level params -- ')

    def printMmeExpClassParams(self):
        print('MmeExp class object - ')
        for key,value in self.__dict__.iteritems():
            print('%s : %s' % (key, value))

    def returnMmeExpClassParams(self):
        param = {}
        for key, value in self.__dict__.iteritems():
            param[key] = value
        return param

    def printMmeGrpStats(self):
        print(' -- later add method to print all stats for each mme grp -- ')

    @testStepToCmdMap
    def addTestStep(self, testStep):
        logger.info('Adding testStep %s on MME Grp : %s , SpawnId : %s\n' % (testStep, self.mmeGrp, self.spawnId))
        # if stepComment:
        #     #self.mmeSeqFileObj.write("# " + stepComment + "\n")
        #     return self.mmeSeqFileObj, stepComment
        # if stepCmds:
        #     #self.mmeSeqFileObj.write(stepCmds + "\n")
        #     return self.mmeSeqFileObj, stepCmds
        return self, testStep
        ''' For each testStep, update corresponding verification objects/methods '''

    def execFile(self):
        print(' -- execute file -- ')

    def command(self):
        print(' -- specific command -- ')


''' Class for writing verification / debug logs '''
class VerificationLogs(MmeExp):
    def __init__(self, MmeExp):
        self.logfile = "mmeGrp_" + str(MmeExp.returnMmeGrpId()) + "_log1.txt"
        self.logfileObj = open(self.logfile,'w')

    def __str__(self):
        return "Verification logs are in : %s" % (self.logfile)

    def returnLogFileNameAndObj(self):
        return self.logfile, self.logfileObj


''' Class for verifying events for each MME Grp '''
class Verification(MmeExp):
    def __init__(self, MmeExp):
        print('--- creating Verification class object, using MmeExp object : ', MmeExp)
        self.mmeGrpObj = MmeExp
        logFileObj = VerificationLogs(MmeExp)
        self.logfile, self.logfileObj = logFileObj.returnLogFileNameAndObj()
        self.verificationType = ['type_A', 'type_B', 'type_C']
 
    def __str__(self):
        print(self.mmeGrpObj)
        return "--- printing Verification class object ---- "

    def verify_type_A(self):
        params = self.mmeGrpObj.returnMmeExpClassParams()
        print('\t\t ----- verification type : type_A')

    def verify_type_B(self):
        print('\t\t ----- verification type : type_B')

    def verify_type_C(self):
        print('\t\t ----- verification type : type_C')

    ''' One way of verifying '''
    def verifyAll(self):
        for type in self.verificationType:
            if type == 'type_A':
                self.verify_type_A()
            elif type == 'type_B':
                self.verify_type_B()
            elif type == 'type_C':
                self.verify_type_C()

if __name__ == '__main__':

    # Trying decorator example
    def writeGrpCmdsToFile(func):
        def func_wrapper(*args, **kwargs):
            mmeGroups.append(func(*args, **kwargs))
        return func_wrapper

    @writeGrpCmdsToFile
    def append_mmeGrps(grp):
        return grp

    mmeGrp1 = MmeExp(mmeGrp='1', spawnId='exp32')
    mmeGroups.append(mmeGrp1)
    # mmeGrp1.printMmeExpClassParams()
    print(mmeGrp1)
    mmeGrp1.mmeSeqFileObj.write(mmeGrp1.addTestStep('doAttach'))
    mmeGrp1.mmeSeqFileObj.write(mmeGrp1.addTestStep('doDetach'))

    mmeGrp2 = MmeExp(mmeGrp='2', spawnId='exp32')
    mmeGroups.append(mmeGrp2)
    print(mmeGrp2)
    mmeGrp2.mmeSeqFileObj.write(mmeGrp2.addTestStep('doAttach'))
    mmeGrp2.mmeSeqFileObj.write(mmeGrp2.addTestStep('mbCmd'))
    mmeGrp2.mmeSeqFileObj.write(mmeGrp2.addTestStep('doDetach'))
    #
    mmeGrp3 = MmeExp(mmeGrp='3', spawnId='exp23')
    #mmeGroups.append(mmeGrp3)
    append_mmeGrps(mmeGrp3)
    print(mmeGrp3)
    mmeGrp3.mmeSeqFileObj.write(mmeGrp3.addTestStep('doAttach'))
    mmeGrp3.mmeSeqFileObj.write(mmeGrp3.addTestStep('idle'))
    mmeGrp3.mmeSeqFileObj.write(mmeGrp3.addTestStep('active'))
    mmeGrp3.mmeSeqFileObj.write(mmeGrp3.addTestStep('doDetach'))

    print mmeGroups

    typeA = Verification(mmeGroups[0])
    print(typeA)
    typeA.verifyAll()
    logA = VerificationLogs(mmeGroups[0])
    print(logA)

    mmeGrpsTh = []
    for i in range(50):
        mmeGrpsTh.append(MmeExp(mmeGrp=str(i), spawnId=str(i)))

    for mme in mmeGrpsTh:
        print('mme - ', mme)
