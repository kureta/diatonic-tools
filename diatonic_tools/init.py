import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-darkgrid')

# Set figure size and DPI
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# Set font sizes
plt.rcParams['font.size'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Enable grid
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.7

# Set default colormap
plt.rcParams['image.cmap'] = 'viridis'

# Set tight layout to avoid overlapping
plt.rcParams['figure.autolayout'] = True

# Set seaborn theme for better aesthetics
sns.set_theme()