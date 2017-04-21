from subprocess import call

# Assemble the name from the component parts. Change this to a config file read.
user_name = "amclennan"
domain_name = "am-linux-laptop"
fully_formed_name = user_name + "@" + domain_name



call(["ssh", fully_formed_name])
