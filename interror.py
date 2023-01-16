#!/usr/bin/env python3

import textfsm
import datetime
import os
import yaml

author = 'Michael Lorincz'
version = '0.9.3'

with open("config.yml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
#// Threshold Variables
input_error_threshold = config["threshold_variables"]["input_error_threshold"]
output_error_threshold = config["threshold_variables"]["output_error_threshold"]
overrun_error_threshold = config["threshold_variables"]["overrun_error_threshold"]
crc_error_threshold = config["threshold_variables"]["crc_error_threshold"]
frame_error_threshold = config["threshold_variables"]["frame_error_threshold"]
runts_error_threshold = config["threshold_variables"]["runts_error_threshold"]
giants_error_threshold = config["threshold_variables"]["giants_error_threshold"]

#// Input and Output File Variables
input_folder = config["file_variables"]["input_folder"]
input_filetype = config["file_variables"]["input_filetype"]
output_folder = config["file_variables"]["output_folder"]
dec_place = config["decimal_variables"]["dec_place"]

#// Get the current date and time
now = datetime.datetime.now()

#// list of error and packet fields
error_fields = ['INPUT_ERRORS', 'CRC', 'ABORT', 'OUTPUT_ERRORS', 'OVERRUN', 'FRAME', 'RUNTS', 'GIANTS']
packet_fields = ['INPUT_PACKETS', 'OUTPUT_PACKETS']

#// #iterating over log files
for log_file in os.listdir(input_folder):
    if log_file.endswith(input_filetype):
        input_file = os.path.join(input_folder, log_file)
        input_file_name = os.path.splitext(os.path.basename(input_file))[0]
        #// Create a TextFSM object and Parse the input text using the FSM table
        textfsm_template = "./templates/cisco_ios_show_interfaces.textfsm"
        re_table = textfsm.TextFSM(open(textfsm_template))
        fsm_results = re_table.ParseText(open(input_file).read())
        re_table.Reset()
#// Create a text file with the input file name and a timestamp appended
        with open(output_folder+now.strftime("%Y-%m-%d_")+input_file_name + "_errors" + ".txt", 'w') as f:
            output_file_name = os.path.splitext(os.path.basename(f.name))[0]
            f.write("Generated by IntError Script on "+ now.strftime("%Y-%m-%d %H:%M")+" from file '"+input_file_name+"'."'\n\n')
            for row in fsm_results:
                #//  First, exclude any intefaces and skip interfaces that aren't up.
                if 'Embedded-Service' in row[0]:
                    continue
                if row[1] != 'up':
                    continue
                #// check if the interface has any errors. 
                has_errors = any(row[re_table.header.index(error_field)] not in ('0', 0, '') for error_field in error_fields)
                #// if the interface has errors, then calculate the percentage of errors
                if has_errors:
                    input_packets = int(row[re_table.header.index('INPUT_PACKETS')])
                    output_packets = int(row[re_table.header.index('OUTPUT_PACKETS')])
                    input_errors = int(row[re_table.header.index('INPUT_ERRORS')])
                    crc_errors = int(row[re_table.header.index('CRC')])
                    overrun_errors = int(row[re_table.header.index('OVERRUN')])
                    frame_errors = int(row[re_table.header.index('FRAME')])
                    runts_errors = int(row[re_table.header.index('RUNTS')])
                    giants_errors = int(row[re_table.header.index('GIANTS')])
                    output_errors = int(row[re_table.header.index('OUTPUT_ERRORS')])
                    #// calculate the percentage of errors, results should be to the nearest 2 decimal places
                    input_errors_percentage = dec_place.format(input_errors / input_packets)
                    crc_errors_percentage = dec_place.format(crc_errors / input_packets)
                    overrun_errors_percentage = dec_place.format(overrun_errors / input_packets)
                    frame_errors_percentage = dec_place.format(frame_errors / input_packets)
                    runts_errors_percentage = dec_place.format(runts_errors / input_packets)
                    giants_errors_percentage = dec_place.format(giants_errors / input_packets)
                    output_errors_percentage = dec_place.format(output_errors / output_packets)
                    #// if the interface has errors, then write the results to the file
                    f.write(row[0] + '\n') #// interface name
                    if input_errors != 0:
                        message = "Input Errors: " + str(input_errors) + " (" + input_errors_percentage + ' of all input packets' + ")"
                        if float(input_errors_percentage.strip('%')) >= input_error_threshold:
                            message += " !!ALERT!! Input Errors are above threshold. Threshold currently set to: " + str(input_error_threshold)+"%."
                        f.write(message + '\n')
                    if crc_errors != 0:
                            message = "CRC Errors: " + str(crc_errors) + " (" + crc_errors_percentage + " of all input packets)"
                            if float(crc_errors_percentage.strip('%')) >= crc_error_threshold:
                                message += " !!ALERT!! CRC Errors are above threshold. Threshold currently set to: " + str(crc_error_threshold)+"%."
                            f.write(message + '\n')
                    if overrun_errors != 0:               
                        message = "Overrun Errors: " + str(overrun_errors) + " (" + overrun_errors_percentage + ' of all input packets' + ")"
                        if float(overrun_errors_percentage.strip('%')) >= overrun_error_threshold:
                            message += " !!ALERT!! Overrun Errors are above threshold. Threshold currently set to: " + str(overrun_error_threshold)+"%."
                        f.write(message + '\n')
                    if frame_errors != 0:
                        message = "Frame Errors: " + str(frame_errors) + " (" + frame_errors_percentage + ' of all input packets' + ")"
                        if float(frame_errors_percentage.strip('%')) >= frame_error_threshold:
                            message += " !!ALERT!! Frame Errors are above threshold. Threshold currently set to: " + str(frame_error_threshold)+"%."
                        f.write(message + '\n')
                    if runts_errors != 0:
                        message = "Runt Errors: " + str(runts_errors) + " (" + runts_errors_percentage + ' of all input packets' + ")"
                        if float(runts_errors_percentage.strip('%')) >= runts_error_threshold:
                            message += " !!ALERT!! Runt Errors are above threshold. Threshold currently set to: " + str(runts_error_threshold)+"%."
                        f.write(message + '\n')
                    if giants_errors != 0:
                        message = "Giant Errors: " + str(giants_errors) + " (" + giants_errors_percentage + ' of all input packets' + ")"
                        if float(giants_errors_percentage.strip('%')) >= giants_error_threshold:
                            message += " !!ALERT!! Giant Errors are above threshold. Threshold currently set to: " + str(giants_error_threshold)+"%."
                        f.write(message + '\n')
                    if output_errors != 0:
                        message = "Output Errors: " + str(output_errors) + " (" + output_errors_percentage + ' of all output packets' + ")"
                        f.write(message + '\n')
                    if float(output_errors_percentage.strip('%')) >= output_error_threshold:
                        message += " !! ALERT !! Output Errors are above the threshold you set set: " + str(output_error_threshold)+"%."
                        f.write(message + '\n')
                    f.write('\n\n')
        os.remove(input_folder+log_file)
        f.close()
        print("Finished writing to file: '" + output_file_name+"'")
        print("")
print("Finished running script.") 
print("Script version: " + version)
print("Script written by: " + author)
print("")