import matplotlib.pyplot as plt
import numpy as np

# Data extracted from the JSON (using the best binding energy from mode 1)
data = {
    "Wild-type": {
        "Apigenin": -7.9,
        "CD38_Inhibitor_1": -7.2,
        "CD38_Inhibitor_2": -6.9,
        "CD38_Inhibitor_3": -6.5,
        "Kuromanin_chloride": -8.1
    },
    "Mutation-1": {
        "Apigenin": -5.7,
        "CD38_Inhibitor_1": -5.9,
        "CD38_Inhibitor_2": -5.9,
        "CD38_Inhibitor_3": -5.6,
        "Kuromanin_chloride": -5.9
    },
    "Mutation-2": {
        "Apigenin": -7.3,
        "CD38 Inhibitor 1": -6.5,
        "CD38 Inhibitor 2": -5.0,
        "CD38 Inhibitor 3": -5.3,
        "Kuromanin Chloride": -6.0
    },
    "Mutation-3": {
        "Apigenin": -6.3,
        "CD38 Inhibitor 1": -5.4,
        "CD38 Inhibitor 2": -5.7,
        "CD38 Inhibitor 3": -5.9,
        "Kuromanin chloride": -5.9
    }
}

# List experiments and ligands
experiments = list(data.keys())
# Create a union of all ligand names
all_ligands = set()
for exp in experiments:
    all_ligands.update(data[exp].keys())
all_ligands = sorted(all_ligands)  # sort for consistency

# Create bar positions
n_experiments = len(experiments)
n_ligands = len(all_ligands)
bar_width = 0.2  # adjust as needed

# Create an index for each ligand category on the x-axis
index = np.arange(n_ligands)

# Plot each experimental group as a set of bars
plt.figure(figsize=(10, 6))
for i, exp in enumerate(experiments):
    affinities = []
    # For ligands missing in an experiment, we set to None or skip them.
    # Here we simply use 0 if missing (you might handle missing data differently)
    for ligand in all_ligands:
        affinities.append(data[exp].get(ligand, 0))
        
    # Offset each group's bars by i * bar_width
    plt.bar(index + i * bar_width, affinities, bar_width, label=exp)

# Labeling the graph
plt.xlabel("Ligands")
plt.ylabel("Mode 1 Binding Energy (kcal/mol)")
plt.title("Comparative Binding Affinities Across Protein–Ligand Combinations")
plt.xticks(index + bar_width * (n_experiments - 1) / 2, all_ligands, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
