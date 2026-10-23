import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import sys

cevap = input("Fiyat bilgilendirme listesini görmek için 'E', görmek istemiyorsanız 'H' yazın. \nCevap: ")
while cevap != 'E' and cevap != 'H':
    cevap = input('HATA! Lütfen doğru yazdığınızdan emin olun \nCevap: ')
    
if cevap == 'E':
    print('Liste hazirlaniyor...\n------------------------------------------------------------------------------------------------------')

    fiyat_bilgi_listesi = pd.MultiIndex.from_tuples([('Abone Bilgileri', 'Abone Tipi kodu'),
        ('Abone Bilgileri', 'Abone Tipi '),
        ('Su Tuketim Tarifesi', 'Kademe'),
        ('Su Tuketim Tarifesi', '   Birim Fiyat'),
        ('Atık Su Tarifesi', 'Kademe'),
        ('Atık Su Tarifesi', '  Birim Fiyat')])

    data = [[1, 'Konut', '1.Kademe (0-13 ton)', '2.24 TL', 'Kademesiz', '1.91 TL'],
        [1, 'Konut', '2.Kademe (14-20 Ton)', '5.78 TL', 'Kademesiz', '1.91 TL'],
        [1, 'Konut', '3.Kademe (21+ Ton)', '9.33 TL', 'Kademesiz', '1.91 TL'],
        [2, 'İşyeri', '1.Kademe (0-10 Ton)', '7.71 TL', 'Kademesiz', '3.79 TL'],
        [2, 'İşyeri', '2.Kademe (11+ Ton)', '8.88 TL', 'Kademesiz', '3.79 TL'],
        [3, 'Kamu Kurumu', 'Kademesiz', '6.64 TL', 'Kademesiz', '2.56 TL'],
        [4, 'Turistlik Tesis', 'Kademesiz', '5.78 TL', 'Kademesiz', '1.91 TL']]

    df = pd.DataFrame(data, index=['->','->','->','->','->','->','->'], columns=fiyat_bilgi_listesi)
    print(df)

else:
    print("Fiyat bilgilendirme listesini görüntüleme işlemi atlandı.")

print('------------------------------------------------------------------------------------------------------')


def Fiyatlandırma(AboneTipi,KullanılanSu,GünSayısı):
    if AboneTipi == 1:
        if KullanılanSu <= (13*(GünSayısı/30)):
            SuFaturası = KullanılanSu * 2.24

        elif KullanılanSu <= (20*(GünSayısı/30)):
            SuFaturası = (13*(GünSayısı/30))*24 + (KullanılanSu - (13*(GünSayısı/30)*5.78))

        else:
            SuFaturası = (13*GünSayısı/30*2.24)+((7*GünSayısı/30)*5.78)+(KullanılanSu-(20*GünSayısı/30))*9.33

        return SuFaturası

    elif AboneTipi == 2:
        if KullanılanSu <= (10 * (GünSayısı / 30)):
            SuFaturası = KullanılanSu * 7.71
        else:
            SuFaturası = ((10 * (GünSayısı / 30)) * 7.71) + ((KullanılanSu - (10 * (GünSayısı / 30))) * 8.88)

        return SuFaturası

    elif AboneTipi == 3:
        SuFaturası = KullanılanSu * 6.64
        return SuFaturası

    else:
        SuFaturası=KullanılanSu * 5.78
        return SuFaturası

