Määrittelydokumentti
--------------------
Tässä määrittelydokumentissa määrittelen harjoitustyöni kurssilla Aineopintojen harjoitustyö: Algoritmit ja tekoäly. Opiskelen Helsingin yliopistossa tietojenkäsittelytieteen kandiohjelmassa (TKT).

Aihe ja toteutus
----------------
Aion toteuttaa musiikin generaattorin, joka generoi musiikkia sille annetun nuotin perusteella. Hyödynnän generoinnissa Markovin ketjua, joka määrittää uuden tilan edellisten tilojen perusteella, eli tässä tapauksessa se valitsee seuraavan nuotin sille annetun asteen perusteella. Esimerkiksi jos aste on 2, seuraavat nuotit valitaan kahden viimeisen perusteella
Käytän koulutusaineistona Pythonin mido-kirjastoa, joka lukee midi-tiedostoja ja jonka avulla midi-tiedoston sisällön voi syöttää ohjelmalle. Ensisijaisena tietorakenteena käytän Trie-puuta, johon tallennan sekä nuotit että niiden frekvenssit. Trien avulla tietoihin on helppo päästä käsiksi ilman suurta viivettä.
Markovin ketjujen pahin mahdollinen tilavaatimus on O(N^(k+1)), jossa k on edellisten nuottien määrä, jotka vaikuttavat seuraavaan ja N on uniikkien nuottien määrä.
Mitä aikavaatimukseen tulee, koulutusvaiheen ei tulisi kestää pitkään, noin O(L*k), jossa L on opetusdatan pituus eli tässä tilanteessa nuottien määrä. Musiikin generoinnin eli uuden nuotin valinta tulisi olemaan O(N) tai O(1) per nuotti.

Ohjelmointikielet
-----------------
Toteutan harjoitustyön ensisijaisesti Pythonilla, käyttöliittymässä mahdollisesti HTML ja css.
Vertaisarvioinnissa pystyn arvioimaan töitä, jotka ovat kirjoitettu Pythonilla.

Muita huomioita
---------------
Dokumennoinnin, kuten viikkoraportit, kirjoitan suomeksi, mutta koodi ja commit-viestit kirjoitan selvyyden vuoksi englanniksi. Käyttöliittymässä käytän myös mahdollisesti englantia.

Lähteet
-------
Aion käyttää apuna ainakin seuraavia lähteitä:
	https://www.datacamp.com/tutorial/markov-chains-python-tutorial
	https://hackernoon.com/generating-music-using-markov-chains-40c3f3f46405
