import boolevard as blv
import pandas as pd
import zipfile
import os
import re
import sys
from pyeda.inter import expr
from mpi4py import MPI
import shutil
from .ORIS_functions import SampleModels

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

zip_path = sys.argv[1]
sample_size = int(sys.argv[2]) if len(sys.argv) > 2 else 10
th = int(sys.argv[3]) if len(sys.argv) > 3 else 300

SampleModels(zip_path, sample_size=sample_size, th=th)
