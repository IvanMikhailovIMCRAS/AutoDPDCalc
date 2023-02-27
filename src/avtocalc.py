import os


class Contr:
    def __init__(self, path: str):
        self.path = path
        self.options: dict = {
            'dt': 0.04,
            'l_bond': 0.69336127,
            'k_bond': 128.0,
            'k_ang': 10.0,
            'num_step': 1000,
            'num_snapshot': 1000,
            'num_track': 1000,
            'wall': 25.0,
            'wall_on': 0,
            'solvent solvent_on': '3 1',
            'interact_on': 0,
            'UL UH dH': '4.16016762 2.0 0.1'
        }

    def print(self) -> None:
        ''' Print CONTR file '''
        path: str = os.path.join(self.path, 'CONTR')
        file = open(path, 'w')
        for opt in self.options:
            file.write(f'{self.options[opt]: <20}  {opt} \n')
        file.close()


def cp_from_to(dir1: str, dir2: str, file: str) -> None:
    ''' Copy file from dir1 to dir2 '''
    path: str = os.path.join(dir1, file)
    os.system(f'cp {path} {dir2}')
