import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the correlation data from the CSV file
df = pd.read_csv('correlation_data.csv')

# Calculate correlation
correlation = df['Number of Commits'].corr(df['Number of Tables'])

# Set up plot styling
plt.style.use('seaborn-whitegrid')
plt.rcParams.update({'font.size': 12, 'axes.facecolor': '#f0f0f0'})

# Create a new figure with desired size
fig = plt.figure(figsize=(10, 8))

# Plot the correlation
plt.scatter(df['Number of Commits'], df['Number of Tables'], color='#4374B3', marker='o', label='Data Points')
plt.xlabel('Number of Commits')
plt.ylabel('Number of Tables')
plt.title('Correlation Analysis', color='#333333')

# Calculate polynomial trend line
poly_degree = 2
coefficients = np.polyfit(df['Number of Commits'], df['Number of Tables'], poly_degree)
polynomial = np.poly1d(coefficients)
x_vals = np.linspace(df['Number of Commits'].min(), df['Number of Commits'].max(), 100)
y_vals = polynomial(x_vals)
plt.plot(x_vals, y_vals, color='#FF7F0E', linewidth=2, label=f'Trend Line (degree {poly_degree})')

# Place the correlation label using plt.annotate()
label_text = f'Correlation: {correlation:.2f}'
plt.annotate(label_text, xy=(0.5, 0.9), xycoords='axes fraction', ha='center', color='#555555')

# Customize legend
legend = plt.legend()
legend.get_frame().set_linewidth(0)
legend.get_texts()[0].set_color('#333333')

# Customize grid lines
plt.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.5)

# Save the correlation plot as a larger PNG image
plt.savefig('correlation_plot.png', dpi=300)

plt.show()
