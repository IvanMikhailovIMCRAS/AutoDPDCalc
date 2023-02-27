import os
from multiprocessing import Pool
from typing import Any
from itertools import product
from src.autocalc import cp_from_to
from src.autocalc import Contr



def action(param: Any, dir: str = 'sample') -> bool:
    ''' Some action in frame of one folder '''
    try:
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
    except:
        return False


if __name__ == '__main__':

    params = [0., 1., 2., 3.]
    with Pool(processes=4) as pool:
        result = pool.starmap( action, product(params, ['folder1']))
    # pool = Pool(processes=4)
    # result = pool.map(lambda x: action(x, dir='folder1'), x = params)
    print(result)
