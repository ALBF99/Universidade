import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TelaGameOver extends JFrame implements ActionListener {
    private JFrame telaOver;
    private JLabel backgroundOver;
    private JLabel gameOver;
    private JButton setaButton;

    public static void main(String[] args) {
        TelaGameOver obj = new TelaGameOver();

    }

    public TelaGameOver(){
        telaOver = new JFrame("");
        telaOver.setBounds(0, 0,  500, 745);
        telaOver.setLocationRelativeTo(null);
        telaOver.setLayout(null);
        telaOver.setResizable(false);
        telaOver.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        backgroundOver = new JLabel();
        backgroundOver.setBounds(0, 0, 500, 745);
        backgroundOver.setIcon(new ImageIcon("IconesFusion/GameOver.jpg"));
        backgroundOver.setVisible(true);
        telaOver.add(backgroundOver);

        gameOver = new JLabel();
        gameOver.setBounds(85, 220, 334, 46);
        gameOver.setIcon(new ImageIcon("IconesFusion/GameOverTitulo.png"));
        gameOver.setVisible(true);
        backgroundOver.add(gameOver);

        setaButton = new JButton();
        setaButton.setBounds(375, 610, 128,128);
        setaButton.setIcon(new ImageIcon("IconesFusion/Seta2.png"));
        setaButton.setBorderPainted(false);
        setaButton.setContentAreaFilled(false);
        setaButton.setFocusPainted(false);
        setaButton.setVisible(true);
        backgroundOver.add(setaButton);
        setaButton.addActionListener(this);

        telaOver.setVisible(true);

    }
    @Override
    public void actionPerformed(ActionEvent event) {
        TelaPrincipal menu = new TelaPrincipal();
        menu.setVisible(true);
        telaOver.setVisible(false);
    }
}
