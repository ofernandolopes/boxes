#!/usr/bin/python
# Copyright (C) 2013-2014 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import Boxes

class Silverware(Boxes):
    ####################################################################
    ### Parts
    ####################################################################

    def basePlate(self, x, y, r):
        self.roundedPlate(x, y, r, callback=[
                lambda: self.fingerHolesAt(x/3.0-r, 0, 0.5*(y-self.thickness)),
                lambda: self.fingerHolesAt(x/6.0, 0, 0.5*(y-self.thickness)),
                lambda: self.fingerHolesAt(y/2.0-r, 0, x),
                lambda: self.fingerHolesAt(x/2.0-r, 0, 0.5*(y-self.thickness))
                ])

    def wall(self, x=100, y=100, h=100, r=0):
        self.surroundingWall(x,y,r,h, bottom='h', callback={
                0 : lambda: self.fingerHolesAt(x/6.0, 0, h-10),
                4 : lambda: self.fingerHolesAt(x/3.0-r, 0, h-10),
                1 : lambda: self.fingerHolesAt(y/2.0-r, 0, h-10),
                3 : lambda: self.fingerHolesAt(y/2.0-r, 0, h-10),
                2 : lambda: self.fingerHolesAt(x/2.0-r, 0, h-10),
                },
                             move="up")

    def centerWall(self, x, h):
        self.ctx.save()

        self.moveTo(self.fingerJointEdge.spacing(), self.fingerJointEdge.spacing())
        for i in range(2, 5):
            self.fingerHolesAt(i*x/6.0, 0, h-10)

        self.fingerJointEdge(x)
        self.corner(90)
        self.fingerJointEdge(h-10)
        self.corner(90)

        self.handle(x, 150, 120)
        #self.handle(x, 40, 30, r=2)

        self.corner(90)
        self.fingerJointEdge(h-10)
        self.corner(90)
        self.ctx.restore()

        self.moveTo(x+2*self.fingerJointEdge.spacing())

    ##################################################
    ### main
    ##################################################

    def render(self, x, y, h, r):
        t = self.thickness
        b = self.burn

        self.wall(x, y, h, r)
        self.centerWall(x,h)

        l = (y-t)/2.0
        for i in range(3):
            self.rectangularWall(l, h-10, edges="ffef", move="right")

        self.moveTo(-3.0*(l+2*t+8*b), h-10+2*t+8*b)
        self.basePlate(x, y, r)

        self.close()

b = Silverware(750, 350, thickness=5.0, burn=0.05)
b.render(250, 250/1.618, 120, 30)
#b = Silverware(300, 300, thickness=3.0, burn=0.05)
#b.fingerJointSettings = (b.thickness, b.thickness)
#b.render(60, 60/1.618, 40, 10)
