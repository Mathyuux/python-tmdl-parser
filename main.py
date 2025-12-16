import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from utils.packing import TMDLPacking
from utils.saver import save

root = tk.Tk()
root.withdraw()

def main():
    print("[?] Sélectionner le dossier (raçine du projet avec le .pbib)...")

    try:
        var_dir = Path(filedialog.askdirectory(title="Sélectionner le dossier"))

        ## Get pbip file
        try:
            pbip_file = os.path.splitext(next(f for f in os.listdir(var_dir) if f.endswith('.pbip')))[0]
        except:
            print("[X] Pas de .pbib dans ce dosser. Arrêt du programme.")
        
        ## Generate metadata
        print(f"[-][G] Génération des métadata du projet '{pbip_file}' en cours...")
        tmdl_packed = {}
        tmdl_packed["tables"] = TMDLPacking(var_dir).pack_table()
        print(f"[O][G] Métadata générées !")

        ## Save metadata
        print(f"[-][S] Sauvegarde des métadata du projet '{pbip_file}' en cours...")
        output_json = f"Metadata\\{pbip_file}\\{pbip_file}-metadata.json"
        output_md = f"Metadata\\{pbip_file}\\{pbip_file}-markdown.md"

        # Create dir if doesn't exist
        os.makedirs(os.path.dirname(output_json), exist_ok=True)
        os.makedirs(os.path.dirname(output_md), exist_ok=True)

        # Saving
        save(tmdl_packed, output_json, format="json")
        print(f"[O][S] Métadata sauvegardés ici '{output_json}' !")
    except:
        print("[X] Le programme a été aborté.")

if __name__ == "__main__":
    main()