package code.words;

import java.io.File;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AllCountModel {

    // 在运行的线程总数
    private int threadCount;

    // 每个线程处理的文件对应的结果集
    private HashMap<List<File>, Map<String, Integer>> lastMap = new HashMap<List<File>, Map<String, Integer>>();
    
    public int getThreadCount() {
        return threadCount;
    }
    public void setThreadCount(int threadCount) {
        this.threadCount = threadCount;
    }
    public HashMap<List<File>, Map<String, Integer>> getLastMap() {
        return lastMap;
    }
    public void setLastMap(HashMap<List<File>, Map<String, Integer>> lastMap) {
        this.lastMap = lastMap;
    }
}