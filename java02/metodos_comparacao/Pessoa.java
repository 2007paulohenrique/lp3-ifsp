package java02.metodos_comparacao;

public class Pessoa{
    private String nome;
    private Integer idade;
    
    public Pessoa(String nome, Integer idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // verifica a igualdade entre dois objetos
    @Override
    public boolean equals(Object obj) {
        //caso o objeto que invocou o metodo tenha o mesmo espaco na memoria que o obj
        if (this == obj) 
            return true;
        
        if (obj == null) 
            return false;
        
        if (getClass() != obj.getClass()) 
            return false;
        
        Pessoa outra = (Pessoa) obj;

        if (nome == null) {
            if (outra.nome != null) 
                return false;

        } else if (!nome.equals(outra.nome)) 
            return false;
        
        if (idade == null) {
            if (outra.idade != null) 
                return false;

        } else if (!idade.equals(outra.idade)) 
            return false;

        return true;
    }

    // cria um codigo para um objeto
    @Override
    public int hashCode() {
        int primo = 7;
        int resultado = 1;
        resultado = primo * resultado + ((nome == null) ? 0 : nome.hashCode());
        resultado = primo * resultado + ((idade == null) ? 0 : idade.hashCode());
        return resultado;
    }

    // cria uma string para um objeto para facilitar a visualizacao de seu conteudo
    @Override
    public String toString() {
        return nome + "@idade=" + idade;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Integer getIdade() {
        return idade;
    }

    public void setIdade(Integer idade) {
        this.idade = idade;
    }

    
}