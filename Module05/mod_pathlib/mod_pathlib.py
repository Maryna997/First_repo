from pathlib import PurePath 
p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)
print("Suffix:", p.suffix)
print("Parent:", p.parent)

from pathlib import Path
p = Path("example.txt")
p.write_text("Hello world!")
print(p.read_text())
print("Exists:", p.exists())

base_path = Path("/usr/bin")
full_path = base_path / "subdir" / "script.py"
print(full_path)

relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
current_working_directory = Path("C:\Projects GoIT\Python_course_GoIT\Module05")
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)

original_name = Path("documents/example.txt")
new_path = original_name.with_name("report.txt")
print(new_path)


original_name = Path("documents/example.txt")
new_path = original_name.with_suffix(".md")
print(new_path)


file_path = Path("example.txt")
file_path.write_text("Привіт світ!", encoding="utf-8")

file_path = Path("example.txt")
text = file_path.read_text(encoding="utf-8")
print(text)

file_path= Path("example.bin")
data = b"Python is great!"
file_path.write_bytes(data)
binary_data = file_path.read_bytes()
print(binary_data)

file_path = Path("C:\Projects GoIT\Python_course_GoIT\Module05\example.txt")
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")

import time
file_path = Path("C:\Projects GoIT\Python_course_GoIT\Module05\example.txt")
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")