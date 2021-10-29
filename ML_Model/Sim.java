record BankEmployee(int id, String name){}

public class Sim {
  public static void main(String[] args) {
    BankEmployee bankEmployee = new BankEmployee(12, "Frank");
    System.out.println(bankEmployee.id());
    System.out.println(bankEmployee.name());
    System.out.println(bankEmployee);
  }
}
