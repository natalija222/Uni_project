# Tiešo mērījumu kļūdu aprēķina automatizācija
## Programmas aktualitāte.
Universitātē veicot fizikas laboratorijas darbus, katrā darbā ir nepieciešams veikt tiešo mērījumu matemātisko apstrādi jeb kļūdu aprēķinu. Šis kļūidu aprēkins sastāv no vairākām formulām un parasti aizņem daudz laika. Ja izmanto Exceli to iespējams paveikt aptuveni stundas laikā un studentu aizņemtajā ikdienā stunda ir ilgs laiks, tādēļ mēs izstrādājām šo programmu, kas kļūdu aprēķinu laiku samazina no stundas līdz dažām minūtēm.
## Programmas darbības pamatprincipi un tajā izmantotās biblioptēkas un datu struktūras
Programmas darbības pamatā ir excel faila apstrāde izmatojot pandas bibliotēku. Kad excel fails ir nolasīts rezultāti tiek saglabāti HashTabulā un tiek veikta to matemātiskā apstrāde izmantojot Python bibliotēku math. Pēc Matemātiskās apstrādes veikšanas rezultāti tiek saglabāti jaunā excel failā.
### **Pandas bibliotēkas lietojums programmā**
Pandas bibliotēku Python programmēšanas valodā parasti izmanto darbā ar datiem. Šī bibliotēka atļauj viegli analizēt un veikt darbības ar lieliem datu apjomiem. Šajā programmā pandas bibliotēka tiek izmantota,
- lai sākumā nolasītu pievienoto excel failu un tā datus saglabātu kā DataFrame ar nosaukumu df; 
- Tālāk ar šīs bibliotēkas palīdzībub tiek iegūti kollonu nosaukumi un atmestas aprēķiniem nederīgās kollonnu vērtības ar metodes dropna() palīdzību; 
- Pēc datu matemātiskās apstrādes veikšanas tiek izveidots jauns DataFrame ar nosaukumu "results", kur tiek saglabātas jaunās aprēķinātās vērtības priekš katras kollonnas; 
- Ar komandu to_excel() vērtības no "results" tiek ierakstītas jaunā excel failā ar nosaukumu "Results.xlsx".

Darbam tika izvēlēta tieši pandas bibliotēka, jo kā redzams programmā nepieciešams strādāt ar atsevišķām kollonām un analizēt datus, un pandas biibliotēka šim darbam ir viss piemērotākā.
### **HashTabulas lietojums programmā**
HashTabula jeb jaucējtabula ir datu struktūra, kas glabā datus "atslēgu" un "vērtību" pāros, kur atslēga glabā adresi uz vērtību. Izmantojot šo datu struktūru var ātri piekļūt un veikt manipulācijas ar datiem. Mūsu veidotās programmas kontekstā HashTable tiek izmantota, lai
- katru excel faila kolonnu saglabātu savā hashtabulā, jo tālāk programmā nepieciešams veikt darbības ar katru kollonnu atsevišķi;
- Kollonnas vērtības tiek pārbaudītas ar funkcijas dropna() palīdzību un derīgās skaitliskās vērtības tiek saglabātas hashTabulā;
- Katra hashTabula tiek saglabāta vārdnīcā, kur kā "atslēga" šoreiz tiek saglabāts kollonas nosaukums. Tas tiek izmantots vēlāk programmā;
- Vēlāk hastabulā sglabātās vērtības tiek izmantotas aprēķinos;
- Tā kā ir nepieciešams apstrādāt katru kolonnu atsevišķi, programmā nepieciešams for cikls, tādēļ implementējot hashtabulu, tajā tiek implementēta funkcija _iter_, kas atļauj tieši veikt iterācijas for ciklā, sglabājot katrā ciklā iegūtās vērtības.
### **Bibliotēka math**
Bibliotēka math ir Python iebūvētā bibliotēka, kas ļauj veikt dažādas matemātiskās darbības, piemēram, izvilkt kvadrātsakni. Šajā programmā šī bibliotēka tika izmantota, lai veiktu datu matemātisko apstrādi (kļūdu aprēķinu)
## Projekta veidotāji
Kristaps Nartišs -> 241RDB217

Natālija Kamina -> 241RDB191