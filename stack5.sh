for m in {247..250}; do for n in {0..255..20}; do echo $n $m; (python /home/user/shell5.py $n $m; cat) | ./stack5; done ; done
