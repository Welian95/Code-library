{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fnil\fcharset0 Menlo-Regular;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red118\green118\blue118;\red255\green255\blue255;
\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c1\c1;\cssrgb\c53749\c53751\c53683;\cssrgb\c100000\c100000\c99985\c0;
\cssrgb\c100000\c100000\c99971\c0;\csgray\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww16820\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs22\fsmilli11250 \cf2 \cb3 \expnd0\expndtw0\kerning0
#README\
\
### This is my github-library, to learn thinks like git, python and more. This README is for using git and its in german.\
\
# Installation\
\
##Install git on macOS
\f1\b0 \
##In comandlinie terminal\
\
## 1. \
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"\
\
##2. \
brew install git\
\cb4 \
# New Repository\
\
## In comandlinie terminal:\
\
## \cb5 1. \cb4 Neues Reposetory in aktuellem Ordner erstellen\
git init  				\
\

\f2\fs22 \cf6 \cb1 \kerning1\expnd0\expndtw0 \CocoaLigature0 ##
\f1\fs22\fsmilli11250 \cf2 \cb4 \expnd0\expndtw0\kerning0
\CocoaLigature1 2. 
\f2\fs22 \cf6 \cb1 \kerning1\expnd0\expndtw0 \CocoaLigature0 Namen des Branches \'e4ndern
\f1\fs22\fsmilli11250 \cf2 \cb4 \expnd0\expndtw0\kerning0
\CocoaLigature1 \

\f2\fs22 \cf6 \cb1 \kerning1\expnd0\expndtw0 \CocoaLigature0 git branch -m <name>\
\

\f1\fs22\fsmilli11250 \cf2 \cb4 \expnd0\expndtw0\kerning0
\CocoaLigature1 ## 3. aktuellen Status des Repos anzeigen\
git status\
\
## 4. Hinzuf\'fcgen einer Datei ins Repo\
git add	
\f2\fs22 \cf6 \cb1 \kerning1\expnd0\expndtw0 \CocoaLigature0 <dataname>
\f1\fs22\fsmilli11250 \cf2 \cb4 \expnd0\expndtw0\kerning0
\CocoaLigature1 			\
\
## 5. comitten! - Wiederherstellungspunkt zum Speichern erstellen -m \'84Nachricht \'fcber \'c4nderungen\'93\
git commit -m <\'84massage\'93>	\
#bei einem Commit werden alle geaddeten Daten gespeichert\
\
\
## 6. Alle Dateien werden geaddet\
git add *				\
\
## 7. Alle .rtf Dateien werden geaddet\
git add.rtf				\
\
## 8. Anzeigen aller \'c4nderungen inkl. Datum \
git log					\
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardeftab720\pardirnatural\partightenfactor0

\f2\fs22 \cf6 \cb1 \kerning1\expnd0\expndtw0 \CocoaLigature0 ## 9. connect repo to GitHub!
\f1\fs22\fsmilli11250 \cf2 \cb4 \expnd0\expndtw0\kerning0
\CocoaLigature1 \

\f2\fs22 \cf6 \cb1 \kerning1\expnd0\expndtw0 \CocoaLigature0 git remote add origin https://github.com/Welian95/Code-library.git 
\f1\fs22\fsmilli11250 \cf2 \cb4 \expnd0\expndtw0\kerning0
\CocoaLigature1 \
\
## 10. Uplaod auf GitHub \'84main or master \'84\
git push -u origin main 		\
\
## 11. Craete a personal access token to use as password for git https://github.com/settings/tokens/new\
## Diesen Token als Passwort eingeben\
\
}