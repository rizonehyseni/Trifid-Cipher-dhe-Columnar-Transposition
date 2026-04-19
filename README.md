# Projekti: Trifid Cipher & Columnar Transposition Cipher

##  Përshkrimi i projektit

Ky projekt është zhvilluar për lëndën **Siguria e të dhënave**.

Qëllimi është implementimi i dy algoritmeve klasike të enkriptimit:

Në këtë projekt janë implementuar dy algoritme klasike:

- **Trifid Cipher**, i cili kombinon zëvendësimin dhe transpozimin duke përdorur një strukturë tredimensionale (3D cube)
- **Columnar Transposition Cipher**, i cili bazohet në riorganizimin e karaktereve sipas një çelësi të caktuar
  
Të dy algoritmet përdoren për enkriptimin dhe dekriptimin e teksteve duke përdorur metoda të kriptografisë klasike.

Qëllimi kryesor i projektit është të kuptohet:
- Si funksionojnë algoritmet bazë të enkriptimit
- Si transformohet informacioni në mënyrë të sigurt
- Dallimi midis metodave të ndryshme të kriptografisë klasike
- Zbatimi praktik i koncepteve teorike në programim me Python

---
## Struktura e projektit
```
Trifid-Cipher-dhe-Columnar-Transposition/
│
├── ColumnarTransposition.py
├── TrifidCipher.py
└── README.md
```


##  Columnar Transposition Cipher

Columnar Transposition Cipher është një algoritëm që:
- Merr tekstin hyrës (plaintext)
- E organizon në një tabelë (grid)
- Riorganizon kolonat sipas një çelësi (key)
- Lexon kolonat sipas rendit të çelësit për të krijuar ciphertext

###  Çelësi i përdorur:
Trimethoprimumsulfamethoxazolum

##  Trifid Cipher

Trifid Cipher është një algoritëm kriptografik që përdor:
- Një kub 3D (3 × 3 × 3 = 27 karaktere)
- Ndarje të tekstit në grupe (period)
- Riorganizim të koordinatave (layer, row, column)

### Alfabeti i përdorur:
ABCDEFGHIJKLMNOPQRSTUVWXYZ+


##  Si të ekzekutohet projekti

Secili file mund të ekzekutohet veçmas:

```bash
python ColumnarTransposition.py
```
dhe për Trifid Cipher:

```bash
python TrifidCipher.py
```

