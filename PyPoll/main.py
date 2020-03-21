import os
import csv
import operator
#format:
'''
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
'''
csv_path = os.path.join("..","Resources","election_data.csv")
with open(csv_path,'r') as csv_file:
    txt_path = os.path.join("..","Resources","final_poll_text.txt")
    csv_reader = csv.reader(csv_file,delimiter = ',')
    header = next(csv_reader)
    with open(txt_path,'w') as txt_file:
        totalVotes = khanCount = khanPercent = correyCount = correyPercent = liCount = liPercent = oTooleyCount = oTooleyPercent = 0
        winner = ""
        for row in csv_reader:
            voterID = int(row[0])
            county = str(row[1])
            candidate = str(row[2])
            totalVotes += 1
            if candidate == "Khan":
                khanCount += 1
            elif candidate == "Correy":
                correyCount += 1
            elif candidate == "Li":
                liCount += 1
            elif candidate == "O'Tooley":
                oTooleyCount += 1
        khanPercent = '%.2f' % float(khanCount / totalVotes*100)
        correyPercent = float(correyCount / totalVotes*100)
        liPercent = float(liCount / totalVotes*100)
        oTooleyPercent = float(oTooleyCount / totalVotes*100)
        percentDict = {"Khan":khanPercent,"Correy":correyPercent,"Li":liPercent,"O'Tooley":oTooleyPercent} #see comment below for explanation of this dict
        winner = max(percentDict.items(),key = operator.itemgetter(1))[0] #didnt want to write a loop/big if statement to find max so did this instead
        #now print to terminal
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {totalVotes}")
        print("-------------------------")
        print(f"Khan: {khanPercent}% {khanCount}")
        print(f"Correy: {correyPercent}% {khanCount}")
        print(f"Li: {liPercent}% {liCount}")
        print(f"O'Tooley: {oTooleyPercent}% {oTooleyCount}")
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")
        txt_file.write("Election Results\n-------------------------\n")
        txt_file.write(f"Total Votes: {totalVotes}\n-------------------------\n")
        txt_file.write(f"Khan: {khanPercent}% {khanCount}\nCorrey: {correyPercent}% {khanCount}\n")
        txt_file.write(f"Li: {liPercent}% {liCount}\nO'Tooley: {oTooleyPercent}% {oTooleyCount}\n")
        txt_file.write(f"-------------------------\nWinner: {winner}\n-------------------------\n")

        