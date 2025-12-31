#WRITE A PROGRAM TO PLOT FOLLOWING CHARTS

#BAR CHART
import matplotlib.pyplot as plt
subjects = ['English', 'Maths', 'Physics', 'Chemistry', 'Computer']
marks = [78, 85, 72, 80, 90]
plt.bar(subjects, marks)
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks of a Student in All Subjects')
plt.show()

#SCATTER CHART
import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [22, 24, 23, 25, 26, 27, 24]
plt.scatter(days, temperature)
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Throughout the Week')
plt.show()

#PIE CHART
import matplotlib.pyplot as plt
activities = ['Social Media', 'Study', 'Gaming', 'Videos', 'Other']
hours = [3, 5, 2, 4, 1]
plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title('Daily Screen Time of a User')
plt.show()
