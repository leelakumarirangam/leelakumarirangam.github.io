import java.util.Scanner;

class BankAccount {
    String name;
    int pin;
    double balance;

    BankAccount(String name, int pin) {
        this.name = name;
        this.pin = pin;
        this.balance = 0;
    }

    void deposit(double amount) {
        balance += amount;
        System.out.println(amount + " deposited. New balance: " + balance);
    }

    void withdraw(double amount) {
        if(amount > balance) {
            System.out.println("Insufficient balance!");
        } else {
            balance -= amount;
            System.out.println(amount + " withdrawn. New balance: " + balance);
        }
    }

    void checkBalance() {
        System.out.println("Hello " + name + ", your balance is: " + balance);
    }

    boolean login(int inputPin) {
        return inputPin == pin;
    }
}

public class BankSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter your name:");
        String name = sc.nextLine();
        System.out.println("Set a 4-digit PIN:");
        int pin = sc.nextInt();

        BankAccount user = new BankAccount(name, pin);

        System.out.println("\nLogin to your account:");
        System.out.println("Enter PIN:");
        int inputPin = sc.nextInt();

        if(user.login(inputPin)) {
            System.out.println("Login successful!");
            while(true) {
                System.out.println("\n1. Deposit  2. Withdraw  3. Check Balance  4. Exit");
                int choice = sc.nextInt();
                if(choice == 1) {
                    System.out.println("Enter amount to deposit:");
                    user.deposit(sc.nextDouble());
                } else if(choice == 2) {
                    System.out.println("Enter amount to withdraw:");
                    user.withdraw(sc.nextDouble());
                } else if(choice == 3) {
                    user.checkBalance();
                } else if(choice == 4) {
                    System.out.println("Thank you! Goodbye!");
                    break;
                } else {
                    System.out.println("Invalid choice");
                }
            }
        } else {
            System.out.println("Incorrect PIN. Access denied!");
        }

        sc.close();
    }
}
