import os

os.system("python google-image-generation.py 20 bike outputFolder1")
os.system("python grayscale.py outputFolder1 outputFolder2")
os.system("python scale.py outputFolder2 outputFolder3")
os.system("python zip.py outputFolder3 outputFolder3.zip")
os.system("python sendToEmail.py outputFolder3.zip guryanshsingla@gmail.com")
