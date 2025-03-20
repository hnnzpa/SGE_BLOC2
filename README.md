# SGE_BLOC2 (Hanna Zipa)

1. Connexió a la database.

El primer que hem fet és crear els fitxers que farem servir més endavant que ens ajudaran a llegir, modificar o eliminar registres de la nostra base de dades. 

Per a que el que sha dit a dalt es pugui complir, primer hem de fer és connectar-nos a la nostra base de dades.

En la seguen captura veurem el codi el qual ens ho permetrà:

![img.png](img.png)

Si hi afegim: conn.close(), al fer la crida de la funcio en indica que el fitxer s'ha tancat 1 cop. 

El resultat del print és que la connexió ha sigut bona.

Ens dona informació sobre que s'ha creat un objecte de conneció en Python i dns que significa Data Source Name, ens dona la informació que es necessita per connectar-se a la bd (la que li hem indicat en el connect.py). 
Com que tota la informació indicada per a la connexió és correcta ens hem pogut connectar a la bd. 
 

2. Visualització de les dades

Per veure els serveis creats i que estan actius hem creat una taula de clientes i li hem afegit dades. 

![img_1.png](img_1.png)

Per accedir hem buscat localhost:80 per poder accedir a pgadmin amb l'usuari i la contrasenya que tenia en el connect.py. 
Un cop dins hem de crear un servei el qual ens permetrà visualitzar la nostra tabla creada en la captura de dalt. 


3. Crear un nou registre.

Per començar, en el nostre arxiu creat al principi (create_registre.py) li afegim el següent codi en el qual li indiquem la informació que volem afegir i el codi per fer-ho.

![img_2.png](img_2.png)

Per poder fer servir la funció creada l'hem de cridar en el main, per això hem d'importar l'arxiu per poder fer servir la funció. 

![img_3.png](img_3.png)

Finalment, en el pgAdmin podem visualitzar els canvis realitzats: 

![img_4.png](img_4.png)

Podem veure com ha augmentat el volum de la nostra tabla (60 - 61 fila) i si baixem cap el final veurem el Roger que hem creat amb la funció create_reg.

4. Llegir registres.

Amb la consulta SELECT * podem seleccionar tots els registres per després mostrar-les. 

![img_6.png](img_6.png)

En el print(variable) li podem indicar un valor el cual correspondrà a l'idex i es seleccionarà només aquell registre que correspon a l'index indicat.

![img_7.png](img_7.png)

També podem seleccionar únicament una dada de la nostra "tabla", indicant la posició d'aquesta dins d'un registre.

![img_8.png](img_8.png)

*INTENTS mini exercicis LISTS*

![img_9.png](img_9.png)

Aquí busquem a Andreu i un cop trobat seleccionem les seves dades i en concret el seu correu. 

![img_10.png](img_10.png)

I finalment busquem les dades del Vivian i l'Albert, i seleccionem d'un la seva direcció i de l'altre la data del seu aniversari.

Tornant a Postgressql. 

Ara que ja sabem com funcionen els selectors podem fer tables amb les dades de cada registre. 

![img_5.png](img_5.png)

5. Actualitzar registres. 

Per actualitzar un registre podem fer servir UPDATE.

Creem una funció que ens ho faciliti i la cridem en el main. (no tenim l'tribut de id_client li posem com clausula de cerca el nom del client)

![img_12.png](img_12.png)

I també podem veure aquest canvi en la nostra tabla de pgAdmin: 

![img_13.png](img_13.png)

Veiem com en els noms d'Vivian tenim el número de teléfon té el que li hem indicat '000000000'.









