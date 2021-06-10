import subprocess

def calculate(value):
    result = subprocess.run(
    value,capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    return 0