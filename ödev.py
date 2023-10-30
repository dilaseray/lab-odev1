import random
import sys
import time
import ast
from termcolor import colored
from consolemenu import *
from consolemenu.items import *


def en_kucuk_deger(listee):
    tekliliste=list(set(listee))
    random_number = random.randint(0, len(tekliliste) -1)
    denetleme = []
    
    randoms = tekliliste[random_number]

    for i in range(0, len(tekliliste)):
        if randoms < tekliliste[i]:
            denetleme.append(True)

    if denetleme.count(True) == len(tekliliste)-1:
        
        
        return randoms
    else:
        return en_kucuk_deger(listee)
    

def k_kucuk(k,liste):
    teklilist=list(set(liste))
    
    if k==1:
        return en_kucuk_deger(liste)
    else:
                                                                      
        for i in range(k-1):
            teklilist.remove(en_kucuk_deger(teklilist))

        return en_kucuk_deger(teklilist)    
    



def en_yakin_cift(int,liste):
    mutlakuzaklıkdict=dict()
    for i in range(len(liste)):
        for a in range(i+1,len(liste)):
            mutlakuzaklık=abs((liste[i]+liste[a])-int)

            mutlakuzaklıkdict[mutlakuzaklık]=(liste[i],liste[a])
    
    mutlakuzaklık=mutlakuzaklıkdict.keys()
    
    return mutlakuzaklıkdict[en_kucuk_deger(mutlakuzaklık)]    





def tekrar_eden_elemanlar(liste):
    
    teklisayılar=[i for i in liste if liste.count(i)!=1]
    indirgenmis=set(teklisayılar)
    return indirgenmis

def matris_carpimi(liste1,liste2):
    sonuc = []
    for satir in liste1:
        s1 = []
        for sutun in list(zip(*liste2)):
            s1.append(sum((sutun[i]*satir[i]  for i in range(len(satir)))))
        sonuc.append(s1)
    return sonuc

def kelime_frekans(yol):
    file=open(yol,"r",encoding="utf-8")
    kelimeler = file.read().split() 
    file.close()
    kelime_sayma = set(kelimeler)
    def hesaplayıcı(kelime):

        return {kelime:kelimeler.count(kelime)}
    
    mapobje=map(hesaplayıcı,kelime_sayma)
    
    duzenlenmislist=list(mapobje)
    return duzenlenmislist




    


maxdonus=0
ortakbolenlist=[]
sayac=1
def eb_ortak_bolen(sayi1,sayi2):
    global ortakbolenlist
    global maxdonus
    global sayac

    if sayi1==0 or sayi2==0:
        return "girilen değer geçersiz"
    
    if sayi1<sayi2:
        maxdonus=sayi1
        sys.setrecursionlimit(maxdonus*100)
    else:
        maxdonus=sayi2
        sys.setrecursionlimit(maxdonus*100)
    if sayi1%sayac==0 and sayi2%sayac==0:
        ortakbolenlist.append(sayac)

    if not (sayac<=maxdonus):

        sonucc=max(ortakbolenlist)
        sayac=1
        ortakbolenlist=[]
        maxdonus=0
       
        return sonucc


    if (sayac<=maxdonus):
        sayac=sayac+1
        return eb_ortak_bolen(sayi1,sayi2)



def asal_veya_degil(int,sayac=2):
    
    if int==sayac:
        return True


    if int%sayac==0:
        return False

    

    return asal_veya_degil(int,sayac=sayac+1)   





def hizlandirici(n,fib_k, fib_k1,k=1):
    if n==1:
        return 1
    if k == n:
        return fib_k
    else:
        fib_k2 = fib_k + fib_k1
        return hizlandirici(n, fib_k2, fib_k,k+1)



def karekok(N, x_0, tol=10**(-10), maxiter=10, iterasyon=0):
    x_son = 0.5 * (x_0 + N / x_0)
    hatapayı = ((x_son**2 - N)**2)**0.5
    if hatapayı < tol:
        return x_son
    if maxiter > iterasyon:
        return karekok(N, x_son, tol, maxiter, iterasyon+1)
    else:
        print("{} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin".format(iterasyon))
        return x_son   


