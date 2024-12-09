from plotting import scatter_plot, line_plot
import json
import pandas as pd
import os
from typing import List

def generate_plot(configfile: str) -> None:
    # Load configuration from a JSON file
    try:
        with open(configfile, "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{configfile}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Configuration file '{configfile}' is not a valid JSON.")

    # Extract configuration parameters
    x_keys = config.get("x_keys", [])
    y_keys = config.get("y_keys", [])
    input_files = config.get("input_files", [])
    output_file = config.get("output_file", "output.png")
    plot_type = config.get("plot_type", "scatter_plot")
    x_label = config.get("x_label", "x")
    y_label = config.get("y_label", "y")
    title = config.get("title", "Title")
    labels = config.get("labels", input_files)
    skiprows = config.get("skiprows", 0)
    figure_width = config.get("figure_width", 16)
    figure_height = config.get("figure_height", 9)
    labels_fontsize = config.get("labels_fontsize", 18)
    title_fontsize = config.get("title_fontsize", 26)

    # Validate configuration lengths
    if len(input_files) != len(x_keys) or len(input_files) != len(y_keys):
        raise ValueError("Mismatch in lengths of input_files, x_keys, and y_keys.")

    # Reading CSV and storing x_values and y_values
    x_values_list: List[pd.Series] = []
    y_values_list: List[pd.Series] = []
    
    for file, x_key, y_key in zip(input_files, x_keys, y_keys):
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file '{file}' not found.")
        try:
            data = pd.read_csv(file, skiprows=skiprows)
        except pd.errors.ParserError:
            raise ValueError(f"Error reading CSV file '{file}'. Please check the format.")
        
        if x_key not in data.columns or y_key not in data.columns:
            raise KeyError(f"Columns '{x_key}' or '{y_key}' not found in {file}.")
        
        x_values_list.append(data[x_key])
        y_values_list.append(data[y_key])

    # Prepare plot parameters
    plot_args = {
        'labels': labels,
        'output_file': output_file,
        'x_label': x_label,
        'y_label': y_label,
        'title': title,
        'width': figure_width,
        'height': figure_height,
        'label_font': labels_fontsize,
        'title_font': title_fontsize
    }

    # Generate plot
    if plot_type == 'scatter_plot':
        scatter_plot(x_values_list, y_values_list, **plot_args)
    elif plot_type == 'line_plot':
        line_plot(x_values_list, y_values_list, **plot_args)
    else:
        raise ValueError(f"Plot type '{plot_type}' is not supported. Please use 'scatter_plot' or 'line_plot'.")
