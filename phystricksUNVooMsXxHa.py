# -*- coding: utf8 -*-
from phystricks import *
def UNVooMsXxHa():
    pspict,fig = SinglePicture("UNVooMsXxHa")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(cosh(x)).graph(-10,10)
    g=phyFunction(sinh(x)).graph(-10,10)

    f.cut_y(-5,5)
    g.cut_y(-5,5)

    f.put_mark(0.2,180,"\( y=cosh(x)\)",automatic_place=(pspict,"E"),mark_point=f.I)
    g.put_mark(0.2,180,"\( y=sinh(x)\)",automatic_place=(pspict,"E"),mark_point=g.I)

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()