import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the style & colors for the plots
sns.set_style('darkgrid')
_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Generate some sample data
x = np.linspace(0, 10, 100)

# Define a basic positive trend
basic_trend = 0.1 * x

# Define an uplifted trend, which starts halfway and has a steeper slope
uplifted_trend = basic_trend.copy()
uplift_point = len(x) // 2
additional_uplift = 0.2 * (x[uplift_point:] - x[uplift_point])
uplifted_trend[uplift_point:] += additional_uplift

# Plot the basic trend
plt.plot(x, basic_trend, '--', label='No intervention', color=_colors[1])

# Plot the uplifted trend
plt.plot(x, uplifted_trend, label='With city actions', color=_colors[0])

# Add labels, title, and legend
plt.xlabel('Time')
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
