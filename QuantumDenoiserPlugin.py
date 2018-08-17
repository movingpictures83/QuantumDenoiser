import sys
import numpy



class QuantumDenoiserPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)

      # Read the entire adjacency matrix
      #self.ADJ = numpy.zeros([self.m, self.n])
      self.ADJ = []
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = int(contents[j+1])
               #print self.ADJ[i][j]
               self.ADJ[i].append(value)
               #self.ADJ[i][j] = value
            i += 1

      # Form a second adjacency matrix with all nodes with only one quantum removed
      # Note the bacteria *and* the row must be gone
      self.QUANTA = []
      for j in range(self.n):
         onlyone = True
         for i in range(self.m):
            if (self.ADJ[i][j] != 1):
               onlyone = False
               continue
         if (onlyone):
            self.bacteria.remove(self.bacteria[i])
         else:
            row = []
            for i in range(self.m):
               row.append(self.ADJ[i][j])
            self.QUANTA.append(row)

      self.n = len(self.bacteria) # New length after removal

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      # First line
      for j in range(self.n):
         if (j != self.n-1):
            filestuff2.write(self.bacteria[j].strip()+",")      
         else:
            filestuff2.write(self.bacteria[j].strip()+"\n") 
      
      # Quanta
      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.QUANTA[j][i]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



