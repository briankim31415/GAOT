#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def main() -> int:
    config_root = Path("config") / "examples"
    configs = sorted(config_root.rglob("*.json"))
    if not configs:
        print(f"No configs found under {config_root}", file=sys.stderr)
        return 1

    logs_dir = Path(".logs")
    logs_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = logs_dir / f"run_all_configs_{timestamp}.log"
    print(f"Logging to {log_path}")

    def log(message: str) -> None:
        log_file.write(message + "\n")
        log_file.flush()

    failures = []
    with log_path.open("w", encoding="utf-8") as log_file:
        total = len(configs)
        for idx, config_path in enumerate(configs, start=1):
            log(f"[{idx}/{total}] Running {config_path}")
            try:
                subprocess.run(
                    [sys.executable, "main.py", "--config", str(config_path)],
                    check=True,
                    stdout=log_file,
                    stderr=log_file,
                )
            except subprocess.CalledProcessError as exc:
                failures.append((config_path, exc.returncode))
                log(f"[{idx}/{total}] FAILED {config_path} (exit {exc.returncode})")

        if failures:
            log("Failures:")
            for config_path, returncode in failures:
                log(f"- {config_path} (exit {returncode})")
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
