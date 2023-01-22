#1/bin/bash
echo -n 'admin' > ./user_name.txt
echo -n '1f2d1e2e67df' > ./pass_word.txt
kubectl create secret generic db-user-pass --from-file=./user_name.txt --from-file=./pass_word.txt
kubectl create secret generic db-user-pass-key --from-file=username=./username.txt --from-file=password=./password.txt
kubectl describe secrets/db-user-pass
k exec -it pod -- bash