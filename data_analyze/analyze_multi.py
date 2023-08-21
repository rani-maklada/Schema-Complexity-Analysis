import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Read the correlation data from the CSV file
    df = pd.read_csv('data_analyze/correlation_data.csv')

    # Create a function to handle the plotting and customization
    def plot_scatter(x, y, x_label, y_label, marker_style, color, plot_title, file_name):
        plt.figure(figsize=(10, 8))
        plt.scatter(x, y, color=color, marker=marker_style, label='Data Points')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(plot_title, color='#333333')
        plt.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.5)
        plt.legend()
        plt.savefig(file_name, dpi=300)
        plt.show()

    # 1. Plot for "Number of Commits" vs. "Number of Issues"
    plot_scatter(df['Number of Commits'], df['Number of Issues'], 
                'Number of Commits', 'Number of Issues', 
                'o', '#4374B3', 'Commits vs Issues', 'commits_vs_issues.png')

    # 2. Plot for "Number of Commits" vs. "Number of Tables"
    plot_scatter(df['Number of Commits'], df['Number of Tables'], 
                'Number of Commits', 'Number of Tables', 
                's', '#FF7F0E', 'Commits vs Tables', 'commits_vs_tables.png')

    # 3. Plot for "Number of Tables" vs. "Number of Issues"
    plot_scatter(df['Number of Tables'], df['Number of Issues'], 
                'Number of Tables', 'Number of Issues', 
                '^', '#2CA02C', 'Tables vs Issues', 'tables_vs_issues.png')

    # Calculate "repo_complexity"
    df['repo_complexity'] = df['Number of Commits'] + df['Number of Issues']

    # Plot for "repo_complexity" vs "Number of Tables" (schema_complexity)
    plot_scatter(df['repo_complexity'], df['Number of Tables'], 
                'Repo Complexity (Commits + Issues)', 'Number of Tables (Schema Complexity)', 
                'd', '#D62728', 'Repo Complexity vs Schema Complexity', 'repo_vs_schema_complexity.png')

if __name__ == '__main__':
    main()
