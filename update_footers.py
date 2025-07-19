#!/usr/bin/env python3
"""
Script pour mettre à jour tous les footers des fichiers HTML
"""

import os
import re

# Le nouveau footer HTML à insérer
NEW_FOOTER = '''    <footer>
        <div class="footer-content">
            <div class="footer-main">
                <h3 class="footer-title">
                    🎓 Holberton School - Guide Étudiant
                </h3>
                <p class="footer-description">
                    Votre plateforme complète pour naviguer dans votre parcours à <span class="footer-holberton">Holberton School</span>.<br>
                    Ressources, outils, et communauté pour réussir votre formation en développement.
                </p>
                <div class="footer-links">
                    <a href="#" class="footer-link">📋 Conditions Générales</a>
                    <a href="#" class="footer-link">🔒 Politique de Confidentialité</a>
                    <a href="#" class="footer-link">📞 Contact & Support</a>
                    <a href="#" class="footer-link">ℹ️ À propos</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="footer-copyright">
                    &copy; <span class="footer-year">2025</span> - Site pédagogique <span class="footer-holberton">Holberton School</span>. Tous droits réservés.
                </p>
                <p>Créé avec ❤️ par et pour la communauté étudiante</p>
            </div>
        </div>
    </footer>'''

def update_footer_in_file(filepath):
    """Met à jour le footer dans un fichier HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern pour matcher le footer existant
        footer_pattern = r'<footer>.*?</footer>'
        
        # Vérifier si il y a un footer existant
        if re.search(footer_pattern, content, re.DOTALL):
            # Remplacer le footer existant
            new_content = re.sub(footer_pattern, NEW_FOOTER, content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Footer mis à jour dans {filepath}")
            return True
        else:
            print(f"⚠️  Aucun footer trouvé dans {filepath}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur avec {filepath}: {e}")
        return False

def main():
    """Met à jour tous les footers des fichiers HTML"""
    html_dir = "html"
    updated_count = 0
    
    # Parcourir tous les fichiers HTML
    for filename in os.listdir(html_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(html_dir, filename)
            if update_footer_in_file(filepath):
                updated_count += 1
    
    print(f"\n🎉 {updated_count} fichiers mis à jour avec succès!")

if __name__ == "__main__":
    main()
