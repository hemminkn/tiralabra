Tällä viikolla aloin käsittelemään midi-tiedostoja tarkemmin ja latasin netistä midi-tiedoston, johon haluan generoinnin perustuvan. Lisäksi aloittelin Markovin mallin/ketjujen kanssa. Koska käyttäjän tulee voida valita generoinnin aste, ohjelmoin yksinkertaisen mallin joka luo defaultdict avulla sanakirjan kaltaisen olion, ja avainten arvoina on sanakirjan alatyyppi Counter, joka laskee edellisiä nuotteja seuraavien nuottien lukumäärän. Tästä seuraavaksi voisi ehkä jo aloittaa ohjelmoimaan yksinkertaista funktiota uuden musiikin generointiin.
Lisäksi pian pitäisi aloittaa tietorakenteen kanssa. Ohjeissa suositellaan trie-tietorakennetta, mutta odottelen vielä tapaamista ohjaajan kanssa.

Työaika:
Maanantaina 2h, etsin sopivan miditiedoston, latasin sen githubiin ja kirjoitin funktion, joka lukee tiedoston.
Perjantaina 1h, ohjelmoin funktion joka valitsee note_on-tyyppiset viestit midi-tiedostosta ja lisää ne listaan
Lauantaina 3h, tein pieniä korjailuja, etsin lisää tietoa ja aloitin yksinkertaisen Markovin mallin luomisen.
