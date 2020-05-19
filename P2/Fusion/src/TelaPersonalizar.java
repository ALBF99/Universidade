import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TelaPersonalizar extends JFrame implements ActionListener {
    private JFrame tela;
    private JLabel background;
    private JLabel titulo;
    private JTextField inputDimensao;
    private JTextField inputCores;
    private JLabel dimensao;
    private JLabel cores;
    private JButton setaButton;
    private JButton playButton;
    int dim, cor;


    public TelaPersonalizar() {
        tela = new JFrame("FUSION");
        tela.setBounds(0, 0, 564, 800);
        tela.setLocationRelativeTo(null);
        tela.setResizable(false);
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        background = new JLabel();
        background.setBounds(0, 0, 564, 865);
        background.setIcon(new ImageIcon("IconesFusion/TelaPersonalizar2.jpg"));
        background.setVisible(true);
        tela.add(background);

        titulo = new JLabel();
        titulo.setBounds(70, 0, 500,150);
        titulo.setIcon(new ImageIcon("IconesFusion/Personalizar75.png"));
        titulo.setVisible(true);
        background.add(titulo);

        dimensao = new JLabel();
        dimensao.setBounds(90,0, 500,425);
        dimensao.setText("Dimensão(2-16):");
        dimensao.setFont(new Font("Arial",1,25));
        background.add(dimensao);
        dimensao.setVisible(true);
        inputDimensao = new JTextField();
        inputDimensao.setBounds(360,200,100,30);
        inputDimensao.setColumns(22);
        inputDimensao.setVisible(true);
        background.add(inputDimensao);

        cores = new JLabel();
        cores.setBounds(90,0, 500,550);
        cores.setText("Nº de cores(2-9):");
        cores.setFont(new Font("Arial",1,25));
        background.add(cores);
        cores.setVisible(true);
        inputCores = new JTextField();
        inputCores.setBounds(360,260,100,30);
        inputCores.setColumns(22);
        inputCores.setVisible(true);
        background.add(inputCores);

        inputDimensao.addActionListener(this);
        inputCores.addActionListener(this);

        setaButton = new JButton();
        setaButton.setBounds(440, 680, 128,128);
        setaButton.setIcon(new ImageIcon("IconesFusion/Seta2.png"));
        setaButton.setBorderPainted(false);
        setaButton.setContentAreaFilled(false);
        setaButton.setFocusPainted(false);
        setaButton.setVisible(true);
        background.add(setaButton);
        setaButton.addActionListener(this);

        playButton = new JButton();
        playButton.setBounds(140, 600, 314,40);
        playButton.setIcon(new ImageIcon("IconesFusion/Letsplay2.png"));
        playButton.setBorderPainted(false);
        playButton.setContentAreaFilled(false);
        playButton.setVisible(true);
        background.add(playButton);
        playButton.addActionListener(this);

        tela.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent event) {
        if(event.getSource() instanceof JButton) {
            JButton clickedButton = (JButton) event.getSource();
            if( clickedButton == setaButton){
                TelaPrincipal menu = new TelaPrincipal();
                menu.setVisible(true);
                tela.setVisible(false);
            }
            else{
                try{
                    String str = inputDimensao.getText();
                    dim = Integer.parseInt(str);
                    String str2 = inputCores.getText();
                    cor = Integer.parseInt(str2);
                    if (dim>=2 && dim<=16 && cor>=2 && cor<=9){
                        Jogo jogo = new Jogo(dim, cor);
                        jogo.setVisible(true);
                        tela.setVisible(false);
                    }
                    else {
                        final JPanel panel = new JPanel();
                        JOptionPane.showMessageDialog( panel, "Invalid Input", "Error", JOptionPane.ERROR_MESSAGE);

                    }

                }catch (NumberFormatException ex) {
                    final JPanel panel = new JPanel();
                    JOptionPane.showMessageDialog(panel, "Invalid Input", "Error", JOptionPane.ERROR_MESSAGE);
                }


            }
        }
    }
}
