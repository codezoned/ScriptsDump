import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
//To use above library don't forget to add json.org.jar file or Using the Maven artifact org.json:json
import java.io.*;
import java.net.URL;
import java.nio.charset.Charset;
//This json Helper is to parse Array of jsonObject
//Sample [{"Name":"Dracula","Languages":["en"]},{"Name":"White Fang","Languages":["en"]}]
public class jsonHelperArray {
//Take each character that is parse from url an convert to string
    private static String readAll(Reader rd) throws IOException {
        StringBuilder sb = new StringBuilder();
        int cp;
        while ((cp = rd.read()) != -1) {

            sb.append((char) cp);
        }
        return sb.toString();
    }
//Read URL
    public static JSONArray readJsonFromUrl(String url) throws IOException, JSONException {
        InputStream is = new URL(url).openStream();
        try {
            BufferedReader rd = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));
            String jsonText = readAll(rd);
            JSONArray json = new JSONArray(jsonText);
            return json;
        } finally {
            is.close();
        }
    }

    public static void main(String[] args) throws IOException, JSONException {
        JSONArray json = readJsonFromUrl("Link which give array of jsonObject");
        //Gives array of jsonObject
        System.out.println(json.toString);
        //Sample how to acces the particular key
        System.out.println(json.getJSONObject(0).get("Languages").toString());
        
    }
}
