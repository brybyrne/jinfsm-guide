# jinfsm-guide

This is the code repo for NetDevOps Live Season 2 Episode 4 'Embrace the Dry Principle.' During the presentation, I will walk through specific examples of how to leverage Jinja and TextFSM to create reusable code for working with both Configuration and Operational Data. I will provide a link to the recording and reference site after the session is recorded on April 22nd. 

In the event you were unable to attend the session or stumbled across this repo, here is a description of the various scripts. The following sections refer to the directories in the repo.

Code is based on Python 3.7 and the attached [requirements](./requirements.txt) file.

## wrong_way

These scripts were generated as a representation of 'bad' code that addressed a specific scenario. To simplify the configuration of a router used by multiple students in a lab, I used two Python scripts, generated with Postman, to configure interfaces on a router. The 'automation' came in the form of the bash script that executed the two Python scripts.

### Code Descriptions

- g2.py and g3.py - Simple python script that configures an interface with IP address, mask and description.
- startup.sh - This bash script executes the two Python scripts in order.

## jinja_example

This directory contains examples of how to use Jinja templating to create CLI templates. The naming convention is such that all files for each example starts with the example number. In all examples:

- The template is explicitly defined in the code.
- The variables are explicitly defined in either the code or the associated YAML file.

### Code Descriptions

- ex1_hello_vlan.py - Simple example of defining a Jinja template and inserting a variable. The variable is defined in the Jinja render statement.
- ex2_vlan_svi_bad.py - Extending on the previous example by showing how the same variable can be used in multiple templates.
- ex3_vlan_svi_good.py - In this example, rather than directly defining the template in code, an external template file is read in and used to render the configuration.
- ex4_svi_template_loop.py - Extending on the previous example, this is an example of using Jinja's loop operation to generate configuration for a series of interfaces. The interfaces are explicitly defined in the code.
- ex5_port_template_conditional.py - In this example we add on to the previous bit of code by adding a conditional statement to check the port type and if it should be enabled or not.
- ex6_yaml_data.py - In the final example, rather than explicitly defining the input data values directly in code, we pass in a YAML file with a command line argument. 

## textfsm_example

This directory contains examples on using TextFSM to parse through CLI operational output to generate structured data. The code uses some common code components.

- device_details.py - Used in example 2 to provide session details for opening the SSH session with Netmiko.
- device_details.yaml - Used in example 3 to provide session details for opening the SSH session with Netmiko and an environment variable that provides the location of the TextFSM templates.
- /ntc-template - These are TextFSM templates created by Network to Code.

### Code Desciptions
- ex1_ship_output.py - This simple code is designed to read in the output form 'show ip interface brief' and pass it through the TextFSM parser. The show output and the TextFSM templates are explicitly defined in the code.
- ex2_ship_netmiko.py - In this example rather than feed the parser a text file the code generates the output by using Netmiko to establish a connection, send the show command, and then parse the data into a readable format.
- ex3_netmiko_sh_ver.py - This example is designed to show Netmiko's built in function that will apply the correct TextFSM template based on the input show command. This requires an environment variable set that tells Netmiko where to find the template files and an Index file that associates the show output with the correct template.


# End 