import os
# Definindo o path para os arquivos de potencial de pseudopotenciais do VASP
# Certifique-se de que o caminho esteja correto para o seu sistema
os.environ['VASP_PP_PATH'] = '/home/public/Programs/vasp.6.5.1/pp'

#os.environ['ASE_VASP_COMMAND'] = 'mpirun -np 1 vasp_std_gpu'
os.environ['ASE_VASP_COMMAND'] = 'mpirun -np 2 vasp_std'

os.environ['NO_STOP_MESSAGE'] = '1' # to avoid warning from mpirun

# Importando o VASP calculator do ASE
import numpy as np
import matplotlib.pyplot as plt
import time

from ase import Atoms, Atom
from ase.build import molecule
from ase.io import write, read
from ase.calculators.vasp import Vasp
from ase.visualize.plot import plot_atoms
from ase.vibrations import Vibrations
from ase.visualize import view
from ase.io import read
from ase.calculators.vasp import Vasp
from ase.md.langevin import Langevin
from ase.io.trajectory import Trajectory
from ase import units
from pathlib import Path

t1 = time.time()
# # 1) Carregar estrutura sI + CO2
# atoms = read("sI_CO2_relaxed.xyz")

# Path("aimd_nvt").mkdir(parents=True, exist_ok=True)


#========================================================================
# Criando calculadora do VASP para realizar single point SCF: `ibrion=-1`
#========================================================================
vasp_calc = Vasp(
    directory='mace_comparison_vasp',
    xc='pbe',
    encut=400,
    ivdw=12, vdw_radius = 10, vdw_cnradius = 10,    # D3(BJ) van der Waals correction
    ismear=0, sigma=0.1,
    ediff=1e-4,       
    isym=0,
    ibrion=-1, nelm=100,                            # single point SCF calculation
    lreal = 'Auto', lwave=False, lcharg=False, lvtot=False
)

#========================================================================
# Efetuando os cálculos ab initio para alguns frames da trajetória `.xyz`
#========================================================================
from tqdm import tqdm
print("Evaluating MACE configurations with VASP")
traj = read('producao_mace_md_sI_CO2_260-K.xyz', ':')

for at in tqdm(traj[::5]): # lendo every 100 frames to save time
    at.calc = vasp_calc
    at.info['energy_vasp'] = at.get_potential_energy()
    at.arrays['forces_vasp'] = at.get_forces()
    at.calc = None  #remove calculator to save memory

# ======= Gravando informações em um novo arquivo só com os frames re-calculados ============ 
# Nesse arquivo temos `energy_mace`, `energy_vasp`, `forces_mace` e `forces_vasp`

write('mace_vs_vasp_md_sI_CO2_260-K.xyz', traj[::5]) #save full result

t2 = time.time()
print('Tempo de execução: ', (t2-t1)/3600, 'horas')