#!/usr/bin/env python
# -*- Coding : UTF-8 -*-

_author = "Eduardo S. Pereira"
_date = "11/06/2017"
_contact = "pereira.somoza@gmail.com"


import easygui as eg
from trilogy import Trilogy, params_cl


class RGBFits:

    def __init__(self):
        self.rImages = None
        self.gImages = None
        self.bImages = None
        self.savefile = None
        self.samplesize = 400
        self.stampsize  = 400
        self.showstamps = 0
        self.satpercent = 0.00001
        self.colorsatfac = 1.5
        self.noiselum = 0.15
        self.deletetests = 1
        self.sampledx = 0
        self.sampledy = 0
        self.inFile = []

        self.saveFile()
        self.selectImages()
        self.genInFile(self.inFile)
        Trilogy(self.inFile[0] + "/trilogy.in", images=None, **params_cl()).run()



    def _selectImages(self, text):
        return eg.fileopenbox(msg=text,
                                  title="Open R images",
                                  default="*.fits", filetypes=["*.fits"],
                                  multiple=True)

    def genInFile(self, inFile):
        inFile += [self.samplesize, self.stampsize, self.showstamps,
                   self.satpercent, self.noiselum, self.colorsatfac,
                   self.deletetests, self.sampledx, self.sampledy]
        outInfile = """B
{2}

G
{3}

R
{4}

indir  {0}
outname  {1}
samplesize {5}
stampsize  {6}
showstamps  {7}
satpercent  {8}
noiselum    {9}
colorsatfac  {10}
deletetests  {11}
sampledx  {12}
sampledy  {13}
        """.format(*inFile)
        with open(inFile[0] + "/trilogy.in", 'w') as fin:
            fin.write(outInfile)


    def selectImages(self):
        print("Select the fits image for R band")
        self.rImages = self._selectImages("Select images for R band")
        self.rImages = '\n'.join(self.rImages)

        print("Select the fits image for G band")
        self.gImages = self._selectImages("Select images for G band")
        self.gImages = '\n'.join(self.gImages)

        print("Select the fits image for B band")
        self.bImages = self._selectImages("Select images for B band")
        self.bImages = '\n'.join(self.bImages)
        self.inFile.append(self.rImages)
        self.inFile.append(self.gImages)
        self.inFile.append(self.bImages)

    def saveFile(self):
        self.savefile = eg.filesavebox(msg="Output file name",
                       title="Output File",
                       default="*.png",
                       filetypes=["*.png"])
        self.savefile = ['/'.join(self.savefile.split("/")[0:-1]),
                         self.savefile.split("/")[-1]]
        self.inFile += self.savefile

def main():
    RGBFits()

if(__name__ == "__main__"):
    main()
