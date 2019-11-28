from naive_bayes import loocv,et
import pandas as pd

fin = pd.DataFrame(columns = ['Dataset','Accuracy(%)'])

# Dataset - Tic-tac-toe endgame
data = pd.read_csv("tic-tac-toe.data",header=None)
x = data.iloc[:,:-1].values.tolist()
y = data.iloc[:,-1].values.tolist()
at = set(y)

s = loocv(x,y,at,data.shape[0])
print("Tic-tac-toe",s)
fin.loc[0,'Dataset'] = 'Tic-tac-toe Endgame'
fin.loc[0,'Accuracy(%)'] = s


# Dataset - SPECT heart dataset
training = pd.read_csv("SPECT.train", header=None)
test = pd.read_csv("SPECT.test", header=None)

x_train = training.iloc[:,1:].values.tolist()
x_test = test.iloc[:,1:].values.tolist()
y_train = training.iloc[:,0].values.tolist()
y_test = test.iloc[:,0].values.tolist()
at = set(y_train)

s = et(x_train,x_test,y_train,y_test,at)
print("SPECT",s)
fin.loc[1,'Dataset'] = 'SPECT heart Dataset'
fin.loc[1,'Accuracy(%)'] = s


# Dataset - Soybean small dataset
data = pd.read_csv("soybean-small.data")
# data = data.sample(frac=1)
x = data.iloc[:,:-1].values.tolist()
y = data.iloc[:,-1].values.tolist()
at = set(y)

s = loocv(x,y,at,data.shape[0])
print("Soybean",s)
fin.loc[2,'Dataset'] = 'Soybean (small)'
fin.loc[2,'Accuracy(%)'] = s


# Dataset - Shuttle Landing Control
data = pd.read_csv("shuttle-landing-control.data")
# data = data.sample(frac=1)
x = data.iloc[:,1:].values.tolist()
y = data.iloc[:,0].values.tolist()
at = set(y)

s = loocv(x,y,at,data.shape[0])
print("Shuttle landing control",s)
fin.loc[3,'Dataset'] = 'Shuttle landing control'
fin.loc[3,'Accuracy(%)'] = s


# Dataset - Monks-1
training = pd.read_csv("monks-1.train", header=None)
test = pd.read_csv("monks-1.test", header=None)
training = training.iloc[:,:-1]
test = test.iloc[:,:-1]

x_train = training.iloc[:,2:].values.tolist()
x_test = test.iloc[:,2:].values.tolist()
y_train = training.iloc[:,1].values.tolist()
y_test = test.iloc[:,1].values.tolist()
at = set(y_train)

s = et(x_train,x_test,y_train,y_test,at)
print("Monks-1",s)
fin.loc[4,'Dataset'] = 'Monks-1'
fin.loc[4,'Accuracy(%)'] = s


# Dataset - Monks-2
training = pd.read_csv("monks-2.train", header=None).iloc[:,:-1]
test = pd.read_csv("monks-2.test", header=None).iloc[:,:-1]

x_train = training.iloc[:,2:].values.tolist()
x_test = test.iloc[:,2:].values.tolist()
y_train = training.iloc[:,1].values.tolist()
y_test = test.iloc[:,1].values.tolist()
at = set(y_train)

s = et(x_train,x_test,y_train,y_test,at)
print("Monks-2",s)
fin.loc[5,'Dataset'] = 'Monks-2'
fin.loc[5,'Accuracy(%)'] = s


# Dataset - Monks-3
training = pd.read_csv("monks-3.train", header=None).iloc[:,:-1]
test = pd.read_csv("monks-3.test", header=None).iloc[:,:-1]

x_train = training.iloc[:,2:].values.tolist()
x_test = test.iloc[:,2:].values.tolist()
y_train = training.iloc[:,1].values.tolist()
y_test = test.iloc[:,1].values.tolist()
at = set(y_train)

s = et(x_train,x_test,y_train,y_test,at)
print("Monks-3",s)
fin.loc[6,'Dataset'] = 'Monks-3'
fin.loc[6,'Accuracy(%)'] = s


fin.to_csv("Data.csv")