def VeriAlma():
    Durum = True
    while Durum:

        Koşul = True

        while Koşul:
            AboneTipi = int(input("Abone Tipini Kodunu Giriniz : "))

            if AboneTipi >= 1 and AboneTipi <= 4:
                Koşul = False
            else :
                print("Lütfen [1-4] arasında bir değer giriniz!")
                pass

        KişiSayısı = input("Başka abone girilecek mi E / H   : ")

        if KişiSayısı == "E":
            KişiSayısı = int(input("Kaç kişi girilecek : "))

            for i in range(1 , KişiSayısı+1):
                while True:
                    ÖncekiSayaç = int(input(f"{i}. kişi için önceki sayaç değerini giriniz : "))
                    if ÖncekiSayaç >= 0:
                        break
                    else:
                        print("Sıfırdan büyük bir değer girmelisiniz!")
                        pass

                while True:
                    ŞimdikiSayaç = int(input(f"{i}. kişi için şimdiki sayaç değerini giriniz : "))
                    if ŞimdikiSayaç >= ÖncekiSayaç:
                        break
                    else:
                        print("Önceki sayaç değerinden büyük veya eşit olmalıdır!")
                        pass

                while True:
                    GünSayısı = int(input(f"{i}.kişi için gün sayısını giriniz : "))
                    if GünSayısı >= 0:
                        break
                    else:
                        print("Sıfırdan büyük bir değer girmelisiniz!")
                        pass
                df.loc[len(df)] = [AboneTipi , ÖncekiSayaç , ŞimdikiSayaç , GünSayısı]


            Durum = False

        elif KişiSayısı == "H":
            KişiSayısı = 1
            while True:
                ÖncekiSayaç = int(input("Önceki sayaç değerini giriniz : "))
                if ÖncekiSayaç >= 0:
                    break
                else:
                    print("Sıfırdan büyük bir değer girmelisiniz!")
                    pass

            while True:
                ŞimdikiSayaç = int(input("Şimdiki sayaç değerini giriniz : "))
                if ŞimdikiSayaç >= ÖncekiSayaç:
                    break
                else:
                    print("Önceki sayaç değerinden büyük veya eşit olmalıdır!")
                    pass

            while True:
                GünSayısı = int(input("Gün sayısını giriniz : "))
                if GünSayısı >= 0:
                    break
                else:
                    print("Sıfırdan büyük bir değer girmelisiniz!")
                    pass

            df.loc[len(df)] = [AboneTipi , ÖncekiSayaç , ŞimdikiSayaç , GünSayısı]
            Durum = False

        else:
            print("Hatalı giriş!\n")
            Durum = True

def AtıkSuÜcretiHesaplama(AboneTipi,KullanılanSu):
    if AboneTipi == 1:
        return KullanılanSu * 1.91
    elif AboneTipi == 2:
        return KullanılanSu * 3.79
    elif AboneTipi == 3:
        return KullanılanSu * 2.56
    else:
        return KullanılanSu * 1.91

df = pd.DataFrame({
    "Abone Tipi" : [],
    "Önceki Sayaç" : [],
    "Şimdiki Sayaç" : [],
    "Gün Sayısı" : []
})


VeriAlma()

while True:
    Döngü = input("Başka veri girişi yapıcak mısınız ? E / H   : ")

    if Döngü == "E":
        VeriAlma()
    elif Döngü == "H":
        break
    else:
        print("Hatalı giriş!\n")


df["Kullanılan Su (Ton)"] = df["Şimdiki Sayaç"] - df["Önceki Sayaç"]
df["Su Tüketim Ücreti"] = df.apply(
                                    lambda __Değer__: Fiyatlandırma(__Değer__["Abone Tipi"], __Değer__["Kullanılan Su (Ton)"], __Değer__["Gün Sayısı"]),
                                    axis=1
                                    )
df["Atık Su Ücreti"] = df.apply(
                                lambda __Değer__: AtıkSuÜcretiHesaplama(__Değer__["Abone Tipi"], __Değer__["Kullanılan Su (Ton)"]),
                                axis=1
                                )
df["KDV Ücreti"] = (df["Su Tüketim Ücreti"] + df["Atık Su Ücreti"]) * 0.08
df["Toplam Ücret"] = df["Su Tüketim Ücreti"] + df["Atık Su Ücreti"] + df["KDV Ücreti"]
print("\n")
print(df[["Abone Tipi","Kullanılan Su (Ton)","Su Tüketim Ücreti","Atık Su Ücreti","KDV Ücreti","Toplam Ücret"]])
print("\n")



##########################################################################-istenilen sorular-#####################################################################################################
# 1. Soru
print("------------------------------------------------------------------------------------------------------ \n")
Aboneler = df.groupby(df["Abone Tipi"]).agg("size")
Veriler1 = pd.DataFrame({
    "Abone Tipi" : Aboneler.index,
    "Abone Sayı" : Aboneler.values
                        })
Veriler1["Yüzde"] = (Veriler1["Abone Sayı"] / len(df)) * 100
ToplamSuMiktarı = df.groupby("Abone Tipi")["Kullanılan Su (Ton)"].sum().reset_index()
ToplamGün = df.groupby("Abone Tipi")["Gün Sayısı"].sum().reset_index()
BirlesmisVeri = pd.merge(ToplamSuMiktarı, ToplamGün, on="Abone Tipi", how="inner")
BirlesmisVeri["GünkOrt"] = BirlesmisVeri["Kullanılan Su (Ton)"] / BirlesmisVeri["Gün Sayısı"]
Veriler1 = pd.merge(Veriler1, BirlesmisVeri[["Abone Tipi", "GünkOrt"]], on="Abone Tipi", how="left")

print(Veriler1.head(len(Veriler1)))

