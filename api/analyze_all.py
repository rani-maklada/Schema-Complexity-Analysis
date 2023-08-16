import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the correlation data from the CSV file
df = pd.read_csv('correlation_data.csv')

# Set up plot styling
plt.style.use('seaborn-whitegrid')
plt.rcParams.update({'font.size': 12, 'axes.facecolor': '#f0f0f0'})

# Create a new figure with desired size
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(df['Number of Commits'], df['Number of Tables'], df['Number of Issues'], 
           c='#4374B3', marker='o', label='Data Points')
ax.set_xlabel('Number of Commits')
ax.set_ylabel('Number of Tables')
ax.set_zlabel('Number of Issues')
ax.set_title('3D Correlation Analysis', color='#333333')

# Customize legend
legend = ax.legend()
legend.get_frame().set_linewidth(0)
legend.get_texts()[0].set_color('#333333')

# Save the correlation plot as a larger PNG image
plt.savefig('correlation_3D_plot.png', dpi=300)

plt.show()
