import callflow as proc

def test_procedure():
    print('test_procedure :- ')
    procedure_params = {'ue': '1234567890', 'addr': '921,E,450'}
    proc.do_procedure(profid=23,
                      grpid=23,
                      timeout=33,
                      **procedure_params)

test_procedure()