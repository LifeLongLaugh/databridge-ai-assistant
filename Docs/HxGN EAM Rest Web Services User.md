![](_page_0_Picture_0.jpeg)

# HxGN EAM Rest Web Services

Version 12.3 November 2025

![](_page_0_Picture_3.jpeg)

### **Copyright**

Copyright © 2025-2026 Hexagon AB and/or its subsidiaries and affiliates. All rights reserved.

This computer program, including software, icons, graphic symbols, documentation, file formats, and audio-visual displays; may be used only as pursuant to applicable software license agreement; contains confidential and proprietary information of Hexagon AB and/or third parties which is protected by patent, trademark, copyright law, trade secret law, and international treaty, and may not be provided or otherwise made available without proper authorization from Hexagon AB and/or its subsidiaries and affiliates.

### **U.S. Government Restricted Rights Legend**

Use, duplication, or disclosure by the government is subject to restrictions as set forth below. For civilian agencies: This was developed at private expense and is "restricted computer software" submitted with restricted rights in accordance with subparagraphs (a) through (d) of the Commercial Computer Software - Restricted Rights clause at 52.227-19 of the Federal Acquisition Regulations ("FAR") and its successors, and is unpublished and all rights are reserved under the copyright laws of the United States. For units of the Department of Defense ("DoD"): This is "commercial computer software" as defined at DFARS 252.227-7014 and the rights of the Government are as specified at DFARS 227.7202-3.

Unpublished - rights reserved under the copyright laws of the United States.

Hexagon PPM 305 Intergraph Way Madison, AL 35758

### **Documentation**

Documentation shall mean, whether in electronic or printed form, User's Guides, Installation Guides, Reference Guides, Administrator's Guides, Customization Guides, Programmer's Guides, Configuration Guides and Help Guides delivered with a particular software product.

### **Other Documentation**

Other Documentation shall mean, whether in electronic or printed form and delivered with software or on Intergraph Smart Support, SharePoint, or box.net, any documentation related to work processes, workflows, and best practices that is provided by Intergraph as guidance for using a software product.

### **Terms of Use**

- a. Use of a software product and Documentation is subject to the Software License Agreement ("SLA") delivered with the software product unless the Licensee has a valid signed license for this software product with Intergraph Corporation. If the Licensee has a valid signed license for this software product with Intergraph Corporation, the valid signed license shall take precedence and govern the use of this software product and Documentation. Subject to the terms contained within the applicable license agreement, Intergraph Corporation gives Licensee permission to print a reasonable number of copies of the Documentation as defined in the applicable license agreement and delivered with the software product for Licensee's internal, non-commercial use. The Documentation may not be printed for resale or redistribution.
- b. For use of Documentation or Other Documentation where end user does not receive a SLA or does not have a valid license agreement with Intergraph, Intergraph grants the Licensee a non-exclusive license to use the Documentation or Other Documentation for Licensee's internal non-commercial use. Intergraph Corporation gives Licensee permission to print a reasonable number of copies of Other Documentation for Licensee's internal, non-commercial use. The Other Documentation may not be printed for resale or redistribution. This license contained in this subsection b) may be terminated at any time and for any reason by Intergraph Corporation by giving written notice to Licensee.

### **Disclaimer of Warranties**

Except for any express warranties as may be stated in the SLA or separate license or separate terms and conditions, Intergraph Corporation disclaims any and all express or implied warranties including, but not limited to the implied warranties of merchantability and fitness for a particular purpose and nothing stated in, or implied by, this document or its contents shall be considered or deemed a modification or amendment of such disclaimer. Intergraph believes the information in this publication is accurate as of its publication date.

The information and the software discussed in this document are subject to change without notice and are subject to applicable technical product descriptions. Intergraph Corporation is not responsible for any error that may appear in this document.

The software, Documentation and Other Documentation discussed in this document are furnished under a license and may be used or copied only in accordance with the terms of this license. THE USER OF THE SOFTWARE IS EXPECTED TO MAKE THE FINAL EVALUATION AS TO THE USEFULNESS OF THE SOFTWARE IN HIS OWN ENVIRONMENT.

Intergraph is not responsible for the accuracy of delivered data including, but not limited to, catalog, reference and symbol data. Users should verify for themselves that the data is accurate and suitable for their project work.

### **Limitation of Damages**

