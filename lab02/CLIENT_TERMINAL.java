import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.util.Scanner;

public class CLIENT_TERMINAL {
    private IMovieTheater stub;

    public CLIENT_TERMINAL() throws MalformedURLException, RemoteException, NotBoundException {
        stub = (IMovieTheater) Naming.lookup("rmi://localhost:1234/MovieTheater");
    }

    public void menu() throws RemoteException {

        Scanner scan = new Scanner(System.in);
        int response;
        do {
            System.out.println("Escolha uma opção:");
            System.out.println("1 - Ver poltronas.");
            System.out.println("2 - Reservar poltrona.");
            System.out.println("3 - Sair.");
            System.out.println("");
            response = scan.nextInt();

            switch (response) {
                case 1:
                    Boolean[] seats = stub.checkEmptySpaces();
                    int index = 0;
                    for (Boolean isOccupied : seats) {

                        if (!isOccupied) {
                            System.out.println("Poltrona " + index + ": Disponível");
                        } else {
                            System.out.println("Poltrona " + index + ": Ocupada");
                        }
                        index++;
                    }
                    break;

                case 2:
                    System.out.println("Digite o número da poltrona:");
                    int seatNum = scan.nextInt();
                    Boolean isSuccess = stub.reservation(seatNum);

                    if (isSuccess) {
                        System.out.println("Poltrona reservada.");
                    } else {

                        System.out.println("Poltrona já está ocupada.");
                    }
                    break;
                case 3:
                    response = 3;
                    break;
                default:
                    System.out.println("Opção inválida");
            }
            System.out.println("");
        } while (response != 3);

    }

    public static void main(String args[]) throws MalformedURLException, RemoteException, NotBoundException {
        CLIENT_TERMINAL guiTerminal = new CLIENT_TERMINAL();
        guiTerminal.menu();
    }
}
