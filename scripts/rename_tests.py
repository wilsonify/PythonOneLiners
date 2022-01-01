import glob
import os
from shutil import move

for f in glob.glob("/mnt/SSD1/repos/PythonOneLiners/tests/test_python_one_liners/**/*.py", recursive=True):
    print(f"f={f}")
    f_root, f_ext = os.path.splitext(f)
    f_head, f_tail = os.path.split(f_root)
    f_head_head, f_head_tail = os.path.split(f_head)
    dst_dir = f"{f_head_head}/test_{f_head_tail}"
    dst = f"{f_head_head}/test_{f_head_tail}/test_{f_tail}{f_ext}"
    print(f"f_ext = {f_ext}")
    print(f"f_root = {f_root}")
    print(f"f_head = {f_head}")
    print(f"f_tail = {f_tail}")
    print(f"f_head_head = {f_head_head}")
    print(f"f_head_tail = {f_head_tail}")
    print(f"dst = {dst}")
    os.makedirs(dst_dir, exist_ok=True)
    move(src=f, dst=dst)
