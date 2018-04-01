'''
MmeSeqFile is derived class of testStep class
'''
class MmeExp(object):
    def __init__(self, **kwargs):
        allowed_keys = ['mmeGrp', 'spawnId']
        self.__dict__.update((k, v) for k, v in kwargs.iteritems() if k in allowed_keys)
        for key, value in kwargs.iteritems():
            if key not in allowed_keys:
                raise ValueError("%s is not a valid variable of class MmeExp." % key)
        self.mmeSeqFile = "mmeGrp" + self.mmeGrp + "CmdSeq.txt"
        self.mmeSeqFileObj = open(self.mmeSeqFile,'w')
        # TODO : Add a variable with IMSI range based on MME GrpId

    def __str__(self):
        return "MME Grp : %s,\n\t on SpawnId : %s\n" % (self.mmeGrp, self.spawnId)

    def printMmeMgExpress(self):
        print('MmeExp class object - ')
        for key,value in self.__dict__.iteritems():
            print('%s : %s' % (key, value))

    def addTestStep(self, testStep, stepCmds=None, stepComment=None):
        print('Adding testStep %s on MME Grp : %s , SpawnId : %s\n' % (testStep, self.mmeGrp, self.spawnId))
        if stepComment:
            self.mmeSeqFileObj.write("# " + stepComment + "\n")
        if stepCmds:
            self.mmeSeqFileObj.write(stepCmds + "\n")
        '''
        For each testStep, update corresponding verification objects/methods
        '''


mmeGrp1 = MmeExp(mmeGrp='1', spawnId='exp32')
print(mmeGrp1)
mmeGrp1.addTestStep('doAttach', stepCmds='proc attach group 1', stepComment="Attach IMSIs in group 1")
mmeGrp1.addTestStep('doDetach', stepCmds='proc detach group 1', stepComment="Detach all IMSIs in group 1")