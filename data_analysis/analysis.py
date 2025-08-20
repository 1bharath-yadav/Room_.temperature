import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Data Definition ---
# Quarterly Patient Satisfaction Scores for 2024
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Score": [0.02, 3.09, 1.1, 3.58]
}

# Industry target
industry_target = 4.5

# --- Data Processing ---
df = pd.DataFrame(data)
average_score = df["Score"].mean()

# --- Visualization ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the quarterly scores
ax.plot(df["Quarter"], df["Score"], marker='o', linestyle='-', color='b', label='Quarterly Score')

# Add a line for the average score
ax.axhline(y=average_score, color='r', linestyle='--', label=f'2024 Average ({average_score:.2f})')

# Add a line for the industry target
ax.axhline(y=industry_target, color='g', linestyle='--', label=f'Industry Target ({industry_target})')

# Add data labels for each quarter's score
for i, txt in enumerate(df['Score']):
    ax.annotate(txt, (df['Quarter'][i], df['Score'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# Set plot titles and labels
ax.set_title('2024 Quarterly Patient Satisfaction Score Analysis', fontsize=16)
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Satisfaction Score', fontsize=12)
ax.set_ylim(0, 5)
ax.legend(loc='best')

# --- Save the Output ---
# Ensure the output directory exists
output_dir = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, 'patient_satisfaction_trend.png')
plt.savefig(output_path)

print(f"Chart saved to {output_path}")
