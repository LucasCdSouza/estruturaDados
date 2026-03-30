public class Email{
   private String aluno;
   private String email;

   public void aluno(String nome){
    this.aluno = nome;
    this.email = gerarEmail(nome);
   }


    private String gerarEmail(String email){
        String [] partes = aluno.toLowerCase().split(" ");
        if(partes.length > 1){
        return partes[0] + "." + partes[partes.length - 1] + "@ufn.edu.br";
        }
        return partes[0] + "@ufn.edu.br";
    }

    public String getAluno(){return aluno;}
    public String getEmail(){return email;}

    public void setAluno(String aluno){
        this.aluno = aluno;
        this.email = gerarEmail(aluno);
    }
    public void setEmail(String email){this.email = email;}

    @Override
    public String toString(){
        return "Aluno: " + aluno + "email: " + email;
    }
}