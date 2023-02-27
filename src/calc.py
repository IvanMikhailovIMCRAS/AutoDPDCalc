import os
from multiprocessing import Pool
from typing import Any
from avtocalc import cp_from_to
from avtocalc import Contr


def action(param: Any, dir: str = 'sample') -> bool:
    ''' Some action in frame of one folder '''
    folder_name = f'k_angle={param}'
    os.system(f'mkdir {folder_name}')
    cp_from_to(dir, folder_name, 'BONDS')
    cp_from_to(dir, folder_name, 'COORD')
    cp_from_to(dir, folder_name, 'FIELD')
    cp_from_to(dir, folder_name, 'dpd.exe')
    contr = Contr(folder_name)
    contr.options['k_ang'] = param
    contr.print()
    path = os.path.join('.', folder_name, 'dpd.exe')
    command = os.path.join(f'{path} -p {folder_name}', '')
    os.system(command)
    return True


if __name__ == '__main__':

    params = [0., 1., 2., 3.]
    pool = Pool(processes=4)
    result = pool.map(action, params)
