# -*- coding: utf-8 -*-
"""
  A little of Rocket Science with Audio.
"""
import os
import time
import itertools
import math
import warnings

import numpy as np
import scipy.io.wavfile

import belonesox_tools.MiscUtils  as ut
import scipy.io.wavfile as wf

class AudioChecker(object):
    """
    """
    def __init__(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            np.seterr(all='ignore')
            
            
    def process_file(self, file_):        
        if not file_.startswith('~~') and file_.endswith('.avi'):
            print "Processing %s" % file_
            wavfile_  = "%s$w32.wav" % file_
            os.system('!sat b "%s" --selfrunned' % wavfile_)
            try:
                rate, wavdata = wf.read(wavfile_)
                # bad = np.any(abs(wavdata)>28000)
                bad = np.where(abs(wavdata)>31500)
                # maxampl = max(wavdata) #np.linalg.norm(wavdata, ord=np.inf)
                if len(bad[0])>0:
                    print bad[0].shape[0]
                    if bad[0].shape[0]>1000:
                        print "Brak %s!" % file_
                        seconds = np.unique(bad[0]/rate)
                        for second in seconds:
                            print ut.ms2time(second*1000)
                        # print bad
                    pass
            except MemoryError as ex_:
                pass
            
    def process_directory(self, dir_):
        os.chdir(dir_)
        files_  =  os.listdir(dir_)
        for file_ in files_:
            self.process_file(file_)

        pass

if __name__ == '__main__':
    ac = AudioChecker()
    ac.process_file(r'bad.avi')
    #ac.process_directory(r'F:\2018-lvee-release')
    pass