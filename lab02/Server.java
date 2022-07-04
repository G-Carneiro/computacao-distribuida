import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server {
    public static void main(String[] args){
        try {

            IMovieTheater movieTheater = new MovieTheater(9);
            
            System.out.println("Registrando o objeto no RMI Registry");

            Registry reg = LocateRegistry.createRegistry(1234);
            
            Naming.rebind("rmi://localhost:1234/MovieTheater", movieTheater);

            System.out.println("Servidor esperando clientes para atender!");
        } catch(Exception e){
            e.printStackTrace();
        }
    }
}