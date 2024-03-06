#include<stdio.h>

int f0 = 0;
int f1 = 1;

int main(){
    int fn1 = f0;
    int fn2 = f1;
    printf("%d\n%d\n",f0,f1);

    for(int i = 0;i<4;i++){
        int fn3=fn1+fn2;
        printf("%d\n",fn3);
        fn1 = fn2;
        fn2 = fn3;
    }

}
