import java.util.Scanner;

public class Main{
    public static void cadastrarAlunoNovo(Email[]lista, Scanner leitor){
        for(int i =0; i < lista.length; i++){
            lista[i] = new Email();
            System.out.println("Digite o nome do Aluno: " + (i+1) + ": ");
            lista[i].setAluno(leitor.nextLine());
        }
    }
    public static void main(String [] args){
        Scanner leitor = new Scanner(System.in);
        Email [] lista = new Email[3];

         cadastrarAlunoNovo(lista, leitor);

        for(Email aluno : lista){
            System.out.println("Nome do Aluno: " + aluno.getAluno()); 
            System.out.println("Email do Aluno: " + aluno.getEmail()); 
        }
    }
}