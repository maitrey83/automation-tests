package com.overstock.webdev.SEOMetaData;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.sql.SQLException;

import static com.jayway.restassured.RestAssured.given;
import static com.overstock.webdev.SEOMetaData.SEOMetaDataServiceCommon.*;
import static org.hamcrest.Matchers.*;

public class SEOMetaDataRuleServiceTest {

    private final int pageTypeId;
    private final int ruleId;

    public SEOMetaDataRuleServiceTest() throws SQLException {
        pageTypeId = getId(getQuery_MetaDataPageType());
        ruleId = getId(getQuery_MetaDataRule());
    }

    @Test
    public void test_StatusCode_GetServiceWithID() throws SQLException {
        int statusCode = given().headers(CONTENT_TYPE, JSON_TYPE, AUTHORIZATION, getServiceAuthAlias())
                .get(getServiceUrl(SERVICE_PATH_GET_RULE_ID), ruleId)
                .statusCode();

        Assert.assertTrue(statusCode == 200, "Expected code was 200 but returned code: " + statusCode);
    }

    @Test
    public void test_ResponseType_GetServiceWithID() throws SQLException {
        given().headers(CONTENT_TYPE, JSON_TYPE, AUTHORIZATION, getServiceAuthAlias())
                .get(getServiceUrl(SERVICE_PATH_GET_RULE_ID), ruleId)
                .then()
                .assertThat()
                .header(CONTENT_TYPE, JSON_TYPE);
    }

    @Test
    public void test_ResponseJson_GetServiceWithID() throws SQLException {
        given().headers(CONTENT_TYPE, JSON_TYPE, AUTHORIZATION, getServiceAuthAlias())
                .get(getServiceUrl(SERVICE_PATH_GET_RULE_ID), ruleId)
                .then()
                .assertThat()
                .body(
                        "data", notNullValue(),
                        "data.size()", greaterThan(0),
                        "data.id", comparesEqualTo(ruleId),
                        "data.lastModifiedBy", notNullValue(),
                        "data._links.size()", greaterThan(0),
                        "data._links.self.href", notNullValue(),
                        "data._links.first.href", notNullValue(),
                        "data._links.first.title", notNullValue(),
                        "data.pageType", notNullValue()
                );
    }

    @Test
    public void test_StatusCode() throws SQLException {
        int statusCode = given().headers(CONTENT_TYPE, JSON_TYPE, AUTHORIZATION, getServiceAuthAlias())
                .get(getServiceUrl(SERVICE_PATH_GET_RULE_PAGETYPEID), pageTypeId)
                .statusCode();

        Assert.assertTrue(statusCode == 200, "Expected code was 200 but returned code: " + statusCode);
    }

    @Test
    public void test_ResponseType() throws SQLException {
        given().headers(CONTENT_TYPE, JSON_TYPE, AUTHORIZATION, getServiceAuthAlias())
                .get(getServiceUrl(SERVICE_PATH_GET_RULE_PAGETYPEID), pageTypeId)
                .then()
                .assertThat()
                .header(CONTENT_TYPE, JSON_TYPE);
    }

    @Test
    public void test_ResponseJson() throws SQLException {
        given().headers(CONTENT_TYPE, JSON_TYPE, AUTHORIZATION, getServiceAuthAlias())
                .get(getServiceUrl(SERVICE_PATH_GET_RULE_PAGETYPEID), pageTypeId)
                .then()
                .assertThat()
                .body("data", notNullValue(),
                        "data.size()", greaterThan(0),
                        "data.items.size()", greaterThan(0),
                        "data.items[0].any {it.key == 'description' }", is(true),
                        "data.items[0].any {it.key == 'version' }", is(true),
                        "data.items[0].tagRuleTemplates.template[0].pageType.id", comparesEqualTo(pageTypeId),
                        "data.items[0].pageType.id", comparesEqualTo(pageTypeId),
                        "data._links.size()", greaterThan(0),
                        "data._links.self.href", notNullValue(),
                        "data._links.first.href", notNullValue(),
                        "data._links.first.title", notNullValue());
    }

    private String postJson() {
        return POSTJSON_METADATA;
    }

    private String getQuery_MetaDataRule() {
        return QUERY_METADATA_RULE;
    }

    private String getQuery_MetaDataPageType() {
        return QUERY_METADATA_PAGE_TYPE;
    }
}