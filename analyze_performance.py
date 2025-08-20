import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
satisfaction_scores = [0.02, 3.09, 1.1, 3.58]
average_score = 1.95
industry_target = 4.5

# Create the plot
plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, satisfaction_scores, color='skyblue', label='Quarterly Score')
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')
plt.axhline(y=average_score, color='g', linestyle='-', label=f'Average Score ({average_score})')

# Add labels and title
plt.xlabel('Quarter')
plt.ylabel('Patient Satisfaction Score')
plt.title('Quarterly Patient Satisfaction Scores vs. Industry Target')
plt.ylim(0, 5)
plt.legend()

# Add data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom', ha='center') # va: vertical alignment

# Save the plot
plt.savefig('performance.png')

print("Data analysis complete. Visualization saved as performance.png")
