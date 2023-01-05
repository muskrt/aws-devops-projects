#!/bin/bash
echo -e "----script_content-----\n"
cat << EOF
#!/bin/bash
RANDOM=2342342343434
for i in \`seq 10\`
do 
  echo \$RANDOM
done
EOF


echo -e "\n\n-----Results-----\n\n"
RANDOM=2342342343434
for i in `seq 10`
do 
  echo $RANDOM
done

