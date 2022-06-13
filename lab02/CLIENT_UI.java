import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.rmi.Naming;
import java.rmi.RemoteException;

import javax.swing.*;

public class CLIENT_UI {

    private JFrame frame;
    private JPanel panel;
    private JButton seat_button;
    private JButton reservation_button;
    private int width;
    private int height;
    private IMovieTheater stub;

    public CLIENT_UI(int w, int h) throws Exception {
        frame = new JFrame();
        seat_button = new JButton("Ver poltronas");
        reservation_button = new JButton("Reservar poltrona");
        width = w;
        height = h;
        panel = new JPanel();
        stub = (IMovieTheater) Naming.lookup("rmi://localhost:1234/MovieTheater");

    }

    public void setUpCLIENT_UI() {
        frame.setSize(width, height);
        frame.setTitle("Bem-vindo ao cinema X");
        panel.add(seat_button);
        panel.add(reservation_button);
        frame.add(panel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public void seatWindow() throws RemoteException {
        JFrame seatFrame = new JFrame();
        JPanel seatPanel = new JPanel();


        seatPanel.setLayout(new GridLayout(3, 3));
        seatFrame.setSize(300, 300);
        Boolean[] seats = stub.checkEmptySpaces();
        int index = 0;
        for (Boolean reserved : seats) {
            if (!reserved) {
                seatPanel.add(new JButton(Integer.toString(index)));
            } else {

                seatPanel.add(new JButton("-")).setEnabled(false);
            }
            index++;
        }
        seatFrame.setVisible(true);
        seatPanel.setVisible(true);
        seatFrame.add(seatPanel);
    }


    public void reservationWindow() throws RemoteException {
        JFrame reservationFrame = new JFrame();
        String seat = JOptionPane.showInputDialog(reservationFrame, "Digite o número da poltrona: ");
        Boolean isSucess = stub.reservation(Integer.parseInt(seat));
        if(!isSucess)
        JOptionPane.showMessageDialog(reservationFrame, "Poltrona já está ocupada.");
        seatWindow();
    }
    public void setUpButtonListeners() {
        ActionListener buttonListener1 = new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                try {
                    seatWindow();
                } catch (RemoteException e1) {
                    e1.printStackTrace();
                }

            }
        };
        ActionListener buttonListener2 = new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                try {
                    reservationWindow();
                } catch (RemoteException e1) {
                    e1.printStackTrace();
                }

            }
        };
        seat_button.addActionListener(buttonListener1);
        reservation_button.addActionListener(buttonListener2);
    }

    public static void main(String args[]) throws Exception {
        CLIENT_UI mainCLIENT_UI = new CLIENT_UI(300, 100);
        mainCLIENT_UI.setUpCLIENT_UI();
        mainCLIENT_UI.setUpButtonListeners();
    }
}
