__version__ = "2025.11.29.01"
__author__ = "Muthukumar Subramanian"

"""
Python Code Quality Utility:
 - Checks Python files using pycodestyle (120-character limit)
 - Automatically formats code using autopep8
 - Scans only .py files
 - Skips venv, .venv, .git, __pycache__
 - Shows summary and colored output
"""

import subprocess
import sys
import argparse
import os
import colorama

colorama.init(autoreset=True)

SKIP_DIRS = {"venv", ".venv", ".git", "__pycache__"}


def get_python_files(base_path):
    """Recursively collect .py files, skipping unwanted folders."""
    python_files = []

    for root, dirs, files in os.walk(base_path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for f in files:
            if f.endswith(".py"):
                python_files.append(os.path.join(root, f))

    return python_files


def main():
    parser = argparse.ArgumentParser(
        description="Run pycodestyle & autopep8 on Python files (max length 120)"
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Directory to scan (default: current directory)"
    )

    args = parser.parse_args()
    target_path = args.path

    if not os.path.exists(target_path):
        print(f"{colorama.Fore.RED}Error: Path does not exist -> {target_path}")
        sys.exit(1)

    abs_path = os.path.abspath(target_path)
    print(f"\n{colorama.Fore.CYAN}Using target path: {abs_path}\n")

    # Collect Python files
    python_files = get_python_files(target_path)
    total_files = len(python_files)

    print(f"{colorama.Fore.BLUE}Python files found: {total_files}\n")

    if total_files == 0:
        print(f"{colorama.Fore.YELLOW}No Python files to scan.\n")
        return

    # -----------------------------
    # Run pycodestyle
    # -----------------------------
    print(f"{colorama.Fore.MAGENTA}\nRunning pycodestyle (120 max line length)...\n")
    subprocess.run([
        sys.executable, "-m", "pycodestyle",
        "--max-line-length=120",
        target_path
    ], check=False)

    # -----------------------------
    # Run autopep8 auto-fix
    # -----------------------------
    print(f"{colorama.Fore.MAGENTA}\nRunning autopep8 auto-fix...\n")

    autopep8_cmd = [
        sys.executable, "-m", "autopep8",
        "--max-line-length=120",
        "--in-place", "--aggressive", "--recursive",
        target_path
    ]

    subprocess.run(autopep8_cmd, check=False)

    # -----------------------------
    # Run pycodestyle again
    # -----------------------------
    print(f"{colorama.Fore.MAGENTA}\nRe-running pycodestyle after fixes...\n")
    subprocess.run([
        sys.executable, "-m", "pycodestyle",
        "--max-line-length=120",
        target_path
    ], check=False)

    # -----------------------------
    # Summary
    # -----------------------------
    print("\n" + "-" * 60)
    print(f"{colorama.Fore.GREEN}Code Quality Check Completed!")
    print(f"{colorama.Fore.CYAN}Total Python files scanned: {total_files}")
    print(f"{colorama.Fore.YELLOW}Autopep8 formatting applied where needed.")
    print("-" * 60 + "\n")


if __name__ == "__main__":
    main()
