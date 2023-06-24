import csv

# Read in the data from the CSV file
with open("UDisc Scorecardscurr.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Define a function to calculate the score for a given hole
def calculate_score(par, score):
    if score == "2":
        return 2
    elif score == "3":
        return 0
    elif score == "4":
        return -1
    elif score == "5":
        return -3
    else:
        return par - int(score)

# Define a dictionary to store the scores for each player on each course
scores = {}

# Loop through each row of data
for row in rows:
    # Extract the relevant data from the row
    name = row["Name"]
    course = row["Course"]
    hole = row["Hole"]
    par = int(row["Par"])
    score = row["Score"]

    # Calculate the score for the hole
    hole_score = calculate_score(par, score)

    # Update the total score for the player on the course
    if name not in scores:
        scores[name] = {}
    if course not in scores[name]:
        scores[name][course] = 0
    scores[name][course] += hole_score

# Write the scores to a new CSV file
with open("player_scores.csv", mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row to the CSV file
    writer.writerow(["Name", "Course", "Score"])

    # Loop through each player and course in the scores dictionary
    for name, course_scores in scores.items():
        for course, score in course_scores.items():
            # Write the player's name, course name, and score to the CSV file
            writer.writerow([name, course, score])
