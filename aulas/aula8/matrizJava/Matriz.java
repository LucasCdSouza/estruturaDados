import java.util.ArrayList;
public class Matriz {
    
    /**
     * Método de classe que inicializa uma matriz de inteiros
     * @param matriz - matriz de inteiros a ser inicializada
     * @param qtdlinhas - quantidade de linhas da matriz
     * @param qtdcolunas - quantidade de colunas da matriz
     */
    public static void inicializarMatriz(int matriz[][], int qtdlinhas, int qtdcolunas) {
        for (int i = 0; i < qtdlinhas; i++) {
            for (int j = 0; j < qtdcolunas; j++) {
                matriz[i][j] = 0;
            }
        }
    }
    
    /**
     * Método de classe que exibe uma matriz de inteiros
     * @param matriz - matriz de inteiros a ser exibida
     * @param qtdlinhas - quantidade de linhas da matriz
     * @param qtdcolunas - quantidade de colunas da matriz
     */
    public static void exibirMatriz(int matriz[][], int qtdlinhas, int qtdcolunas) {
        for (int i = 0; i < qtdlinhas; i++) {
            for (int j = 0; j < qtdcolunas; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
    }

    /**
     * Método de classe que converte uma matriz especial em uma lista de dados
     * @param matriz - matriz de inteiros
     * @param qtdlinhas - quantidade de linhas da matriz
     * @param qtdcolunas - quantidade de colunas da matriz
     * @param lista - lista de dados a ser preenchida com os dados da matriz
     */
    public static void converterMatrizLista(int matriz[][], int qtdlinhas, int qtdcolunas, ArrayList<Dado> lista) {
        for (int i = 0; i < qtdlinhas; i++) {
            for (int j = 0; j < qtdcolunas; j++) {
                if (matriz[i][j] != 0) {
                    lista.add(new Dado(matriz[i][j], i, j));
                }
            }
        }
    }

    public static void exibirLista(ArrayList<Dado> lista) {
        System.out.println("Valor\tLinha\tColuna");
        for (Dado item : lista) {
            System.out.println(item.valor + "\t" + item.linha + "\t" + item.coluna);
        }
        System.out.println("Total de elementos: " + lista.size());
    }
}