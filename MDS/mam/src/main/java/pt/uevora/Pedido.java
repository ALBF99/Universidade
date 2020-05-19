package pt.uevora;

import java.time.LocalDate;

public class Pedido
{
    String username;
    LocalDate dataInit;
    LocalDate dataFin;
    int diasDisponiveis;
    boolean validado;

    
    public Pedido(String username, LocalDate dataInit, LocalDate dataFin, boolean validado)
    {
        this.dataFin = dataFin;
        this.dataInit = dataInit;
        this.username = username;
        this.diasDisponiveis = 22;
        this.validado = validado;
    }

    public LocalDate getDataFin()
    {
        return dataFin;
    }

    public LocalDate getDataInit()
    {
        return dataInit;
    }

    public void setDataFin(LocalDate dataFin)
    {
        this.dataFin = dataFin;
    }

    public void setDataInit(LocalDate dataInit)
    {
        this.dataInit = dataInit;
    }

    public void setValidado(boolean validado)
    {
        this.validado=validado;

    }

    public int getDiasDisponiveis()
    {
        return diasDisponiveis;
    }

    public void setDiasDisponiveis(int diasDisponiveis){
        this.diasDisponiveis = diasDisponiveis;

    }
}