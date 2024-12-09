import os

def create_latex_fig(outputfile, fig, caption='Figure caption', outputdir='latex_figures'):
    # Ensure the output directory exists
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    
    # LaTeX figure code
    latex_fig = (
        "\n\n"
        "%------------------------------FIGURE------------------------------\n"
        "\\begin{figure}[ht!]\n"
        "   \\centering\n"
        f"   \\includegraphics[width=0.9\\textwidth]{{{fig}}}\n"
        f"   \\caption{{\\small {caption}}}\n"
        "\\end{figure}\n"
        "%------------------------------FIGURE------------------------------\n"
        "\n\n"
    )

    # Full path to the output file
    filepath = os.path.join(outputdir, outputfile)
    
    # Write to the output file
    with open(filepath, 'w') as f:  
        f.write(latex_fig)
    
