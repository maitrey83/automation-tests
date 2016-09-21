import com.jayway.restassured.http.ContentType;
import org.junit.Test;
import static com.jayway.restassured.RestAssured.*;
import static com.jayway.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;
import static org.junit.Assert.*;

/**
 * Created by maitreypatel on 9/20/2016.
 */
public class FirstTestRestAssured {
    String baseUrls = "http://erex01.latte.test.ostk.com";
    String path = "/content/directory/4";
    @Test
    public void myFirstRestAssuredTest()
    {
        String url = baseUrls + path;
        int statuscode = given()
        .get(url)
            .statusCode();
        assertTrue(statuscode == 200);
    }
}
