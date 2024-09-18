#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Logan Cox
    Description:  Calculates total river miles within expanded ecoregion boundary.
    Date created: 9/11/24
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "C:\\Users\\lrcox\\Documents\\GitHub\\firstpythonscript-LoganRCox\\GIS_Project\\GitHub-FirstPythonScript.gdb"

#This line selects the Flint Hills ecoregion based off of it's name attribute
selectEcoregion = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

#This line makes a 10 km buffer around the Flint Hills ecoregion
regionBuffer = arcpy.analysis.Buffer(selectEcoregion, 'FlintHills_Buffer', '10 Kilometers')

#This line clips all of the ks rivers that are within the buffered ecoregion
riverClip = arcpy.analysis.Clip('ks_major_rivers', regionBuffer, 'FH_River_Clip')

#This line takes the distance of each river segment and converts it from meters to miles
arcpy.management.AddGeometryAttributes("FH_River_Clip", "LENGTH", "MILES_US")

#This line gets the total distance of the rivers in the clip
arcpy.analysis.Statistics("FH_River_Clip", "outStats", [["LENGTH", "SUM"]])

#Calculate stream length in miles first, then sum to produce a table with correct result:
#arcpy.management.AddGeometryAttributes("FH_River_Clip", "LENGTH", "MILES_US")
#arcpy.analysis.Statistics("FH_River_Clip", "outStats", [["LENGTH", "SUM"]])
