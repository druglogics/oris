import sys
from mpi4py import MPI
from .ORIS_functions import FilterLazyModels

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

zip_path = sys.argv[1]
timeout  = int(sys.argv[2]) if len(sys.argv) > 2 else 20

FilterLazyModels(zip_path, timeout=timeout)
