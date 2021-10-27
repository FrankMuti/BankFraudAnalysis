import java.util.Scanner;

public class Run {

  private String dataFile;
  private String jsonOutFile;
  private String scalerFile;
  private String classifierFile;

  private boolean running;

  private final Scanner sc;

  public Run() {
    this.running = true;
    this.sc = new Scanner(System.in);
  }

  public Run(String dataFile, String jsonOutFile, String scalerFile, String classifierFile) {
    this();
    this.dataFile = dataFile;
    this.jsonOutFile = jsonOutFile;
    this.scalerFile = scalerFile;
    this.classifierFile = classifierFile;
  }

  public void run() {
    while (this.running) {
      System.out.println("Options: ");
      System.out.println("1) Build Model");
      System.out.println("2) Classify Transactions");
      System.out.println("3) Both (1) and (2)");
      System.out.println("4) Exit");

      int opt = -1;

      try {
        opt = Integer.parseInt(sc.nextLine().trim());
        if (opt < 1 || opt > 4) {
          Integer.parseInt("get caught");
        }
      } catch(Exception e) {
        System.out.println("Invalid input. Try again");
      }

      switch(opt) {
        case 1:
          buildModel();
          break;
        case 2:
          classifyTransaction();
          break;
        case 3:
          buildModel();
          classifyTransaction();
          break;
        case 4:
          exit();
      }
    }
  }

  private void buildModel() {

  }

  private void classifyTransaction() {

  }

  private void exit() {
    this.sc.close();
    this.running = false;
    System.out.println("Adios");
  }

  public String getDataFile() {
    return dataFile;
  }

  public void setDataFile(String dataFile) {
    this.dataFile = dataFile;
  }

  public String getJsonOutFile() {
    return jsonOutFile;
  }

  public void setJsonOutFile(String jsonOutFile) {
    this.jsonOutFile = jsonOutFile;
  }

  public String getScalerFile() {
    return scalerFile;
  }

  public void setScalerFile(String scalerFile) {
    this.scalerFile = scalerFile;
  }

  public String getClassifierFile() {
    return classifierFile;
  }

  public void setClassifierFile(String classifierFile) {
    this.classifierFile = classifierFile;
  }

  public static void main(String[] args) {
    new Run().run();
  }
}