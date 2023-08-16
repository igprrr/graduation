#include <stdio.h>
#include <mpi.h>

// 2 - Fazer um programa em MPI que calcule a velocidade de um carro (V = D/T), a
// distancia deve ser enviada por um processo e o tempo por outro processo. O
// processo raíz deve efetuar o calculo e mostrar o resultado.

int main(int argc, char** argv) {
    int meu_rank, np, origem, destino, tag = 0;
    int valor, velocidade, distancia, tempo;
    int lista[2]; // Adiciona um array para armazenar os valores recebidos

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    printf("----------Q2----------\n"); // Adiciona uma nova linha

    if (meu_rank != 0) {
        if(meu_rank == 1) {
            destino = 0;
            printf("Informe uma distancia para o processo %d: ", meu_rank);
            scanf("%d", &valor);
            MPI_Send(&valor, 1, MPI_INT, destino, tag, MPI_COMM_WORLD);
        } else {
            destino = 0;
            printf("Informe um tempo para o processo %d: ", meu_rank);
            scanf("%d", &valor);
            MPI_Send(&valor, 1, MPI_INT, destino, tag, MPI_COMM_WORLD);
        }
    } else {
        for (origem = 1; origem < np; origem++) {
            MPI_Recv(&valor, 1, MPI_INT, origem, tag, MPI_COMM_WORLD, &status);
            lista[origem - 1] = valor;
        }
        distancia = lista[0];
        tempo = lista[1];

        velocidade = distancia / tempo; // Adiciona um ponto e vírgula no final

        printf("Velocidade: %d\n", velocidade); // Adiciona um espaço após a palavra "Velocidade"

    }
   
    MPI_Finalize();
    return 0;
}