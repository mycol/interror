# IntError
When run, this app is designed to scan all the files an a defined folder. Checking for a specific extention (by default '.log'). If found, it checks the files for the 'show interface' output. This output is then parsed using TextFSM/NTC-Templates. The resulting table is referenced to determine if there are errors on interfaces in that file output. if so, it will record the detials to a txt file. Thresholds can also be set to govern "!!ALERT!!" messages, which highlight potential issues.

To use this app...
Modify the config.yml with input and output folder locations. 
You can also set the threshold percentage and decimal placement for output percentages. By default the script will use the ./input/ and ./output folder that comes with the script.

I hope this helps!

"Putting the 'terror' in interface errors since 2023."
