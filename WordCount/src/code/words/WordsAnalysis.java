package code.words;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class WordsAnalysis {

    /**
     * @param args
     * @throws IOException 
     */
    public static void main(String[] args) throws IOException {
    	//要统计的文件夹目录
        File f = new File("F:\\Test");
//    	File f = new File("F:\\TestYS");
//    	File f = new File("F:\\splitedText\\zhonghuaNet\\football");
        File[] fs = f.listFiles();
        // 分成两半
        List<File> files1 = new ArrayList<File>();
//        for (int i = 0; i < fs.length/2; i++) {+
        for (int i = 0; i < fs.length; i++) {
            files1.add(fs[i]);
            
        }
        List<File> files2 = new ArrayList<File>();
        for (int i = fs.length/2; i < fs.length; i++) {
            files2.add(fs[i]);
            
        }
        // 工作线程总数
        int threadCount = 0;
        // 共享数据
        AllCountModel acm = new AllCountModel();
        acm.setThreadCount(++threadCount);
        ThreadTest tt1 = new ThreadTest(files1, acm);
        // 1号线程
        tt1.start();
//        acm.setThreadCount(++threadCount);
//        ThreadTest tt2 = new ThreadTest(files2, acm);
//        // 2号线程
//        tt2.start();
        MonitorThread mt = new MonitorThread(acm);
        // 监视线程
        mt.start();
    }
    
    /**
     * 
     * @param file
     * @param wordsMap
     * @return
     * @throws IOException
     */
    public Map<String, Integer> countWords(File file, Map<String, Integer> wordsMap) throws IOException{
        
        // 读流
        BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file)));
        // 一行字符串
        String str;
        // 读取每一行
        while((str = reader.readLine()) != null ){
            str = str.trim();
            // 跳过空行
            if(str.equals("") || str == null){
                continue;
            }
            // 按空格分离成单词
            String[] strs = str.split(" ");
            for (int i = 0; i < strs.length; i++) {
                String word = strs[i].trim();
                // 重现的单词
                if(wordsMap.containsKey(word)){
                    // 计数
                    wordsMap.put(word, (wordsMap.get(word) + 1));
                }else{
                    // 第一次出现的新单词
                    wordsMap.put(word, 1);
                }
            }
        }
        // 关闭流
        reader.close();
        return wordsMap;
    }
    
    /**
     * 打印结果
     * @param AllCountModel 共享的结果集
     */
    public static void show(AllCountModel acm){
    	//将统计好的词频写入的文件目录,文件名为wordCount.txt
//    	String fileName="F:\\wordNum\\wordCount.txt";
//    	String fileName="F:\\wordNum\\wordCountYS.txt";
    	String fileName="F:\\wordNum\\wordCountBF.txt";
        System.out.println(acm.getThreadCount());
        int num=0;
        for (List<File> lists : acm.getLastMap().keySet()) {
            System.out.println(lists);
            for (String str : acm.getLastMap().get(lists).keySet()) {
            	str=str + " : " + acm.getLastMap().get(lists).get(str);
//                System.out.println(str);
                num++;
                WriteToTxt.writeToTxt(fileName, str);
            }
            System.out.println("------------------------------------------");
            System.out.println(lists.size());
        }
        System.out.println(num);
        
    }
}