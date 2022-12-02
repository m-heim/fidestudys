#!/bin/bash
if [ ! -f "players_list.zip" -a "players_list.csv" ]
then
    wget http://ratings.fide.com/download/players_list.zip
    unzip players_list.zip
    mv players_list_foa.txt players_list.csv
fi