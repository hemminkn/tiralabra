# Ohjelman yleisrakenne

Musiikkigeneraattori generoi Markovin ketjujen avulla kappaleen käyttäjän antaman syötteen ohjeiden mukaisesti ja tallentaa sen midi-tiedostoksi. Markovin ketjujen toiminta perustuu siis siihen, että seuraava tila valitaan edellisten perusteella. Jos vaihtoehtoja on monia, seuraava tila arvotaan painotetusti. Tässä projektissa edelliset tilat eli nuottisekvenssit olen säästänyt trie-tietorakenteeseen, josta ohjelma ne poimii. Koulutuksessa käytetyt midi-tiedostot (kappaleet) ovat saatu ilmaisista kirjastoista Githubista, jotka ovat sitten tallennettu trie-tietorakenteeseen.  
Ohjelmassa käyttäjältä pyydetään haluttu sävelaste (duuri/molli), haluttu aste (eli monenko edellisen tilan perusteella seuraava valitaan), toivottu kappaleen pituus sekä nimi midi-tiedostolle, johon kappale tallennetaan.  
Aineisto tallennetaan trieen käyttäjän antaman syötteen perusteella. Ohjelma valitsee siis datasta kaikki valitun sävelasteen mukaiset midi-tiedostot, lukee ne ja säästää ne trieen edellisten tilojen ja niitä seuraavan nuotin joukkioina. Eli siis jos tila on kaksi, trieen tallennetaan nuotit kolmen nuotin joukkiona.  
Trieen tallentamisen jälkeen ohjelma generoi kappaletta kunnes toivottu kappaleen pituus on täynnä tai kunnes seuraavia nuotteja ei enää löydy. Tämän jälkeen ohjelma tallentaa generoidun kappaleen midi-tiedostoksi, joka tallentuu käyttäjän laitteelle. Ohjelmassa ei itsessään ole mahdollisuutta soittaa tai kuunnella midi-tiedostoa, mutta netistä voi löytää helposti siihen tarkoitettuja työkaluja.  

# Tila- ja aikavaativuudet

Trien lisäys- ja etsintäoperaatioiden aikavaativuus on O(n), jossa n on edellisten tilojen määrä. Markovin ketjujen aikavaativuus on O(n^(k+1)), jossa k on valittu aste ja n uniikkien nuottien määrä. Itse generoinnin aikavaativuus on O(n) tai O(n) per nuotti, sillä se arvotaan edellistä tilaa seuraavista nuoteista.  

# Puutteet ja jatkokehitysmahdollisuudet

Yksi selvä puute oli mielestäni datan määrä ja sen järjestäminen. Aluksi luulin säästäneeni jo hyvän määrän dataa, mutta testatessani ohjelmaa myöhemmin suuremmalla astemäärällä generoidun kappaleen pituus jäi lyhyeksi, mikä oli tietenkin odotettavissa. Lisäksi suurella asteella, kuten 10:stä eteenpäin, kappale oli vain suoraa kopiota jostain aineiston kappaleesta. Näinhän se siis aina on, mutta kun aste oli 10:stä eteenpäin, generoitu kappale oli aina sama. Lisäsin siis reilusti lisää dataa, ja suurellakin asteella generoidut kappaleet näyttivät satunnaisemmilta, vaikkakin jäivät lyhyiksi. Vertaisarvioidessani työtä, joka oli myös musiikkigeneraattori, sain hieman inspiraatiota miten toteuttaisin projektin datan ja sen tallentamisen jos aloittaisin uudestaan. Kuitenkin valitettavasti tällä kertaa tajutessani tämän puutteen aikaa ei ollut enää tarpeeksi kaiken tekemiseen uudestaan. Toinen puute datassa oli se, että käyttäjä ei pysty valitsemaan sävelkorkeuksia tiettyjen nuottien perusteella. Nyt data on jaoteltu vain molleihin ja duureihin.   
Lisäksi mahdollinen puute on aloitustilat/-nuotit, joista generointi aloitetaan. Ensiksi valitsin aloitusnuotit jokaisen midi-tiedoston alusta siten, että ne tallennetaan start_notes-nimisteen listaan ja arvotaan sieltä. Muokkasin ohjelmaa kuitenkin valitsemaan mahdollisen aloitustilat kaikkien tilojen joukosta, jotta vaihtelua olisi enemmän. Parempi tapa olisi ehkä suorittaa trieen tyhjä haku ja etsiä seuraavia nuotteja kunnes tilojen pituus on riittävä, mutta tämänhetkinenkin ratkaisu on riittävä kappaleen generointiin.  

# Laajojen kielimallien käyttö

Käytin Microsoftin Copilot -kielimallia bugien selvittämiseen, jos en itse ymmärtänyt mikä meni pieleen.  

# Lähteet

## Dataan käytin seuraavia Github repositorioita:  
https://github.com/ldrolez/free-midi-chords  
https://github.com/BenLeon2001/Free-Chord-Progressions  
## Muita lähteitä:  
https://en.wikipedia.org/wiki/Trie  
https://www.geeksforgeeks.org/dsa/trie-insert-and-search/  
https://mido.readthedocs.io/en/stable/files/midi.html  
