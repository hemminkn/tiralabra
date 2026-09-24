# 4. Viikkoraportti
Aloitin generaattorin luomisesta tiistaina. Ensiksi minun piti hieman suunnitella, miten sen toteutan. Generaattorille annetaan siis alussa aste, jonka perusteella se valitsee seuraavan nuotin. Ajattelin, että 1. nuotti arvotaan, mutta minulla oli vähän ongelmia sen kanssa, että miten se tehdään.  

Torstaina sain generaattorifunktion siihen pisteeseen, että se luo sadan nuotin kappaleen ja muuntaa sen midi-tiedostoksi. Testasin toimintaa siis pääohjelmalla, jonka laitoin app.py-tiedostoon. Kuuntelin generoidun midi-tiedoston ohjelmalla, jonka löysin netistä ja huomasin, että kappale on aika lyhyt. Mietin jos sitä pidentäisi hieman. Lisäksi 1. tilan arvonnan hoidin siten, että kun opetustiedostoja luetaan, ohjelma nappaa välistä tiedostojen alkutilat asteen perusteella yhteen listaan ja arpoo generoinnin alussa niistä yhden. Mielestäni tämä on ihan hyvä tapa. Ensiksi otin tilat talteen joka kerta, kun trieen lisätään uusi sekvenssi, mutta aloitustilojen nappaaminen kappaleiden keskeltä saattaisi vaikuttaa negatiivisesti lopputulokseen. Aloin lisäksi miettiä yksikkötestejä, jotta pääsisin alkuun ohjelman testauksessa. Minulla ei ole aiempaa kokemusta yksikkötesteistä tms. joten luulisin aikaa menevän nyt hieman suunnitteluun ja tiedonhakuun.  

## Työaika
Tiistai 3h, korjailin hieman määrittelydokumenttia, aloitin README-tiedostoa sekä generaattorin suunnittelun ja luomisen.  
Torstai 4h, generaattorin eli ohjelman 1. versio loppuun, pääohjelmalla testaus ja hieman yksikkötesteihin tutustumista.  
