import sys
from mpi4py import MPI
from .ORIS_functions import AddMedia, InitialConditions

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

zips = sys.argv[1]
targets = sys.argv[2].split(",") if len(sys.argv) > 2 and sys.argv[2] else []

if targets:
    if rank == 0:
        print("[INITIAL SCRIPT] Starting AddMedia", flush=True)

    AddMedia(zips, targets)
    comm.Barrier()

    if rank == 0:
        print("[INITIAL SCRIPT] Finished AddMedia", flush=True)

if rank == 0:
    print("[INITIAL SCRIPT] Starting InitialConditions", flush=True)

InitialConditions(zips)
comm.Barrier()

if rank == 0:
    print("[INITIAL SCRIPT] Finished InitialConditions", flush=True)
