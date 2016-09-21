/**
 * Created by maitreypatel on 9/21/2016.
 */

package com.overstock.webdev.SEOMetaData;

import com.overstock.framework.Bordello;
import com.overstock.framework.Config;

import java.sql.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CommonServiceTest {
        // ostk-config strings
        private static final String DB_CONNECTION_STRING = "com.overstock.webdev.SEOMetaData.dbUrl";
        private static final String SERVICE_BASE_URL = "com.overstock.webdev.SEOMetaData.Service.URL";
        private static final String USER_SEOMETADATA_DB = "com.overstock.webdev.SEOMetaData.dbAuthUser";
        private static final String PASS_SEOMETADATA_DB = "com.overstock.webdev.SEOMetaData.dbAuthPass";
        private static final String DB_USER = "com.overstock.webdev.dbAuthUser";
        private static final String DB_PASS = "com.overstock.webdev.dbAuthPass";
        private static final String SERVICE_CREDENTIAL = "com.overstock.webdev.SEOMetaData.Service.AuthAlias";

        static final String CONTENT_TYPE = "Content-Type";
        static final String JSON_TYPE = "application/json";
        static final String AUTHORIZATION = "Authorization";

        // data base queries
        static final String QUERY_TAXONOMY_VIEW = "select distinct %s  from taxonomy_view";
        static final String QUERY_METADATA_PAGE_TYPE = "select distinct id  from metadata_page_type";
        static final String QUERY_METADATA_TEMPLATE = "select distinct id  from metadata_template";
        static final String QUERY_METADATA_RULE = "select distinct id  from metadata_rule";

        // service path and json
        static final String SERVICE_PATH_METADATA = "/metadata?taxonomyId={0}&taxonomyLevel={1}";
        static final String POSTJSON_METADATA = "{\"objectType\":\"TaxonomyPageMetaDataContext\",\"childTaxonomies\": null, \"currentTaxonomy\": \"DAYBED COVERS\", \"allRefinements\": null}";
        static final String SERVICE_PATH_GET_RULE_PAGETYPEID = "/workspace/rules?pageTypeId={0}";
        static final String SERVICE_PATH_GET_RULE_ID = "/workspace/rules/{0}";
        static final String POSTJSON_METADATA_RULE = "";
        static final String SERVICE_PATH_GET_TEMPLATE_ID = "/workspace/templates/{0}";
        static final String SERVICE_PATH_GET_TEMPLATE_PAGETYPEID = "/workspace/templates?pageTypeId={0}";
        static final String POSTJSON_METADATA_TEMPLATE = "";

        protected static String getUrlDb() {
            return Bordello.get(Config.class).getString(DB_CONNECTION_STRING);
        }

        private static String getDbUser_SeoMetaData() {
            return Bordello.get(Config.class).getString(USER_SEOMETADATA_DB);
        }

        private static String getDbPass_SeoMetaData() {
            return Bordello.get(Config.class).getString(PASS_SEOMETADATA_DB);
        }

        protected static String getDbUser() {
            return Bordello.get(Config.class).getString(DB_USER);
        }

        protected static String getDbPass() {
            return Bordello.get(Config.class).getString(DB_PASS);
        }

        protected static String getServiceAuthAlias() {
            return Bordello.get(Config.class).getString(SERVICE_CREDENTIAL);
        }

        protected static String getServiceUrl(String path) {
            return Bordello.get(Config.class).getString(SERVICE_BASE_URL) + path;
        }

        protected enum taxonomy {
            Store("sto_id", "STORE"),
            Dept("stl_id", "DEPARTMENT"),
            Cat("sct_sub_id", "CATEGORY"),
            Subcat("sst_id", "SUBCATEGORY");

            private final String taxonomyId;
            private final String taxonomyLevel;

            taxonomy(String column, String level) {
                taxonomyId = column;
                taxonomyLevel = level;
            }

            protected String getTaxonomyId() {
                return taxonomyId;
            }

            protected String getTaxonomyLevel() {
                return taxonomyLevel;
            }
        }

        protected static Connection getDbConnection(String urlDb, String dbUser, String dbPass) throws SQLException {
            return DriverManager.getConnection(urlDb, dbUser, dbPass);
        }

        protected static int getId(String query, String... columnName) throws SQLException {
            ResultSet resultSet;
            Statement statement = null;

            Connection conn = getDbConnection(getUrlDb(), getDbUser_SeoMetaData(), getDbPass_SeoMetaData());
            List<Integer> list = new ArrayList<Integer>();
            try {
                statement = conn.createStatement();
                resultSet = statement.executeQuery(String.format(query, columnName));

                while (resultSet.next()) {
                    list.add(resultSet.getInt("id"));
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

