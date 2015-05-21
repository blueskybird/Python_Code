import java.util.Map;
import java.util.HashMap;

public class TestMap {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map<String, Integer> testMap = new HashMap<String, Integer>();
		mapEdit(testMap);
		for(String key:testMap.keySet()){
			System.out.println(key+testMap.get(key));
		}
	}
	
	public static void mapEdit(Map<String, Integer> wordMap){
		Map<String, Integer> wordsMap = new HashMap<String, Integer>();
		wordsMap=wordMap;
		wordsMap.put("nihao",1);
		wordsMap.put("hi",2);
		wordsMap.put("hello",3);
	}

}
