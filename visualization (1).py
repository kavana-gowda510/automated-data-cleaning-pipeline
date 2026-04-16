import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("clean_data.csv")

# graph 1
plt.scatter(data["studytime"], data["G3"])
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.title("Study Time vs Final Grade")
plt.savefig("study_time_vs_grade.png")
plt.show()

# graph 2
plt.scatter(data["absences"], data["G3"])
plt.xlabel("Absences")
plt.ylabel("Final Grade")
plt.title("Absences vs Final Grade")
plt.savefig("absences_vs_grade.png")
plt.show()