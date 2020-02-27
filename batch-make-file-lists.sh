D=$PWD

bsub -q short-serial \
     -o $D/lotus.out \
     -e $D/lotus.err \
     -W 23:59 \
     $D/make-file-lists.sh 

