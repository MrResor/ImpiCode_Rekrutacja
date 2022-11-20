# ImpiCode_Recruitment
Solution of recruitment program received from ImpiCode.

# Other languages
Versions in other languages:
<a href = https://github.com/MrResor/ImpiCode_Rekrutacja/blob/main/README.pl.md>Polski</a>

# Introduction
Program is designed to calculate smallest "cost" of moving elephants from current to desired layout. It takes data from files and presents the output in the console.

# Data
Data comes in form on .in file. The files contain text which denotes number of elephants (first line), weights of elephants (second line), current layout of elephants (third line) and desired layout of elephants (fourth line).

# Usage
Code takes path to input file as parameter and prints a result of that problem to the console.

# Method
The cost of move is obtained by adding weights of both moved elephants. Knowing the current and desired layouts we can obtain the cycles. After calculating sum of weights and minimal weight in each cycle, it is possible to obtain the lowest cost for given cycle by choosing the lower result from two methods. The sum of those, for each cycle, gives us the result.
