import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.Arrays;

public class MovieTheater extends UnicastRemoteObject implements IMovieTheater{

    private Boolean[] seats;
    public MovieTheater(int seats) throws RemoteException{
        this.seats = new Boolean[seats];
        Arrays.fill(this.seats, Boolean.FALSE);
    }

    @Override
    public synchronized Boolean[] checkEmptySpaces() throws RemoteException {
        return seats;
    }

    @Override
    public synchronized Boolean reservation(int seat_id) throws RemoteException {
        
        Boolean reserved = seats[seat_id];
        
        if(!reserved){
            seats[seat_id] = true;
            return true;
        } 
        
        return false;
    }
    
}
