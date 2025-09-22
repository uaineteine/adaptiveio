import os

from uainepydat import fileio
from uainepydat import datatransform


main_package_name = "adaptiveio"  # Your main package name
relative_directory = "../" + main_package_name  # Your source code root
absolute_directory = os.path.abspath(relative_directory)

# --- Recursive listing of all .py files ---
def list_python_files(base_dir):
    python_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                python_files.append(os.path.join(root, file))
    return python_files

python_files = list_python_files(absolute_directory)

# --- Convert file paths to module import paths ---
def filepath_to_module(filepath, base_dir):
    rel_path = os.path.relpath(filepath, base_dir)
    module_path = os.path.splitext(rel_path)[0]
    module_path = module_path.replace(os.path.sep, ".")
    return main_package_name + "." + module_path

# --- Group modules by top-level subfolder ---
from collections import defaultdict
subfolder_modules = defaultdict(list)
for f in python_files:
    rel_path = os.path.relpath(f, absolute_directory)
    parts = rel_path.split(os.path.sep)
    if len(parts) > 1:
        subfolder = parts[0]
    else:
        subfolder = "(root)"
    mod = filepath_to_module(f, absolute_directory)
    subfolder_modules[subfolder].append(mod)

# --- Update pre-compile index.rst_pre ---
pre_compile_path = "source/index.rst_pre"
pre_str = fileio.read_file_to_string(pre_compile_path)

# --- Purpose ---
purpose_path = "../meta/purpose.txt"
pur = fileio.read_file_to_string(purpose_path)
pur = datatransform.break_into_lines(pur)
post_str = datatransform.replace_between_tags(pre_str, "purpose", pur, deleteTags=True)

# --- Changelog ---
changelog_path = "../meta/changelog.txt"
chlog = fileio.read_file_to_string(changelog_path)
chlog = datatransform.break_into_lines(chlog)
post_str = datatransform.replace_between_tags(post_str, "changelog", chlog, deleteTags=True)

# --- Optional description ---
description_path = "../meta/description.txt"
if os.path.exists(description_path):
    description_content = fileio.read_file_to_string(description_path)
    description_content = datatransform.break_into_lines(description_content)
    post_str = datatransform.replace_between_tags(post_str, "description", description_content, deleteTags=True)
else:
    print(f"Warning: {description_path} does not exist. Skipping description replacement.")

# --- Write out final index.rst ---
post_compile_path = "source/index.rst"
with open(post_compile_path, "w", encoding="utf-8") as text_file:
    text_file.write(post_str)

print("Updated rst file and subfolder pages.")
