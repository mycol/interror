<h1>IntError</h1>

<p>A Python script that reads Cisco IOS 'show interfaces' output and uses TextFSM library to extract specified error and packet fields, and provides added context by checking interface status and description. It can filter the interfaces to process based on their status, as defined in a configuration file (config.yml) which also includes threshold variables, file variables, and decimal place settings.</p>

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
<li>interface: the interface name</li>
<li>description: the interface description</li>
<li>input_errors_percentage: the percentage of input errors</li>
<li>crc_errors_percentage: the percentage of crc errors</li>
<li>overrun_errors_percentage: the percentage of overrun errors</li>
<li>frame_errors_percentage: the percentage of frame errors</li>
<li>runts_errors_percentage: the percentage of runts errors</li>
<li>giants_errors_percentage: the percentage of giants errors</li>
<li>output_errors_percentage: the percentage of output errors</li>
</ul>
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
