import math
print("""Bienvenido al programa de colisión de trenes, introduce los datos  a medida que sean solicitados
	para determinar si existira o no una colision y en que momento sucedera, la velocidad maxima de los trenes sera compartida
	y la capacidad de desaceleracion solo puede llegar a ser un 60% de la aceleracion.""")

print("Introduce La velocidad punta de los trenes km/h")
vmax=input()
print("Introduce La aceleracion del primer tren km/h2")
atren1=input()
print("Introduce El tiempo de salida del segundo tren en minutos")
tet=input()
tet=float(tet)/60
print("Introduce La aceleracion del segundo tren")
atren2=input()

if atren1>atren2:
	print("Los trenes nunca se chocaran!  La aceleracion del segundo tren debe ser mayor para poder alcanzarlo!")
else:
	tvmax1=(float(vmax)/float(atren1))-float(tet)   # Tiempos en alcanzar velocidad maxima, vtest y xtest,
	tvmax2=float(vmax)/float(atren2)				#  se refieren a la velocidad y posicion del primer tren en el momento en que 2 parte del reposo
	vtest=(float(tet)*float(atren1))*(-1)
	xtest=(float(atren1)*float(tet)*float(tet)/2)*(-1)
	adif=(float(atren2)-float(atren1))/2
	frenmax2=float(atren2)*-0.6
	w= float(atren2)/(2*(float(atren2+atren1)**2))  # Variables basadas en los calculos, que ayudan a simplificar  y remplazar la ecuacion final
	m= float(atren1)/(2*(float(atren2+atren1)**2))  # para visualizar de manera mas simple. PARA LA PARTE SEGUNDA DEL EJERCICIO
	k= float(atren2)/float(atren2+atren1)
	j= float(atren1)/float(atren2+atren1)
	q= float(-vtest)/float(atren2+atren1)
	l= float(frenmax2)/2
	i= float(atren1)/2
	h=float(atren1)-float(frenmax2)
	insqrt=float(vtest**2)-(4*float(adif)*float(xtest))
	sqr = math.sqrt(insqrt)
	t1=(float(-vtest)+float(sqr))/(float(adif)*2)   #Ambos resultados de la funcion cuadratica, donde sqr es el producto de la raiz, obtenida previamente
	t2=(float(-vtest)-float(sqr))/(float(adif)*2)
	check=float(t1)-float(tet)
	if t2<0 and check<tvmax1:
		t=float(t1)+float(tet)
		t=(float(t)*60)
		th=float(t)//60
		tm=float(t)%60
		tm=(float(tm)*60)
		ts=float(tm)%60
		tm=float(tm)//60
		print("El tiempo estimado de colision sera a las " + str(th)+ " horas, "+ str(tm)+ " minutos, "+ str(ts)+ " segundos. ")
		atf=((float(w)*(float(h)**2))+float(l))-(float(i)+(float(j)*float(h))+(float(w)*(float(h)**2)))
		btf=(float(w*h)+float(w*2*vtest*h))-(float(j*vtest)+float(vtest)+float(m*vtest*2*h)+float(q*h))
		
		ctf=((float(w)*(float(vtest)**2))+(float(k)*float(atren2)*float(vtest)))-(float(xtest)+(float(m)*(float(vtest)**2))+float(q*vtest))
		
		insqrt2=float(btf**2)-(4*float(atf)*float(ctf))
		
		sqr2 = math.sqrt(insqrt2)
		
		tf3=(float(-btf)+float(sqr2))/(float(atf)*2)   #Ambos resultados de la funcion cuadratica, donde sqr es el producto de la raiz, obtenida previamente
		tf2=(float(-btf)-float(sqr2))/(float(atf)*2)
		if tf3> tf2:
			tf1=tf3
		else:
			tf1=tf2
		
		div=float(atren2)+float(atren1)
		
		tac=(float(h*tf1)-float(vtest))/float(div)
		
		tf=float(tet)+float(tac)+float(tf1)
		
		xf=(float(atren1)*(float(tf)**2))/2
		vf=float(atren1)*float(tf)
		print("Si el tren 2, decide frenar en el ultimo momento posible, a maxima potencia de frenos, debera hacerlo a las " +str(tac)+ " horas desde el momento en que partio")
		print("De esta manera se encontraran a "+str(xf)+"km del punto de salida, a una velocidad comun de "+str(vf)+"km/h, a "+str(tf)+"h de la partida del primer tren")
		print("desde ese punto en tiempo y espacio, el primer tren mantendra una velocidad y aceleracion mayor.")
		tf=(float(tf)*60)
		tfh=float(tf)//60
		tfm=float(tf)%60
		tfm=(float(tfm)*60)
		tfs=float(tfm)%60
		tfm=float(tfm)//60
		
		print("El tiempo estimado es de " + str(tfh)+ " horas, "+ str(tfm)+ " minutos, "+ str(tfs)+ " segundos. ")
	else:
		print("Los trenes nunca se chocaran!")

