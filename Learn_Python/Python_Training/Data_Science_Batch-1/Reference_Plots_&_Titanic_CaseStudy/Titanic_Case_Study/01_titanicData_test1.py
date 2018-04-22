import numpy as np
import pandas as pd
import pylab
import matplotlib.pyplot as plt

df = pd.read_csv("titanic_dataset.csv")
#~ df = df.drop("name","ticket","cabin")
df = df.drop(["name","ticket","cabin","home.dest","body","boat","embarked"],axis=1)
print df.head()
age1 = df.age.replace(np.nan,df.age.mean())
numOf_male = df.sex.value_counts()["male"]
numOf_female = df.sex.value_counts()["female"]
genderCount = np.array([numOf_male, numOf_female])
#~ print age2
classType = np.array(df.pclass.nunique())
#~ print classType
classCount =np.array([df.pclass.value_counts()[1],df.pclass.value_counts()[2],df.pclass.value_counts()[3]])
#~ print classCount

class_Vs_Survived = df.groupby(["pclass","survived"])
cVs_arr = np.array(())
for i in np.arange(1.0,4.0):
    cVs_arr = np.append(cVs_arr,len(class_Vs_Survived.get_group((i,0.0))))
    cVs_arr = np.append(cVs_arr,len(class_Vs_Survived.get_group((i,1.0))))
print cVs_arr
#~ print len(class_Vs_Survived[(1.0,1.0)])
#~ print [y for y in range(1.0,4.0) [x for x in range(0.,2.)]

plt.subplot(2,3,1)
plt.hist(age1)
plt.title("Age")
plt.subplot(2,3,2)
plt.bar(["male","female"],genderCount)
plt.title("genderCount")
plt.subplot(2,3,3)
plt.bar(('C1', 'C2', 'C3'),classCount)
#~ plt.xticks(np.arange(1,4), ('C1', 'C2', 'C3'))
plt.title("no.Of Passenger by class")
plt.subplot(2,3,4)
#~ plt.plot(np.linspace(0,len(fare),len(fae)),fare)
#~ plt.title("Fare")
x = [0,1,0,1,0,1]
#~ plt.bar(x,cVs_arr,width=0.5,color="b")
#~ plt.bar(x,cVs_arr,width=0.5,color="b")
plt.bar([1],cVs_arr[0],width=0.5,color="r",label='NotSurvived')
plt.bar([1+.3],cVs_arr[1],width=0.5,color="g",label='Survived')
plt.bar([2],cVs_arr[2],width=0.5,color="r")
plt.bar([2+.3],cVs_arr[3],width=0.5,color="g")
plt.bar([3],cVs_arr[4],width=0.5,color="r")
plt.bar([3+.3],cVs_arr[5],width=0.5,color="g")
plt.xticks(np.arange(1,4), ('C1', 'C2', 'C3'))
plt.tight_layout()
plt.plot(np.linspace(1,classType,len(cVs_arr)),cVs_arr)
plt.title("class Vs Survived")
plt.legend()
plt.subplot(2,3,5)
plt.pie(genderCount,labels=["Male","Female"],autopct='%1.1f%%',explode=(0.1,0))
plt.title("Male/Female %")
plt.subplot(2,3,6)
plt.pie(classCount,labels=('C1', 'C2', 'C3'),autopct='%1.1f%%',explode=(0.1,.2,0))
plt.title("% of no.of passengesrs by Class")
#~ plt.show()