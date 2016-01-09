import csv
from numpy import *

total_rankers = 11
team_skaters = 23 #num in Luna's version - number of skaters on the team we're running
num_std_devs = 1 #factor in Luna's version - number of std deviations to define which points to keep/toss
directory = "csvsForMeatRanking/"
team = "meat" #set the team to choose your input files

if __name__ == "__main__":
	# set up storage variables
	keepRevised = zeros((team_skaters)) #creating arrays of size skaters
	keepMedians = zeros((team_skaters))
	keepAvgs = zeros((team_skaters))
	
	i = 1
	while i <= team_skaters:
		Total = zeros((total_rankers))
		tossed = []
		kept = []

		# read individual skater file with rankings from all rankers
		filename = "outliers2014/" + directory + team + str(i) + ".csv"
		with open(filename, mode = "U") as csvfile:
			reader = csv.reader(csvfile,dialect='excel')
			r = 0
			for row in reader:
				li = [] # all of the ranks by an individual ranker
				for cell in row:
					li.append(int(cell))
				Total[r] = sum(li) + li[9]
				r = r + 1

		average_rank = average(Total)
		std_dev = Total.std(ddof=1)
		range_top = average_rank + num_std_devs * std_dev
		range_bottom = average_rank - num_std_devs * std_dev
		middle = median(Total, axis=None, out=None, overwrite_input=False)
	
		ranker = 1
		while ranker <= total_rankers:
			if Total[ranker - 1] > range_top or Total[ranker - 1] < range_bottom:
				tossed.append(ranker)
			else:
				kept.append(ranker)
			ranker = ranker + 1

		# keep only the rankings in the range
		ranker = 1
		skipped = 0
		revised_list = zeros(total_rankers - len(tossed))
		while ranker <= total_rankers:
			if set(kept) - set([ranker]) != set(kept): #if the ranker was not kept
				revised_list[ranker - 1 - skipped] = Total[ranker - 1] #expecting 0, 1, 3, 4
			else:
				skipped = skipped + 1
			ranker = ranker + 1
			
		revised_average = float(sum(revised_list))/len(revised_list)	

		# store average, median and std dev for each player
		keepRevised[i - 1] = revised_average
		keepMedians[i - 1] = middle
		keepAvgs[i - 1] =  average_rank
		
		print team + str(i) + " : Std Dev: " +  str(std_dev) + " Votes discarded: " + str(len(tossed)) +  ", Average of remaining votes: " + \
		 	str(revised_average) + ", Average of all votes: " + str(average_rank) + ", Median: " + str(middle)
		
		i=i+1
	
	print "Team averages. Average of kept votes: " + str(average(keepRevised)) + " Average of all votes: " + str(average(keepAvgs)) + \
	 	" Average of median votes: " + str(average(keepMedians))
