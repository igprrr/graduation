#include <stdio.h>
#include <string.h>
#include <mpi.h>

void main(int argc, char** argv){
    int meu_rank, np, origem, tag=0;
    int valor, sum, div, sub, mult, v1, v2;

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    printf("----------Q1----------");

    if (np != 3) {
        printf("O programa precisa ser executado com exatamente 3 processos.\n");
        MPI_Finalize();
        return;
    }

    if (meu_rank == 0){
        int valores[2];

        for (origem=1; origem<np; origem++){
            MPI_Recv(&valor, 1, MPI_INT, origem, tag, MPI_COMM_WORLD, &status);
            valores[origem - 1] = valor;
        }
        v1 = valores[0];
        v2 = valores[1];

        sum = v1+v2;
        mult = v1*v2;
        div = v1/v2;
        sub = v1-v2;

        printf("Adição: %d\n", sum);
        printf("Multiplicação: %d\n", mult);
        printf("Subtração: %d\n", sub);
        printf("Divisão: %d\n", div);
    }
    else {
        int destino = 0;

        printf("Informe um valor inteiro para o processo %d: ", meu_rank);
        scanf("%d", &valor);
        MPI_Send(&valor, 1, MPI_INT, destino, tag, MPI_COMM_WORLD);
    }

    MPI_Finalize();
}20:48 09/07/2023