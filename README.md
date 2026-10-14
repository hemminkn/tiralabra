# Music Generator using Markov Chains
A program for generating music made for the Helsinki University course Algorithms and Artificial Intelligence.

## Documentation
[Specification document](docs/maarittelydokumentti.md)  
[First weekly report](docs/viikkoraportit/viikkoraportti1.md)  
[Second weekly report](docs/viikkoraportit/viikkoraportti2.md)  
[Third weekly report](docs/viikkoraportit/viikkoraportti3.md)  
[Fourth weekly report](docs/viikkoraportit/viikkoraportti4.md)  
[Fifth weekly report](docs/viikkoraportit/viikkoraportti5.md)   
[Sixth weekly report](docs/viikkoraportit/viikkoraportti6.md) 

## Installation and starting up
1. Clone the repository into your own computer  
2. To run the app:  
Start the virtual environment by writing:  
```
python3 -m venv venv
source venv/bin/activate
install mido
python3 -m src.app
```  
3. When the app has ran, you can find the midi-file in the same directory. :)  
4. Have fun with the app!

## Directions for testing
After you've done the aforementioned steps, you can test the trie data structure by moving into the root directory and running  
```
python3 -m src.tests.trie_test
python3 -m src.tests.markov_test
python3 -m src.tests.generator_test
python3 -m src.tests.end_to_end_test

```
