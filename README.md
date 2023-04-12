# Tugas Kecil 3 IF2122 Strategi Algoritma

> Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan Terpendek

## Table of contents
* [General info](#general-info)
* [Deskripsi Tugas](#deskripsi-tugas)
* [Technologies](#technologies)
* [Setup](#setup)
* [How To Run](#how-to-run)
* [Status](#status)
* [Author](#author)

## General info
Proyek ini dibuat untuk memenuhi tugas kecil 3 IF2211 Strategi Algoritma 2020/2021.

## Deskripsi Tugas
    Algoritma UCS (Uniform cost search) dan A* (atau A star) dapat digunakan untuk menentukan 
lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, anda diminta menentukan 
lintasan terpendek berdasarkan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan
di peta dibentuk graf. Simpul menyatakan persilangan jalan (simpang 3, 4 atau 5) atau ujung jalan. 
Asumsikan jalan dapat dilalui dari dua arah. Bobot graf menyatakan jarak (m atau km) antar simpul. 
Jarak antar dua simpul dapat dihitung dari koordinat kedua simpul menggunakan rumus jarak 
Euclidean (berdasarkan koordinat) atau dapat menggunakan ruler di Google Map, atau cara 
lainnya yang disediakan oleh Google Map.

    Langkah pertama di dalam program ini adalah membuat graf yang merepresentasikan peta (di area 
tertentu, misalnya di sekitar Bandung Utara/Dago). Berdasarkan graf yang dibentuk, lalu program 
menerima input simpul asal dan simpul tujuan, lalu menentukan lintasan terpendek antara 
keduanya menggunakan algoritma UCS dan A*. Lintasan terpendek dapat ditampilkan pada 
peta/graf (misalnya jalan-jalan yang menyatakan lintasan terpendek diberi warna merah). Nilai 
heuristik yang dipakai adalah jarak garis lurus dari suatu titik ke tujuan.

## Technologies
* python - version 3.9
* heapq
* folium

## Setup
- install package folium dengan memasukkan perintah di dalam terminal 'pip install folium'

## How To Run
- clone repository ini

- buka terminal di file test didalam repo yang sudah di clone

- masukkan perintah 'python -u ".\Tucil3_13521016_13521026\src\main.py"'

## Status
Project is: _finished_

## Author
|NIM|Nama|
|----------|---------------|
| 13521016 | Laila Bilbina |
| 13521026 | Kartini Copa |
