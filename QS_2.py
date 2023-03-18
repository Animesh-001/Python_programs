currency_he_has=float(input())
ctype=str(input())
e="Euro"
bp="British pound"
ad="australian dollar"
cd="canadian dollr"
if ctype==e:
    E_in_rupee=0.011*currency_he_has
    print(E_in_rupee)
elif ctype==bp:
    BP_in_rupee=0.010*currency_he_has
    print(BP_in_rupee)
elif ctype==ad:
    AD_in_rupee=0.018*currency_he_has
    print(AD_in_rupee)
elif ctype==cd:
    CD_in_rupee=0.017*currency_he_has
    print(CD_in_rupee)
else:
    print(-1)