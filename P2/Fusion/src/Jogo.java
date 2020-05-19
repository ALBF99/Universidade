import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import java.util.Random;

public class Jogo extends JFrame {
    private JFrame tela;
    private JButton tab[][];
    private int dim, cor, cor_definida;
    private int tabuleiro[][];
    private Random aleatorio;
    int score = 0;


    public Jogo(int dim, int cor) {


        tela = new JFrame("");
        tela.setBounds(0, 0, dim * 60, dim * 60);
        tela.setLocationRelativeTo(null);
        tela.setLayout(null);
        tela.setResizable(false);
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        tab = new JButton[dim][dim];
        tabuleiro = new int[dim][dim];
        aleatorio = new Random();

        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                tab[i][j] = new JButton("");
                tab[i][j].setBounds(0 + i * 60, 0 + j * 60, 60, 60);
                tab[i][j].addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent actionEvent) {
                        for (int m = 0; m < tab.length; m++) {
                            for (int n = 0; n < tab.length; n++) {
                                if (tab[m][n] == actionEvent.getSource()) {
                                    Eliminar(m, n);
                                    String a = Integer.toString(score);
                                    tela.setTitle("Score:"+a);
                                }
                            }
                        }
                        /*for(int r = 0; r<tab.length; r++){
                            for(int s=0; s<tab.length; s++){
                                if(s>0 && tabuleiro[r][s]==0){
                                    tabuleiro[r][s] = tabuleiro[r][s-1];
                                    tabuleiro[r][s-1] = 0;
                                }
                                if (tabuleiro[r][s] == 0){
                                    tab[r][s].setBackground(Color.white);
                                }
                                if(tabuleiro[r][s] == 1){
                                    tab[r][s].setBackground(Color.blue);
                                }
                                if(tabuleiro[r][s] == 2){
                                    tab[r][s].setBackground(Color.red);
                                }
                                if (tabuleiro[r][s] == 3) {
                                    tab[r][s].setBackground(Color.yellow);
                                }
                                if (tabuleiro[r][s] == 4) {
                                    tab[r][s].setBackground(Color.green);
                                }
                                if (tabuleiro[r][s] == 5) {
                                    tab[r][s].setBackground(Color.black);
                                }
                                if (tabuleiro[r][s] == 6) {
                                    tab[r][s].setBackground(Color.pink);
                                }
                                if (tabuleiro[r][s] == 7) {
                                    tab[r][s].setBackground(Color.cyan);
                                }
                                if (tabuleiro[r][s] == 8) {
                                    tab[r][s].setBackground(Color.gray);
                                }
                                if (tabuleiro[r][s] == 9) {
                                    tab[r][s].setBackground(Color.magenta);
                                }
                            }

                        }*/
                    }
                });
            }
        }

        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                cor_definida = aleatorio.nextInt(cor)+1;
                tab[i][j].setVisible(true);
                tela.add(tab[i][j]);

                if (i >= 0 && j >= 0 && i <= dim + 1 && j <= dim + 1) {
                    tabuleiro[i][j] = cor_definida;
                }
                if (cor_definida == 1) {
                    tab[i][j].setBackground(Color.blue);
                }
                if (cor_definida == 2) {
                    tab[i][j].setBackground(Color.red);
                }
                if (cor_definida == 3) {
                    tab[i][j].setBackground(Color.yellow);
                }
                if (cor_definida == 4) {
                    tab[i][j].setBackground(Color.green);
                }
                if (cor_definida == 5) {
                    tab[i][j].setBackground(Color.black);
                }
                if (cor_definida == 6) {
                    tab[i][j].setBackground(Color.pink);
                }
                if (cor_definida == 7) {
                    tab[i][j].setBackground(Color.cyan);
                }
                if (cor_definida == 8) {
                    tab[i][j].setBackground(Color.gray);
                }
                if (cor_definida == 9) {
                    tab[i][j].setBackground(Color.magenta);
                }
            }
        }

        if (score==dim*2){
            TelaGameOver obj = new TelaGameOver();
            obj.setVisible(true);
            tela.setVisible(false);
        }

        tela.setVisible(true);

    }

    public int Eliminar(int x, int y) {
        int pontos = 1;
        int a = x;
        int b = x;
        int c = y;
        int d = y;

        while (a< dim-1 && tabuleiro[a][y] == tabuleiro[a+1][y]){
            //tabuleiro[a][y]=0;
            a+=1;
            tab[a][y].setBackground(Color.white);
            pontos+=1;

        }
        while(b>0 && tabuleiro[b][y] == tabuleiro[b-1][y]){
            //tabuleiro[b][y]=0;
            b-=1;
            tab[b][y].setBackground(Color.white);
            pontos+=1;

        }
        while(c< dim-1 && tabuleiro[x][c] == tabuleiro[x][c+1] ){
            //tabuleiro[x][c]=0;
            c+=1;
            tab[x][c].setBackground(Color.white);
            pontos+=1;

        }
        while (d>0 && tabuleiro[x][d] == tabuleiro[x][d-1]){
            //tabuleiro[x][d]=0;
            d-=1;
            tab[x][d].setBackground(Color.white);
            pontos+=1;

        }
        //tabuleiro[x][y]=0;

        tab[x][y].setBackground(Color.white);
        score+=pontos;
        return score;


    }

}
