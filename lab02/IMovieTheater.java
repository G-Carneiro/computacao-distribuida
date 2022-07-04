import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IMovieTheater extends Remote{

    Boolean[] checkEmptySpaces() throws RemoteException;
    Boolean reservation(int seat_id) throws RemoteException;
}