def control(fonk):

    if fonk=="1":
        giris=input("sayı ve liste yapısını boşluk bırakarak giriniz örn: 2  [3,5,6,7,8]   ").split()
        sayı=int(giris[0])
        liste=ast.literal_eval(giris[1])
        
        sonuc=k_kucuk(sayı,liste)
        print("SONUÇ",sonuc)
        time.sleep(5)
        return
    elif fonk=="2":
        giris=input("sayı ve liste yapısını boşluk bırakarak giriniz örn: 2  [3,5,6,7,8]   ").split()
        sayı=int(giris[0])
        liste=ast.literal_eval(giris[1])
        sonuc=en_yakin_cift(sayı,liste)
        print("SONUÇ",sonuc)
        time.sleep(5)
        return
    elif fonk=="3":
        giris=input("listeyi liste formatında girin örn: [2,3,4,5,6,7,8,1]     ")
        liste=ast.literal_eval(giris)
        sonuc=tekrar_eden_elemanlar(liste)
        print("SONUÇ",sonuc)
        time.sleep(5)
        return
    elif fonk=="4":
        giris1=input("ilk matrisi liste formatında girin örn:[[2,3,4],[2,1,2]]      ")
        giris2=input("ikinci matrisi liste formatında girin örn:[[2,3,4],[2,1,2]]    ")
        liste1=ast.literal_eval(giris1)
        liste2=ast.literal_eval(giris2)
        sonuc=matris_carpimi(liste1,liste2)
        print("SONUÇ",sonuc)
        time.sleep(5)
        return
    elif fonk=="5":
        giris=input("dosya uzantısını .txt formatıyla beraber girin  ")
        sonuc=kelime_frekans(giris)
        print("SONUC",sonuc)
        time.sleep(5)
        return
    elif fonk=="6":
        giris=input("listeyi list formatinda girin örn:[2,3,4,5,6,7,]   ")
        liste=ast.literal_eval(giris)
        sonuc=en_kucuk_deger(liste)
        print("SONUÇ",sonuc)
        time.sleep(5)
        return
    elif fonk=="7":
        giris=input("değerlerinizi liste yapısında girin maximiter ve tolerans değeri girmicekseniz 0 yazın parametre sırası [N,x1,maximiter,tolerans] şeklindedir. maximiter ve tolerans girmicekseniz örn kullanım [100,0.1,0,0] şeklindedir   ")
        liste=ast.literal_eval(giris)
        if liste[2]==0 and liste[3]==0:

            sonuc=karekok(N=liste[0],x_0=liste[1])
            print("SONUC",sonuc)
            time.sleep(5)
            return
        elif liste[2]!=0 and liste[3]==0:
            sonuc=karekok(N=liste[0],x_0=liste[1],maxiter=liste[2])
            print("SONUC",sonuc)
            time.sleep(5)
            return
        elif liste[2]==0 and liste[3]!=0:
            sonuc=karekok(N=liste[0],x_0=liste[1],tol=liste[3])
            print("SONUC",sonuc)
            time.sleep(5)
            return
        elif liste[2]!=0 and liste[3]!=0:
            sonuc=karekok(N=liste[0],x_0=liste[1],maxiter=liste[2],tol=liste[3])
            print("SONUC",sonuc)
            time.sleep(5)
            return 


    elif fonk=="8":
        giris=input(" ebobu alınacak 2 sayıyı virgülle ayırarak giriniz örn : 54,32").split(",")
        sayi1=int(giris[0])
        sayi2=int(giris[1])
        sonuc=eb_ortak_bolen(sayi1,sayi2)
        print("SONUÇ",sonuc)
        time.sleep(5)
        return
    elif fonk=="9":
        giris=input(" lüften bir sayı giriniz  ")
        sayi=int(giris)
        sonuc=asal_veya_degil(sayi)
        print("SONUC",sonuc)
        time.sleep(5)
        return

    elif fonk=="10":
        giris=input(" fibonaccinin kaçıncı terimini istiyorsunuz  ")
        sayi=int(giris)
        
        sonuc=hizlandirici(n=sayi,fib_k=1,fib_k1=0)
        print("SONUC",sonuc)
        time.sleep(5)
        return




menu = ConsoleMenu("220501031-220501022 LAB ÖDEV 1", "Seçiniz")

menu_items = [
    colored("k_kucuk", 'red'),
    colored("en_yakin_cift", 'green'),
    colored("tekrar_eden_elemanlar","blue"),
    colored("matris","white"),
    colored("kelime_frekans","yellow"),
    colored("en_kucuk_deger","green"),
    colored("karekok","blue"),
    colored("eb_ortak_bolen","blue"),
    colored("asal_veya_degil","red"),
    colored("hizlandirici","yellow")]

k_kucuk1 = FunctionItem(menu_items[0], control, ["1"])
en_yakin_cift1 = FunctionItem(menu_items[1], control, ["2"])
tekrar_eden_elemanlar1 = FunctionItem(menu_items[2], control, ["3"])
matris1=FunctionItem(menu_items[3],control,["4"])
kelime_frekans1=FunctionItem(menu_items[4],control,["5"])
en_kucuk_deger1=FunctionItem(menu_items[5],control,["6"])
karekok1=FunctionItem(menu_items[6],control,["7"])
eb_ortak_bolen1=FunctionItem(menu_items[7],control,["8"])
asal_veya_degil1=FunctionItem(menu_items[8],control,["9"])
hizlandirici1=FunctionItem(menu_items[9],control,["10"])



menu.append_item(k_kucuk1)
menu.append_item(en_yakin_cift1)
menu.append_item(tekrar_eden_elemanlar1)
menu.append_item(matris1)
menu.append_item(kelime_frekans1)
menu.append_item(en_kucuk_deger1)
menu.append_item(karekok1)
menu.append_item(eb_ortak_bolen1)
menu.append_item(asal_veya_degil1)
menu.append_item(hizlandirici1)

menu.show()