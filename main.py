from dataclasses import asdict
import os
import sqlite3
import numpy
import shutil
import time
import csv
from sqlite3 import Error
import re

def copia():
    # Copia o arquivo de histórico do Chrome
    shutil.copy(r"C:/Users/Joao/AppData/Local/Google/Chrome/User Data/Default/History", r"C:/Users/Joao/Scrap anime/History.db")

def conecta():
    conn = None
    try:
        conn = sqlite3.connect(r"C:/Users/Joao/Scrap anime/History.db")
    except Error as e:
        print(e)
    return conn

# limpa a tabela toda pra deixar só a coluna de titulo
def format():
    conn = None
    conn = sqlite3.connect(r"C:/Users/Joao/Scrap anime/History.db")
    conn.executescript("""
    DROP TABLE if exists "clusters";
    DROP TABLE if exists "content_annotations";
    DROP TABLE if exists "context_annotations";
    DROP TABLE if exists "downloads";
    DROP TABLE if exists "downloads_reroute_info";
    DROP TABLE if exists "downloads_slices";
    DROP TABLE if exists "keyword_search_terms";
    DROP TABLE if exists "downloads_url_chains";
    DROP TABLE if exists "meta";
    DROP TABLE if exists "segment_usage";
    DROP TABLE if exists "visit_source";
    DROP TABLE if exists "visits";
    DROP TABLE if exists "typed_url_sync_metadata";
    DROP TABLE if exists "segments";
    DROP TABLE if exists "clusters_and_visits";
    DELETE FROM urls WHERE url like '%rotten%';
    DELETE FROM urls WHERE url like '%google%';
    DELETE FROM urls WHERE url like '%twitter%';
    CREATE TABLE "Anime" (
	"title"	TEXT,
	"episodio"	INTEGER,
    "semNada" TEXT
    );
    INSERT INTO Anime (title)
    SELECT title
    FROM urls;
    DELETE FROM Anime WHERE title not like '%epis%' OR title like '%todos%' OR title like '%YouTube%' OR title like '%Gshow%' OR title like '%Globoplay%';
    UPDATE Anime
    SET episodio = title;
    UPDATE Anime
    SET semNada = title;
    UPDATE Anime
    SET title = SUBSTR(
        title,
        1,
        INSTR(UPPER(title), 'EPIS') + LENGTH('EPIS') - 5
        ) 
    WHERE title LIKE '%EPIS%';
    UPDATE Anime
    SET episodio = SUBSTR(
        episodio,
        INSTR(UPPER(episodio), 'EPIS'),
        length(episodio) - INSTR(UPPER(episodio), 'EPIS')
        ) 
    WHERE episodio LIKE '%EPIS%';
    UPDATE Anime
    SET title = REPLACE(REPLACE(title, '-',''), '–','');
    UPDATE Anime
    SET episodio = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(episodio, 'a',''), 'b',''), 'c',''), 'd',''), 'e',''), 'f',''), 'g',''), 'h',''), 'i',''), 'j',''), 'k',''), 'l',''), 'm',''), 'n',''), 'o',''), 'p',''), 'q',''), 'r',''), 's',''), 't',''), 'u',''), 'v',''), 'w',''), 'x',''), 'y',''), 'z',''), ' ','');
    UPDATE Anime
    SET episodio = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(episodio, 'A',''), 'B',''), 'C',''), 'D',''), 'E',''), 'F',''), 'G',''), 'H',''), 'I',''), 'J',''), 'K',''), 'L',''), 'M',''), 'N',''), 'O',''), 'P',''), 'Q',''), 'R',''), 'S',''), 'T',''), 'U',''), 'V',''), 'W',''), 'X',''), 'Y',''), 'Z',''), ' ','');
    UPDATE Anime
    SET episodio= REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(episodio, 'á',''), 'Á',''), 'é',''), 'É',''), 'í',''), 'Í',''), 'ó',''), 'Ó',''), 'ú',''), 'Ú',''), '-',''), 'ç',''), 'Ç',''), '|',''), '–',''), 'Ê',''), '!',''), '@',''), '#',''), '$',''), '%',''), 'ê',''), '&',''), '*',''), '(',''), ')',''), '?','');
    ALTER TABLE Anime DROP COLUMN semNada;
    """)
    conn.commit()
    #TODO arrumar um jeito de limpar caracter da coluna pq esses nests tão feios

def bdCola():
    os.rename("C:/Users/Joao/Scrap anime/History.db","C:/Users/Joao/Scrap anime/Anime.db")

copia()
conecta()
format()
bdCola()
