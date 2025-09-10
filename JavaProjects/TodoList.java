package JavaProjects;

import java.util.ArrayList;
import java.util.Scanner;

public class TodoList {
    private ArrayList<String> tasks;

    public TodoList() {
        tasks = new ArrayList<>();
    }

    public void addTask(String task) {
        tasks.add(task);
        System.out.println("Task added: " + task);
    }

    public void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks in the list.");
        } else {
            System.out.println("Todo List:");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
        }
    }

    public void removeTask(int index) {
        if (index > 0 && index <= tasks.size()) {
            String removed = tasks.remove(index - 1);
            System.out.println("Task removed: " + removed);
        } else {
            System.out.println("Invalid task number.");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TodoList todo = new TodoList();
        int choice;

        do {
            System.out.println("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter task: ");
                    String task = sc.nextLine();
                    todo.addTask(task);
                    break;
                case 2:
                    todo.viewTasks();
                    break;
                case 3:
                    System.out.print("Enter task number to remove: ");
                    int num = sc.nextInt();
                    todo.removeTask(num);
                    break;
                case 4:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 4);

        sc.close();
    }
}
