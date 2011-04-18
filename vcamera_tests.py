#!/usr/bin/python

import os, sys
from SimpleCV import * 
from nose.tools import with_setup


testimage = "sampleimages/9dots4lines.png"
testoutput = "sampleimages/cam.jpg"


def test_camera_constructor():
  mycam = VirtualCamera(testimage, "image")

  props = mycam.getAllProperties()

  for i in props.keys():
    print str(i) + ": " + str(props[i]) + "\n"
  
  return 1

def test_camera_image():
  mycam = VirtualCamera(testimage, "image")

  img = mycam.getImage()
  img.save(testoutput)
