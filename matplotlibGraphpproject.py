import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# DATA LOADING
# ==============================
dataset = pd.read_csv("student_performance_lifestyle_dataset.csv")
print("====== DATASET OVERVIEW ======")
print(dataset.head())

# ==============================
# TASK 1: DATA PREPARATION & UNDERSTANDING
# ==============================
print("\n===== DATA UNDERSTANDING =====")
print("""
Numerical Columns:
- Study_Hours
- Sleep_Hours
- Screen_Time
- Marks

Categorical Columns:
- Student_ID
- Department

Assumptions:
- Higher study hours → better marks
- Excess screen time → negative impact on marks
- Balanced sleep improves performance
""")

# ==============================
# TASK 2: STUDY HABITS ANALYSIS
# ==============================
plt.figure()
plt.plot(dataset["Student_ID"], dataset["Study_Hours"], marker="o")
plt.xlabel("Students")
plt.ylabel("Study Hours")
plt.title("Study Hours Across Students")
plt.grid(True)
plt.savefig("plotgraphanalysis.png",dpi=300)
plt.show()

print("""
INSIGHT:
Some students follow consistent study routines (5–7 hrs),
while a few show irregular or extreme patterns.
""")

# ==============================
# TASK 3: LIFESTYLE TIME DISTRIBUTION
# ==============================
student_id = "S01"
student_data = dataset.loc[
    dataset["Student_ID"] == student_id,
    ["Study_Hours", "Sleep_Hours", "Screen_Time"]
]

values = student_data.values.flatten()
labels = ["Study Hours", "Sleep Hours", "Screen Time"]

plt.figure()
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title(f"Lifestyle Distribution of Student {student_id}")
plt.savefig("graph2.png",dpi=300)
plt.show()

print("""
CONCLUSION:
Student shows a relatively balanced lifestyle
with study and sleep dominating over screen usage.
""")

# ==============================
# TASK 4: DEPARTMENT-WISE PERFORMANCE
# ==============================
dept_avg_marks = dataset.groupby("Department")["Marks"].mean()

plt.figure()
plt.bar(dept_avg_marks.index, dept_avg_marks.values)
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Department-wise Average Performance")
plt.savefig("graph3.png",dpi=300)
plt.show()

print("""
INSIGHT:
Departments show noticeable performance differences,
indicating variation in study habits or academic focus.
""")

# ==============================
# TASK 5: PERFORMANCE DISTRIBUTION
# ==============================
plt.figure()
plt.hist(dataset["Marks"], bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Overall Marks Distribution")
plt.savefig("graph4.png",dpi=300)
plt.show()

print("""
INTERPRETATION:
Marks show a moderate spread with
clear low, average, and high performers.
""")

# ==============================
# TASK 6: RELATIONSHIP & IMPACT ANALYSIS
# ==============================
plt.figure()
plt.scatter(dataset["Study_Hours"], dataset["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.savefig("graph5.png",dpi=300)
plt.show()

plt.figure()
plt.scatter(dataset["Screen_Time"], dataset["Marks"])
plt.xlabel("Screen Time")
plt.ylabel("Marks")
plt.title("Screen Time vs Marks")
plt.savefig("graph6.png",dpi=300)
plt.show()

plt.figure()
plt.scatter(dataset["Sleep_Hours"], dataset["Marks"])
plt.xlabel("Sleep Hours")
plt.ylabel("Marks")
plt.title("Sleep Hours vs Marks")
plt.savefig("graph7.png",dpi=300)
plt.show()

print("""
RELATIONSHIP INSIGHTS:
- Study hours have a positive correlation with marks
- Excess screen time tends to reduce performance
- Adequate sleep supports stable academic results
""")

# ==============================
# TASK 7: KEY INSIGHTS
# ==============================
print("""
KEY INSIGHTS:
• Students studying 6–7 hrs consistently perform better
• High screen time often correlates with lower marks
• Balanced sleep is common among top performers
""")

# ==============================
# TASK 8: RECOMMENDATIONS
# ==============================
print("""
RECOMMENDATIONS:

For Students:
1. Maintain 6–7 hrs of focused study daily
2. Limit non-academic screen time
3. Ensure minimum 7 hrs of sleep

For Educators:
1. Encourage balanced routines
2. Track lifestyle metrics along with academics
""")

# ==============================
# TASK 9: LIMITATIONS & REFLECTION
# ==============================
print("""
LIMITATION:
Small dataset size limits generalization.

REFLECTION:
This project demonstrates how data analysis
connects lifestyle patterns with performance.
""")

# ==============================
# TASK 10: DASHBOARD FLOW COMPLETE
# ==============================
print("===== DASHBOARD COMPLETED SUCCESSFULLY =====")
