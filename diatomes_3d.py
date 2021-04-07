# diatomes3d.py
# Tasos Bithas
# December 2020
def diatomes():
	onoma=str(input("Onoma:"));
	xthes=float(input("Xiliometriki Thesi:"));
	orizon=float(input("Orizontas:"));
	apostasi=[];
	ypsometro=[];
	while True:
		temp=str(input("Enter Point or enter to cancel:"))
		if len(temp)==0: break;
		temp=temp.split(" ")
		apostasi.append(float(temp[0]))
		ypsometro.append(float(temp[1]))
	erythra=float(input("Ypsometro erythras:"))
	epikar=float(input("Epiklish aristera:"))
	epikde=float(input("Epiklish deksia:"))
	roadlen=float(input("Road length:"))
	
	fout=open("output.scr",'w')
	fout.write('PLINE ');
	for i in range(len(apostasi)):
		fout.write("{:.3f}".format(apostasi[i])+","+"{:.3f}".format(ypsometro[i]-orizon)+"\n")
	fout.write("\n")
	for i in range(len(apostasi)):
		fout.write("-TEXT J ML "+"{:.3f}".format(apostasi[i])+",-2.727 0.24 90 "+'{0:.2f}'.format(ypsometro[i])+"\n")
	for i in range(len(apostasi)):
		fout.write("-TEXT J ML "+"{:.3f}".format(apostasi[i])+",-4.10 0.24 90 "+'{0:.3f}'.format(apostasi[i])+"\n")
	for i in range(len(apostasi)):
		fout.write("line "+"{:.3f}".format(apostasi[i])+",0 "+"{:.3f}".format(apostasi[i])+","+"{:.3f}".format(ypsometro[i]-orizon)+"  ")
	ypsomar=erythra+epikar*roadlen/100
	ypsomde=erythra+epikde*roadlen/100
	fout.write("PLINE ")
	fout.write(str(-roadlen)+","+"{:.3f}".format(ypsomar-orizon)+"\n")
	fout.write("0,"+"{:.3f}".format(erythra-orizon)+"\n")
	fout.write(str(roadlen)+","+"{:.3f}".format(ypsomde-orizon)+"\n")
	fout.write("\n")
	
	fout.write("-TEXT J ML "+str(-roadlen)+",-1.34 0.24 90 "+'{0:.2f}'.format(ypsomar)+"\n")
	fout.write("-TEXT J ML 0,-1.34 0.24 90 "+'{0:.2f}'.format(erythra)+"\n")
	fout.write("-TEXT J ML "+str(roadlen)+",-1.34 0.24 90 "+'{0:.2f}'.format(ypsomde)+"\n")
	
	print("Ypsometro aristera:"+str(ypsomar))
	print("Ypsometro deksia:"+str(ypsomde))
	print("Ypsometra:"+str(ypsometro))
	aristera=str(input("Aristera orygma(o) h epixwma(e)?")).lower()
	if aristera=="o": 
		orygma(ypsomar,orizon,roadlen,0,fout)
	else:
		epixwma(ypsomar,orizon,roadlen,0,fout)
	deksia=str(input("Deksia orygma(o) h epixwma(e)?")).lower()
	if deksia=="o":
		orygma(ypsomde,orizon,roadlen,1,fout)
	else:
		epixwma(ypsomde,orizon,roadlen,1,fout)
	
	
def orygma(ypsom,orizontas,roadlen,direction,fout):	
	kl1=float(input("Klish kladou 1:"))
	kl2=float(input("Klish kladou 2:"))
	b=[0.5,1.3,0.1,0.05,0.35,0.05,0.1,0.9]
	bcum=[0.5,1.8,1.9,1.95,2.3,2.35,2.45,3.35]
	orygma=[]
	orygma.append(ypsom+kl1*b[0]/100)
	orygma.append(orygma[0]+kl1*b[1]/100)
	orygma.append(orygma[1])
	orygma.append(orygma[2]+b[3]*-5)
	orygma.append(orygma[3])
	orygma.append(orygma[4]+b[5]*5)
	orygma.append(orygma[5])
	orygma.append(orygma[6]+kl2*b[7]/100)
	fout.write("PLINE ")
	if direction==0: 
		bcum=[-i for i in bcum]
		roadlen=-roadlen
	fout.write(str(roadlen)+","+str(ypsom-orizontas)+"\n")
	for i in range(len(bcum)):
		fout.write("{:.3f}".format(roadlen+bcum[i])+","+"{:.3f}".format(orygma[i]-orizontas)+"\n")
	fout.write("\n")

def epixwma(ypsom,orizontas,roadlen,direction,fout):	
	kl=float(input("Klish kladou 1:"))
	b=[0.5,1.3]
	bcum=[0.5,1.8]
	orygma=[]
	orygma.append(ypsom+kl*b[0]/100)
	orygma.append(orygma[0]+kl*b[1]/100)
	fout.write("PLINE ")
	if direction==0: 
		bcum=[-i for i in bcum]
		roadlen=-roadlen
	fout.write(str(roadlen)+","+str(ypsom-orizontas)+"\n")
	for i in range(len(bcum)):
		fout.write("{:.3f}".format(roadlen+bcum[i])+","+"{:.3f}".format(orygma[i]-orizontas)+"\n")
	fout.write("\n")

diatomes()
		
		
		
