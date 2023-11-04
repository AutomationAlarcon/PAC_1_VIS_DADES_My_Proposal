import matplotlib.pyplot as plt


type_crime = ["Homicide", "Rape", "Robbery", "Aggravated assault", "Burglary", "Motor vehicle theft", "All violent crime**"]
type_crime_values = [6.3, 40, 66.1, 268.2, 269.8, 282.7, 380.7]
change_from_2021 = [-0.5, -2.4, 0.6, -4.0, -1.1, 26.8, -6.3]
change_from_2019 = [1.2, -3.6, -15.7, 17.8, -70.7, 61.9, -0.1]

plt.figure(figsize=(10,10))

bars = plt.barh(type_crime, type_crime_values, color='brown')
plt.xlim(0, 450)
plt.legend(['Year 2022'], loc='lower right', fontsize=16)
plt.ylabel('Type of Crime', fontsize=20)
plt.xlabel('Rate per 100.000 people', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


for bar in bars:
    xval = bar.get_width()
    plt.text(xval + 0.05, bar.get_y() + bar.get_height() / 2, round(xval, 2), ha='left', va='center', fontsize=16)

plt.savefig("graph_1", dpi=100, bbox_inches='tight')

pos = list(range(len(type_crime)))
width = 0.5

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

bars_2021 = plt.barh(pos, change_from_2021, width, alpha=0.5, color='grey', label='Change from 2021*')
bars_2019 = plt.barh([p + width for p in pos], change_from_2019, width, alpha=0.5, color='green',
                     label='Change from 2019')

# Adding the corresponding value on top of each bar
for bars in [bars_2021, bars_2019]:
    for bar in bars:
        xval = bar.get_width()
        plt.text(xval + 0.05, bar.get_y() + bar.get_height()/2, round(xval,2), ha='left', va='center', fontsize=16)

# Setting axis labels and ticks
ax.set_xlabel('Rate change', fontsize=20)
ax.set_yticks([p + width/2 for p in pos])
ax.set_yticklabels(type_crime)
plt.ylim(min(pos)-width, max(pos)+width*2)
plt.xlim([-75, max(change_from_2021 + change_from_2019) + 15])
plt.legend(['Change from 2021*', 'Change from 2019'], loc='lower right', fontsize=16)
plt.grid()
plt.ylabel('Type of Crime', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig("graph_2", dpi=100, bbox_inches='tight')
