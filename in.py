import os
import sys
import time
from time import sleep

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4.0/90)

os.system("clear")
gilang=(W+"""
      ###################
     #                   #
     #        $          #
     #       $$$         #
############$$$$$#################

    #    ' *'      '* '   #
    #     ''        ''    #
    #         $$$$        #
    #                     $
    #   $             $   #
     #   $$$$$$$$$$$$$   #
      #                #
        ##############
sebuah duka yang telah menjadi luka
dalam memori lama yang kini telah ku buka
disaat ku terluka akupun terlupa
ditertawakan saat ku kehilangan semua

saat tertatih ..
ku pun berlatih ..
disaat merekapun terus berdalih ..
ku berlari ..
dan mencari ..
harapan yang akan datang menepi ..
""")

h=(GR+"""
$ InYourXerXez7
  SEORAMG SC KIDHIE YANG HAUS AKAN DUNIA IT MUNGKIN SAYA YANG TER CAMPAKAN DI DUNIA MAYA DAN TA DI ANGGAP OLEH TEMAN SAYA
UMUR = 14
TTL  = BOGOR~17~OKTO~2005
SKOLA= SMA
                                                                       
   CIE YANG MIKIR BOCIL HUEHEHEHEEHEHEHEHE
()==(=)==(=)==(=)==(=)==(=)==(=)==(=)==(=)==(=)==(=)==(=)==(=)==(=)==()
  { I } = INFO
  { L } = LANJUT NANTI KAMU MASUKAN PW AMA USERYA KALO
         NGGA TAU HUBUNGI DI 62858866++++41
  { X } = EXIT TOOLS

CODING BY = IyXerXez
SPESIAL TO= BOGOR BLACKHAT
THANL TO  = GBLK CREW
      UDAH AH BINGUMG MAU APA LAGI HEHE
""")
slowprints(h)
input('\n \033[1;31mEnTerUnTukLanjut~$ ')
slowprints(gilang)
