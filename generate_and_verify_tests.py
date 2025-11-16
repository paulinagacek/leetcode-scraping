"""
Generate tests ONLY from canonical solution using Gemini.
If tests fail, correct ONLY failing tests.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

from dotenv import load_dotenv
from google import genai

# ------------------------------------------------------
# Load Gemini key
# ------------------------------------------------------
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")
MODEL = os.getenv("GEMINI_MODEL")

if not GEMINI_KEY:
    raise RuntimeError("GEMINI_KEY missing in .env")
if not MODEL:
    raise RuntimeError("GEMINI_MODEL missing in .env")

client = genai.Client(api_key=GEMINI_KEY)

# ------------------------------------------------------
# Helper: run pytest and extract failing tests
# ------------------------------------------------------
def run_pytest(test_file: Path) -> Tuple[int, str]:
    """Run pytest, return (exit_code, output)."""
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-q"],
        capture_output=True, text=True
    )
    return proc.returncode, proc.stdout + "\n" + proc.stderr


def extract_failing_tests(pytest_output: str) -> List[str]:
    """
    Parses pytest output, returns list of failing test names.
    Example lines:
        FAILED tests/foo.py::test_large_input - AssertionError ...
    """
    fails = []
    for line in pytest_output.splitlines():
        m = re.search(r"FAILED\s+\S+::(\w+)", line)
        if m:
            fails.append(m.group(1))
    return fails


# ------------------------------------------------------
# Ask Gemini to generate full tests from scratch
# ------------------------------------------------------
def generate_tests_from_solution(canonical_code: str, title_slug: str) -> str:
    prompt = f"""
You are given Leetcode canonical solution to a problem.

Create a **python file** with pytest **unit tests** that can test this canonical solution.
The tests must:
- Import the solution from solutions/{title_slug}.py
- Cover edge cases and large inputs.
- Do NOT modify or re-implement the canonical solution.

Canonical solution:
{canonical_code}
"""
    response = client.models.generate_content(model=MODEL, contents=prompt) # type: ignore
    return response.text


# ------------------------------------------------------
# Ask Gemini to fix ONLY failing tests
# ------------------------------------------------------
def fix_failing_tests(canonical_code: str, full_test_file: str,
                      test_names: List[str]) -> str:

    failing_list = "\n".join(test_names)

    prompt = f"""
You are given a canonical LeetCode solution and a test file that was generated earlier.

Some tests failed. You must **fix ONLY the failing test functions**, not the whole file.

Canonical solution:
{canonical_code}

Full current test file:
{failing_list}

Please output ONLY the corrected updated test file. Do not remove passing tests.
"""
    response = client.models.generate_content(model=MODEL, contents=prompt) # type: ignore
    return response.text


# ------------------------------------------------------
# Main logic
# ------------------------------------------------------
def main(json_path: str):
    problems = json.loads(Path(json_path).read_text())
    tests_dir = Path("tests")
    solutions_dir = Path("sol")

    tests_dir.mkdir(exist_ok=True)
    solutions_dir.mkdir(exist_ok=True)

    for p in problems:
        slug = p.get("titleSlug")
        if not slug:
            continue

        print(f"\n===== {slug} =====")

        solution_file = solutions_dir / f"{slug}.py"

        if not solution_file.exists():
            print(f"❗ Missing canonical solution: {solution_file}")
            continue

        test_file = tests_dir / f"{slug}.py"
        if test_file.exists():
            print(f"😃 Test file already exists! {test_file}")
            continue

        # canonical_code = solution_file.read_text()

        # # 1. Generate tests
        # test_text = generate_tests_from_solution(canonical_code, slug)

        # test_file.write_text(test_text)
        

        # # 2. Run pytest
        # for correction_round in range(3):
        #     code, out = run_pytest(test_file)

        #     if code == 0:
        #         print("✅ All tests passed.")
        #         break

        #     print("❌ Tests failed, extracting failing tests…")
        #     failing = extract_failing_tests(out)

        #     if not failing:
        #         print("⚠️ Pytest failed but no individual failing tests recognized.")
        #         break

        #     print("Failing tests:", failing)

        #     # 3. Ask Gemini to fix ONLY the failing tests
        #     updated_test_file = fix_failing_tests(
        #         canonical_code,
        #         test_file.read_text(),
        #         failing
        #     )

        #     test_file.write_text(updated_test_file)

        # else:
        #     print("❗ Tests still failing after correction attempts.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True)
    args = parser.parse_args()
    main(args.json)

