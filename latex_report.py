import json

def create_latex_report(filename, config_file): 
    # Read configuration from the JSON file
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    title = config.get("title", "Default Title")
    tasks = config.get("tasks", [])
    questions = config.get("questions", [])
    
    # Setup the latex document for report
    latex_report = ["\\documentclass[11pt,a4paper,twoside]{article}\n",
                    "\\input{latex_configuration/preamble.tex}\n"
                    "\\graphicspath{{./figures/}}\n",
                    "\n"]
    
    # Structuring the document
    latex_report += [
        "\n\\begin{document}\n", 
        "\\sloppy\n", 
        f"\\title{{{title}}}\n", 
        "\\author{Domantas Jasudas \\\\ Light engineering, Faculty of Physics, Vilnius University}\n", 
        "\\maketitle\n", 
        "\\onehalfspace\n"
    ]
    
    # Abstract section
    latex_report += [
        "\\paragraph*{Abstract:}\n"
        "%Abstract goes here\n\n"
    ]
    
    # Tasks section
    latex_report += ["\\section{Tasks}\n\n",
                     "\\begin{enumerate}\n",]
    for task in tasks:
        latex_report += [
            f"\\item {task}\n"
        ]
    latex_report+=["\\end{enumerate}\n\n"]
    
    # Question section 
    latex_report += ["\\section{Main theoretical questions}\n\n",
                     "\\begin{itemize}\n"]
    for question in questions:
        latex_report += [
            f"\\item {question}\n",
        ]
    latex_report += ["\\end{itemize}\n\n"]
    
    latex_report += ["\\newpage\n\n"]

    # Results and discussion section
    latex_report += [
        "\\section{Results and discussion}\n", 
        "\\subsection{Dividing experiment into parts}\n", 
        "% Delete if not needed\n\n"
    ]
    
    # Conclusions
    latex_report += [
        "\\newpage\n",
        "\\paragraph*{Conclusions:}\n", 
        "%Summarize the main findings and their implications here.\n", 
        "\\end{document}\n"
    ]
    
    # Join the list into a single string and write it to the file
    with open(filename, 'w') as f:
        f.write(''.join(latex_report))  # Join the list into one string before writing