IN NO EVENT WILL INTERGRAPH CORPORATION BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL INCIDENTAL, SPECIAL, OR PUNITIVE DAMAGES, INCLUDING BUT NOT LIMITED TO, LOSS OF USE OR PRODUCTION, LOSS OF REVENUE OR PROFIT, LOSS OF DATA, OR CLAIMS OF THIRD PARTIES, EVEN IF INTERGRAPH CORPORATION HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

UNDER NO CIRCUMSTANCES SHALL INTERGRAPH CORPORATION'S LIABILITY EXCEED THE AMOUNT THAT INTERGRAPH CORPORATION HAS BEEN PAID BY LICENSEE UNDER THIS AGREEMENT AT THE TIME THE CLAIM IS MADE. EXCEPT WHERE PROHIBITED BY APPLICABLE LAW, NO CLAIM, REGARDLESS OF FORM, ARISING OUT OF OR IN CONNECTION WITH THE SUBJECT MATTER OF THIS DOCUMENT MAY BE BROUGHT BY LICENSEE MORE THAN TWO (2) YEARS AFTER THE EVENT GIVING RISE TO THE CAUSE OF ACTION HAS OCCURRED.

IF UNDER THE LAW RULED APPLICABLE ANY PART OF THIS SECTION IS INVALID, THEN INTERGRAPH LIMITS ITS LIABILITY TO THE MAXIMUM EXTENT ALLOWED BY SAID LAW.

### **Export Controls**

Intergraph Corporation's commercial-off-the-shelf software products, customized software and/or third-party software, including any technical data related thereto ("Technical Data"), obtained from Intergraph Corporation, its subsidiaries or distributors, is subject to the export control laws and regulations of the United States of America. Diversion contrary to U.S. law is prohibited. To the extent prohibited by United States or other applicable laws, Intergraph Corporation software products, customized software, Technical Data, and/or third-party software, or any derivatives thereof, obtained from Intergraph Corporation, its subsidiaries or distributors must not be exported or re-exported, directly or indirectly (including via remote access) under the following circumstances:

