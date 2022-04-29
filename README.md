# spotify_mysql
# MICRO SPOTIFY

Para rodar o Micro Micro Spotify precisaremos rodar as seguintes instruções depois de baixar este repositório:
````
cd spotify_mysql/camadaPersistencia
python3 main.py
````
ou
````
python3 spotify_mysql/camadaPersistencia/main.py
````

O *script* utilizado para fundamentar o nosso banco de dados está na pasta *db*.

Para inicializar o MYSQL em sua máquina Ubuntu:

INICIALIZAR O MYSQL
````
sudo service mysql start
mysql -h localhost -P 3306 -u root -p

MySQL> use SPOTIFY_FINAL;
MySQL> EXIT
````
