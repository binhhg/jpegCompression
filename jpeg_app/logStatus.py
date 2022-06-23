import os, cv2
import numpy as np

def mse(ori, re):
    return np.mean((ori - re) ** 2)

def psnr(ori, re):
    mse_value = mse(ori, re)
    return 10*(np.log10(255*255/mse_value))

def ratio(imageFile, outputPath):
    sizeFileInput = os.path.getsize(imageFile)
    sizeFileOutput = os.path.getsize(outputPath)
    return sizeFileInput/sizeFileOutput

def showCompress(imageFile, outputPath, time):
   
    compressionRatio = ratio(imageFile,outputPath)

    # return nameAlogthim + " Compress: \n" + "   Input File: " + imageFile + "\n   Output File: " + outputPath + "\n   Compress ratio: " + str(compressionRatio)
    
    return  "\n   Output File: "+ outputPath + "\n   Compression Ratio: " + "{:.2f} : 1".format(compressionRatio) +"\n" + "Encode time: "+ str(round(time,3))

def showDecompress(outputPath, fileToSave,  time):
    return  "\n   Output File: " + fileToSave +"\n" + "Decode time: "+ str(round(time,3))


def showMetric(inputPath,compressedPath, outputPath):
    input_img = cv2.imread(inputPath)
    output_img = cv2.imread(outputPath)
    mse_value = mse(input_img, output_img)
    psnr_value = psnr(input_img, output_img)
    compressionRatio = ratio(inputPath,compressedPath)
    # print('Compression Ratio = ',"{:.2f} : 1".format(compressionRatio))
    # print('MSE = ', "{:.3f}".format(mse_value))
    # print('PSNR = ', "{:.3f}".format(psnr_value))
    return "\n Compression Ratio: " + "{:.2f} : 1".format(compressionRatio) + "\n MSE: " +"{:.3f}".format(mse_value) + "\n PSNR: " +"{:.3f}".format(psnr_value)
