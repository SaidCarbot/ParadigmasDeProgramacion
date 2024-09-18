#include <stdio.h>


int main(){
    int A[]={2, 7, 11, 15};
    int target=9, tam;

    for (int i=0;i<tam-1;i++){
        for(int j=i+1;j<tam;j++){
            if(A[i]+A[j]==target){

                printf("Los indices son: %d y %d\n",i,j);
                return;
            }
        }
    }
    return 0;
    }
