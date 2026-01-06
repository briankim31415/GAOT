#!/bin/bash
#SBATCH -J gaot_all_configs
#SBATCH -o run_logs/gaot_all_configs/job.o%j
#SBATCH -e run_logs/gaot_all_configs/job.e%j
#SBATCH -A ASC24027
#SBATCH -p gpu-a100-small
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 01:00:00
#SBATCH --mail-type=all
#SBATCH --mail-user=briankim31415@gmail.com

module load cuda python3

cd ..
source .venv/bin/activate
python run_all_configs.py
