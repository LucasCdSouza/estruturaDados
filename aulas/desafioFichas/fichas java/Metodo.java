import java.util.Queue;

public class Metodo {
        /**
     * método de classe que gera ficha normal
     * @param filaNormal - fila contendo as fichas normais
     * @param contadorNormal - controla o número de fichas normais
     * @return
     */
    public static int geraFichaNormal(Queue<Integer> filaNormal, int contadorNormal) {
        System.out.print("Imprimindo ficha normal.... ");
        System.out.println(contadorNormal);
        filaNormal.offer(contadorNormal);
        contadorNormal++;
        return contadorNormal;
    }

    /**
     * método de classe que gera ficha prioritária
     * @param filaPrioritaria - fila contendo as fichas prioritárias
     * @param contadorPrioritario - controla o número de fichas prioritárias    
     * @return
     */

    public static int geraFichaPrioritaria(Queue<Integer> filaPrioritaria, int contadorPrioritario) {
        System.out.print("Imprimindo ficha prioritaria.... ");
        System.out.println(contadorPrioritario);
        filaPrioritaria.offer(contadorPrioritario);
        contadorPrioritario++;
        return contadorPrioritario;
    }
    /**
     * método de classe que gera atendimento, chamando as fichas de acordo com a regra: a cada 3 atendimentos normais, chamar um prioritário. Se não houver ficha normal, chamar prioritário. Se não houver ficha prioritária, chamar normal.
     * @param filaNormal - fila contendo as fichas normais
     * @param filaPrioritaria -  fila contendo as fichas prioritárias
     * @param contadorAtendimentos
     * @return
     */

    public static int geraAtendimento(Queue<Integer> filaNormal, Queue<Integer> filaPrioritaria, int contadorAtendimentos) {
        if (filaNormal.isEmpty() && filaPrioritaria.isEmpty()) {
            System.out.println("Nao ha fichas para chamar");
            return contadorAtendimentos;
        }
        System.out.print("Chamando ficha.... ");
        int ficha;
        if (contadorAtendimentos % 3 == 0 || filaNormal.isEmpty()) {
            //chamar prioritario
            if (!filaPrioritaria.isEmpty()) {
                ficha = filaPrioritaria.poll();
                System.out.println(" PRIORITARIA... "+ ficha);
                contadorAtendimentos++;
                return contadorAtendimentos;
            }
        }
        if (!filaNormal.isEmpty()) {
            ficha = filaNormal.poll();
            System.out.println(" NORMAL... "+ ficha);
            contadorAtendimentos++;
        }
        return contadorAtendimentos;
    }
    /**
     * método de classe que mostra as fichas faltantes, ou seja, as fichas que ainda estão nas filas
     * @param filaNormal  
     * @param filaPrioritaria
     */
    public static void mostraFichasFaltantes (Queue<Integer> filaNormal, Queue<Integer> filaPrioritaria) {
        if (filaNormal.isEmpty() && filaPrioritaria.isEmpty()) {
            System.out.println("Nao ha fichas para chamar");
            return;
        }
        if (!filaNormal.isEmpty()) {
            System.out.println("Total de fichas faltantes NORMAL... " + filaNormal.size() + " - " + filaNormal);
        }
        if (!filaPrioritaria.isEmpty()) {
            System.out.println("Total de fichas faltantes PRIORITARIA... " + filaPrioritaria.size() + " - " + filaPrioritaria);
        }
    }
    /** método de classe que mostra o menu de opções para o usuário
     * @param filaNormal  
     * @param filaPrioritaria
     */
}
