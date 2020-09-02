#importing scikit learn library
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import pandas as pd

import pickle

df = pd.read_csv('colours_rgb_shades.csv')
#print(df.isnull().sum())

colormap={}
count=0
for i in df['matching color'].unique():
	if i not in colormap:
		colormap[i]=count
		count+=1

print(colormap)

df['color']=df.apply(lambda x:colormap[x[4]],axis=1)

print(df.tail(5))

X = df[['R','G','B']]
y = df['color']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)

#defining model
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train,y_train)

#checking its accuracy
print("trained accuracy:",model.score(X_train,y_train))
print("generalized accuracy:",model.score(X_test,y_test))

file_name = 'colour_model.sav'
#saving model
pickle.dump(model,open(file_name,'wb'))

#loading model
loaded_model = pickle.load(open(file_name, 'rb'))
result = loaded_model.score(X_test, y_test)
print("loaded model score:",result)


