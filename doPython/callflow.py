import AllParams as master_params

def do_procedure(profid=1,
                 grpid=1,
                 timeout=1,
                 **kwargs):
    print('do_procedure : profid : ',profid)
    print('do_procedure : grpid : ', grpid)
    print('do_procedure : timeout : ', timeout)
    print('do_procedure : rest -- : ', kwargs)

    local_param = {'profid': profid,
                   'grpid': grpid,
                   'timeout': timeout,
                   'ue': kwargs.get('ue')}

    # param_obj = master_params.AllParams(profid=profid, grpid=grpid, timeout=timeout)
    param_obj = master_params.AllParams(**local_param)
    print('do_procedure : param_obj.profid : ', param_obj.profid)
    print('do_procedure : param_obj.grpid : ', param_obj.grpid)
    print('do_procedure : param_obj.timeout : ', param_obj.timeout)
    print('do_procedure : param_obj.ue : ', param_obj.ue)
    print('do_procedure : param_obj.addr : ', param_obj.addr)
    print('do_procedure : param_obj.mme_file_id : ', param_obj.mme_file_id)
    print('do_procedure : param_obj.cfs_file_id : ', param_obj.cfs_file_id)

    param_obj_2 = master_params.AllParams()
    print('do_procedure : param_obj_2.profid : ', param_obj_2.profid)
    print('do_procedure : param_obj_2.grpid : ', param_obj_2.grpid)
    print('do_procedure : param_obj_2.timeout : ', param_obj_2.timeout)
    print('do_procedure : param_obj_2.ue : ', param_obj_2.ue)
    print('do_procedure : param_obj_2.addr : ', param_obj_2.addr)
    print('do_procedure : param_obj_2.mme_file_id : ', param_obj_2.mme_file_id)
    print('do_procedure : param_obj_2.cfs_file_id : ', param_obj_2.cfs_file_id)