#!/bin/bash
#SBATCH -J gaot_poisson_gauss
#SBATCH -o run_logs/gaot_poisson_gauss/job.o%j
#SBATCH -e run_logs/gaot_poisson_gauss/job.e%j
#SBATCH -A ASC24027
#SBATCH -p gpu-a100
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 02:00:00
#SBATCH --mail-type=all
#SBATCH --mail-user=briankim31415@gmail.com

module load cuda python3

cd ..
source .venv/bin/activate
python main.py --config config/examples/time_indep/poisson_gauss.json
