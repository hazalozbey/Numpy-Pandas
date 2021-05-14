import pandas as pd
import numpy as np
import seaborn as sns
seri=pd.Series([10,88,3,4,5])
print(type(seri))
print(seri.axes)#serini index bilgilerine erişimi sağlar
#numpy array özellikleri pandas serilerindede geçerlidir.
print(seri.values)#değerlerine array formatında ulaşılır
print(seri.head())#en baştan listeler-parametre alır
print(seri.tail())#en sondan listeler-paremetre alır
#index isimlendirme
print("index isimlendirme")
print(pd.Series([99,22,332,94,5]))
print(pd.Series([99,22,332,94,5],index=[1,3,5,7,9]))
seri=pd.Series([99,22,332,94,5],index=["a","b","c","d","e"])
print(pd.Series([99,22,332,94,5],index=["a","b","c","d","e"]))
print(seri["a"])
print(seri["a":"c"])
#Sözlük üzerinden liste oluşturma

sozluk=pd.Series({"reg":10,"log":11,"cart":12})
print(sozluk)
#iki seriyi birleştirerek seri oluşturma

print(pd.concat([seri,seri]))
a=np.array([1,2,33,444,75])
seri=pd.Series(a)
print(seri)
print(seri.keys)
print(list(seri.items()))
#eleman sorgulama
print("a" in seri)
#fancy eleman
print(seri[[2,3]])

print(seri[2:4])

#Pandas DataFrame oluşturma
print("Pandas DataFrame oluşturma")
l=[1,2,39,67,90]
df=pd.DataFrame(l,columns=["degisken_ismi"])
print(df)
m=np.arange(1,10).reshape((3,3))

print(pd.DataFrame(m,columns=["var1","var2","var3"]))

#dataframe isimlendirme

df=pd.DataFrame(m,columns=["var1","var2","var3"])

print(df.head())
df.columns=("deg1","deg2","deg3")

s1=np.random.randint(10,size=5)
s2=np.random.randint(10,size=5)
s3=np.random.randint(10,size=5)

sozluk={"var1":s1,"var2":s2,"var3":s3}
print(sozluk)
df=pd.DataFrame(sozluk)
print(df)
df.index=["a","b","c","d","e"]
print(df)
#Silme
df.drop("a",axis=0,inplace=True)#inplace fonksiyonu dataframe üzerindeki değişikliğin kalıcı olmasını sağlar

print(df)

#fancy ile silme işlemi

l=["c","e"]
print(df.drop(l,axis=0))

print("var1"in df)

l=["var1","var4","var2"]
for i in l:
    print(i in df)

df["var4"]=df["var1"]/df["var2"]

#gözlem ve değişken seçimi loc ve iloc

m=np.random.randint(1,30,size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df)
#loc:tanımlandığı şekli ile seçim yapmak için kullanılır
print(df.loc[0:3])
#iloc:alışık olduğumuz indexleme mantığıyla seçim yapar
print(df.iloc[0:3])
print(df.iloc[0,0])
print(df.iloc[:3,:2])
print(df.loc[0:3,"var3"])
print(df.iloc[0:3]["var3"])
#Koşullu eleman işlemleri
print(df[df.var1>15]["var1"])
#Birleştirme(join)işlemleri
m=np.random.randint(1,30,size=(5,3))
df1=pd.DataFrame(m,columns=["var1","var2","var3"])
df2=df1+99
print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],ignore_index=True))
df2.columns=["var1","var2","deg1"]
print(pd.concat([df1,df2],join="inner"))#ortak olan sütunları birleştirir
#print(pd.concat([df1,df2],join_axes=[df1.columns]))#df1 e göre birleştirmeyi yapar

#ileri birleştirme işlemleri

df1=pd.DataFrame({'calisanlar':['ali','veli','ayse' ,'fatma'],
                  'grup':['Muhasebe','muhendislik','muhendislik','İK']})

df2=pd.DataFrame({'calisanlar':['ayse','ali','veli','fatma'],
                  'ilk_gris':[2010,2009,2014,2019]})

print(pd.merge(df1,df2,on="calisanlar"))

#çoktan teke

df4=pd.DataFrame({'grup':['muhasebe','muhendislik','İK'],
                  'mudur':['caner','mustafa','berkcan']})

df3=pd.merge(df1,df2)

df5=ps.merge(df3,df4)

#çoktan çoka

df6=pd.DataFrame({'grup':['muhasebe','muhasebe','muhendsilik','muhendslik','ik','ik'],
                          'yetenekler':['matematik','excel','kodlama','linux','excel','yonetim']})

df7=pd.merge(df1,df6)
print(df7)

#toplulaştırma ve gruplaştırma

df=sns.load_dataset("planets")
print(df)
print(df.head())
print(df.shape)#gözlem ve değişken sayısı
print(df.mean())#ortalama değer bulur
print(df.count())#içerisindeki değerleri saymak için kullanılır
print(df["mass"].min())
print(df["mass"].max())
print(df["mass"].sum())#değişkenlerin değerlerini toplar
print(df["mass"].std())#standart sapma
print(df.describe())#tüm verilerin betimsel istatislik değerlerini getirir
#df.describe().T --- transpozunu alarak daha rahat okumamızı sağlar
#df.dropna().describe().T ---eksik gözlemleri sildi ve betimsel istatisliği getirdi

#gruplama işlemleri

df=pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                 'veri': [10,11,52,23,43,55]}, columns=['gruplar','veri'])

print(df.groupby("gruplar").mean())#gruplaştırdık ortalamasını aldık.

#İleri toplulaştırma işlemleri(Aggregate,filter,transform,apply)
df=pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                 'degisken1': [10,23,33,22,11,99],
                 'degisken2': [100,253,333,262,111,969]}, columns=['gruplar','degisken1','degisken2'])

#Aggregate
print(df.groupby("gruplar".mean()))

print(df.groupby("gruplar".aggregate([min,np.median,max])))

print(df.groupby("gruplar".aggregate({"degisken1":"min","degisken2":"max"})))

#filter

def filter_func(x):
    return x["degisken1"].std()>9
print(df.groupby("gruplar".filter(filter_func)))

#transform
df_a=df.iloc[:,1:3]
print(df_a.transform(lambda x: x-x.mean()))

#apply

df=pd.DataFrame({
                 'degisken1': [10,23,33,22,11,99],
                 'degisken2': [100,253,333,262,111,969]}, columns=['degisken1','degisken2'])

print(df.apply(np.sum))






























