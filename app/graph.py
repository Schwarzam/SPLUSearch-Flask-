from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import sys
import argparse
import os
from colour import Color
from app.models import *


class Graph:
    def __init__(self, Galaxy):
        self.data = Galaxy
        data = self.data
        n = data.RA
        Number = []

        self.wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
        self.color = "#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"

        # wl1 = [3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
        # color1 = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
        # marker1 = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro

        Number = []

        Number = []
        mag_auto  = []

        mag_petro = []
        mag_aper = []

        #Error
        mag_auto_err  = []
        mag_petro_err  = []

        #sys.exit()
        #auto

        mag_auto.append(data.uJAVA_auto)
        mag_auto.append(data.F378_auto)
        mag_auto.append(data.F395_auto)
        mag_auto.append(data.F410_auto)
        mag_auto.append(data.F430_auto)
        mag_auto.append(data.g_auto)
        mag_auto.append(data.F515_auto)
        mag_auto.append(data.r_auto)
        mag_auto.append(data.F660_auto)
        mag_auto.append(data.i_auto)
        mag_auto.append(data.F861_auto)
        mag_auto.append(data.z_auto)
            #Petro
        mag_petro.append(data.uJAVA_petro)
        mag_petro.append(data.F378_petro)
        mag_petro.append(data.F395_petro)
        mag_petro.append(data.F410_petro)
        mag_petro.append(data.F430_petro)
        mag_petro.append(data.g_petro)
        mag_petro.append(data.F515_petro)
        mag_petro.append(data.r_petro)
        mag_petro.append(data.F660_petro)
        mag_petro.append(data.i_petro)
        mag_petro.append(data.F861_petro)
        mag_petro.append(data.z_petro)


            #ERRO AUTO
        mag_auto_err.append(data.euJAVA_auto)
        mag_auto_err.append(data.eF378_auto)
        mag_auto_err.append(data.eF395_auto)
        mag_auto_err.append(data.eF410_auto)
        mag_auto_err.append(data.eF430_auto)
        mag_auto_err.append(data.eg_auto)
        mag_auto_err.append(data.eF515_auto)
        mag_auto_err.append(data.er_auto)
        mag_auto_err.append(data.eF660_auto)
        mag_auto_err.append(data.ei_auto)
        mag_auto_err.append(data.eF861_auto)
        mag_auto_err.append(data.ez_auto)

            #ERRO petro
        mag_petro_err.append(data.euJAVA_petro)
        mag_petro_err.append(data.eF378_petro)
        mag_petro_err.append(data.eF395_petro)
        mag_petro_err.append(data.eF410_petro)
        mag_petro_err.append(data.eF430_petro)
        mag_petro_err.append(data.eg_petro)
        mag_petro_err.append(data.eF515_petro)
        mag_petro_err.append(data.er_petro)
        mag_petro_err.append(data.eF660_petro)
        mag_petro_err.append(data.ei_petro)
        mag_petro_err.append(data.eF861_petro)
        mag_petro_err.append(data.ez_petro)

        font = {'family': 'serif',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
                }

        for i in range(len(mag_auto)):
          mag_auto[i] = float(mag_auto[i])
        for i in range(len(mag_auto_err)):
          mag_auto_err[i] = float(mag_auto_err[i])
        for i in range(len(mag_petro)):
          mag_petro[i] = float(mag_petro[i])
        for i in range(len(mag_petro_err)):
          mag_petro_err[i] = float(mag_petro_err[i])

        self.mag_auto = mag_auto
        self.mag_petro = mag_petro
        self.mag_auto_err = mag_auto_err
        self.mag_petro_err = mag_petro_err

    def autoplot(self):
        data = self.data
        n = data.RA
        Number = []

        wl = self.wl
        color = self.color

        # wl1 = [3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
        # color1 = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
        # marker1 = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro

        Number = []

        Number = []
        mag_auto  =self.mag_auto

        mag_petro = self.mag_petro
        mag_aper = []

        #Error
        mag_auto_err  = self.mag_auto_err
        mag_petro_err  = self.mag_petro_err

        mag_auto = [np.nan if x == 99.0 else x for x in mag_auto]

        #plotfile = "photos-pectrum_splus_"+str(data.FIELD.split("-")[-1])+"-"+str(data.ID.split(".0")[-1].split(".g")[0])+"_auto.jpg"
        fig = plt.figure(figsize=(15.5, 9.5))
        ax = fig.add_subplot(1,1,1)
        plt.tick_params(axis='x', labelsize=42)
        plt.tick_params(axis='y', labelsize=42)
        ax.set_xlim(xmin=3000, xmax=9700)
        #ax.set_ylim(ymin=17.5,ymax=23)
        #ax1.set_xlabel(r'$\lambda$')
        ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
        ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)
        ax.plot(wl, mag_auto, '-k', alpha=0.2)
        #, label='Auto')

        ax.scatter(wl, mag_auto, c=color, marker='s', s=600, zorder=10)
        ax.errorbar(wl, mag_auto, mag_auto_err, marker='s', fmt='.', elinewidth=5.9, markeredgewidth=5.2,  capsize=20)
        #     # plt.text(0.06, 0.1, "Fr 2-21",
        #     #          transform=ax.transAxes, fontsize=48,  fontdict=font)
            #plt.subplots_adjust(bottom=0.19)
        plt.legend(fontsize=16.0)
        plt.title('auto', fontsize=40)
        plt.tight_layout()
        plt.gca().invert_yaxis()
            #save_path = '../../../Dropbox/JPAS/paper-phot/'
            #file_save = os.path.join(save_path, plotfile)
        #plt.savefig(plotfile)
        f2 = plt
        return f2
        plt.clf()
        plt.close()

    def petroplot(self):
        data = self.data
        n = data.RA
        Number = []

        wl = self.wl
        color = self.color

        # wl1 = [3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
        # color1 = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
        # marker1 = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro

        Number = []

        Number = []
        mag_auto  =self.mag_auto

        mag_petro = self.mag_petro
        mag_aper = []

        #Error
        mag_auto_err  = self.mag_auto_err
        mag_petro_err  = self.mag_petro_err

        mag_petro = [np.nan if x == 99.0 else x for x in mag_petro]
        #plotfile = "photos-pectrum_splus_"+str(data.FIELD.split("-")[-1])+"-"+str(data.ID.split(".0")[-1].split(".g")[0])+"_petro.jpg"
        fig = plt.figure(figsize=(15.5, 9.5))
        ax1 = fig.add_subplot(1,1,1)
        plt.tick_params(axis='x', labelsize=42)
        plt.tick_params(axis='y', labelsize=42)
        ax1.set_xlim(xmin=3000, xmax=9700)
        #ax1.set_ylim(ymin=17.5,ymax=23)
        #ax1.set_xlabel(r'$\lambda$')
        ax1.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
        ax1.set_ylabel(r'Magnitude [AB]', fontsize = 44)
        ax1.plot(wl, mag_petro, '-k', alpha=0.2)#, label='Auto')

        ax1.scatter(wl, mag_petro, c = color, s=600, zorder=10)
        ax1.errorbar(wl, mag_petro, mag_petro_err, fmt='.', elinewidth=5.9, markeredgewidth=5.2,  capsize=20)
            # plt.text(0.06, 0.1, "Fr 2-21",
            #          transform=ax.transAxes, fontsize=48,  fontdict=font)
            #plt.subplots_adjust(bottom=0.19)
        plt.legend(fontsize=20.0)
        plt.title('petro', fontsize=40)
        plt.tight_layout()
        plt.gca().invert_yaxis()
            #save_path = '../../../Dropbox/JPAS/paper-phot/'
            #file_save = os.path.join(save_path, plotfile)
        #plt.savefig(plotfile)
        #plt.clf()

        f = plt
        return f
        plt.close()
