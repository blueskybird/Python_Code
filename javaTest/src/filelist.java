import java.io.*;
import java.util.List;
import java.util.ArrayList;;
public class filelist {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		File f = new File("F:\\Test");
		File[] fs=f.listFiles();
		List<File> files1=new ArrayList<File>();
		
		for(int i=0;i<fs.length;i++){
			System.out.println(fs[i]);
		}
		
		System.out.println(fs.length);
		System.out.println(fs[0].exists());

	}

}
