# IntError
When run, this app scans all the files in a defined 'input' folder. It wll scan the folder for a specific extention, the default is '.log'. If matching files are found, the script parses the output using TextFSM with NTC-Template 'cisco ios show interfaces' template . The resulting table is parsed and referenced to determine if there are specific input or output errors on 'up' interfaces. If errors are seen, it will record the detials to a txt file. Thresholds are applied and can be customized to append "!!ALERT!!" messages if thresholds are exceeded. After the source input file is processed, the script input file will be deleted.

** Optional: Modify the config.yml **
- Change the input and output folder locations. By default the script will use the ./input/ and ./output folders.
- Set the threshold percentage for various errors.
- Set the decimal placement for output percentages. By default it will display to the 4th place (0.0001%).

"Putting the 'terror' in interface errors since 2023."
