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

    def __str__(self):
        # TODO : As more variables are added, update the return string
        return "MME Grp : %s,\n\t on SpawnId : %s\n\t IMSI range : %s\n" % (self.mmeGrp, self.spawnId, self.mmeImsiRange)

    def printMmeMgExpress(self):
        print('MmeExp class object - ')
        for key,value in self.__dict__.iteritems():
            print('%s : %s' % (key, value))

    def addTestStep(self, testStep, stepCmds=None, stepComment=None):
        logger.info('Adding testStep %s on MME Grp : %s , SpawnId : %s\n' % (testStep, self.mmeGrp, self.spawnId))
        if stepComment:
            self.mmeSeqFileObj.write("# " + stepComment + "\n")
        if stepCmds:
            self.mmeSeqFileObj.write(stepCmds + "\n")
        '''
        For each testStep, update corresponding verification objects/methods
        '''

if __name__ == '__main__':
    mmeGroups = []

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
    print(mmeGrp1)
    mmeGrp1.addTestStep('doAttach', stepCmds='proc attach group 1', stepComment="Attach IMSIs in group 1")
    mmeGrp1.addTestStep('doDetach', stepCmds='proc detach group 1', stepComment="Detach all IMSIs in group 1")

    mmeGrp2 = MmeExp(mmeGrp='2', spawnId='exp32')
    mmeGroups.append(mmeGrp2)
    print(mmeGrp2)
    mmeGrp2.addTestStep('doAttach', stepCmds='proc attach group 2', stepComment="Attach IMSIs in group 2")
    mmeGrp2.addTestStep('mbCmd', stepCmds='proc mbcmd group 2', stepComment="MBCmd on all IMSIs in group 2")
    mmeGrp2.addTestStep('doDetach', stepCmds='proc detach group 2', stepComment="Detach all IMSIs in group 2")

    mmeGrp3 = MmeExp(mmeGrp='3', spawnId='exp23')
    #mmeGroups.append(mmeGrp3)
    append_mmeGrps(mmeGrp3)
    print(mmeGrp3)
    mmeGrp3.addTestStep('doAttach', stepCmds='proc attach group 3', stepComment="Attach IMSIs in group 3")
    mmeGrp3.addTestStep('idle', stepCmds='idle group 3', stepComment="Move all IMSIs in group 3 to IDLE state")
    mmeGrp3.addTestStep('active', stepCmds='active group 3', stepComment="Move all IMSIs in group 3 to ACTIVE state")
    mmeGrp3.addTestStep('doDetach', stepCmds='proc detach group 3', stepComment="Detach all IMSIs in group 3")

    print mmeGroups