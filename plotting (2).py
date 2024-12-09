import matplotlib.pyplot as plt


def format_figure(x_label, y_label, title, width, height, label_font, title_font):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.tick_params(top=True, bottom=True, left=True, right=True, direction='in', width=2)
    ax.set_xlabel(x_label, fontsize=label_font, horizontalalignment='left')
    ax.set_ylabel(y_label, fontsize=label_font, verticalalignment='bottom')
    ax.set_title(title, fontsize=title_font)
    return fig, ax

def line_plot(x_value_list, y_value_list, labels, output_file, x_label, y_label, title, width, height, label_font, title_font):
    fig, ax = format_figure(x_label, y_label, title, width, height, label_font, title_font)

    for x, y, label in zip(x_value_list, y_value_list, labels):
        ax.plot(x, y, label=label)

    ax.legend()
    plt.savefig(output_file)
    plt.show()

def scatter_plot(x_value_list, y_value_list, labels, output_file, x_label, y_label, title, width, height, label_font, title_font):
    fig, ax = format_figure(x_label, y_label, title, width, height, label_font, title_font)

    for x, y, label in zip(x_value_list, y_value_list, labels):
        ax.scatter(x, y, label=label)

    ax.legend()
    plt.savefig(output_file)
    plt.show()
