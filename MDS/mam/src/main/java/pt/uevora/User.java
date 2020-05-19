package pt.uevora;

import java.time.Period;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;
import java.time.LocalDate;
import java.util.ArrayList;

public class User
{
    String username;
    String password;
    long diasDisponiveis;
    boolean gestor;
    ArrayList<Pedido> pedidos;

    public User(String username, String password)
    {
        this.username = username;
        this.password = password;
        this.gestor = false;
        this.diasDisponiveis = 22;
        pedidos = new ArrayList<>();

    }

    public String getUsername()
    {
        return username;
    }

    public String getPassword()
    {
        return password;
    }

    public void setPassword(String password)
    {
        this.password = password;
    }

    public void setUsername(String username)
    {
        this.username = username;
    }

    public long getDiasDisponiveis()
    {
        return diasDisponiveis;
    }

    public void setDiasDisponiveis(long diasDisponiveis){
        this.diasDisponiveis = diasDisponiveis;

    }

    public void marcarferias(User atual,App app)
    {
        LocalDate dataInit, dataFin;
        LocalDate dataInitAux, dataFinAux;

        Scanner scanner = new Scanner(System.in);

        int year1, year2, month1, month2, dayofMonth1, dayofMonth2;
        int diasFds = 0;
        long diasUteis, pontuacao;

        LocalDate data = LocalDate.now();
        System.out.println("Hoje é dia: " + data);

        System.out.println("Insira o ano inicial das suas férias: ");
        year1 = scanner.nextInt();

        System.out.println("Insira o mês inicial das suas férias: ");
        month1 = scanner.nextInt();

        System.out.println("Insira o dia incial das suas férias");
        dayofMonth1 = scanner.nextInt();

        System.out.println("Insira o ano final das suas férias: ");
        year2 = scanner.nextInt();

        System.out.println("Insira o mês final das suas férias: ");
        month2 = scanner.nextInt();

        System.out.println("Insira o dia final das suas férias");
        dayofMonth2 = scanner.nextInt();

        dataInit = LocalDate.of(year1, month1,dayofMonth1);

        dataFin = LocalDate.of(year2, month2,dayofMonth2);


        long totalDias = ChronoUnit.DAYS.between(dataInit, dataFin)+ 1;

        while(!dataFin.isAfter(dataInit) || dataInit.isBefore(data) || totalDias > getDiasDisponiveis())
        {
            if(totalDias > getDiasDisponiveis())
            {
                System.out.println("Não possui dias disponíveis suficientes para o período indicado");
            }
            else if(!dataFin.isAfter(dataInit))
            {
                System.out.println("Data de ínicio é posterior à data de fim");
            }
            else
            {
                System.out.println("Data Inválida");
            }

            System.out.println("Insira o ano inicial das suas férias: ");
            year1 = scanner.nextInt();

            System.out.println("Insira o mês inicial das suas férias: ");
            month1 = scanner.nextInt();

            System.out.println("Insira o dia incial das suas férias");
            dayofMonth1 = scanner.nextInt();

            System.out.println("Insira o ano final das suas férias: ");
            year2 = scanner.nextInt();

            System.out.println("Insira o mês final das suas férias: ");
            month2 = scanner.nextInt();

            System.out.println("Insira o dia final das suas férias");
            dayofMonth2 = scanner.nextInt();

            dataInit = LocalDate.of(year1, month1,dayofMonth1);

            dataFin = LocalDate.of(year2, month2,dayofMonth2);

            totalDias = ChronoUnit.DAYS.between(dataInit, dataFin);

        }

        //Auxiliares
        dataInitAux = dataInit;
        dataFinAux = dataFin;
        Period diasAux = Period.between(dataInitAux,dataFinAux);

        while(diasAux.getDays()+1 != 0)
        {

            // > 4, ou seja 5 (sábado) e 6(domingo)
            if(dataInitAux.getDayOfWeek().ordinal() > 4)
            {
                diasFds++;
            }
            dataInitAux = dataInitAux.plusDays(1);
            diasAux = Period.between(dataInitAux,dataFinAux);
        }



        diasUteis = totalDias - diasFds;
        pontuacao =  pontos(diasUteis, dataInit, dataFin);


        System.out.println("Dias úteis do período marcado: " + diasUteis);
        System.out.println("Pontuação: " + pontuacao);
        System.out.println("Dias de férias disponíveis: "+ atual.diasDisponiveis);

        Pedido pedido = new Pedido(username, dataInit, dataFin, false);
        atual.pedidos.add(pedido);
        app.pedidosgestor.add(pedido);
        System.out.println("O período de férias encontra-se a aguardar por validação");
        app.opcoes(atual,app);

    }

    public long calculaPontos(int mes, long dias)
    {
        //Janeiro, Fevereiro e Novembro
        if(mes == 1 || mes == 2 || mes == 11)
        {
            return dias;

        }
        //Março, Abril, Maio e Outubro
        else if(mes == 3 || mes == 4 || mes == 5 || mes == 10)
        {
            return dias * 2;

        }
        //Junho e Setembro
        else if(mes == 6 || mes == 9)
        {
            return dias * 3;

        }
        //Julho, Agosto e Dezembro
        else
        {
            return dias * 4;
        }
    }

