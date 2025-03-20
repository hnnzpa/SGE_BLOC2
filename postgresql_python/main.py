#import create_registre as cr
import read_registre as rr

#cr.create_reg()

results = rr.read_reg()
for i in results:
    print('/n')
    print('Nom: ' + i[0])
    print('Adreça: ' + i[1])
    print('Telèfon: ' + i[2])
    print('Email: '+ i[3])
    print('Neixament: ' + i[4])
