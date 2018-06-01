# BattingAverageParser
## Description
<br/>This file was created for my "Rapid Prototype Development and Creative Programming" course. It calculates the batting average of each baseball player from an input .txt file. Then, it prints out the players and their batting averages, sorted by their batting averages. This output is printed to the console and to a .txt file called "team_batting_average.txt".

## Formats
### Script Usage
```BattingAverageParser filename```
### Input Text FileInput
#### Line Format:
```[First Name] [Last Name] batted[Number] times with [Number] hits and [Number] runs.```
#### Line Format in Regex Form:
```(\w+\s+\w+)(?:\s+batted\s+)(\d)(?:\s+times\s+with\s+)(\d)(?:\s+hits\s+and\s+)(\d)(?:\s+runs)```
<br/><br/>Note: Lines in the file that do not match the format will not be processed.
## Inputs and Outputs
### Example Input:
```
---Justice League of America ---

----- Justice League of America VS  Justice Society of America -----
John Jones batted 4 times with 2 hits and 2 runs
Shayera Hol batted 4 times with 4 hits and 2 runs
Dinah Drake batted 2 times with 2 hits and 2 runs
Jaime Reyes batted 3 times with 3 hits and 1 runs
Jessie Chambers batted 3 times with 2 hits and 2 runs
Jefferson Pierce batted 4 times with 3 hits and 2 runs

----- Justice League of America VS Doom Patrol -----
Shayera Hol batted 2 times with 1 hits and 1 runs
Katar Hol batted 3 times with 2 hits and 0 runs
John Jones batted 3 times with 2 hits and 1 runs
Dinah Drake batted 1 times with 1 hits and 0 runs
Jaime Reyes batted 4 times with 3 hits and 2 runs
Zatanna Zatara batted 4 times with 2 hits and 1 runs
```

### Example Output:
```
Dinah Drake: 1.000
Jaime Reyes: 0.857
Shayera Hol: 0.833
Jefferson Pierce: 0.750
Jessie Chambers: 0.667
Katar Hol: 0.667
John Jones: 0.571
Zatanna Zatara: 0.500
```