- c. To Cuba, Iran, North Korea, the Crimean region of Ukraine, or Syria, or any national of these countries or territories.
- d. To any person or entity listed on any United States government denial list, including, but not limited to, the United States Department of Commerce Denied Persons, Entities, and Unverified Lists, the United States Department of Treasury Specially Designated Nationals List, and the United States Department of State Debarred List (https://build.export.gov/main/ecr/eg\_main\_023148).
- e. To any entity when Customer knows, or has reason to know, the end use of the software product, customized software, Technical Data and/or third-party software obtained from Intergraph Corporation, its subsidiaries or distributors is related to the design, development, production, or use of missiles, chemical, biological, or nuclear weapons, or other un-safeguarded or sensitive nuclear uses.
- f. To any entity when Customer knows, or has reason to know, that an illegal reshipment will take place.

Any questions regarding export/re-export of relevant Intergraph Corporation software product, customized software, Technical Data and/or third-party software obtained from Intergraph Corporation, its subsidiaries or distributors, should be addressed to PPM's Export Compliance Department, 305 Intergraph Way, Madison, Alabama 35758 USA or at exportcompliance@intergraph.com. Customer shall hold harmless and indemnify PPM and Hexagon Group Company for any causes of action, claims, costs, expenses and/or damages resulting to PPM or Hexagon Group Company from a breach by Customer.

### **Trademarks**

Intergraph®, the Intergraph logo®, Intergraph Smart®, SmartPlant®, SmartMarine, SmartSketch®, SmartPlant Cloud®, PDS®, FrameWorks®, I-Route, I-Export, ISOGEN®, SPOOLGEN, SupportManager®, SupportModeler®, SAPPHIRE®, TANK, PV Elite®, CADWorx®, CADWorx DraftPro®, GTSTRUDL®, and CAESAR II® are trademarks or registered trademarks of Intergraph Corporation or its affiliates, parents, subsidiaries. Hexagon and the Hexagon logo are registered trademarks of Hexagon AB or its subsidiaries. Microsoft and Windows are registered trademarks of Microsoft Corporation. MicroStation is a registered trademark of Bentley Systems, Inc. Other brands and product names are trademarks of their respective owners.

# HxGN EAM Rest Web Services

This document describes procedures for using the HxGN EAM Rest Web Services. It details the EAM Rest Web Services APIs and the format of EAM rest webservice messages. All the business components will be exposed as a set of Rest Web Services. The model for calling these components is a simple http request/response model with requests and responses defined in Open API 3 standard.

# Intended audience

This document is intended for the HxGN EAM system administrator.

# EAM rest web services

# Overview

EAM rest web services are defined in Open API 3 standard. It contains 4 major parts: URLs, Parameters, request body, and response.

## List of available EAM rest web service APIs

You can see the list of available EAM rest web service APIs by using {yourEAMApplicationServer}/ web/swagger/index.html in your browser.

# EAM configuration and setup to support web service operation and accessibility

Web service functionality, operation and accessibility are directly associated to how install parameters, users, user groups, and Dataspys are configured in EAM.

## Setting install parameters for EAM and web services

The following install parameters are all involved with logon and authentication. These parameters must be set in alignment (i.e. all STD). If these values are set to EXTERN, the customer must additionally provide configuration on the SSO Configuration screen.

| Installation Parameter | Description                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------------------|
| LGNCAL                 | Login Type for Portals. Set to STD for standard or EXTERN to<br>support SSO.                             |
| LGNCON                 | The login authentication method used for the EAM Connector<br>(web services) users. It has these values: |
|                        | Standard (STD) - Use the standard credentials defined on user<br>records within EAM.                     |
|                        | LDAP (LDAP) - Use the credential defined in the LDAP<br>provider configured for the EAM deployment.      |

|        | External (EXTERN) - Use an external authentication service<br>configured for the EAM deployment.    |  |  |  |
|--------|-----------------------------------------------------------------------------------------------------|--|--|--|
| LGNDBR | Logon type for Databridge logons                                                                    |  |  |  |
| LGNEAM | The default login authentication method used for EAM web<br>users. It has these values:             |  |  |  |
|        | Standard (STD) - Use the credential defined on user records<br>within EAM.                          |  |  |  |
|        | LDAP (LDAP) - Use the credential defined in the LDAP<br>provider configured for the EAM deployment. |  |  |  |
|        | External (EXTERN) - Use an external authentication service<br>configured for the EAM deployment.    |  |  |  |
| LGNMOB | Logon type for Mobile logons                                                                        |  |  |  |

**Note:** The SSO Configuration screen in EAM is used to support Single Sign-On authentication. Both WS-Trust and OIDC configuration will be supported using the parameters populated on this screen. A customer may choose to configure both WS-Trust and OIDC; these are not mutually exclusive. See [HxGN EAM SSO Configuration](https://docs.hexagonali.com/r/en-US/HxGN-EAM-SSO-Configuration/12.1.0.1/1355143) for more information.

# Configuring user groups

For the User Group of the user being referenced for web service requests, Interface Permissions must be configured. The Interface Permissions tab will update user group records with a list of Web Services, Transaction Types, and Web Service Prompt screens to which they have access and their permissions for each of these (Query, Insert, Update, Delete).

# Configuring user setup

The user (user record) that will be referenced for API requests must have the Connector checkbox selected in the HxGN EAM Products section of the User record.

# Configuring Dataspys

EAM web services access the default Dataspy for the associated screen or tab. All necessary fields for verification or function by the web service must be included in the default Dataspy.

# EAM rest web services URLs and actions

# Main rest web services (corresponding to EAM record view)

![](_page_6_Picture_2.jpeg)

**Figure 1** 

Figure 1 is a sample main EAM rest web services URL and corresponding rest web service actions.

- 1 is a POST action for get default webservices.
- 2 is a POST action to add a single record.
- 3 is a PUT action to update a single record.
- 4 is a GET action, it returns a collection of data records. We will call this **Get Collection** in this document.
- 5 is a GET action to return a single record.
- 6 is the DELETE action to delete a single record.
- 7 is the PATCH action to update selected data fields.

In 5, 6 and 7, there is a {id} parameter. {id} should be the unique id to identify the entity/screen. Normally it will be entity code plus organization code separated by the # symbol. In the top section of every EAM Rest Web service API document (also called Swagger API), a sample {id} will provided.

## Child rest web services (corresponding to EAM tabs)

Figure 2 is a sample set of EAM rest web services URLs and corresponding actions. They are similar to the main rest web services. For 1, 2, and 3, the only differences from the main rest web services are the URLs. For 4, 5, 6, and 7, there is one additional parameter {parentid}. Just like {id}, {parented} is the parent entity key. Both { parentid } and {id} samples will be in the top section of every EAM Rest Web service API document.

**Figure 2** 

# EAM rest web service parameters

## Header parameters

This table describes EAM rest web service header parameters. The Actions column in the table lists the rest web service actions applicable to the header parameter.

| Header Parameter Name | Description                                                                                                                                                                                 | Actions        |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| tenant                | Tenant of EAM application                                                                                                                                                                   | All            |
| Role                  | role of EAM user                                                                                                                                                                            | All            |
| Organization          | Default organization of EAM user                                                                                                                                                            | All            |
| apiversion            | Version of an EAM rest web service. It is an<br>optional header parameter. If the version is not<br>specified or the specified version is not<br>available, a default version will be used. | All            |
| keepsession           | It has a value true/false. Default is false. If it is<br>true, a session id will be returned in the<br>response and can be used later on.                                                   | All            |
| sessionid             | EAM session id. If a valid session provided, it<br>will be used to access EAN.                                                                                                              | All            |
| clonedscreen          | Specify EAM close screen name.                                                                                                                                                              | Get Collection |
| authenticationmode    | If "internal" is used as authentication mode,<br>value for installation parameter "LGNCON" will<br>be ignored.                                                                              | All            |

Note: EAM REST APIs can support persistent HTTP connections by leveraging keepsession and sessionid.

## Path parameters

This table describes EAM rest web service path parameters

| Path Parameter Name | Description                                                                                                                     | Actions                    |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| parentid            | The unique id to identify the parent<br>entity/screen. Normally it will be entity code<br>plus organization code separated by # | Get, Get collection, Patch |

| Path Parameter Name | Description                                                                                                                                                                                                                                                         | Actions    |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
|                     | symbol.<br>Normally Organization should be after<br>the last #.                                                                                                                                                                                                     |            |
| id                  | The unique id<br>to identify the entity/screen<br>(together with parentid if it is a child<br>entity/screen). Normally it will be entity code<br>plus organization code separated by<br>the<br>#<br>symbol.<br>Normally Organization should be after<br>the last #. | Get, Patch |

# EAM rest web service request body

Unless SOAP requests, there are no request bodies for Get, Get Collection, and Delete rest web services per Open API standard. Only Post, Put, and Patch web services have request bodies. All EAM rest web services APIs are defined in Open API 3. To see any available EAM rest web service samples, see the following steps.

## Steps to see available EAM rest web service samples

- **1** Type in [{youeamapplicationserver}/web/swagger/index.html](http://youeamapplicationserver.com/web/swagger/index.html)
- **2** From the menu (the left panel), select an interested rest web service, all available actions for the selected rest web service will display on Web service Panel (the right panel).There is one "Deprecated" section in the menu. Deprecated rest webservices should not be used in any new development and they are in the menu for backward compatibility purpose only. Deprecated rest webservices may be removed for future releases.
- **3** Select any available action, the related parameters and request body will display (see Figures 3, 4, and 5).

![](_page_10_Figure_0.jpeg)

**Figure 3 – available actions**

![](_page_10_Figure_2.jpeg)

### **Figure 4 – header parameter**

**Figure 5 – post request body**

# EAM rest web service response

EAM rest web services provide 4 different response code. 200, 400, 404, and 500.

## EAM rest web service general response structure

This is the standard response to indicate the transaction was successful. Figure 6 is a sample response data.

**Figure 6 – EAM response structure** 

There are 3 parts of the response.

### • ErrorAlert

If this element is not null, it indicates something is wrong in the request and the message will tell what is wrong in the request.

### • ConfirmationAlert

If this element is not null, it indicates the request is OK, however additional information is needed to confirm the request. The message will be a question to tell users to confirm the request.

### • Result

If this element is not null, it indicates the request is successful and data requested is inside ResultData element.

- i. ResultData element will be different for different entities/screens and the structure of ResultData will be specified in the corresponding swagger API json.
- ii. InfoAlert

This is a successful message to indicate the transaction was successful.

### iii. WarningAlert

If it is not null, it indicates the transaction was successful, but there are some warnings.

### iv. SessionID

SessionID will have a value if the keepsession header parameter is set to true. It is the session id that can be used in later request.

# 200 response

When EAM rest web service returns, ErrorAlert and ConfirmationAlert will be null.

# 400 response

In this case, one of ErrorAlert or ConfirmationAlert will not be null and Result will be null.

# 404 response

This is the standard resource not found error. No real response message will be returned.

# 500 response

This indicates some unexpected internal error happened.

# Trying/testing EAM rest web services

# Get ready to try/test EAM rest web services

- **1** Type in [{yourEAMApplicationserver}/web/swagger/index.html](http://youeamapplicationserver.com/web/swagger/index.html)
- **2** From the menu (the left panel), select an interested rest web service, all available actions for the selected rest web service will display in the Web service Panel (the right panel). See Figure 7.
- **3** Change the server variable {eamhost} value to your EAM application server host if it is different. The Computed URL will change automatically as well. See Figure 8.
- **4** Click the Authorize button and a popup will allow you to enter your EAM username/password for basic Auth or API key or bearer token for OIDC security (for OIDC security, follow HxGN EAM OpenID Connect Guide to get OIDC/bearer token). See Figure 9.
- **5** In the popup, enter your EAM username/password and then click Authorize button and then click Close button. See Figure 10.

![](_page_14_Picture_7.jpeg)

**Figure 7 – selected EAM rest web service**

![](_page_15_Picture_1.jpeg)

![](_page_15_Picture_3.jpeg)

![](_page_16_Picture_0.jpeg)

# Run EAM rest web services

Main EAM rest web services (Record View)

### POST

**1** Select POST action from the available actions and then click on Try It Out button. See Figures 11 and 12.

![](_page_17_Picture_0.jpeg)

- **2** Fill in the correspond values in Header Parameters. **See Header Parameters** section for detail.
- **3** Fill in the required request body. By default, a sample request body content is provided. See Figure 13.

![](_page_18_Picture_0.jpeg)

**4** Click Execute to run the web service. A response will be provided in the response section. See Figure 14.

```
Figure 14 – EAM Response
```

### PUT

The steps to run the PUT action is the same as the POST action. The PUT action will replace existing data with data provided in the request. Any fields that are not present in the request will be blanked out. The recordid field must have a valid value, otherwise the system will raise an error message "This record has been modified by another user. Reload the record to view and/or edit the updated record."

![](_page_19_Picture_0.jpeg)

## PATCH

The steps to run the PATCH action are the same as the PUT action. The difference is that it has an additional {id} parameter. See Figure 15(B). PATCH is used to update selected data fields. Unlike PUT, fields that are not present in the request will not be updated. If the recordid field is provided with a value, the value must match with the database value. If the recordid field value does not match with the database value, an error message will display "This record has been modified by another user. Reload the record to view and/or edit the updated record."

![](_page_19_Picture_3.jpeg)

### GET Collection

- **1** Select the GET collection action from the available action list and then click Try It Out.
- **2** Enter the corresponding values in Header Parameters. **See Header Parameters** section for detail.
- **3** If you run against a cloned screen, provide the cloned screen name in the clonedscreen header parameter. See Figure 16.

![](_page_20_Picture_5.jpeg)

**4** Click Execute to run the web service. A response will be provided in the response section. See Figure 17.

**Figure 17 – Get collection response**

## GET

The steps to execute the GET web service are the same as the GET collection. The only difference is that there is one Path Parameter id available to allow you to provide the entity key id. See the top section of the selected EAM API for a sample value for the id field. See Figures 18 and 19 for request parameters and response samples.

![](_page_21_Picture_4.jpeg)

**Figure 18 – GET action parameters sample**

**Figure 19 – GET action response sample**

### DELETE

- **1** Select the DELETE action from the available action list and then click on Try It Out button.
- **2** Enter the corresponding values in the Header Parameters. **See Header Parameters** section for detail.
- **3** Click Execute to run the web service. A response will be provided in the response section. See Figures 20 and 21 for request parameters and response samples.

![](_page_23_Figure_0.jpeg)

**Figure 20 – DELETE action parameters sample.**

**Figure 21 -DELETE action response sample**

## Get default

Get default web services, like Grid web services, are special. The action is POST. It is actually performing a get request. The reason for using POST is that Open API specifications do not allow for a request body. Below is one sample.

{

```
 "ORGANIZATIONID": { 
 "ORGANIZATIONCODE": "ORG1" 
 } 
}
```

# Child EAM rest web services(tabs)

## POST

Same as POST in Main EAM Web services.

## PUT

Same as PUT in Main EAM Web services.

### PATCH

Same as PATCH in Main EAM Web services with an additional parameter {parentid}. See Figure 22.

| PATCH /workorde                               | rs/{parentid}/activities/{id} Partially Update WorkOrder Activity |
|-----------------------------------------------|-------------------------------------------------------------------|
| Parameters                                    |                                                                   |
| Name                                          | Description                                                       |
| tenant * required string (header)             | tenant                                                            |
| role<br>string<br>(header)                    | role                                                              |
| organization * required<br>string<br>(header) | organization                                                      |
| apiversion<br>string<br>(header)              | apiversion                                                        |
| sessionid<br>string<br>(header)               | sessionid                                                         |
| keepsession<br>string<br>(header)             | keepsession                                                       |
| parentid * required<br>string<br>(path)       | parentid                                                          |
| <pre>id * required string (path)</pre>        | id                                                                |
|                                               |                                                                   |

## GET Collection

**Figure 22**

Same as GET Collection in Main EAM Web services. The only difference is there is one new Path Parameter parentid available to provide the parent entity key ID value. See the top section of the selected EAM API for a sample value of the parentid field value. See Figure 23 to see a sample of request parameters.

### GET

Same as GET in Main EAM Web services. The only difference is there is one new Path Parameter parentid available to provide the parent entity key ID value. See the top section of the selected EAM API for a sample value of the parentid field value. See Figure 24 to see a sample of request parameters.

![](_page_26_Picture_4.jpeg)

```
Figure 24 – Child GET request parameters sample
```

### DELETE

Same as DELETE in Main EAM Web services. The only difference is there is one new Path Parameter parentid available to provide the parent entity key ID value. See the top section of the selected EAM API for a sample value of the parentid field value. See Figure 25 to see a sample of request parameters.

![](_page_27_Picture_3.jpeg)

**Figure 25 – Child DELETE request parameters sample**

## Get Default

Same as Get Default in Main EAM Web services. The only difference is there is one new Path Parameter parentid available to provide parent entity key ID value.

# Grid web services

Grid web services are special. The action is POST. It is actually performing a get request. The reason for using POST is that Open API specifications do not allow for a request body. Below is sample grid request for the alert grid.

```
{ 
 "GRID_TYPE": {
```

```
"TYPE": "LIST"
    }, 
    "GRID": { 
           "CURRENT_TAB_NAME": "LST", 
           "GRID_ID": "2489", 
           "GRID_NAME": "BSALRT", 
           "USER_FUNCTION_NAME": "BSALRT"
    }, 
    "DATASPY": { 
           "DATASPY_ID": "2462"
    }, 
    "ADDON_FILTER": { 
           "ALIAS_NAME": "alertcode", 
           "OPERATOR": "BEGINS", 
           "VALUE": "00001"
    }, 
    "REQUEST_TYPE": "LIST.HEAD_DATA.STORED"
 }
```

## CSV Grid Rest web service

The CSV Grid web service will enable users to retrieve the data content of the specified grid in CSV format. This result set includes the actual returned data, the metadata, the boiler text of each grid column, the database column name, and the database data type of each column.

- 1. CSV grid rest webservice swagger URL csvgrids (/axis/restservices/csvgrids)
- 2. CSV grid request will be same as grids webservice(/axis/restservices/grids). See Figure 26.

Figure 26 – CSV Grid sample Request

3. CSV response will be flat. The grid content will be just csv format string (in ResultData element), See Figure 27.

Figure 27 – Sample CSV Grid Response

### 4. When grid content is saved in a csv file. It looks like below:

|   | А               | В                     | С                  | D              | Е      | F         |
|---|-----------------|-----------------------|--------------------|----------------|--------|-----------|
| 1 | 10000           | O1                    | 6/13/2024 15:56    | A A1 -V        |        |           |
| 2 | 10001           | O1                    | 6/13/2024 16:00    | wo 1           |        |           |
| 3 |                 |                       |                    |                |        |           |
| 4 | GRIDLABEL       | CURRENTCURSORPOSITION | NEXTCURSORPOSITION | RECORDS        | GRIDID | DATASPYID |
| 5 | List View       | 2                     |                    | 2              | 100013 | 100015    |
| 6 | work order code | WO Organization       | Date reported      | WO description |        |           |
| 7 | evt_code        | evt_org               | evt_reported       | evt_desc       |        |           |
| 8 | VARCHAR         | VARCHAR               | DATETIME           | MIXVARCHAR     |        |           |
| _ |                 |                       |                    |                |        |           |

Figure 28 - Data in CSV format

### 5. Explanation of CSV grid content

- a. The first two rows are actual grid data returned from EAM. We can call these two rows as the *grid field data* section.
- b. The empty line/record encountered (line#3 in this example) means that the EAM grid data record ends here.
- c. The first line (line#4 in this example) after the empty line (line#3 in this example) is grid meta data field name and the second line (line#5 in this example) is the grid meta data field value. These two lines would be the *meta data* section. In this example:
  - i. GRIDLABEL = List View. The value can be "Work Order", "Alerts", etc. depending on the grid definition.
  - ii. CURRENTCURSORPOSITION = 2.
  - iii. NEXTCURSORPOSITION = nothing. This means all the records have been retrieved in this grid call, there are no more records to retrieve. If NEXTCURSORPOSITION = 51, this would mean there are more records to retrieve and you would retrieve data from cursor position 51 for your next grid call.
  - iv. RECORDS =2. This means that this call retrieved a total of 2 data records for the grid.
  - v. GRIDID = 100013. This is the grid ID used in this grid call.
  - vi. DATASPYID= 100013. This is the data spy ID used in this grid call.
- d. We will call the remaining rows as the *field meta data* section.
  - i. Line#6 (third line from the empty line) is the field label/description.

- ii. Line#7 (fourth line from the empty line) is the field alias.
- iii. Line#8 (fifth line from the empty line) is the field data type.
- iv. In this sample, the field data would be like below:

| Field Label        | Work Order | WO           | Date      | WO          |
|--------------------|------------|--------------|-----------|-------------|
|                    | Code       | Organization | Reported  | Description |
| Field Data<br>Type | VARCHAR    | VARCHAR      | DATETIME  | MIXVARCHAR  |
|                    |            |              | 6/13/2024 |             |
| Field Data         | 10000      | O1           | 15:56     | A A1 -V     |
|                    |            |              | 6/13/2024 |             |
|                    | 10001      | O1           | 16:00     | wo 1        |

- 6. Processing the CSV grid data. The following is one of the ways to process CSV grid data.
  - a. Save the value of ResultData element from the CSV grid response into one text file with extension .csv
  - b. Read the CSV file line by line using any tool you prefer. After encountering the empty line, process the next two lines as meta data and you can save them somewhere for future use.
  - c. After processing the meta data section, process the next 3 lines as field meta data. You may need to create a data object to retain the data mappings. Be sure to maintain the column sequence.
  - d. Now, read the CSV file again from the start and process each row from the field data section as below:
    - i. The first column in each row will match with the first column of your field meta data mapping.
    - ii. Based on the corresponding data type of each column, you may process your data to present it in a way you like to present information to your end users.

# Date fields in EAM rest web services

# Sample date field data

```
"DATEWORKED": 
{
   "YEAR": 1609477200000,
   "MONTH": 12,
   "DAY": 21,
   "HOUR": 0,
   "MINUTE": 0,
   "SECOND": 0,
   "SUBSECOND": 0,
   "TIMEZONE": "-0500",
   "qualifier": "OTHER"
}
```

# Year value

The year value in EAM data field is the EPOCH time value of start of a given year in the specified time zone in milliseconds. No time zone conversion is required. You might write your routine to get the year value. See below tool to get year value without any programs.

# Epoch time year value tool

- 1. Go to website<https://www.epochconverter.com/>
- 2. Scroll to *Epoch dates for the start and end of the year/month/day* Section
- 3. Select Year radio button
- 4. Enter any date of the year of your selection
- 5. Select Local time
- 6. Click on Convert button

- 7. The year value will be Epoch time value for start of year times 1000.
- 8. In Figure 29 sample, the year value will be 1609477200\*1000 = 1609477200000

![](_page_32_Figure_2.jpeg)

# Installation parameters

Many install parameters are delivered with EAM. Install parameters represent configuration, features, and functional settings clients may use to customize EAM to their operational business practices. Install parameters are applied at the enterprise level and all users for a client will experience the same system behavior, settings, and data requirements based on their enablement or defined value.

Specifically for REST APIs, the following install parameters will affect usage when submitting a request or receiving a response. This list is presented in alphabetical order.

## REST Behavior for Comments

The install parameter **RSCLROWS** determines the number of rows of data returned by GET Collection webservices. The response of the GET Collection operation for all screens will behave as expected, based on the **RSCLROWS** install parameter. However, for all Comment tabs, there is no grid present on the screen, so the GET Collection response is handled differently. The response for Comment tabs will not include any metadata like the other screen responses, it will only return a collection of records.

### For example:

• The *Part Comments GET Collection* response will return a COMMENT array. The **RSCLROWS** install parameter is not considered.

• In contrast, the *GET Collection* response for other screens (e.g., Lot) will return a DATARECORD array and will consider the **RSCLROWS** install parameter.

This applies to the following REST APIs;

- Asset Comments
- Call Center Comments
- Case Management Comments
- Flex Python Event Comments
- Notebook Comments
- Part Comments
- Position Comments
- Purchase Order Comment
- Quotation Comments
- Requisition Comment
- Supplier Comment
- System Comments
- Task Plan Comments
- Work Order Comments

## REST DATETIME Field Year Format

Beginning with EAM 12.3 the install parameter **RSYRYYYY** will control the year format in DATETIME fields used in REST API requests and responses. Set to **YES** to represent the year as a standard 4-digit calendar year (e.g., 2025). Set to **NO** to represent the year as epoch time in milliseconds (e.g., 1735669800000).

- Existing API clients sending or expecting year values in epoch milliseconds must explicitly set RSYRYYYY = NO (this is the default value) to preserve compatibility.
- If the parameter is unset (empty), it will be considered as "NO" which is the default value for this install Parameter.
- This parameter only applies to API fields that explicitly represent year-based data.
- Clients must ensure request payloads conform to the selected format.
- The same format is inherent in both API requests and returned in responses. Mixed formats are not supported.

# Technology sustenance

It is the ongoing strategy of HxGN EAM to maintain and improve existing technologies and product offerings throughout their lifecycle, ensuring they remain functional, efficient, and relevant over time.

### Entity schemas

For REST APIs, the default REST web service returns the default values for that entity in the API response. The default schema acts as a form of metadata and may be used for clarifying the arrangement of exchanged data.

Prior to EAM v12.3, the Positions and Systems REST APIs were leveraging the assetdefault schema for returned responses. With the release of EAM v12.3, new default entity schemas for Positions and Systems have been introduced. To maintain operability for SOAP, similar default entity schemas have been implemented for Positions and Systems (MP0310\_GetPositionEquipmentDefault\_001\_Result, MP0315\_GetSystemEquipmentDefault\_001\_Result).

# Swagger documentation

Beginning with EAM version 12.2, a drop-down with four options is delivered in Swagger for **POST**, **PUT** and **PATCH** operations for the top 24 APIs.

**POST, PUT** operations will have three options whereas **PATCH** will have four options in the drop-down.

The four options are:

- **1** An example with sample fields
- **2** An example with required fields
- **3** An example for patch. This is for patch only and not for post or put.
- **4** All available fields

### POST and PUT operations with options

Figure 30 - **POST** Operation with three options

![](_page_35_Picture_8.jpeg)

Figure 31 - **PUT** operation with three options

## PATCH Operation with options

Figure 32 - **PATCH** Operation with four options

## Details on drop-down options

**1.** When selecting the **"An example with required fields"** option for any of the three operations **(POST, PUT, or PATCH)**, the request will include the minimum number of fields with sample values, as shown in Figure 33.

Figure 33

![](_page_37_Picture_3.jpeg)

**2.** When selecting the **"An example with sample fields"** option, the request will contain a larger number of fields with sample values, as shown in Figure 34.

Figure 34

![](_page_37_Picture_6.jpeg)

**3.** On selecting the **"All available fields"** option, the request will contain all available fields with their default values, as shown in Figure 35.

Figure 35

This option name will appear as **"All available fields"** until you click the **"Try it out"** button. After clicking the **"Try it out"** button, the option name will change to **"[Modified value]"**. however, the request itself will remain unchanged before and after this action, only the label will be updated as shown in Figure 36.

Figure 36

![](_page_38_Picture_5.jpeg)

**4.** When selecting the **"An example for patch. This is for patch only not for post and put."** option (available only for PATCH operations), the request will contain a single field for updating, as shown in Figure 37.

Figure 37

![](_page_39_Picture_2.jpeg)
