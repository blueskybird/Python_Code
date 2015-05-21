package mycode;

import java.io.*;
import java.util.List;

//将接口独立出来一样可以用，不用非要像给的例子一样写在类中,但是这样有一点不好，就是CLibrary中的"./NLPIR"这个地方如果写错了，就不太好找是哪个地方
//import mycode.CLibrary;//在同一个包中，不用引用也是可以的

public class NlpTest {

	public static void main(String[] args) {

		String argu = "./";// Data包所在文件夹
		String system_charset = "UTF-8";
		int charset_type = 1;
		int init_flag = CLibrary.Instance.NLPIR_Init(argu, charset_type, "0");
		String nativeBytes = null;
		String sInput = "";
		if (0 == init_flag) {
			nativeBytes = CLibrary.Instance.NLPIR_GetLastErrorMsg();
			System.err.println("初始化失败！fail reason is " + nativeBytes);
			return;
		}

		// Test get and read all file
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\xinlangweibo\\constellation"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\xinlangweibo\\economic"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\xinlangweibo\\food"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\xinlangweibo\\health"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\xinlangweibo\\sport"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\xinlangweibo\\tecnology"));
		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\xinlangweibo\\travel"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\test"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\house"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\health"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\game"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\football"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\car"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\Economic"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\Education"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\IT"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\Military"));
//		List<String> fileList = FileUtils.getFileList(new File("F:\\srcText\\zhonghuaNet\\Music"));
		String fileContent = null;
		String fileName = "";

		System.out.println("共有" + fileList.size() + "个文件");
		for (String s : fileList) {
			// 打印文件名
			// s的格式：F:\test\NewsTitle4.txt
			fileName = s.substring(s.lastIndexOf('\\') + 1, s.length());
			fileName = fileName.substring(0, fileName.indexOf('.'));

			System.out.println(FileUtils.trimExtension(s));// 同一个包内，不用引用，也没比要是static类，就能直接引用
			// 文件内容
			try {
				fileContent = FileUtils.getContentByLocalFile(new File(s));
			} catch (IOException e) {
				e.printStackTrace();
			}
			sInput = fileContent;
			System.out.println(sInput);

			// 分词
			nativeBytes = CLibrary.Instance.NLPIR_ParagraphProcess(sInput, 0);// 0代表无词性，1代表有词性
			System.out.println("分词结果为： " + nativeBytes);

			// 将结果写入txt导出
			try {
//				File f = new File("F:\\splitedText\\xinlangweibo\\constellation\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\xinlangweibo\\economic\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\xinlangweibo\\food\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\xinlangweibo\\health\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\xinlangweibo\\sport\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\xinlangweibo\\tecnology\\" + fileName + ".txt");
				File f = new File("F:\\splitedText\\xinlangweibo\\travel\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\health\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\game\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\football\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\car\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\Economic\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\Education\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\IT\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\Military\\" + fileName + ".txt");
//				File f = new File("F:\\splitedText\\zhonghuaNet\\Music\\" + fileName + ".txt");
				f.delete();
				f.createNewFile();
				BufferedWriter writeIn = new BufferedWriter(new FileWriter(f));
				writeIn.write(nativeBytes);
				writeIn.close();
			} catch (Exception e) {
				// TODO: handle exception
				e.printStackTrace();
			}
		}

//		sInput = "据悉，质检总局已将最新有关情况再次通报美方，要求美方加强对输华玉米的产地来源、运输及仓储等环节的管控措施，有效避免输华玉米被未经我国农业部安全评估并批准的转基因品系污染。";
//		sInput = "踢球时被对手炫技了NBA是怎样的体验";
//		 try {
//		
//		 nativeBytes = CLibrary.Instance.NLPIR_ParagraphProcess(sInput, 1);// 0代表无词性，1代表有词性
//		
//		 System.out.println("分词结果为： " + nativeBytes);
//		 
//		
//		 CLibrary.Instance.NLPIR_AddUserWord("要求美方加强对输 n");
//		 CLibrary.Instance.NLPIR_AddUserWord("华玉米的产地来源 n");
//		 nativeBytes = CLibrary.Instance.NLPIR_ParagraphProcess(sInput, 1);
//		 System.out.println("增加用户词典后分词结果为： " + nativeBytes);
//		
//		 CLibrary.Instance.NLPIR_DelUsrWord("要求美方加强对输");
//		 nativeBytes = CLibrary.Instance.NLPIR_ParagraphProcess(sInput, 1);
//		 System.out.println("删除用户词典后分词结果为： " + nativeBytes);
//		
//		 CLibrary.Instance.NLPIR_Exit();
//		
//		 } catch (Exception ex) {
//		 // TODO Auto-generated catch block
//		 ex.printStackTrace();
//		 }

	}
}
