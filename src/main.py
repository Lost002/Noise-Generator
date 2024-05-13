from random import randint
from createimg import create_noise
from sys import argv

class Generate_Noise:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def discrete_noise(self, name="Discrete_Noise"): ## name
    noise = []
    row = []
    
    for y in range(self.height):
      for x in range(self.width):
        row.append(randint(0,100)/100)
      noise.append(row)
      row = []

      create_noise(noise, name)

  def spotted_noise(self, infrequence=10, density=2, inverse=0, name="Spotted_Noise"): ## infrequence, density, inverse, name
    if not inverse:
      main_color = 0
      spotted_color = 1
    elif inverse:
      main_color = 1
      spotted_color = 0
    else:
      main_color = 0
      spotted_color = 1
      
    noise = []
    row = []

    count = 0

    for y in range(self.height):
      for x in range(self.width):
        
        if randint(0,infrequence) == 0 and count < density:
          row.append(spotted_color)
          count += 1
        else:
          row.append(main_color)
          
      noise.append(row)
      row = []
              
      create_noise(noise, name)

    

if __name__ == "__main__":
  if argv[1] == "-d":
    Generate_Noise(int(argv[2]), int(argv[3])).discrete_noise(argv[4])
  elif argv[1] == "-s":
    Generate_Noise(int(argv[2]), int(argv[3])).spotted_noise(int(argv[4]), int(argv[5]), int(argv[6]), argv[7])
    
