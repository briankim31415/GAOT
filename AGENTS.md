# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the primary entry point; `run_all_configs.py` runs every example config and logs to `.logs/`.
- `src/` contains the implementation: `core/` (configs/train loop), `datasets/` (data loading/graph building), `model/` (GAOT + layers), `trainer/` (static/sequential trainers), and `utils/` (metrics/plotting/scaling).
- `config/examples/` holds JSON configs for `time_indep/` and `time_dep/` runs.
- `datasets/` stores NetCDF data in `time_indep/` and `time_dep/` (see `datasets/README.md` for structure).
- `assets/` and `plots/` hold documentation images and sample outputs; `sbatch/` contains HPC batch scripts and run logs.

## Build, Test, and Development Commands
```bash
python -m venv venv-gaot
source venv-gaot/bin/activate
pip install -r requirements.txt

# Train or test a single config
python main.py --config config/examples/time_indep/poisson_gauss.json

# Run all configs under a folder
python main.py --folder config/examples/time_dep

# Run every example config and capture a combined log
python run_all_configs.py
```
Notes: `--debug` disables multiprocessing; `--visible_devices 0 1` sets CUDA devices.

## Coding Style & Naming Conventions
- Python, 4-space indentation; follow existing docstring-heavy style in `src/`.
- Use `snake_case` for functions/variables and `CapWords` for classes.
- No formatter/linter is enforced; keep imports grouped and avoid large refactors in a single change.

## Testing Guidelines
- No automated test suite or coverage targets are present.
- Use config-based smoke tests (`python main.py --config ...`) and inspect outputs under the `path.*` locations in the config.
- `test.ipynb` is available for exploratory validation.

## Commit & Pull Request Guidelines
- Recent commits use short, sentence-case summaries without prefixes (e.g., "Add dataset configs"). Keep messages concise and imperative.
- PRs should include: purpose, configs used, dataset source, and relevant logs/plots or metrics. Note CUDA/PyTorch versions for performance changes.

## Configuration & Data Tips
- Set `dataset.base_path` to the root of your `.nc` files; `dataset.name` matches the filename without extension.
- Large datasets are expected; avoid committing raw data files unless explicitly intended.
