import numpy as np # numpy kütüphanesi import etme
print("numpy array oluşturma")
a = np.array([1, 2, 3, 4, 5]) # numpy.ndarray tipinde dizi
print(a)
np.array([3.14, 4, 2, 13],dtype="float32") # tip belirtebiliriz
#Sıfırdan Array  oluşturma
np.zeros(10, dtype=int) #sıfırlardan oluşan array
np.ones((3, 5), dtype=int) #3 satır 5 sütunluk birlerden oluşan matris
np.full((3, 5), 3)
np.arange(0, 31, 3) # 0dan 31 e kadar 3er artan dizi
np.linspace(0, 1, 10) # 0 ile 1 arasında 10 tane elemanlı dizi
np.random.normal(10, 4, (3, 4)) #ortalamsı 10 standart sapması:4 dağılımı opsiyonel 3 e 4 lük matris
np.random.randint(0, 10, (3, 3)) #0 ile 10 arasında 3 e 3lük matris
print("Array özellikleri")
# Array özellikleri
'''
   ndim:boyut sayısı
   shape:boyut bilgisi
   size:toplm eleman sayısı
   dtype:array veri tipi
'''
a = np.random.randint(10, size=10)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

b = np.random.randint(10, size=(3, 5))
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)

# Yeniden Şekillendirme
print("Yeniden Şekillendirme")
c = np.arange(1, 10)
print(c)
c = np.arange(1, 10) .reshape((3, 3))
print(c)

#Array Birleştirme
print("Array Birleştirme")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
xy = np.concatenate([x, y])

#iki boyut için
print("iki boyut için")
q = np.array([[1, 2, 3],
            [4, 5, 6]])
w = np.concatenate([q, q])
print(w)
#axis metodu 0 olursa satır bazında birleştirme 1 olursa sütun bazlı birleştirme olur
w=np.concatenate([q,q],axis=1)
print(w)

#Array Ayırma işlemleri

print("Array Ayırma işlemleri")

e=np.array([1,2,3,99,99,3,2,1])
print(e)
r=np.split(e,[3,5])#3 e kadar bir ayır 5 e kadar bir ayır
print(r)
a,b,c=np.split(e,[3,5])
print(a)
print(b)
print(c)
# iki boyutlu ayırma
print("iki boyutlu ayırma")
t=np.arange(16).reshape(4,4)
print(t)

u=np.vsplit(t,[2])#ikinci satıra kadar
print(u)

o=np.hsplit(t,[2])#ikinci sütuna kadar
print(o)

#Array Sıralama

print("Array Sıralama")
p=np.array([2,1,4,3,5])
print(np.short(p))
#iki boyutlu için

print("iki boyut için")
s=np.random.normal(20,5,(3,3))
print(np.sort(s,axis=1))
print(np.sort(s,axis=0))

#İndex ile elemana erişmek
d=np.random.randint(10,size=10)
print(d[-1])

#iki boyutlu için
print("iki boyut için")
f=np.random.randint(10,size=(3,5))
print(f[2,2])
f[2,2]=99
print(f[2,2])

#Slicing ile elemanlara erişmek

g = np.arange(20,30)
print(g[0:3])

#iki boyutlu için
print("iki boyutlu için")

h=np.random.randint(10,size=(5,5))
print(h[:,1])

#Alt küme üzerinde işlem yapmak

j=np.random.randint(10,size=(5,5))

alt_j=j[0:3,0:2]
print(alt_j)
alt_j[0,0]=9999
alt_j[1,1]=88
print(alt_j)
print(j)

k=np.random.randint(10,size=(5,5))
alt_j=j[0:3,0:2].copy()
print(alt_j)
alt_j[0,0]=111123
alt_j[1,1]=41232435
print(alt_j)
print(j)

#Fancy Index ile elemanlara erişmek

l=np.arange(0,30,3)

print([l[1],l[3],l[5]])

al_getir=[1,2,3]
print(l[al_getir])

#iki boyut için
print("iki boyut için")

z=np.arange(9).reshape((3,3))
satir=np.array([0,1])
sutun=np.array([1,2])
print(z[satir,sutun])

#Koşullu eleman işlemleri
#matematiksel ve karşılastırma operatörlerinde çalışır

v=np.array([1,2,3,4,5])

print(v<3)

print(v[v<3])

print(v*5/10)

#ufunc
#operatörleri yazdığımızda python arka tarafta operatörle ilgili fonksiyonu çalıştırır.

print(np.subtract(v,1)) #çıkarma
print(np.add(v,1)) #toplama
print(np.multiply(v,4)) #çarpma
print(np.divide(v,3))
print(np.power(v,3))#kuvvet alma
print(np.mod(v,2))# mod alma

print(np.sin(360))#trigonometrik ifadeler
v=np.array([1,2,3])
print(np.log(v))#logaritmik ifadeler
print(np.log2(v))

#iki bilinmeyenli denklem çözümü
'''
5*x0+x1=12
x0+3*x1=10
denkleminin çözümü
'''
a=np.array([[5,1],[1,3]])
b=np.array([12,10])

x=np.linalg.solve(a,b)
print(x)
