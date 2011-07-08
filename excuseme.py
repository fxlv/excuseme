#!/usr/bin/env python
"""
super primitive random excuse chooser
"""
import random

excuses_file = open('excuses')
excuses = excuses_file.readlines()
print excuses[random.randrange(0,len(excuses))].strip()

