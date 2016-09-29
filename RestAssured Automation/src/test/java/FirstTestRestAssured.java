import com.jayway.restassured.http.ContentType;
import com.jayway.restassured.path.json.JsonPath;
import com.jayway.restassured.response.Response;
import oracle.jrockit.jfr.StringConstantPool;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static com.jayway.restassured.RestAssured.*;
import static com.jayway.restassured.matcher.RestAssuredMatchers.*;
import static com.jayway.restassured.path.json.JsonPath.from;
import static org.hamcrest.Matchers.*;
import static org.junit.Assert.*;

/**
 * Created by maitreypatel on 9/20/2016.
 */
public class FirstTestRestAssured {
    String baseUrls = "http://erex01.latte.test.ostk.com";
    String path = "/content/directory/4";


    @Test
    public void myFirstRestAssuredTest() {
        String url = baseUrls + path;
        int statuscode = given()
                .get(url)
                .statusCode();
        assertTrue(statuscode == 200);
    }

    @Test
    public void testResponeType() {
        String url = baseUrls + path;
        Response json = given()
                .get(url)
                .then()
                .contentType(ContentType.JSON)
                .extract()
                .response();
        String jsonAsString = json.asString();
        // /String status = respone.path("leaf");
        //JsonPath jsonpath = new JsonPath(json).setRoot("Id");
        //List<String> id = jsonpath.get("id");
        //System.out.println(jsonpath);
        //System.out.println(json);
        //System.out.println(jsonAsString);
        int id = json.path("id");
        int parentId = json.path("parentId");
        boolean leaf = json.path("leaf");
        String description = json.path("description");
        String imageUrl = json.path("imageUrl");
        String landingPageUrl = json.path("landingPageUrl");
        List<Response> ancestors = json.path("ancestors");
        List<Response> featuredContent = json.path("featuredContent");
        List<Response> contentList = json.path("contentList");
        Map<Response, String> contentpaging = json.path("contentPaging");
        //String ancestorsAsString = ancestors.toString();
        int i;
        for (i = 0; i < featuredContent.size(); i++) {
            Map<String, String> a = (Map<String, String>) featuredContent.get(i);
         //   System.out.println(a);
            for (int p=i; p<a.size()-1;p++   )
            System.out.println((((java.util.HashMap)featuredContent.get(p)).entrySet().toArray()[p]).toString());
        }
        /*System.out.println("**********");
        int j;
        for (j = 0; j < contentList.size(); j++) {
            System.out.println(contentList.get(j));
        }
        System.out.println("**********");
        int k;
        for (k = 0; k < contentpaging.size(); k++) {
            System.out.println(contentpaging.get(k));
        }*/
    }


    @Test
    public void testResponeTypeWithForEachLoop() {
        String url = baseUrls + path;
        Response json = given()
                .get(url)
                .then()
                .contentType(ContentType.JSON)
                .extract()
                .response();
        String jsonAsString = json.asString();
        // /String status = respone.path("leaf");
        //JsonPath jsonpath = new JsonPath(json).setRoot("Id");
        //List<String> id = jsonpath.get("id");
        //System.out.println(jsonpath);
        //System.out.println(json);
        //System.out.println(jsonAsString);
        int id = json.path("id");
        int parentId = json.path("parentId");
        boolean leaf = json.path("leaf");
        String description = json.path("description");
        String imageUrl = json.path("imageUrl");
        String landingPageUrl = json.path("landingPageUrl");
        List<Response> ancestors = json.path("ancestors");
        List<Response> featuredContent = json.path("featuredContent");
        List<Response> contentList = json.path("contentList");
        Map<Response, String> contentpaging = json.path("contentPaging");

        for (Response content : featuredContent){
            System.out.println(content);
        }
    }
}