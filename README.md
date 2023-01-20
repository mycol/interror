<h1>IntError</h1>

<p>A Python script that reads Cisco IOS 'show interfaces' output files and uses TextFSM library to extract specified error and packet fields, and provides added context by checking interface status and description. It can filter the interfaces to process based on their status, as defined in a configuration file (config.yml) which also includes alert threshold variables, file variables, and decimal place settings.
<b>Once run, the program will process and delete the input files, new output files will be saved to the designated output folder. No new output file will be created if no errors are detected. *future version will permit setting variable to retain input files or delete*</b></p>

<h2>Getting Started</h2>

<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

<h3>Prerequisites</h3>

<ul>
  <li>Python3</li>
  <li>TextFSM library</li>
  <li>YAML library</li>
</ul>

<h3>Installing</h3>

<ol>
  <li>Clone the repository</li>
  <pre><code>git clone https://github.com/username/IntError.git</code></pre>
  <li>Install the required libraries</li>
  <pre><code>pip install textfsm
pip install pyyaml</code></pre>
  <li>Update the config.yml file with your desired settings</li>
</ol>

<h3>Running the script</h3>

<ol>
  <li>Navigate to the directory where the script is located</li>
  <li>Run the script with the command</li>
  <pre><code>python IntError.py</code></pre>
</ol>

<h2>Configuration file</h2>

<p>The script requires a configuration file named config.yml in the same directory as the script file. This file contains the following fields:</p>
<ul>
  <li>threshold_variables: contains the threshold values for each error type</li>
  <li>file_variables: contains the input folder, input filetype, and output folder</li>
  <li>decimal_variables: contains the decimal place for the percentage of errors</li>
  <li>interface_variables: contains the status of the interface which the script will only process if it's "up"</li>
</ul>

<h2>Output</h2>

<p>The output file will only display an alert if one is detected (dictated by thresholds defined in config.yml).</p>
<li>Interface: the interface name</li>
<li>Description: the interface description</li>
<li>Interface Status: the interface status "up" or "down"</li>
<li>Input Error count and the percentage of input errors</li>
<li>CRC errors count and the percentage of crc errors</li>
<li>Overrun errors count and the percentage of overrun errors</li>
<li>Frame errors count and the percentage of frame errors</li>
<li>Runt error count and the percentage of runts errors</li>
<li>Giant errors count and the percentage of giants errors</li>
<li>Output errors count and the percentage of output errors</li>
</ul>
<br>
<pre><code>
GigabitEthernet0/0
Description: 
Status: up
Input Errors: 230613 (13.5424% of all input packets) !!ALERT!! Input Errors are above threshold. Threshold currently set to: 1.0%.
Overrun Errors: 230613 (13.5424% of all input packets) !!ALERT!! Overrun Errors are above threshold. Threshold currently set to: 1.0%.
</code></pre>
<h2>Built With</h2>
<ul>
  <li><a href='https://www.python.org/'>Python3</a> - Programming language used</li>
  <li><a href='https://github.com/google/textfsm'>TextFSM</a> - Library used for parsing semi-structured text</li>
  <li><a href='https://yaml.org/'>YAML</a> - Library used for configuration file</li>
</ul>
<h2>Author</h2>
Michael Lorincz - <a href='https://github.com/username'>GitHub</a>
<h2>License</h2>
<p>This project
