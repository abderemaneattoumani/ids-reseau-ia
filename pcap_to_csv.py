import pyshark
import pandas as pd
import os

# lecture d'un fichier .pcap et extraction des features de chaque paquet
def pcap_to_csv(pcap_file, label, output_rows):
    # affichage de l'avancement
    print(f"Traitement de {pcap_file}...")
    
    # extraction des features
    try:
        capture = pyshark.FileCapture(pcap_file)
        
        # traitement de chaque paquet
        for packet in capture:
            try:
                row = {
                    # feature 1 : protocole utilisé (TCP, UDP, ARP...)
                    'protocol' : packet.transport_layer,
                    
                    # feature 2 : IP source
                    'ip_src' : packet.ip.src,
                    
                    # feature 3 : IP destination  
                    'ip_dst' : packet.ip.dst,
                    
                    # feature 4 : Port source
                    'port_src' : int(packet[packet.transport_layer].srcport),
                    
                    # feature 5 : Port destination
                    'port_dst' : int(packet[packet.transport_layer].dstport),
                    
                    # feature 6 : Taille du paquet en octets
                    'packet_length' : int(packet.length),
                    
                    # feature 7 : Timestamp (moment de capture)
                    'timestamp' : float(packet.sniff_timestamp),
                    
                    # feature 8 : TTL (durée de vie du paquet)
                    'ttl' : int(packet.ip.ttl),
                    
                    # étiquette : normal / nmap / dos
                    'label' : label
                }
                output_rows.append(row)
            
            # traitement des exceptions
            except AttributeError:
                # Certains paquets n'ont pas tous les champs (ex: ARP) on les ignore simplement
                continue

        # fermeture du fichier        
        capture.close()
        
        # affichage de l'avancement
        print(f"    {len(output_rows)} paquets traités jusqu'ici")
    
    # traitement des exceptions
    except Exception as e:
        print(f"    Erreur : {e}")



# création du DataFrame et sauvegarde en CSV

all_rows = []

# chemin des fichiers .pcap
fichiers = [
    (r"E:\IDS_Project\Captures\capture_saine.pcap", "normal"),
    (r"E:\IDS_Project\Captures\capture_nmap.pcap",  "nmap"),
    (r"E:\IDS_Project\Captures\capture_dos.pcap",   "dos"),
]

# traitement de chaque fichier
for pcap_path, label in fichiers:
    # extraction des features
    pcap_to_csv(pcap_path, label, all_rows)

# création du DataFrame
df = pd.DataFrame(all_rows)

# sauvegarde en CSV
output_path = r"E:\IDS_Project\Datasets\dataset_ids.csv"
df.to_csv(output_path, index=False)

# affichage de l'avancement
print(f"\nDataset généré avec succès !")
print(f"   Fichier : {output_path}")
print(f"   Lignes  : {len(df)}")
print(f"   Colonnes: {list(df.columns)}")
print(f"\nRépartition des labels :")
print(df['label'].value_counts())