package code.words;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

public class ThreadTest extends Thread{
    
    private List<File> files = new ArrayList<File>();
    private Map<String, Integer> wordsMap = new HashMap<String, Integer>();
    private AllCountModel allCountModel;
    
    // 每一个线程都传入不一样的files，所以不用担心这个对象的同步冲突
    public ThreadTest(List<File> files, AllCountModel allCountModel){
        this.files = files;
        this.allCountModel = allCountModel;
    }
    
    public void run() {
        WordsAnalysis wa = new WordsAnalysis();
        // 解析传入的全部文件
        for (File file : files) {
            try {
                // 解析文件内容
                wordsMap = wa.countWords(file, wordsMap);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        // 锁住共享数据（必须这么做，否则共享的数据会紊乱）
        synchronized (allCountModel) {
            // 更新线程总数
            allCountModel.setThreadCount(allCountModel.getThreadCount() - 1);
            // 更新结果集
            allCountModel.getLastMap().put(files, wordsMap);
        }
    }
}