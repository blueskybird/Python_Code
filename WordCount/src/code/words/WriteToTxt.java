package code.words;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

public class WriteToTxt {
	//此方法是在源文件后面追加内容
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
            
            //先保存文件原有内容
            while ((str = input.readLine()) != null) {  
                s1 += str + "\r\n";  
            }  
            System.out.println(s1);  
            input.close();
            
            //在原有文件后面追加新内容
            s1 += content;  
  
            BufferedWriter output = new BufferedWriter(new FileWriter(f));  
            output.write(s1);  
            output.close();  
        } catch (Exception e) {
            e.printStackTrace();  
  
        }  
    } 
}
