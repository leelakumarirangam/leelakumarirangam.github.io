import java.util.ArrayList;
import java.util.Scanner;

public class TodoList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> tasks = new ArrayList<>();

        while(true) {
            System.out.println("\n--- To-Do List ---");
            System.out.println("1. Add Task  2. View Tasks  3. Delete Task  4. Exit");
            int choice = sc.nextInt();
            sc.nextLine(); // consume newline

            if(choice == 1) {
                System.out.println("Enter task:");
                String task = sc.nextLine();
                tasks.add(task);
                System.out.println("Task added!");
            } else if(choice == 2) {
                if(tasks.isEmpty()) {
                    System.out.println("No tasks found!");
                } else {
                    System.out.println("Your tasks:");
                    for(int i = 0; i < tasks.size(); i++) {
                        System.out.println((i+1) + ". " + tasks.get(i));
                    }
                }
            } else if(choice == 3) {
                System.out.println("Enter task number to delete:");
                int taskNum = sc.nextInt();
                if(taskNum <= tasks.size() && taskNum > 0) {
                    tasks.remove(taskNum - 1);
                    System.out.println("Task deleted!");
                } else {
                    System.out.println("Invalid task number");
                }
            } else if(choice == 4) {
                System.out.println("Goodbye!");
                break;
            } else {
                System.out.println("Invalid choice");
            }
        }

        sc.close();
    }
}
