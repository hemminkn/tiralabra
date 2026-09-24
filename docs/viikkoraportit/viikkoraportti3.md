# 3. viikko
Viikkoa aloittelin opetusdatan löytämisellä. Ensimmäinen ideani oli siis ladata midi-tiedostoja, joissa on jokin tietty laulu. Ohjaajan kanssa puhuttuani kuitenkin tajusin, että käyttämältäni sivustolta suurin osa lauluista oli sävellajissa C, mikä aiheuttaisi vinoumaa datassa. Löysin lopulta GitHubista kirjaston, johon oli lisätty sävellajittain sointukulkuja midi-tiedostoihin, joita sai vapaasti käyttää. Repositorio on BenLeon2001:n Free-Chord-Progressions julkinen repositorio, josta latasin GitHub Free Progressions.zip-tiedoston. Latasin tiedostot koneelleni ja lisäsin ne omaan repositoriooni. Yksinkertaisuuden vuoksi latasin vain molli- ja duurinuottitiedostot ja lisäsin ne omiin kansioihinsa.  

Lisäksi edellisellä viikolla tekemäni yksinkertainen versio Markovin ketjuista luki kerrallaan vain yhden tiedoston, mutta koska tiedostoja oli nyt monia, sitä tuli muokata. Nyt funktio lukee koko opetusdatan riippuen siitä, valitaanko opetusdataksi molli- vai duurinuotit.  

Menin hieman sekaisin tietorakenteissa, olin tehnyt yksinkertaisen Markov-mallin tajuamatta, että Trie-rakenne ja sanakirja, jonka tein Markov-mallilla ovat samaan tarkoitukseen. Tällä viikolla tein siis erikseen Trie-luokat ja edellinen tiedosto, johon olin aloittanut tekemään Markov-mallia, muuntui opetustiedostoksi. Sain Trie:n perusfunktiot loppuun. Trie:tä tulisi testata, mutta en ole vielä aivan varma miten. Ohjaajalta vinkkiä?  

Mietin myös hieman, että teenkö käyttöliittymän itse vai en, sillä käyttöliittymä ei liity kurssin aiheisiin eikä sitä arvostella.  

Ensi viikolla haluaisin alkaa kehittämään testejä ohjelmalle. Trie:n jälkeen on myös mielestäni sopiva aika alkaa kirjoittamaan funktioita generointiin. En tiedä pääsenkö sen pidemmälle, mutta jos aikaa jää, niin alan etsimään tietoa siitä, miten kirjoitan generoidut kappaleet MIDI-tiedostoiksi. Epäilen kyllä että aikaa jäisi, koska generoinnin kanssa tulee ottaa huomioon reunatapaukset ja käsitellä ne, esimerkiksi jos generointi ei onnistukaan ja siihen tulee menemään paljon aikaa.  


## Työmäärä:  
Tiistai 3h, etsin opetusdataa ja muokkasin Markovin ketjun funktiota siten, että se voi lukea monen eri tiedoston  
Keskiviikko 4h, suunnittelin Trie-rakennetta ja jäsentelin tiedostoja sekä aloitin hieman Trie-rakenteen funktioita. Edellisestä markov_model.py:stä tuli train.py. Lisäksi valmistelin käyttöliittymän pohjaa.  
Lauantai 1,5h, koodasin loppuun trie:n find_next-funktion, joka palauttaa seuraavat nuotit ja niiden painot kahden listan tuplena.