print("\n------------------------------------------------------------------------------------------------------\n")
# 2. Soru
Tip1Kademe = df.loc[
    (df["Abone Tipi"] == 1) & (df["Kullanılan Su (Ton)"] <= (13 * (df["Gün Sayısı"] / 30))),
    "Kullanılan Su (Ton)"
].count()
Tip1Toplam = df.loc[df["Abone Tipi"] == 1, "Kullanılan Su (Ton)"].count()
if Tip1Toplam > 0:
    Tip1Yüzde = (Tip1Kademe / Tip1Toplam) * 100
else:
    Tip1Yüzde = 0

print("Aylık su tüketim miktarı, 1. kademeyi aşmayan konut abonelerinin:")
print(f"Sayısı: {Tip1Kademe}")
print(f"Yüzdesi: %{Tip1Yüzde:.2f}")
print("\n------------------------------------------------------------------------------------------------------\n")
# 3. Soru

Tip2Kademe = df.loc[
    (df["Abone Tipi"] == 2) & (df["Kullanılan Su (Ton)"] > (10 * (df["Gün Sayısı"] / 30))),
    "Kullanılan Su (Ton)"
].count()
Tip2Toplam = df.loc[df["Abone Tipi"] == 2, "Kullanılan Su (Ton)"].count()
if Tip2Toplam > 0:
    Tip2Yüzde = (Tip2Kademe / Tip2Toplam) * 100
else:
    Tip2Yüzde = 0

print("Aylık su tüketim miktarı, 2. kademeyi aşan işyeri abonelerinin:")
print(f"Sayısı: {Tip2Kademe}")
print(f"Yüzdesi: %{Tip2Yüzde:.2f}")
print("\n------------------------------------------------------------------------------------------------------\n")

# 4. Soru
result = df.loc[df["Abone Tipi"] == 1].copy()
result["Günlük Ortalama Su Tüketimi"] = result["Kullanılan Su (Ton)"] / result["Gün Sayısı"]
MaxTük = result["Günlük Ortalama Su Tüketimi"].max()

print("Günlük ortalama su tüketim miktarı en yüksek olan konut tipi abonenin:")
print(f"Günlük ortalama su tüketim miktarı: {MaxTük:.2f} ton")
print("\n------------------------------------------------------------------------------------------------------\n")

# 5. Soru
MaxÜcretId = df["Su Tüketim Ücreti"].idxmax()
MaxÜcretId_ = df.loc[MaxÜcretId]
Abone = {
    1: "Konut",
    2: "İşyeri",
    3: "Kamu Kurumu",
    4: "Turistik Yer"
}.get(MaxÜcretId_['Abone Tipi'], "Bilinmeyen")

print("\nAylık su tüketim ücreti en yüksek olan abonenin:")
print(f"Abone tipi: {Abone}")
print(f"Aylık su tüketim miktarı: {MaxÜcretId_['Kullanılan Su (Ton)']} ton")
print(f"Ödediği aylık su tüketim ücreti: {MaxÜcretId_['Su Tüketim Ücreti']:.2f} TL")
print("\n------------------------------------------------------------------------------------------------------\n")

# 6. Soru
MaxÜcretIdAtıkSu = df["Atık Su Ücreti"].idxmax()
MaxÜcretId_ = df.loc[MaxÜcretId]
Abone = {
    1: "Konut",
    2: "İşyeri",
    3: "Kamu Kurumu",
    4: "Turistik Yer"
}.get(MaxÜcretId_['Abone Tipi'], "Bilinmeyen")

print("Aylık atık su ücreti en yüksek olan abonenin:")
print(f"Abone tipi: {Abone}")
print(f"Aylık su tüketim miktarı: {MaxÜcretId_['Kullanılan Su (Ton)']} ton")
print(f"Ödediği aylık atık su ücreti: {MaxÜcretId_['Atık Su Ücreti']:.2f} TL")
print("\n------------------------------------------------------------------------------------------------------")

# 7. Soru
Abone = {
    1: "Konut",
    2: "İşyeri",
    3: "Kamu Kurumu",
    4: "Turistik Yer"
}
ToplamSu = df.groupby("Abone Tipi")["Kullanılan Su (Ton)"].sum().reset_index()
ToplamSu["Abone Tipi"] = ToplamSu["Abone Tipi"].map(Abone)
Toplam = ToplamSu["Kullanılan Su (Ton)"].sum()
ToplamSu.loc[len(ToplamSu)] = ["Toplam", Toplam]
print("\n")
print(f"Abone Tipine Göre Toplam Su Tüketim Miktarı :  \n{ToplamSu}")
print("\n------------------------------------------------------------------------------------------------------")


