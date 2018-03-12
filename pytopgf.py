# -*- coding: utf-8 -*-
from __future__ import division
import __main__ as main
import os
import numpy as np
import matplotlib as mpl
    
pgf_with_latex = {               # setup matplotlib to use latex for output
"pgf.texsystem": "pdflatex",     # change this if using xetex or lautex
"text.usetex": True,             # use LaTeX to write all text
"font.family": [0],
"font.serif": [],                # blank entries should cause plots to inherit fonts from the document
"font.sans-serif": [],
"font.monospace": [],
"axes.labelsize": 8,             # LaTeX default is 10pt font.
"font.size": 8,
"legend.fontsize": 8,            # Make the legend/label fonts a little smaller
"xtick.labelsize": 8,
"ytick.labelsize": 8,
#"figure.figsize": figsize(0.9), # default fig size of 0.9 textwidth
"pgf.preamble": [
r"\usepackage[utf8x]{inputenc}", # use utf8 fonts becasue your computer can handle it :)
r"\usepackage[T1]{fontenc}",     # plots will be generated using this preamble
        ]
    }
mpl.rcParams.update(pgf_with_latex)
import matplotlib.pyplot as plt

def draft():
    """For plotting in standard matplotlib
    Style: 'Draft' (Default None)
    """
    mpl.rcParams.update(mpl.rcParamsDefault)

def figsize(fig_width_pt, scale=None, ratio=None): # Used through newfig()
    """Define the figure size. 
    fig_width_pt: Get this from LaTeX using \\the\\textwidth
    Scale: Optional (Default: 0.9)
    Ratio: Optional (height/width. Default:Golden ratio)
    """
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    if ratio == None:
        ratio= (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this), default Golden ratio
    if scale==None:
        scale=0.9
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*ratio              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size


def newfig(width,scale=None,ratio=None):
    """Creates the figure with the added subplot. This functions calles figsize()
    width: Get this from LaTeX using \\the\\textwidth
    Scale: Optional (Default: 0.9)
    Ratio: Optional (height/width. Default:Golden ratio)
    """
    plt.clf()
    fig = plt.figure(figsize=figsize(width,scale,ratio))
    ax = fig.add_subplot(111)
    return fig, ax

def savefig(filename=os.path.splitext(os.path.basename(main.__file__))[0]):
    """Saves the file
    filename: String"""
    plt.savefig('{}.pgf'.format(filename), bbox_inches='tight')
    plt.savefig('{}.pdf'.format(filename), bbox_inches='tight')

def sexyplot():
    mpl.rcParams['lines.linewidth'] = 0.8
    mpl.rcParams['axes.prop_cycle']=mpl.cycler(color=['k','k'])
    mpl.rcParams['axes.grid']=True
    mpl.rcParams['legend.loc'] = 'Best'
    #mpl.rcParams['grid.color'] ='k'
    mpl.rcParams['grid.linestyle']='--'
