import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

# Read the image file
image = sitk.ReadImage("./Data/t2.nii.gz")

##
print(type(image))
print(image.GetMetaDataKeys