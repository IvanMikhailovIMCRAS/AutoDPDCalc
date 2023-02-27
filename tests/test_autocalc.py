from src.autocalc import Contr
import pytest

@pytest.fixture
def opt() -> dict:
    options: dict = {
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
    return options

class TestContr():
    def test_init(self):
        name = 'name'
        cntr = Contr(name)
        print(type(cntr.path))
        assert cntr.path == name
    def test_options(self, opt):
        cntr = Contr('')
        cntr.options['dt'] = 5
        assert cntr.options['dt'] != opt['dt']
        