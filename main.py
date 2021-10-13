import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pgo
import statistics
import random

getData = pd.read_csv("savings_data.csv")
population = getData["quant_saved"].tolist()

scatter = px.scatter(getData, y="quant_saved",color="female")
# scatter.show()

meanPop = statistics.mean(population)
medianPop = statistics.median(population)
modePop = statistics.mode(population)
sdPop = statistics.stdev(population)

def findSample1 (counter) :
  sample1 = []
  for i in range (0,counter) :
    index = random.randint(0,len(population)-1)
    value = population[index]
    sample1.append(value)
  meanFind = statistics.mean(sample1)
  return meanFind

def findSample2 (counter) :
  sample2 = []
  for i in range (0,counter) :
    index = random.randint(0,len(population)-1)
    value = population[index]
    sample2.append(value)
  meanFind = statistics.mean(sample2)
  return meanFind

sampleList1 = []
sampleList2 = []
for i in range (0,100) :
  sample1 = findSample1(100)
  sample2 = findSample2(100)
  sampleList1.append(sample1)
  sampleList2.append(sample2)

meanSampleList1 = statistics.mean(sampleList1)
medianSampleList1 = statistics.median(sampleList1)
modeSampleList1 = statistics.mode(sampleList1)
sdSampleList1 = statistics.stdev(sampleList1)
meanSampleList2 = statistics.mean(sampleList2)
medianSampleList2 = statistics.median(sampleList2)
modeSampleList2 = statistics.mode(sampleList2)
sdSampleList2 = statistics.stdev(sampleList2)

correlation1 = meanPop - meanSampleList1
correlation2 = meanPop - meanSampleList2
correlation3 = meanSampleList1 - meanSampleList2

print("The first correlation is", correlation1)
print("The second correlation is", correlation2)
print("The third correlation is", correlation3)