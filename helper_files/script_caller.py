import subprocess
import sys

def call_script(n=2, dataset="debug", model="ItemKNN", choice_model="rank_based", config="recbole_config_default.yaml"):
    for i in range(1, n + 1):
        command = [
            sys.executable, "main.py", dataset, str(i),
            "--clean",
            "--model", model,
            "--choice-model", choice_model,
            "--config", config,
        ]
        result = subprocess.run(command, check=True)

        if result.returncode == 0:
            print(f"Iteration {i}: Success")
        else:
            print(f"Iteration {i}: Error")