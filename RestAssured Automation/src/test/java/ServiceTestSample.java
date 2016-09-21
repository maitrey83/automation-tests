/**
 * Created by maitreypatel on 9/21/2016.
 */

package com.overstock.webdev.SEOMetaData;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static com.jayway.restassured.RestAssured.given;
import static com.overstock.webdev.SEOMetaData.SEOMetaDataServiceCommon.*;
import static org.hamcrest.Matchers.notNullValue;

public class ServiceTestSample {

        private final int storeId;
        private final int deptId;
        private final int catId;
        private final int subCatId;

        public SEOMetaDataServiceTest() throws SQLException {
            storeId = getTaxonomyId(getQuery(), taxonomy.Store.getTaxonomyId());
            deptId = getTaxonomyId(getQuery(), taxonomy.Dept.getTaxonomyId());
            catId = getTaxonomyId(getQuery(), taxonomy.Cat.getTaxonomyId());
            subCatId = getTaxonomyId(getQuery(), taxonomy.Subcat.getTaxonomyId());
        }

        @Test
        public void test_Store_StatusCode() throws SQLException {
            int statusCode = given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), storeId, taxonomy.Store.getTaxonomyLevel())
                    .statusCode();

            Assert.assertTrue(statusCode == 200);
        }

        @Test
        public void test_Store_ResponseType() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), storeId, taxonomy.Store.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .header(CONTENT_TYPE, JSON_TYPE);
        }

        @Test
        public void test_Store_Response() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), storeId, taxonomy.Store.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .body(
                            "title", notNullValue(),
                            "description", notNullValue(),
                            "keywords", notNullValue(),
                            "h1", notNullValue()
                    );
        }

        @Test
        public void test_Dept_StatusCode() throws SQLException {
            int statusCode = given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), deptId, taxonomy.Dept.getTaxonomyLevel())
                    .statusCode();

            Assert.assertTrue(statusCode == 200);
        }

        @Test
        public void test_Dept_ResponseType() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), deptId, taxonomy.Dept.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .header(CONTENT_TYPE, JSON_TYPE);
        }

        @Test
        public void test_Dept_Response() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), deptId, taxonomy.Dept.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .body(
                            "title", notNullValue(),
                            "description", notNullValue(),
                            "keywords", notNullValue(),
                            "h1", notNullValue()
                    );
        }

        @Test
        public void test_Category_StatusCode() throws SQLException {
            int statusCode = given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), catId, taxonomy.Cat.getTaxonomyLevel())
                    .statusCode();

            Assert.assertTrue(statusCode == 200);
        }

        @Test
        public void test_Category_ResponseType() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), catId, taxonomy.Cat.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .header(CONTENT_TYPE, JSON_TYPE);
        }

        @Test
        public void test_Category_Response() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), catId, taxonomy.Cat.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .body(
                            "title", notNullValue(),
                            "description", notNullValue(),
                            "keywords", notNullValue(),
                            "h1", notNullValue()
                    );
        }

        @Test
        public void test_Subcategory_StatusCode() throws SQLException {
            int statusCode = given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), subCatId, taxonomy.Subcat.getTaxonomyLevel())
                    .statusCode();

            Assert.assertTrue(statusCode == 200);
        }

        @Test
        public void test_Subcategory_ResponseType() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), subCatId, taxonomy.Subcat.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .header(CONTENT_TYPE, JSON_TYPE);
        }

        @Test
        public void test_Subcategory_Response() throws SQLException {
            given().header(CONTENT_TYPE, JSON_TYPE)
                    .body(postJson())
                    .post(getServiceUrl(SERVICE_PATH_METADATA), subCatId, taxonomy.Subcat.getTaxonomyLevel())
                    .then()
                    .assertThat()
                    .body(
                            "title", notNullValue(),
                            "description", notNullValue(),
                            "keywords", notNullValue(),
                            "h1", notNullValue()
                    );
        }

        private String postJson() {
            return POSTJSON_METADATA;
        }

        private String getQuery() {
            return QUERY_TAXONOMY_VIEW;
        }

        public int getTaxonomyId(String query, String taxonomyTypeColumnName) throws SQLException {
            ResultSet resultSet;
            Statement statement = null;

            Connection conn = getDbConnection(getUrlDb(), getDbUser(), getDbPass());
            List<Integer> list = new ArrayList<Integer>();
            try {
                statement = conn.createStatement();
                resultSet = statement.executeQuery(String.format(query, taxonomyTypeColumnName));

                while (resultSet.next()) {
                    list.add(resultSet.getInt(taxonomyTypeColumnName));
                }
                Collections.shuffle(list);

            } catch (SQLException e) {
                e.printStackTrace();
            } finally {
                if (statement != null) {
                    statement.close();
                }
            }
            return list.get(0);
        }
    }
}
