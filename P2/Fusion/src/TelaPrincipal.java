import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import static java.awt.Color.white;

public class TelaPrincipal extends JFrame implements ActionListener  {
    private JFrame tela;
    private JLabel background;
    private JLabel titulo;
    private JButton playButton;
    private JButton personalizarButton;
    private JButton creditosButton;
    private int dim = 10;
    private int cor = 4;

    public static void main(String[] args) {
        TelaPrincipal obj = new TelaPrincipal();

    }

    public TelaPrincipal() {
        tela = new JFrame("FUSION- Ana Ferro(39872) e Rui Luís(39919)");
        tela.setBounds(0,0,1000,750);
        tela.setLocationRelativeTo(null);
        tela.setLayout(null);
        tela.setResizable(false);
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        background = new JLabel();
        background.setBounds(0,0,1000,750);
        background.setIcon(new ImageIcon("IconesFusion/Background.jpg"));
        background.setVisible(true);
        tela.add(background);

        titulo = new JLabel();
        titulo.setBounds(323, 0, 500,150);
        titulo.setIcon(new ImageIcon("IconesFusion/Fusion130.png"));
        titulo.setVisible(true);
        background.add(titulo);

        playButton = new JButton();
        playButton.setBounds(440, 237, 128,128);
        playButton.setIcon(new ImageIcon("IconesFusion/playbutton.png"));
        playButton.setBorderPainted(false);
        playButton.setContentAreaFilled(false);
        playButton.setBackground(white);
        playButton.setVisible(true);
        background.add(playButton);
        playButton.addActionListener(this);

        personalizarButton = new JButton();
        personalizarButton.setBounds(380, 500, 243, 24);
        personalizarButton.setIcon(new ImageIcon("IconesFusion/Personalizar.png"));
        personalizarButton.setBorderPainted(false);
        personalizarButton.setContentAreaFilled(false);
        personalizarButton.setVisible(true);
        background.add(personalizarButton);
        personalizarButton.addActionListener(this);

        creditosButton = new JButton();
        creditosButton.setBounds(425, 550, 165, 24);
        creditosButton.setIcon(new ImageIcon("IconesFusion/Creditos.png"));
        creditosButton.setBorderPainted(false);
        creditosButton.setContentAreaFilled(false);
        creditosButton.setVisible(true);
        background.add(creditosButton);
        creditosButton.addActionListener(this);

        tela.setVisible(true);

    }
    @Override
    public void actionPerformed(ActionEvent event) {
        if(event.getSource() instanceof JButton) {
            JButton clickedButton = (JButton) event.getSource();
            if (clickedButton == playButton) {
                Jogo jogo = new Jogo(dim, cor);
                jogo.setVisible(true);
                tela.setVisible(false);

            }
            else if (clickedButton == personalizarButton){
               TelaPersonalizar novatela = new TelaPersonalizar();
               novatela.setVisible(true);
               tela.setVisible(false);

            }
            else {
                TelaCreditos creditos = new TelaCreditos();
                creditos.setVisible(true);
                tela.setVisible(false);

            }

        }
    }

}
