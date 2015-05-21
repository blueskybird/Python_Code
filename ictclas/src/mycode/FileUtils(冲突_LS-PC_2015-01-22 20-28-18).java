package mycode;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileFilter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class FileUtils {

	/**
	 * 
	 * 读取文件中的内容
	 * 
	 * @param filePath
	 * 
	 */
	public static StringBuffer readTxtFile(String filePath) {
		StringBuffer fileCon = new StringBuffer();
		try {
			String encoding = "GB2312";// 或者GBK格式
			File file = new File(filePath);
			if (file.isFile() && file.exists()) {
				InputStreamReader read = new InputStreamReader(
						new FileInputStream(file), encoding);
				BufferedReader brr = new BufferedReader(read);
				String lineTxt = null;
				while ((lineTxt = brr.readLine()) != null) {
					System.out.print(lineTxt);
					fileCon.append(lineTxt);
				}
				read.close();
			} else {
				System.out.println("找不到指定文件");
			}

		} catch (Exception e) {
			System.out.println("读取文件内容出错");
			e.printStackTrace();
		}
		return fileCon;
	}

	/**
	 * 获取文件的扩展名
	 * 
	 * @param filename
	 * @param defExt
	 * @return
	 */
	public static String getExtension(String filename, String defExt) {
		if ((filename != null) && (filename.length() > 0)) {
			int i = filename.lastIndexOf('.');

			if ((i > -1) && (i < (filename.length() - 1))) {
				return filename.substring(i + 1);
			}
		}
		return defExt;
	}

	public static String getExtension(String filename) {
		return getExtension(filename, "");
	}

	/**
	 * 获取一个文件夹下的所有文件 要求：后缀名为txt (可自己修改)
	 * 
	 * @param file
	 * @return
	 */
	public static List<String> getFileList(File file) {
		List<String> result = new ArrayList<String>();
		if (!file.isDirectory()) {
			System.out.println(file.getAbsolutePath());
			result.add(file.getAbsolutePath());
		} else {
			// 内部匿名类，用来过滤文件类型，拿到满足条件的文件的全路径
			File[] directoryList = file.listFiles(new FileFilter() {
				public boolean accept(File file) {
					if (file.isFile() && file.getName().indexOf(".txt") > -1) {
						return true;
					} else {
						return false;
					}
				}
			});
			for (int i = 0; i < directoryList.length; i++) {
				result.add(directoryList[i].getAbsolutePath());
			}
		}
		return result;
	}

	/**
	 * 以UTF-8编码方式读取文件内容
	 * 
	 * @param path
	 * @return
	 * @throws IOException
	 */
	public static String getContentByLocalFile(File path) throws IOException {
		InputStream input = new FileInputStream(path);
		InputStreamReader reader = new InputStreamReader(input, "utf-8");//之前是gbk，这个看情况吧，因为外部文件存的格式也是utf-8
		BufferedReader br = new BufferedReader(reader);
		StringBuilder builder = new StringBuilder();
		// System.out.print(trimExtension(path.getName())+" ");

		String temp = br.readLine();
		while (temp != null) {
			builder.append(temp);
			temp = br.readLine();
		}
		return builder.toString();
	}

	/**
	 * 去掉文件的扩展名
	 * 
	 * @param filename
	 * @return
	 */
	public static String trimExtension(String filename) {
		if ((filename != null) && (filename.length() > 0)) {
			int i = filename.lastIndexOf('.');
			if ((i > -1) && (i < (filename.length()))) {
				return filename.substring(0, i);
			}
		}
		return filename;
	}
}
