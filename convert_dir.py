import os
from latex_figures import create_latex_fig
def folderpng_to_latex(folderpath):
    files = os.listdir(folderpath)

    if not os.path.isdir(folderpath):
        raise ValueError(f"The specified path '{folderpath}' is not a valid directory.")
    
    png_files = []
    for file in files: 
        if file.endswith(".png"):
            png_files.append(file)

    if not png_files:
        print("No PNG files found in the specified folder.")
        return []
    
    output_files = [os.path.splitext(png_file)[0] + ".tex" for png_file in png_files]
    
    for png_file, output_file in zip(png_files, output_files):
        # Call the function to create the LaTeX figure
        create_latex_fig(output_file, png_file)
    
    print(f"Processed {len(png_files)} PNG files.")