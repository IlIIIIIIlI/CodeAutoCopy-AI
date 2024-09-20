import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def integrate_files(directory, prefix):
    result = ""
    total_lines = 0
    non_empty_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.jsx', '.ts', '.tsx', '.html', '.css')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                full_path = os.path.join(prefix, relative_path).replace('\\', '/')
                result += f"// {full_path}\n"
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    result += file_content
                    result += "\n\n"
                    
                    # Count lines immediately after reading the file
                    lines = file_content.splitlines()
                    total_lines += len(lines)
                    non_empty_lines += sum(1 for line in lines if line.strip())

    return result, total_lines, non_empty_lines

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, directory)

def integrate():
    directory = entry_path.get()
    prefix = entry_prefix.get().strip()
    if not directory:
        messagebox.showerror("Error", "Please select a directory")
        return
    
    integrated_content, total_lines, non_empty_lines = integrate_files(directory, prefix)
    
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(integrated_content)
        
        message = f"Files integrated and saved to {output_file}\n\n"
        message += f"Total lines: {total_lines}\n"
        message += f"Non-empty lines: {non_empty_lines}"
        messagebox.showinfo("Success", message)

# Create main window
root = tk.Tk()
root.title("Code Integration Tool")

# Set icon
icon_path = resource_path("icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# Create and place components
tk.Label(root, text="Select Directory:").pack(pady=5)
entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)

btn_browse = tk.Button(root, text="Browse", command=select_directory)
btn_browse.pack(pady=5)

tk.Label(root, text="Prefix Path (optional):").pack(pady=5)
entry_prefix = tk.Entry(root, width=50)
entry_prefix.pack(pady=5)

btn_integrate = tk.Button(text="Integrate Code", command=integrate)
btn_integrate.pack(pady=10)

root.mainloop()