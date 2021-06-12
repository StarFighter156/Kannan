# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:56:07 2021

@author: Kannan
"""
import Source.ergy
import Source.time

test=Source.ergy.Energy()
test_time= Source.time.Time()

print (test.kinetic(100,100))
print (test_time.days_to_seconds(1))