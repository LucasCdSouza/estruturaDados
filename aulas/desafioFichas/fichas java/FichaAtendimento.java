import java.util.Scanner;
import java.util.Queue;

public class FichaAtendimento {

    public static void menu(Queue<Integer> filaNormal, Queue<Integer> filaPrioritaria) {
        String opcao = "";
        Scanner teclado = new Scanner(System.in);
        int contadorPrioritario = 501;
        int contadorNormal = 1;
        int contadorAtendimentos = 0;

        do {
            System.out.println("M E N U");
            System.out.println("1 - Ficha normal");
            System.out.println("2 - Ficha prioritaria");
            System.out.println("3 - Chamar ficha");
            System.out.println("4 - Mostrar fichas faltantes");
            System.out.println("5 - Sair");
            System.out.print("Opcao: ");
            opcao = teclado.nextLine();

            switch (opcao) {
                case "1":
                    contadorNormal = Metodo.geraFichaNormal(filaNormal, contadorNormal);
                    break;
                case "2":
                    contadorPrioritario = Metodo.geraFichaPrioritaria(filaPrioritaria, contadorPrioritario);
                    break;
                case "3":
                    contadorAtendimentos = Metodo.geraAtendimento(filaNormal, filaPrioritaria, contadorAtendimentos);
                    break;
                case "4":
                    Metodo.mostraFichasFaltantes(filaNormal, filaPrioritaria);
                    break;
                case "5":
                    System.out.println("Obrigado por usar o programa.... ");
                    break;
                default:
                    System.out.println("Opcao invalida!");
                    break;
            }
        } while (!opcao.equals("5"));
    }
}