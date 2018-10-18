# python-port-test

## Usage: command line 
`python ic-ping.py google.com:80 yahoo.com:80 mysql.com:3306`

## Usage: hard coded 
Fill out the hc_list array:

`hc_list = ["www.google.com:80", "mysql.com:3306", "www.lfdskgjdsa.com:80"]`

`python ic-ping.py`

**if both are done, command line will win** 

**Originally,** created for Raspberry Pi to diagnose Comcast firewall issues when the end user isn't comfortable on the command line, has come in handy over the years since. 


