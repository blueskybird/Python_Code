import java.io.*;


public class filewrite {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String filePath="F:\\wordNum\\test.txt";
		String content="测试!";
		writeToTxt(filePath, content);
	}
	
	public static void writeToTxt(String filePath, String content) {
        String str = new String(); //原有txt内容  
        String s1 = new String();//内容更新  
        try {  
            File f = new File(filePath);  
            if (f.exists()) {  
                System.out.print("文件存在");  
            } else {  
                System.out.print("文件不存在");  
                f.createNewFile();// 不存在则创建  
            }  
            BufferedReader input = new BufferedReader(new FileReader(f));  
  
            while ((str = input.readLine()) != null) {  
                s1 += str + "\r\n";  
            }  
            System.out.println(s1);  
            input.close();  
            s1 += content;  
  
            BufferedWriter output = new BufferedWriter(new FileWriter(f));  
            output.write(s1);  
            output.close();  
        } catch (Exception e) {
            e.printStackTrace(); 
        }  
    }  

}
