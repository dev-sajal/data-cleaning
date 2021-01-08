## Hands-on for wings1 involving Data Cleaning

**Data Cleaning:**

This challenge deals with the cleaning of the data. Perform various cleaning methods specified in the Notebook.

------------------------------------------------------------------------------
**IPL Dataset :**

Indian Premier League (IPL) is a Twenty20 cricket format league in India. It is usually played in April and May every year. The league was founded by Board of Control for Cricket India (BCCI) in 2008.

This dataset contains match by match data of the seasons from 2008 to 2016.

**Data features description:**

1. id - Unique id of the match
2. season - Denotes the year in which the match took place
3. city – Name of the city the match took place at
4. date - Date of the match
5. team1 - One of the 2 teams played
6. team2 - One of the 2 teams played
7. toss_winner - The team which won the toss
8. toss_decision - Bat/field decision chosen by the team which won the toss
9. result - Result of the match (tie/normal/no result)
10. dl_applied - Whether the D/L method applied or not (1/0) respectively
11. winner - The team which won the match
12. win_by_runs - The difference in runs between the teams when the team which batted first won the match
13. win_by_wickets - The number of wickets remaining for the team which won the match by batting second
14. player_of_match - Best Player of the match
15. venue - Name of the stadium where the match was held
16. umpire1 - Name of the 1st umpire
17. umpire2 - Name of the 2nd umpire
18. umpire3 - Name of the 3rd umpire

------------------------------------------------------------------------------
**Coding**
- Open the Question.ipynb file and follow the instructions to do the coding.
- Run each cell with the "SHIFT+ENTER" or run button in menu.
- Make sure to run the last cell to save your answers
- **Note**: Please save your notebook with CTRL+S now and then to avoid loss.

------------------------------------------------------------------------------
**Testing the solution:**

- Open the terminal.
- You will see a blank terminal. Press any key for the pointer to appear on the terminal
- Proceed to the folder named 'wings1-t3uc1-datacleaning' with command. Note the tilde(~) symbol before slash (/)

		cd ~/Desktop/Project/wings1-t3uc1-datacleaning
- Then execute the following command in the terminal

         py.test tests/test_1.py
		
- **NOTE:** These test cases are only preliminary test cases. Hidden test cases will also be executed after the test submission to determine the score. 

------------------------------------------------------------------------------

**Note:**
- Additional packages can be installed in the terminal with the command 
		> pip3 install --user package_name
		
		
- The sample testing done using the above code is performed only at high level and the actual testing is done upon closing the hands-on.
