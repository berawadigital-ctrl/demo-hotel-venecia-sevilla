# Contenido de la demo Hotel Venecia (Sevilla) (es/ca/en/fr). Hechos de hotelveneciasevilla.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación individual','Habitación doble','Habitación familiar'],'ca':['Habitació individual','Habitació doble','Habitació familiar'],'en':['Single room','Double room','Family room'],'fr':['Chambre individuelle','Chambre double','Chambre familiale']}
RD={
'es':['Espacio cálido y acogedor de 10 m² con cama de 135×190.','Amplia, de 15 m², moderna y minimalista; con una o dos camas. También hay doble con cama supletoria.','Para 4 personas: dos dormitorios dobles independientes con un baño común.'],
'ca':['Espai càlid i acollidor de 10 m² amb llit de 135×190.','Àmplia, de 15 m², moderna i minimalista; amb un o dos llits. També hi ha doble amb llit supletori.','Per a 4 persones: dos dormitoris dobles independents amb un bany comú.'],
'en':['A warm, cosy 10 m² space with a 135×190 bed.','Spacious, 15 m², modern and minimalist; with one or two beds. A double with an extra bed is also available.','For 4 guests: two separate double bedrooms sharing one bathroom.'],
'fr':['Un espace chaleureux et accueillant de 10 m² avec un lit de 135×190.','Spacieuse, 15 m², moderne et minimaliste ; avec un ou deux lits. Il existe aussi une double avec lit d\'appoint.','Pour 4 personnes : deux chambres doubles indépendantes avec une salle de bain commune.']}
ART={
'hero':('arches',5101,['#f4e6d4','#e9c08a','#c0703a','#8a3b1e','#4f2412']),
'intro':('columns',5102,['#f3eadf','#f8f1e8','#c58a3e','#1f4e5a','#13323a']),
'r1':('arches',5111,['#f3e7d8','#e5bd8c','#bb6c39','#1f4e5a','#13323a']),
'r2':('columns',5112,['#f2e9de','#f8f1e7','#c88d40','#1f4e5a','#13323a']),
'r3':('skyline',5113,['#1f4e5a','#e3955a','#f7d49c','#1d4a55','#163a43','#0f282e']),
'g1':('arches',5121,['#f4e8d9','#e7c08e','#bf6f3a','#8a3b1e','#4f2412']),
'g2':('columns',5122,['#f1e8dd','#f7f0e6','#c48a3d','#1f4e5a','#13323a']),
'g3':('skyline',5123,['#24535f','#e6985c','#f8d6a0','#214f5a','#183d46','#102a31']),
'g4':('hills',5124,['#ece6cf','#f4e4bf','#f5c985','#b3c39a','#8aa481','#5f7a62']),
'g5':('arches',5125,['#f3e6d6','#e3ba88','#b86a37','#8a3b1e','#4f2412']),
'g6':('columns',5126,['#f0e7dc','#f7efe5','#c18840','#1f4e5a','#13323a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Venecia · Hotel en el centro histórico de Sevilla, en la calle Trajano',see_rooms='Ver habitaciones',hero_k='Sevilla · Centro histórico',hero_t='Disfruta de Sevilla con tu estancia en el Hotel Venecia',hero_s='En la calle Trajano, 31, entre la Alameda de Hércules y la plaza del Duque de la Victoria.',
 intro_t='Un hotel de 21 habitaciones con historia',intro_p1='Está en el solar donde tuvo su taller el pintor Francisco Pacheco, maestro de Velázquez y Alonso Cano, a un paso de la calle Sierpes y a 10 minutos a pie de la Catedral y el Alcázar.',
 intro_p2='Un hotel de tres estrellas con trato personal, habitaciones insonorizadas, recepción 24 horas, cafetería para desayunar y parking privado en el propio edificio.',
 stats=['21 habitaciones','Parking privado','Recepción 24 horas','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Para viajar solo, en pareja o en familia.',
 svcs=['Wifi gratuito','Parking privado','Aire acondicionado y calefacción','Habitaciones insonorizadas','Cuna gratis (menores de 2 años)','Caja fuerte gratuita','Recepción 24 horas','Venta de entradas y visitas turísticas'],
 loc_p='C/ Trajano, 31 · 41002 Sevilla. Aviso del hotel: la calle está cerrada al tráfico por obras del 19 de mayo de 2026 al 4 de febrero de 2027; solo se accede a pie.',
 chips=['¿Qué habitaciones tiene?','¿Hay parking?','¿Hay desayuno?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Venecia · Hotel al centre històric de Sevilla, al carrer Trajano',see_rooms='Veure habitacions',hero_k='Sevilla · Centre històric',hero_t='Gaudeix de Sevilla amb la teva estada a l\'Hotel Venecia',hero_s='Al carrer Trajano, 31, entre l\'Alameda de Hércules i la plaça del Duque de la Victoria.',
 intro_t='Un hotel de 21 habitacions amb història',intro_p1='És al solar on tenia el taller el pintor Francisco Pacheco, mestre de Velázquez i Alonso Cano, a un pas del carrer Sierpes i a 10 minuts a peu de la Catedral i l\'Alcázar.',
 intro_p2='Un hotel de tres estrelles amb tracte personal, habitacions insonoritzades, recepció 24 hores, cafeteria per esmorzar i pàrquing privat al mateix edifici.',
 stats=['21 habitacions','Pàrquing privat','Recepció 24 hores','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Per viatjar sol, en parella o en família.',
 svcs=['Wifi gratuït','Pàrquing privat','Aire condicionat i calefacció','Habitacions insonoritzades','Bressol gratis (menors de 2 anys)','Caixa forta gratuïta','Recepció 24 hores','Venda d\'entrades i visites turístiques'],
 loc_p='C/ Trajano, 31 · 41002 Sevilla. Avís de l\'hotel: el carrer està tancat al trànsit per obres del 19 de maig de 2026 al 4 de febrer de 2027; només s\'hi accedeix a peu.',
 chips=['Quines habitacions té?','Hi ha pàrquing?','Hi ha esmorzar?','Com es reserva?']),
'en':dict(title='Hotel Venecia · Hotel in Seville\'s historic centre, on Calle Trajano',see_rooms='See the rooms',hero_k='Seville · Historic centre',hero_t='Enjoy Seville with your stay at Hotel Venecia',hero_s='At Calle Trajano, 31, between the Alameda de Hércules and Plaza del Duque de la Victoria.',
 intro_t='A 21-room hotel with history',intro_p1='It stands on the site of the workshop of the painter Francisco Pacheco, teacher of Velázquez and Alonso Cano, a step from Calle Sierpes and a 10-minute walk from the Cathedral and the Alcázar.',
 intro_p2='A three-star hotel with a personal touch, soundproofed rooms, 24-hour reception, a café for breakfast and private parking in the building itself.',
 stats=['21 rooms','Private parking','24-hour reception','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='For travelling alone, as a couple or as a family.',
 svcs=['Free wifi','Private parking','Air conditioning and heating','Soundproofed rooms','Free cot (under 2s)','Free safe','24-hour reception','Tickets and sightseeing tours'],
 loc_p='C/ Trajano, 31 · 41002 Seville. Hotel notice: the street is closed to traffic for works from 19 May 2026 to 4 February 2027; access on foot only.',
 chips=['What rooms does it have?','Is there parking?','Is there breakfast?','How do I book?']),
'fr':dict(title='Hotel Venecia · Hôtel dans le centre historique de Séville, calle Trajano',see_rooms='Voir les chambres',hero_k='Séville · Centre historique',hero_t='Profitez de Séville avec votre séjour à l\'Hotel Venecia',hero_s='Calle Trajano, 31, entre l\'Alameda de Hércules et la plaza del Duque de la Victoria.',
 intro_t='Un hôtel de 21 chambres chargé d\'histoire',intro_p1='Il occupe le terrain de l\'atelier du peintre Francisco Pacheco, maître de Velázquez et d\'Alonso Cano, à deux pas de la calle Sierpes et à 10 minutes à pied de la Cathédrale et de l\'Alcázar.',
 intro_p2='Un hôtel trois étoiles à l\'accueil personnalisé, chambres insonorisées, réception 24 heures, cafétéria pour le petit-déjeuner et parking privé dans l\'immeuble.',
 stats=['21 chambres','Parking privé','Réception 24 heures','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Pour voyager seul, en couple ou en famille.',
 svcs=['Wifi gratuit','Parking privé','Climatisation et chauffage','Chambres insonorisées','Lit bébé gratuit (moins de 2 ans)','Coffre-fort gratuit','Réception 24 heures','Billets et visites touristiques'],
 loc_p='C/ Trajano, 31 · 41002 Séville. Avis de l\'hôtel : la rue est fermée à la circulation pour travaux du 19 mai 2026 au 4 février 2027 ; accès à pied uniquement.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','Y a-t-il un petit-déjeuner ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://booking.redforts.com/BHq8/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Hotel Venecia',ac='#1f4e5a',ac2='#c0703a',ac2_a11y='#8a4a1e',book=BOOK,around=[],foot=FOOT,
 address='C/ Trajano, 31 · 41002 Sevilla',phones=['+34 954 381 161'],emails=['info@hotelveneciasevilla.es'],maps='Hotel Venecia, Calle Trajano 31, Sevilla',t=T)
META=dict(repo='demo-hotel-venecia-sevilla',name='Hotel Venecia',legal_name='Hotel Venecia S.L.',registry_ids=['CIF B-91848143','Registro de Turismo de Andalucía H-SE-00564'],
 url='https://www.hotelveneciasevilla.es/',domain='hotelveneciasevilla.es',municipality='Sevilla',province='Sevilla',sector='hotel en el centro histórico de Sevilla',
 read_at='2026-10-29T10:51:00+01:00',created_at='2026-10-29T11:00:00+01:00',built_at='2026-10-29T11:00:00+01:00',audit_date='2026-10-29T10:49:00+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T10:19:09+01:00',url='https://www.google.com/maps/place/Hotel+Venecia+Sevilla/@37.3954209,-5.995145,17z/data=!4m9!3m8!1s0xd126c0f40c0517f:0xb90476d861e43fba!5m2!4m1!1i2!8m2!3d37.3954209!4d-5.995145!16s%2Fg%2F1tdygwws'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas real del hotel (Redforts, booking.redforts.com/BHq8/, titulo «HOTEL VENECIA - Redforts»; es el widget.js que carga el buscador de su portada); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Cómo es la habitación familiar?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿Se puede llegar en coche?','K05'),('¿Dónde está el hotel?','K06'),('¿Qué ver cerca?','K07'),('¿Qué servicios tiene?','K08'),('¿A qué hora es la entrada?','K09'),('¿Cómo reservo?','K10'),('¿Admiten mascotas?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Com és l\'habitació familiar?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('S\'hi pot arribar amb cotxe?','K05'),('On és l\'hotel?','K06'),('Què es pot veure a prop?','K07'),('Quins serveis té?','K08'),('A quina hora és l\'entrada?','K09'),('Com reservo?','K10'),('Admeteu mascotes?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What is the family room like?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('Is the street open to traffic?','K05'),('Where is the hotel?','K06'),('What is there to see nearby?','K07'),('What services does it offer?','K08'),('What time is check-in?','K09'),('How do I book?','K10'),('Are pets allowed?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Comment est la chambre familiale ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('Peut-on arriver en voiture ?','K05'),('Où est l\'hôtel ?','K06'),('Que voir à proximité ?','K07'),('Quels services propose-t-il ?','K08'),('À quelle heure est l\'arrivée ?','K09'),('Comment réserver ?','K10'),('Les animaux sont-ils admis ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