# 8. Soru
ToplamÜcret = df.groupby("Abone Tipi")["Su Tüketim Ücreti"].sum().reset_index()
Abone = {
    1: "Konut",
    2: "İşyeri",
    3: "Kamu Kurumu",
    4: "Turistik Yer"
}
ToplamÜcret["Abone Tipi"] = ToplamÜcret["Abone Tipi"].map(Abone)
Toplam = ToplamÜcret["Su Tüketim Ücreti"].sum()
ToplamÜcret.loc[len(ToplamÜcret)] = ["Toplam", Toplam]
print("\n")
print(f"Abone Tipine Göre Toplam Su Tüketim Ücretleri : \n {ToplamÜcret}")
print("\n")
print('------------------------------------------------------------------------------------------------------')

# 9. Soru
ToplamAtıkSuÜcteri = df["Atık Su Ücreti"].sum()
print("\n")
print(f"Aylık toplam atık su ücreti: {ToplamAtıkSuÜcteri:.2f} TL")
print("\n")
print('------------------------------------------------------------------------------------------------------')

# 10. Soru
ToplamKDV = df["KDV Ücreti"].sum()
print("\n")
print(f"Devlete ödenen aylık toplam KDV tutarı: {ToplamKDV:.2f} TL")
print("\n")
print('------------------------------------------------------------------------------------------------------')

##########################################################################-Grafikler-#####################################################################################################
#Pasta grafigi

