class AllParams(object):
    def __init__(self, **kwargs):
        print('AllParams __init__')
        self.profid = kwargs.get('profid', 10)
        self.grpid = kwargs.get('grpid', 10)
        self.timeout = kwargs.get('timeout', 20)
        self.ue = kwargs.get('ue', '0987654321')
        self.addr = kwargs.get('addr', '123,G,000')
        self.mme_file_id = kwargs.get('mme_file_id', '0x123')
        self.cfs_file_id = kwargs.get('cfs_file_id', '0x444')