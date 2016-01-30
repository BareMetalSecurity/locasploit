#!/usr/bin/env python
import os, sys, importlib, re, argparse
from source.lib.define import *
#import source.lib.define as lib
from source.lib.parameters import *
from source.lib.commands import *
from source.lib.include import *
import source.lib.log as log


parser = argparse.ArgumentParser(prog='locasploit', description='Local enumeration and exploitation framework.')
parser.add_argument('-c', type=str, help = 'Load the specified configuration file', nargs=1, metavar='input_file', dest='input_file')
args = parser.parse_args()


def main():
	if is_admin():
		log.ok('Administrator privileges already granted.')
	
	# input from file?
	if args.input_file is not None:
		with open(args.input_file[0], 'r') as f:
			lib.input_commands = f.read().splitlines()
			#print commands
			while len(lib.input_commands)>0:
				c = lib.input_commands[0]
				del lib.input_commands[0]
				log.prompt()
				log.attachline(c)
				execute_command(c)

	# main program loop
	while True:
		log.prompt()
		command = raw_input()
		execute_command(command)
	# end of main program loop


load_modules()
main()