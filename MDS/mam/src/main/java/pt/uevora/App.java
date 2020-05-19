package pt.uevora;
import java.awt.image.AreaAveragingScaleFilter;
import java.util.ArrayList;
import java.util.Scanner;
public class App
{
    ArrayList<User> utilizadores = new ArrayList<>();
    ArrayList<Pedido> pedidosgestor=new ArrayList<>();

    public void Login(App app)
    {
        String resposta;
        Scanner scanner = new Scanner(System.in);
        System.out.println("É novo utilizador? ");
        resposta = scanner.nextLine();

        String username, password;

        for (int i = 0; i < 100; i++)
        {
            if (resposta.equals("Sim"))
            {
                System.out.println("Se for colaborador insira como: C-xxxxx");
                System.out.println("Se for gestor insira como: G-xxxxx");
                System.out.println("Insira um username: ");
                username = scanner.nextLine();
                System.out.println("Insira uma password: ");
                password = scanner.nextLine();
                User user = new User(username, password);

                if(username.charAt(0) == 'G')
                {
                    user.gestor = true;
                }
                else
                {
                    user.gestor = false;
                }

                utilizadores.add(user);
                opcoes(user,app);
            }
            else if (resposta.equals("Não"))
            {
                System.out.println("Insira um username válido: ");
                username = scanner.nextLine();
                System.out.println("Insira uma password válida:");
                password = scanner.nextLine();

                for (int j = 0; j < utilizadores.size(); j++)
                {
                    User atual = utilizadores.get(j);

                    if(atual.username.equals(username)){

                        while(!atual.password.equals(password)){
                            System.out.println("Password ou username incorreto!");
                            System.out.println("Insira um username válido: ");
                            username = scanner.nextLine();
                            System.out.println("Insira uma password válida:");
                            password = scanner.nextLine();
                        }

                        opcoes(atual,app);
                    }
                }
            }
            else{
                System.out.println("Resposta tem que ser Sim ou Não");
                Login(app);
            }
        }
    }

    public void opcoes(User atual,App app){
        Scanner scanner = new Scanner(System.in);

        int opcao;

        if (!atual.gestor) {
            System.out.println("-------");
            System.out.println("Marcar férias - 1");
            System.out.println("Consultar férias - 2");
            System.out.println("Exit-3");
            System.out.println("-------");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    atual.marcarferias(atual,app);
                    break;
                case 2:
                    atual.consultarferias(atual,app);
                    break;
                case 3:
                    Login(app);
                    break;
                default:
                    break;
            }
        } else {
            System.out.println("-------");
            System.out.println("Marcar férias - 1");
            System.out.println("Consultar férias - 2");
            System.out.println("Aprovar férias - 3");
            System.out.println("Exit-4");
            System.out.println("-------");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    atual.marcarferias(atual,app);
                    break;
                case 2:
                    atual.consultarferias(atual,app);
                    break;
                case 3:
                    atual.aprovarferias(atual,app);
                    break;
                case 4:
                    Login(app);
                    break;
                default:
                    break;
            }
        }
    }

    public static void main(String[] args)
    {
        App app = new App();
        app.Login(app);
    }
}
