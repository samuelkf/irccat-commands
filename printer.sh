#!/bin/bash

file=/usr/share/irccat/.printer.txt
equipment=Printer
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