    public long pontos(long diasUteis, LocalDate dataInit, LocalDate dataFin)
    {
        int diasMesInit, diasMesFin, aux_diasFds1 = 0, aux_diasFds2 = 0;
        int mes1, mes2;
        long pontos = 0;


        mes1 = dataInit.getMonthValue();
        //Atualiza os dias disponíveis do colaborador
        setDiasDisponiveis(getDiasDisponiveis()-diasUteis);

        //Quando as férias são marcadas na transição de meses
        if(dataInit.getMonth() != dataFin.getMonth())
        {
            diasMesInit = (dataInit.lengthOfMonth() - dataInit.getDayOfMonth())+ 1;
            diasMesFin =  dataFin.getDayOfMonth();

            Period diasAux = Period.between(dataInit,dataFin);

            while(diasAux.getDays()+1 != 0)
            {

                // > 4, ou seja 5 (sábado) e 6(domingo)
                if(dataInit.getDayOfWeek().ordinal() > 4)
                {
                    if(dataInit.getMonthValue()!= dataFin.getMonthValue()){
                        aux_diasFds1++;
                    }
                    else{
                        aux_diasFds2++;
                    }
                }
                dataInit = dataInit.plusDays(1);
                diasAux = Period.between(dataInit,dataFin);
            }

            diasMesInit = diasMesInit - aux_diasFds1;
            diasMesFin = diasMesFin - aux_diasFds2;
            mes2 = dataFin.getMonthValue();

            pontos = calculaPontos(mes1, diasMesInit);
            pontos = pontos + calculaPontos(mes2, diasMesFin);

            return pontos;

        }

        pontos = calculaPontos(mes1, diasUteis);
        return pontos;
    }

    public void consultarferias(User atual,App app) {

        if (atual.pedidos.size() == 0){
            System.out.println("Não possui nenhum período de férias marcado");

        }
        else{

            for(int i = 0; i < atual.pedidos.size(); i++){

                System.out.println("|| ANO  ||  MÊS  ||  DIA  ||");
                System.out.println("Inicio: " +atual.pedidos.get(i).dataInit);
                System.out.println("Fim: " +atual.pedidos.get(i).dataFin);

                if(atual.pedidos.get(i).validado){

                    System.out.println("Estado: Aprovado");
                }
                else{
                    System.out.println("Estado: Por aprovar/ rejeitado");
                }
            }

        }

        System.out.println("Dias de férias disponíveis: "+ atual.diasDisponiveis);
        app.opcoes(atual,app);


    }

    public void aprovarferias(User atual,App app){
        int id;
        Scanner scanner = new Scanner(System.in);
        int resposta;

        if(app.pedidosgestor.size() == 0)
        {
            System.out.println("Nenhum período de férias por aprovar");

            app.opcoes(atual,app);
        }

        for (int i = 0; i < app.pedidosgestor.size(); i++)
        {
            System.out.println("ID:"+ i);
            System.out.println(app.pedidosgestor.get(i).username);
            System.out.println(app.pedidosgestor.get(i).dataInit);
            System.out.println(app.pedidosgestor.get(i).dataFin);
            System.out.println("--------");
        }

        System.out.println("ID a aprovar:");
        id = scanner.nextInt();

        if(id<app.pedidosgestor.size() && id>-1) {
            System.out.println("username: " + app.pedidosgestor.get(id).username);
            System.out.println("Aprovar- 1");
            System.out.println("Rejeitar - 2");
            resposta = scanner.nextInt();

            switch (resposta) {
                case 1:
                    app.pedidosgestor.get(id).setValidado(true);

                    for (int i = 0; i < app.utilizadores.size(); i++) {

                        if (app.utilizadores.get(i).username == app.pedidosgestor.get(id).username) {

                            for (int j = 0; j < app.utilizadores.get(i).pedidos.size(); j++) {

                                if (app.utilizadores.get(i).pedidos.get(j).dataInit == app.pedidosgestor.get(id).dataInit && app.utilizadores.get(i).pedidos.get(j).dataFin == app.pedidosgestor.get(id).dataFin) {
                                    app.utilizadores.get(i).pedidos.get(j).setValidado(true);
                                }
                            }
                        }
                    }

                    System.out.println("Período aprovado com sucesso");
                    app.pedidosgestor.remove(id);
                    app.opcoes(atual, app);
                    break;
                case 2:
                    app.pedidosgestor.get(id).setValidado(false);
                    System.out.println("Período de férias rejeitado");
                    app.pedidosgestor.remove(id);
                    app.opcoes(atual, app);
                    break;
                default:
                        break;
            }
        }
        else
            {
                System.out.println("ID não existe");

                aprovarferias(atual,app);
            }
        }
    }
