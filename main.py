import pandas as pd
import math
from pandas.api.types import is_number 
# HashTable & Node class definitions
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(str(key)) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
            self.size += 1
    def values(self):
        for node in self.table:
            current = node
            while current:
                yield current.value
                current = current.next
    def __iter__(self):  
        return self.values()

# Load Excel file
excel_file = "piemers.xlsx"
df = pd.read_excel(excel_file)

# Dictionary to hold HashTables per column
hash_tables = {}
results = []

# Process each column
for col in df.columns:
    if df[col].dropna().empty or len(df[col].dropna()) == 2:
        continue
    first_value = df[col].dropna().iloc[0]
    col_name = str(first_value)
    

    table = HashTable()
    for index, value in df[col].items():
        if pd.notna(value) and is_number(value):  # Skip NaN
            table.insert(index, value)
    if table.size == 0:
        continue
    hash_tables[col_name] = table
    globals()[col_name] = table  # Create variable with column name
    print(f"\n=== Rezultāti kolonnai: {col_name} ===")
    count = table.size
    values_list = list(table.values())

    #videjais
    videjais = sum(values_list)/count
    print(f"videjais: {round(videjais,5)}")


    #kvadrātiskais vidējais
    kvadratiskais_videjais = 0
    starpibas_sum =0
    for x in table:
        starpiba = (x-videjais)**2
        starpibas_sum +=starpiba
    dalijums = starpibas_sum/(count*(count-1))
    kvadratiskais_videjais= math.sqrt(dalijums)
    print(f"kvadratiskais videjais: {round(kvadratiskais_videjais,5)}")

    # merijumu absolutā kļūda
    stjudenta_koeficients = float(input("Studenta koeficients: "))
    absoluta_kluda= kvadratiskais_videjais*stjudenta_koeficients
    print(f"merijumu absoluta kluda: {round(absoluta_kluda,5)}")

    #mērinstrumenta kļūda
    patstavigais_koeficients = float(1.96)
    merinstrumenta_kluda =float(input("merinstrumenta kluda: "))
    sistematiska_kluda = (merinstrumenta_kluda/3.0)*patstavigais_koeficients
    print(f"sistematiska kluda: {round(sistematiska_kluda,5)}")

    #galīgā absolūtā kļūda
    galiga_absoluta_kluda=0.0
    if absoluta_kluda/sistematiska_kluda<3:
        absoluta_kluda= absoluta_kluda**2
        sistematiska_kluda = sistematiska_kluda**2
        galiga_absoluta_kluda=math.sqrt(absoluta_kluda+sistematiska_kluda)
        print(f"galiga absoluta kluda: {round(galiga_absoluta_kluda,5)}")
    else:
        if absoluta_kluda>sistematiska_kluda:
            galiga_absoluta_kluda=absoluta_kluda
            print(f"galiga absoluta kluda: {round(galiga_absoluta_kluda,5)}")

        else:
            galiga_absoluta_kluda= sistematiska_kluda 
        print(f"galiga absoluta kluda: {round(galiga_absoluta_kluda,5)}")

        #relatīvā kļūda
        relativa_kluda = (galiga_absoluta_kluda/videjais)*100
        print(f"relativa kluda: {round(relativa_kluda,5)} %")
        results.append({
        "Kolonna": col_name,
        "Vidējais": round(videjais, 5),
        "Kvadrātiskais vidējais": round(kvadratiskais_videjais, 5),
        "Absolūtā kļūda": round(absoluta_kluda, 5),
        "Sistēmiskā kļūda": round(sistematiska_kluda, 5),
        "Galīgā absolūtā kļūda": round(galiga_absoluta_kluda, 5),
        "Relatīvā kļūda (%)": round(relativa_kluda, 5)
    })
results_df = pd.DataFrame(results)
results_df.to_excel("Results.xlsx", index=False)
df = pd.read_excel("Results.xlsx")
df.head()

print("\n✅ Visi rezultāti aprēķināti katrai kolonnai.")