Durum1 = True
while Durum1:
    abc = input('Hesaplamalarla alakali grafikleri görmek için \'E\' görmek istemiyorsaniz \'H\' yazin: ' )
    if abc == 'E':
        
        toplam_ucret = ToplamÜcret.loc[ToplamÜcret["Abone Tipi"] != "Toplam", "Su Tüketim Ücreti"]
        abone_tipi = ToplamÜcret.loc[ToplamÜcret["Abone Tipi"] != "Toplam", "Abone Tipi"]

        plt.figure(figsize=(8, 6))
        plt.pie(toplam_ucret, labels=abone_tipi, autopct='%1.1f%%', startangle=140, 
                colors=["red", "blue", "green", "orange"])
        plt.title("Abone Tipine Göre Ücret Dağılımı (Yüzde)")
        plt.show()

        #-------------------------------------------------
        #abone dagilimi

        abone_sayilari = Veriler1["Abone Sayı"]
        abone_tipi = ["Konut", "İşyeri", "Kamu Kurumu", "Turistik Yer"]

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        wedges, texts, autotexts = ax.pie(abone_sayilari, autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100.*np.sum(abone_sayilari))} kişi)",
                                        textprops=dict(color="w"), colors=["red", "blue", "green", "orange"])

        ax.legend(wedges, abone_tipi,
                title="Abone Tipleri",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")
        ax.set_title("Kişilerin Dağılımı")
        plt.show()


        #-------------------------------------

        # Ücret dağılımı
        toplam12 = df["Su Tüketim Ücreti"].sum()  
        toplam13 = df["Atık Su Ücreti"].sum()     
        toplam14 = df["KDV Ücreti"].sum()         

        grafik2 = ['Su tuketim ücreti', 'Atık su ucreti', 'Kdv tutarı']
        counts = [toplam12, toplam13, toplam14]
        bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

        fig, ax = plt.subplots()
        ax.bar(grafik2, counts, color=bar_colors)

        ax.set_ylabel('Ücret Dağılımı')
        ax.set_title('Toplam Ücret Dağılımı')

        for i, v in enumerate(counts):
            ax.text(i, v + 0.02 * max(counts), f"{v:.2f}", ha='center', va='bottom', fontsize=10)

        plt.show()

        #-------------------------------------------

        # Toplam değerlerin hesaplanması
        toplam_su_tuketim_ucretleri = df.groupby("Abone Tipi")["Su Tüketim Ücreti"].sum()
        toplam_atik_su_ucretleri = df.groupby("Abone Tipi")["Atık Su Ücreti"].sum()
        toplam_kdv_ucretleri = df.groupby("Abone Tipi")["KDV Ücreti"].sum()

        Abone_Tipleri= ["Konut", "İşyeri", "Kamu Kurumu", "Turistlik Tesis"]


        Fiyat_Tarifesi = {
            'Su Tük. Ücreti (TL)': [toplam_su_tuketim_ucretleri.get(i, 0) for i in range(1, 5)],
            'Atık Su Tük. Ücreti (TL)': [toplam_atik_su_ucretleri.get(i, 0) for i in range(1, 5)],
            'KDV (TL)': [toplam_kdv_ucretleri.get(i, 0) for i in range(1, 5)],
        }


        x = np.arange(len(Abone_Tipleri))  
        genislik = 0.25  
        carpan = 0

        fig, ax = plt.subplots(layout='constrained')

        for ozellik, olcum in Fiyat_Tarifesi.items():
            dnge = genislik * carpan
            dörtgen = ax.bar(x + dnge, olcum, genislik, label=ozellik)
            ax.bar_label(dörtgen, padding=3)
            carpan += 1


        ax.set_ylabel('Ücret (TL)')
        ax.set_title('Ödenen Toplam Ücretlere Göre Dağılım')
        ax.set_xticks(x + genislik, Abone_Tipleri)
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, max(max(v) for v in Fiyat_Tarifesi.values()) + 50)

        plt.show()



        toplam_ucret = ToplamÜcret.loc[ToplamÜcret["Abone Tipi"] != "Toplam", "Su Tüketim Ücreti"]
        abone_tipi = ToplamÜcret.loc[ToplamÜcret["Abone Tipi"] != "Toplam", "Abone Tipi"]


        abone_sayilari = Veriler1["Abone Sayı"]
        abone_tipi_2 = ["Konut", "İşyeri", "Kamu Kurumu", "Turistik Yer"]


        toplam12 = df["Su Tüketim Ücreti"].sum()  
        toplam13 = df["Atık Su Ücreti"].sum()     
        toplam14 = df["KDV Ücreti"].sum()     

        grafik2 = ['Su tuketim ücreti', 'Atık su ucreti', 'Kdv tutarı']
        counts = [toplam12, toplam13, toplam14]
        bar_colors = ['tab:red', 'tab:blue', 'tab:orange']


        toplam_su_tuketim_ucretleri = df.groupby("Abone Tipi")["Su Tüketim Ücreti"].sum()
        toplam_atik_su_ucretleri = df.groupby("Abone Tipi")["Atık Su Ücreti"].sum()
        toplam_kdv_ucretleri = df.groupby("Abone Tipi")["KDV Ücreti"].sum()

        Abone_Tipleri = ["Konut", "İşyeri", "Kamu Kurumu", "Turistlik Tesis"]

        Fiyat_Tarifesi = {
            'Su Tük. Ücreti (TL)': [toplam_su_tuketim_ucretleri.get(i, 0) for i in range(1, 5)],
            'Atık Su Tük. Ücreti (TL)': [toplam_atik_su_ucretleri.get(i, 0) for i in range(1, 5)],
            'KDV (TL)': [toplam_kdv_ucretleri.get(i, 0) for i in range(1, 5)],
        }

        x = np.arange(len(Abone_Tipleri))
        genislik = 0.25


        fig, axs = plt.subplots(2, 2, figsize=(15, 12))


        axs[0, 0].pie(toplam_ucret, labels=abone_tipi, autopct='%1.1f%%', startangle=140, 
                    colors=["red", "blue", "green", "orange"])
        axs[0, 0].set_title("Abone Tipine Göre Ücret Dağılımı (Yüzde)")


        wedges, texts, autotexts = axs[0, 1].pie(abone_sayilari, autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100.*np.sum(abone_sayilari))} kişi)",
                                                textprops=dict(color="w"), colors=["red", "blue", "green", "orange"])
        axs[0, 1].legend(wedges, abone_tipi_2, title="Abone Tipleri", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        axs[0, 1].set_title("Kişilerin Dağılımı")


        axs[1, 0].bar(grafik2, counts, color=bar_colors)
        axs[1, 0].set_ylabel('Ücret Dağılımı')
        axs[1, 0].set_title('Toplam Ücret Dağılımı')

        for i, v in enumerate(counts):
            axs[1, 0].text(i, v + 0.02 * max(counts), f"{v:.2f}", ha='center', va='bottom', fontsize=10)


        carpan = 0
        for ozellik, olcum in Fiyat_Tarifesi.items():
            dnge = genislik * carpan
            dörtgen = axs[1, 1].bar(x + dnge, olcum, genislik, label=ozellik)
            axs[1, 1].bar_label(dörtgen, padding=3)
            carpan += 1

        axs[1, 1].set_ylabel('Ücret (TL)')
        axs[1, 1].set_title('Ödenen Toplam Ücretlere Göre Dağılım')
        axs[1, 1].set_xticks(x + genislik, Abone_Tipleri)
        axs[1, 1].legend(loc='upper left', ncols=3)


        plt.tight_layout()
        plt.show()


    else:
        print('Program sonlandiriliyor...')
        sys.exit()








