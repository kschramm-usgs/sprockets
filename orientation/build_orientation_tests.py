"""
  This python script takes some real data and creates a number of tests data sets for
  examining rotation. 
  
  The examples start with real data, but the original source of the data is unimportant 
  and the test data could be recreated with seismic data from any 3-component broadband
  sensor.
  IU.ANMO.10.BH1 | 2017-08-26T00:00:00.019500Z - 2017-08-26T23:59:59.994500Z | 40.0 Hz, 3456000 samples
  IU.ANMO.10.BH2 | 2017-08-26T00:00:00.019500Z - 2017-08-26T23:59:59.994500Z | 40.0 Hz, 3456000 samples
  
"""
from obspy.core import *
import obspy.signal.rotate as rotate
import numpy as np
import numpy.testing as npt

def rms(x):
  """ Calculate the RMS for validating test data sets.  
  x is a numpy array
  Output
    Returns a scalar
  """
  return np.sqrt(np.mean(np.power(x,2)))
  
def create_rotation_examples(N,E,angles):
  for angle in angles
    r,t=rotate.rotate_ne_rt(N[0].data,E[0].data,angle)
    dir="%03d" % (angle)
    try:
      os.mkdir(dir)
    except:
      # Directory exists do nothing
      pass
    tr_n=N[0].copy()
    tr_n.data=r
    tr_e=E[0].copy()
    tr_e.data=t
    tr_n.write("%s/%s" % (dir,tr_n.stats.id),format='MSEED')
    tr_n.write("%s/%s" % (dir,tr_n.stats.id),fortmat='MSEED')
    
def check_rotation(N,E,angles):
  """ Check rotation angles by rotating the partially rotated the rest of the way to 360 
  since obspy doesn't do the negative and compare to original values.  Should be close to 
  zero"""
  ntests=0
  testsfailed=0
  for angle in angles:
    dir="%03d" % (angle)
    n=read("%s/%s" % (dir,N[0].stats.id))
    e=read("%s/%s" % (dir,N[0].stats.id))
    r,t=rotate.rotate_ne_rt(n[0].data,e[0].data,360.-angle)
    try:
      npt.assert_almost_equal(N[0].data,r)
      ntests+=1
      npt.assert_almost_equal(E[0].data,t)
      ntests+=1
    except:
      testsfailed+=1
  print("Check rotation %d tests passed test %d tests failed" % (ntests,testsfailed)
  return True
    
    
  

  
if __name__=='__main__':
  # Low Noise Examples for data rotation
  N=read('IU.ANMO.10.BH1')
  E=read('IU.ANMO.10.BH2')
  simple_rotation_angles=np.array([2.,5.,20.,90.,110.,180.,200.,270.,290.,355.,358.])
  create_rotation_examples(N,E,simple_rotation_angles)
  check_rotation_examples(N,E,simple_rotation_angles)