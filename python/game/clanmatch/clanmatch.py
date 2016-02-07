# ClanMatch Project
#
# $Id: clanmatch.py 2016-02-07 05:14:12Z tema567 $
# $Desc: ClanMatch $
#
# Coders:
#  Tema567

__module__ = "clanmatch"
__version__ = "dev"
__instance__ = None
__enabled__ = False

# Imports:
try:
	import sys
	import bf2
	import host
	import time
	import math
	import random
	import string
	import re
	import ConfigParser
except:
	sys.exit( "%s: imports failed, exiting.." % __module__ )

# Class definition:
class ClanMatch( object ):
	def __init__( self ):
		"""Class initialization"""
		self.info( "ClanMatch init" )
		self.parser = None

	def init( self ):
		"""Init"""
		# ... #

	def info( self, msg ):
		"""Print information"""
		print "<%s> Info: %s" % ( __module__, msg )

	def error( self, msg ):
		"""Print error"""
		print "<%s> Error: %s" % ( __module__, msg )

# Interface methods:

def init():
	"""Module initialization"""
	global __instance__
	if ( __instance__ is None ):
		__instance__ = ClanMatch()
		__instance__.init()

def deinit():
	"""Module deinitialization"""
	global __instance__
	if not ( __instance__ is None ):
		del __instance__
		__instance__ = None

def enable():
	"""Module enabling"""
	global __enabled__
	__enabled__ = True

def disable():
	"""Module disabling"""
	global __enabled__
	__enabled__ = False

def update():
	"""Loop update"""
	pass

# Execution

init()
enable()

# EOF