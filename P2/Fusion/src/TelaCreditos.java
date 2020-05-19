import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TelaCreditos extends JFrame implements ActionListener {
    private JFrame tela;
    private JLabel background;
    private JLabel titulo;
    private JLabel cabeçalho;
    private JLabel autores;
    private JButton setaButton;


    public TelaCreditos() {
        tela = new JFrame();
        tela.setBounds(0,0,555,850);
        tela.setLocationRelativeTo(null);
        tela.setResizable(false);
        tela.setLayout(null);
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        background = new JLabel();
        background.setBounds(0,0,555,850);
        background.setIcon(new ImageIcon("IconesFusion/CreditosFinais.jpg"));
        background.setVisible(true);
        tela.add(background);

        titulo = new JLabel();
        titulo.setBounds(120, 20, 328,87);
        titulo.setIcon(new ImageIcon("IconesFusion/CreditosTitle.png"));
        titulo.setVisible(true);
        background.add(titulo);

        cabeçalho = new JLabel();
        cabeçalho.setBounds(80, 200, 397,68);
        cabeçalho.setIcon(new ImageIcon("IconesFusion/UniCurso.png"));
        cabeçalho.setVisible(true);
        background.add(cabeçalho);
        
        autores = new JLabel();
        autores.setBounds(175,350,224,47);
        autores.setIcon(new ImageIcon("IconesFusion/Autores.png"));
        autores.setVisible(true);
        background.add(autores);

        setaButton = new JButton();
        setaButton.setBounds(430, 720, 128,128);
        setaButton.setIcon(new ImageIcon("IconesFusion/Seta2.png"));
        setaButton.setBorderPainted(false);
        setaButton.setContentAreaFilled(false);
        setaButton.setFocusPainted(false);
        setaButton.setVisible(true);
        background.add(setaButton);
        setaButton.addActionListener(this);

        tela.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent event) {
        TelaPrincipal menu = new TelaPrincipal();
        menu.setVisible(true);
        tela.setVisible(false);
    }
}
