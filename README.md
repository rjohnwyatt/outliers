How to calculate the rankings

Make the ranking spreadsheets. Historically, there has been one for current home team skaters and one for draftable skaters (including diamond district). The current home team skater spreadsheet usually goes out first so people have more time to look at new skaters.
 - Each spreadsheet should be ordered so that the skaters are mixed and not collected by team. This helps prevent people from adjusting their rubrics per team. In 2015, we used alphabetical order.
 - Home team skater spreadsheet goes out to 4 rankers per home team plus unaffiliated coaches
 - Draftable skater spreadsheet goes out to coaches who have observed the meat at enough practices. In 2015, we solicited additional rankings from some home team captains because there were so few eligible rankers
 - send them out

When the spreadsheets start coming back, check them for completeness. Someone always forgets a few spots. Also, start pestering everybody who hasn't submitted. This will be the most fun part.

This is now the part that sucks. You have to reformat the data from how it comes in (in files per ranker with all the skaters ranked by one person) to how it can be processed by the calculator (in a file per skater with all of the rankings for that individual skater. You can chop this stuff up in excel or google docs but it is a pain in the ass manual process. I might be able to automate it.

Once the data is chopped up so that it's in files per skater, you drop them into folders per team and edit the calculator to point to those files and know how many files it's trying to pull. 

Then run the calculator:
 - The calculator is a simple python script. It takes in all the rankings for each player and exports the averages. 
 - The script is called outliers.py and is available in this repository.
