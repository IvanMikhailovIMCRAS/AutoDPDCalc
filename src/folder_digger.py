import os
from multiprocessing import Pool
from typing import Any
from itertools import product
from autocalc import cp_from_to
from autocalc import Contr



def action(param: Any, dir: str = 'sample') -> bool:
    ''' Some action in frame of one folder '''
    try:
        #Folder cleaning
        os.system(f'rm {os.path.join(param,"INFOR")}')
        os.system(f'rm {os.path.join(param,"TRACK")}')
        os.system(f'rm {os.path.join(param,"*.ent")}')
        os.system(f'rm {os.path.join(param,"DPDI")}')
        #File renaming 
        os.system(f'mv {os.path.join(param,"COORDF")} {os.path.join(param,"COORD")}')
        os.system(f'mv {os.path.join(param,"VELOCF")} {os.path.join(param,"VELOC")}')
        os.system(f'mv {os.path.join(param,"CONTR")} {os.path.join(param,"CONTRF")}')
        #
        with open(os.path.join(param,"CONTRF"), "r") as file:
            for _ in range(8):
                s = file.readline()      
        os.system(f'rm {os.path.join(param,"CONTRF")}')    
        folder_name = f'{param}'

        os.system(f'cp /home/imc/SEMISHIN/autocalc/sample/dpd.exe {folder_name}')
        contr = Contr(folder_name)
        contr.options['num_step'] = 2000000
        contr.options['num_snapshot'] = 400000
        contr.options['num_track'] = 1000
        contr.options['solvent solvent_on'] = '3 0'
        contr.options['wall_on'] = 1      
        contr.options['interact_on'] = 1  
        contr.options['UL UH dH'] = str(' '.join(s.split()[:3]))
        contr.print()
        # path = os.path.join('.', folder_name, 'dpd.exe')
        # command = os.path.join(f'{path} -p {folder_name}', '')
        # os.system(command)
        return True
    except:
        return False


if __name__ == '__main__':
    path_name = list()
    for current_dir, dirs, files in os.walk('/home/imc/Ivan/Klushin_test/'):
            for dir in dirs:
                tp_path = os.path.join(current_dir, dir)
                if tp_path.count('/') == 6:
                    path_name.append(os.path.join(current_dir, dir))
                # print(os.path.join(current_dir, dir))

    # params = [0., 1., 2., 3.]
    with Pool(processes=4) as pool:
        result = pool.starmap( action, product(path_name, ['folder1']))
    print(result)
    