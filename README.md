# Python Line Counter

A simple and efficient Python script to count lines of code in your project directories. This tool helps you track and analyze the size of your codebase by counting lines in various file types.

## Features

- Counts lines in multiple file types: `.py`, `.html`, `.css`, and `.js`
- Types of file types can be changed in the code
- Ignores common non-code files and directories:
  - `.txt` files
  - `__pycache__` folders
  - `logs` and `log` folders
  - `.git` directory
  - `.venv` directory
- Types of ignored file types and directories can be changed in the code
- Provides detailed statistics by file type
- Supports both single file and directory analysis
- Handles empty lines intelligently (only counts non-empty lines)

## Installation

No installation required! Simply download the script and make it executable:

Current Directory:
```bash
chmod +x count_lines.py
```

Seperate Directory:
```bash
chmod +x count_lines.py /path/to/your/project
```

## Usage

Run the script from the command line:

```bash
# Count lines in current directory
python count_lines.py

# Count lines in a specific directory
python count_lines.py /path/to/your/project
```

## Output

The script will display:
- Total number of lines across all supported file types
- Breakdown of lines by file extension
- Summary statistics

Example output:
```
Counting lines of code in: /path/to/project
Scanning .py, .html, .css, and .js files...
Ignoring .txt files, __pycache__ folders, and log folders...
--------------------------------------------------

Results:
--------------------------------------------------
css files: 1,234 lines
html files: 5,678 lines
js files: 3,456 lines
py files: 2,345 lines
--------------------------------------------------
Total lines of code: 12,713
```

## Requirements

- Python 3.x
- No external dependencies required
