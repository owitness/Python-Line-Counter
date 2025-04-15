#!/usr/bin/env python3
import os
import argparse
from pathlib import Path

def count_lines_in_file(file_path):
    """Count the number of lines in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())  # Only count non-empty lines
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def count_lines_in_directory(directory_path):
    """
    Count lines of code in .py, .html, .css, and .js files,
    ignoring .txt files, __pycache__ folders, and log folders.
    """
    total_lines = 0
    file_counts = {}
    allowed_extensions = {'.py', '.html', '.css', '.js'}
    ignored_dirs = {'__pycache__', 'logs', 'log', '.git', '.venv'}

    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        # Remove ignored directories
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        
        for file in files:
            file_path = Path(root) / file
            extension = file_path.suffix.lower()
            
            # Skip if not in allowed extensions
            if extension not in allowed_extensions:
                continue
            
            # Count lines in the file
            lines = count_lines_in_file(file_path)
            total_lines += lines
            
            # Update file type statistics
            file_counts[extension] = file_counts.get(extension, 0) + lines

    return total_lines, file_counts

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Count lines of code in a project directory.'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default=os.getcwd(),
        help='Path to the project directory (defaults to current directory)'
    )
    args = parser.parse_args()
    
    directory = args.directory
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        return
    
    print(f"Counting lines of code in: {directory}")
    print("Scanning .py, .html, .css, and .js files...")
    print("Ignoring .txt files, __pycache__ folders, and log folders...")
    print("-" * 50)
    
    total_lines, file_counts = count_lines_in_directory(directory)
    
    # Print results
    print("\nResults:")
    print("-" * 50)
    for ext, count in sorted(file_counts.items()):
        print(f"{ext[1:]} files: {count:,} lines")
    print("-" * 50)
    print(f"Total lines of code: {total_lines:,}")

if __name__ == "__main__":
    main() 