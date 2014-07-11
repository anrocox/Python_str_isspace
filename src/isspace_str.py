#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

In python how to know if the characters of a string are whitespace?

En python ¿como saber si los caracteres de un string son espacios en blanco?
'''

#create a str
s = 'example string\t'
print(s)

#verify if there are only whitespace characters in the string. Return True or
#False. Whitespace characters are those defined in the systme Unicode as
#'Other' or 'Separator'
print(s.isspace())

#create a str
s = ' \n\t\r'
print(s)

#return True because the string have only whitespace characters.
print(s.isspace())
