import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
//To use above library don't forget to add json.org.jar file or Using the Maven artifact org.json:json
import java.io.*;
import java.net.URL;
import java.nio.charset.Charset;
//This json Helper is to parse JsonObject and its inside objects and Jsonarray inner to it
//Sample {"Name":"Dracula","Languages":["en"]},{"Name":"White Fang","Languages":["en"]}
public class jsonHelper {
//Take each character that is parse from url an convert to string
    private static String readAll(Reader rd) throws IOException {
        StringBuilder sb = new StringBuilder();
        int cp;
        while ((cp = rd.read()) != -1) {

            sb.append((char) cp);
        }
        return sb.toString();
    }
//Read url
    public static JSONObject readJsonFromUrl(String url) throws IOException, JSONException {
        InputStream is = new URL(url).openStream();
        try {
            BufferedReader rd = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));
            String jsonText = readAll(rd);
            JSONObject json = new JSONObject(jsonText);
            return json;
        } finally {
            is.close();
        }
    }

    public static void main(String[] args) throws IOException, JSONException {
        JSONObject json = readJsonFromUrl("Link that give json");
        //To retrieve full json
        System.out.println(json.toString);
        //to retrieve as per key
        System.out.println(json.get("key").toString);
    }
}
