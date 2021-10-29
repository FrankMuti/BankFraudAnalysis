import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Run {
  private String dataFile;
  private String jsonOutFile;
  private String scalerFile;
  private String classifierFile;

  private String builderScript;
  private String classifyScript;

  private boolean running;

  private final Scanner sc;

  public Run() {
    this.running = true;
    this.sc = new Scanner(System.in);

    // hardcoded
    this.builderScript = "builder.py";
    this.classifyScript = "classify.py";

    this.dataFile = "data/creditcard.csv";
    this.jsonOutFile = "data/out.json";
    this.scalerFile = "static/Scaler.pkl";
    this.classifierFile = "static/Model.pkl";
  }

  public Run(String dataFile, String jsonOutFile, String scalerFile, String classifierFile) {
    this();
    this.dataFile = dataFile;
    this.jsonOutFile = jsonOutFile;
    this.scalerFile = scalerFile;
    this.classifierFile = classifierFile;
  }

  public void run() throws IOException, InterruptedException {
    while (this.running) {
      System.out.println("============================================");
      System.out.println("Options: ");
      System.out.println("1) Build Model");
      System.out.println("2) Classify Transactions");
      System.out.println("3) Both (1) and (2)");
      System.out.println("4) Exit");
      System.out.println("===========================================");
      System.out.print  ("Enter Option: ");

      int opt = -1;

      try {
        opt = Integer.parseInt(sc.nextLine().trim());
        if (opt < 1 || opt > 4) {
          Integer.parseInt("get caught");
        }
      } catch(Exception e) {
        System.out.println("Invalid input. Try again");
      }
      System.out.println("===========================================");

      switch(opt) {
        case 1 -> buildModel();
        case 2 -> classifyTransaction();
        case 3 -> {
          buildModel(); 
          classifyTransaction();
        }
        case 4 -> exit();
      }
      // switch(opt) {
      //   case 1:
      //     buildModel();
      //     break;
      //   case 2:
      //     classifyTransaction();
      //     break;
      //   case 3:
      //     buildModel();
      //     classifyTransaction();
      //     break;
      //   case 4:
      //     exit();
      // }
    }
  }

  private void buildModel() {
    String command = String.format("python %s", 
    this.builderScript);

    System.out.printf("$ %s\n", command);
    try {
      execute(command);
    } catch (IOException | InterruptedException e) {
      System.out.println(e.getMessage());
      System.out.println("Something bad happened");
    }
  }

  private void classifyTransaction() {
    String command = String.format("python %s -d %s -j %s -s %s -c %s -t noth", 
      this.classifyScript, 
      this.dataFile,
      this.jsonOutFile,
      this.scalerFile,
      this.classifierFile);

    System.out.printf("$ %s\n", command);
    try {
      execute(command);
    } catch (IOException | InterruptedException e) {
      System.out.println(e.getMessage());
      System.out.println("Something bad happened");
    }
  }

  private void execute(String command) throws IOException, InterruptedException {
    Process p = Runtime.getRuntime().exec(command);
    System.out.println("Running....");
    p.waitFor();
    BufferedReader bf = new BufferedReader(new InputStreamReader(p.getInputStream()));
    BufferedReader bfError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
    String tmpLine = "";
    while ((tmpLine = bf.readLine()) != null) {
      System.out.println(tmpLine);
    }
    bf.close();
    while ((tmpLine = bfError.readLine()) != null) {
      System.out.println(tmpLine);
    }
    bfError.close();
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

  public String getBuilderScript() {
    return builderScript;
  }

  public void setBuilderScript(String builderScript) {
    this.builderScript = builderScript;
  }

  public String getClassifyScript() {
    return classifyScript;
  }

  public void setClassifyScript(String classifyScript) {
    this.classifyScript = classifyScript;
  }

  public static void main(String[] args) throws IOException, InterruptedException {
    new Run().run();
  }
}