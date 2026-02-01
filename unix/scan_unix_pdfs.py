#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour scanner les PDFs du dossier unix et extraire le contenu
"""

import os
import sys
from pathlib import Path

try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False
    print("PyPDF2 non installé. Tentative avec pdfplumber...")
    try:
        import pdfplumber
        HAS_PDFPLUMBER = True
    except ImportError:
        HAS_PDFPLUMBER = False
        print("Aucune bibliothèque PDF trouvée. Installation de PyPDF2...")
        print("Veuillez exécuter: pip install PyPDF2 pdfplumber")

def extract_text_pypdf2(pdf_path):
    """Extrait le texte d'un PDF avec PyPDF2"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Erreur lors de l'extraction de {pdf_path}: {e}")
    return text

def extract_text_pdfplumber(pdf_path):
    """Extrait le texte d'un PDF avec pdfplumber"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Erreur lors de l'extraction de {pdf_path}: {e}")
    return text

def scan_pdfs(directory="."):
    """Scanne tous les PDFs dans le répertoire"""
    pdf_files = {}
    directory_path = Path(directory)
    
    # Trouver tous les PDFs
    for pdf_file in directory_path.glob("*.pdf"):
        print(f"Scanning: {pdf_file.name}")
        
        # Extraire le texte
        if HAS_PYPDF2:
            content = extract_text_pypdf2(pdf_file)
        elif HAS_PDFPLUMBER:
            content = extract_text_pdfplumber(pdf_file)
        else:
            print("Aucune bibliothèque PDF disponible!")
            return {}
        
        pdf_files[pdf_file.name] = {
            'path': str(pdf_file),
            'content': content,
            'size': len(content)
        }
        print(f"  -> {len(content)} caractères extraits")
    
    return pdf_files

def save_extracted_content(pdf_files, output_file="extracted_content.txt"):
    """Sauvegarde le contenu extrait dans un fichier texte"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for filename, info in pdf_files.items():
            f.write(f"\n{'='*80}\n")
            f.write(f"FICHIER: {filename}\n")
            f.write(f"{'='*80}\n\n")
            f.write(info['content'])
            f.write("\n\n")
    print(f"\nContenu extrait sauvegardé dans: {output_file}")

if __name__ == "__main__":
    # Scanner les PDFs
    print("Scan des PDFs Unix en cours...\n")
    pdf_files = scan_pdfs()
    
    if not pdf_files:
        print("Aucun PDF trouvé!")
        sys.exit(1)
    
    print(f"\n{len(pdf_files)} PDF(s) scanné(s)\n")
    
    # Sauvegarder le contenu extrait
    save_extracted_content(pdf_files)



