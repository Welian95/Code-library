# README

### This is my github-library, to learn thinks like git, python and more. This README is for using git and its in german.

# Installation

## Install git on macOS
### In comandlinie terminal

## 1. install hombrew 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

## 2. install git
brew install git

## Install git on Windows
### In comandlinie terminal

## 1.

## 2.

# Connect to GitHub

## 3. connect repo to GitHub!
git remote add origin https://github.com/Welian95/Code-library.git 
### hier muss ein git reposetory unter github erstellt werden 

### 4. login mit einem dafür erstellten Token als Passwort 
Craete a personal access token to use as password for git https://github.com/settings/tokens/new




# New Repository

### In comandlinie terminal:

## 1. Neues Reposetory in aktuellem Ordner erstellen
git init  				

##2. Namen des Branches ändern
git branch -m <name>

## 3. aktuellen Status des Repos anzeigen
git status

## 4. Hinzufügen einer Datei ins Repo
git add	<dataname>			

## 5. comitten! - Wiederherstellungspunkt zum Speichern erstellen -m „Nachricht über Änderungen“
git commit -m <„massage“>	
#bei einem Commit werden alle geaddeten Daten gespeichert

## 6. Alle Dateien werden geaddet
git add *				

## 7. Alle .rtf Dateien werden geaddet
git add.rtf				

## 8. Anzeigen aller Änderungen inkl. Datum 
git log					

## 9. Uplaod auf GitHub „main or master„
git push -u origin main 		

### git push -f origin main #nur im Notfall, das repo wird 1:1 mit den lokalen Daten überschrieben 