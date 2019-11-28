# import pandas as pd
import operator

def loocv(x,y,at,num):
  count = 0

  for i in range(num):
    x_train = x[:i]+x[i+1:]
    # x_train = x
    x_test = x[i]
    y_train = y[:i]+y[i+1:]
    # y_train = y
    y_test = y[i]

    p = dict()
    for a in at:
      pa = y_train.count(a)/len(y_train)
      xt = []
      for q in range(len(x_train)):
        if (y[q] == a):
          xt.append(x_train[q])
      # xt = [q if (q[-1] == a) for q in x_train]
      # print(xt)

      for j in range(len(x_test)):
        col1 = [q[j] for q in x_train]
        col2 = [q[j] for q in xt]

        e = col2.count(x_test[j])
        b = len(col2)
        c = len(col1)
        d = col1.count(x_test[j])
        if(d == 0):
          d=1

        # print(i,a,b,c,d)

        pa *= (e/b) * (c/d)

      p[a] = pa

    key = max(p.items(), key=operator.itemgetter(1))[0]

    if key == y_test:
      count+=1

  return count/num*100


def et(x_train,x_test,y_train,y_test,at):
  count = 0
  for i in range(len(x_test)):
    p = dict()
    for a in at:
      pa = y_train.count(a)/len(y_train)
      xt = []
      for q in range(len(x_train)):
        if (y_train[q] == a):
          xt.append(x_train[q])
      # xt = [q if (q[-1] == a) for q in x_train]
      # print(xt)

      for j in range(len(x_test[i])):
        col1 = [q[j] for q in x_train]
        col2 = [q[j] for q in xt]

        e = col2.count(x_test[i][j])
        b = len(col2)
        c = len(col1)
        d = col1.count(x_test[i][j])
        if(d == 0):
          d=1

        # print(i,a,b,c,d)

        pa *= (e/b) * (c/d)

      p[a] = pa

    key = max(p.items(), key=operator.itemgetter(1))[0]

    if key == y_test[i]:
      count+=1

  return count/len(y_test)*100

