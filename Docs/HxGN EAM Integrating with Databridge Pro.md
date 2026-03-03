![](_page_0_Picture_0.jpeg)

## HxGN EAM Integrating with Databridge Pro

Version 12.3.0.2 March 2026

![](_page_0_Picture_3.jpeg)

### **Copyright**

Copyright © 2026-2027 Hexagon AB and/or its subsidiaries and affiliates. All rights reserved.

This computer program, including software, icons, graphic symbols, documentation, file formats, and audio-visual displays; may be used only as pursuant to applicable software license agreement; contains confidential and proprietary information of Hexagon AB and/or third parties which is protected by patent, trademark, copyright law, trade secret law, and international treaty, and may not be provided or otherwise made available without proper authorization from Hexagon AB and/or its subsidiaries and affiliates.

### **U.S. Government Restricted Rights Legend**

Use, duplication, or disclosure by the government is subject to restrictions as set forth below. For civilian agencies: This was developed at private expense and is "restricted computer software" submitted with restricted rights in accordance with subparagraphs (a) through (d) of the Commercial Computer Software - Restricted Rights clause at 52.227-19 of the Federal Acquisition Regulations ("FAR") and its successors, and is unpublished and all rights are reserved under the copyright laws of the United States. For units of the Department of Defense ("DoD"): This is "commercial computer software" as defined at DFARS 252.227-7014 and the rights of the Government are as specified at DFARS 227.7202-3.

Unpublished - rights reserved under the copyright laws of the United States.

Hexagon PPM 305 Intergraph Way Madison, AL 35758

#### **Documentation**

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

## **Contents**

| About this brief                                     | 5  |
|------------------------------------------------------|----|
| Overview                                             | 6  |
| Intended audience                                    | 6  |
| Databridge Pro                                       | 6  |
| Integration of solution components                   | 6  |
| EAM configuration                                    | 8  |
| Databridge partner for Databridge Pro                | 8  |
| Dataflow Studio endpoint catalog                     | 9  |
| Endpoint catalog UUID references                     |    |
| Dataflow events                                      | 12 |
| Databridge Pro configuration                         | 14 |
| Process flow connection points                       | 14 |
| Defining and executing a process in Databridge Pro   |    |
| Appendix A – Type System Delivered Values            | 16 |
| Appendix B – Method System Delivered Values          | 17 |
| Appendix C – Region System Delivered Values          | 17 |
| Appendix D – HTTP Method System Delivered Values     | 18 |
| Appendix E – Filesystem Object Type Delivered Values | 19 |
| Appendix F – Databridge Event Subscriptions          | 19 |
| Appendix G – Data Lake Connectivity and Support      | 21 |

## <span id="page-4-0"></span>**About this brief**

This brief provides configuration and implementation information for the integration of HxGN EAM with Databridge Pro when Databridge Pro is used to exchange data with another Hexagon product or third-party product. This document describes configuration requirements, provides setup instructions, and details the Databridge Pro connection points that are used in the integration. This brief is intended to supplement the documentation of this feature. It is not comprehensive and may not include all the details about this functionality.

## <span id="page-5-0"></span>**Overview**

This brief provides configuration and implementation information for the integration of HxGN EAM with Databridge Pro when Databridge Pro is used to exchange data with another Hexagon product or third-party product.

See [HxGN Databridge Pro](https://docs.hexagonppm.com/r/en-US/Databridge-Pro-Help/25.3/1496197) for more information on Databridge Pro.

## <span id="page-5-1"></span>**Intended audience**

This brief is intended for the system administrator or consultant who configures HxGN EAM for use with Databridge Pro.

## <span id="page-5-2"></span>**Databridge Pro**

Databridge Pro, powered by Apache NiFi, is the next generation of EAM Databridge, delivering advanced capabilities for data integration between EAM and external applications. Utilizing components both internal and outside of the EAM application, Databridge Pro provides the ability to build and manage customized data pipelines, streamline endpoint connections and usage, and simplify troubleshooting by offering insights into the complete EAM message journey.

Databridge Pro is a graphical interface middleware utility based on Apache Ni-Fi used to integrate EAM with other software applications.

## <span id="page-5-3"></span>**Integration of solution components**

The diagram below reflects the flow of data between EAM and Databridge Pro.

![](_page_6_Figure_0.jpeg)

### **Process flow: Endpoint Catalog**

The EAM user will create/define the endpoint catalog record. Databridge Pro will retrieve all defined and active endpoint catalog records from EAM when the user clicks the EAM Endpoint Processors icon within the utility.

If the EAM user updates an endpoint catalog record, EAM will call Databridge Pro for each UUID associated to the Endpoint ID using the "processors" API within the Databridge 2.0 REST API swagger (path /processors/update-processors) to update the catalog detail in Databridge Pro.

#### **Process flow: Endpoint Catalog Record UUID**

Databridge Pro will determine and populate UUID reference values once the endpoint is added/used on the Databridge Pro canvas. Databridge Pro will send these values to EAM and EAM will display this data on the **UUID References** pop-up of the endpoint catalog record.

### **Process flow: Dataflow Events**

In EAM when the user clicks the Dataflow Events tab for a Message record associated to the HXGN-DFS partner, an internal cross reference table is accessed to identify all the Dataflow UUIDs associated to the Databridge Message ID. Once identified, the Databridge Pro Provenance API is called for each corresponding Dataflow UUID. Data for all Dataflow UUIDs is rendered and displayed in a single grid view for the user, grouped by the API call, or Dataflow UUID, and in chronological order based on the date/time stamp.

### **Process flow: Dataflow Event ID**

In EAM, if the user clicks an Event ID hyperlink populated to the Dataflow Event record, EAM will call the GET /provenance-events/{id}/content/output API using the Event ID as the ID for the GET call to then display the flowfile payload content

## <span id="page-7-0"></span>**EAM configuration**

## <span id="page-7-1"></span>**Databridge partner for Databridge Pro**

A partner record has been defined within HxGN EAM specifically for integration using Databridge Pro. This partner, HXGN-DFS, will be dedicated for integration with Databridge Pro and no other partner within EAM will be able to leverage the endpoint catalog capabilities for integration purposes.

To utilize the HXGN-DFS partner for integrations, the customer must enable the partner record. If the HXGN-DFS partner is enabled, both the INFOR-ONRAMP partner and INFOR-IMS partner records should be disabled.

The features and functionality of the HXGN-DFS partner will only be available in the Hexagon Cloud and not in the Infor Cloud nor On-premise deployments of EAM.

## **Web service configuration**

Web services to support Databridge Pro utility requirements will have no external exposure. Communication will be strictly cloud to cloud processing with no browser path involved. To enforce the security of these web services, enable communication with the HXGN-DFS partner, and support web service usage by Databridge Pro, a ClientID for the HXGN-DFS partner will need to be defined for the install parameter DFSCID. This parameter value can be anything that can identify the client (i.e. a simple string, a generated string, etc). The customer will manage this parameter value, and it will be harvested by Databridge Pro for usage of web services and API calls.

To populate the DFSCID parameter, follow the navigation **Administration** > **Security** > **Install Parameters**, and then select DFSCID.

### **Partner configuration to employ BODs**

Databridge Pro has the capability to support integrations using BODs. On the Subscriptions tab of the HXGN-DFS partner record, the user will add the necessary integration event(s) and populate the **Document Type** field value with the name of the specific BOD (e.g. SyncPurchaseOrder or ProcessPurchaseOrder for the ADDPO event subscription). In the Message Delivery section for each event subscription, the user will need to additionally populate the **Special Handling** field. The **Special Handling** field is pre-configured for each partner subscription record and it contains processing directives including the processing handler, current version of implementation, and delivery channel that are associated with the partner subscription record. This value can be copied from the INFOR-ONRAMP partner subscription record for the specified Event and **Document Type**. This value should not be altered unless instructed by HxGN EAM team. See Appendix F – Databridge Event Subscriptions for additional detail.

**Note:** These event subscriptions are pre-configured for the HXGN-DFS partner beginning with EAM 12.1 2024201. The client will still need to enable the necessary event subscriptions.

**Note:** Databridge should be enabled for the client tenant during provisioning. This is separate from enablement of Databridge Pro. Additionally, the \* partner record on the Partners screen in EAM should be enabled (Active) and valid values populated for the Credentials (User ID and Password).

## <span id="page-8-0"></span>**Dataflow Studio endpoint catalog**

DFS Catalog is a new tab within the EAM application developed to define the Dataflow Studio Endpoint Catalog. The new tab is accessible on the Databridge Partner screen.

The DFS Catalog tab is a centralized endpoint catalog within EAM for customers to configure and manage their integration network connections, enabling communication between Databridge Pro and designated "delivery" applications (e.g. AWS Kinesis, SFTP, Azure Datalake Storage).

EAM users define their third-party endpoint connections along with authorization protocols for Databridge Pro to communicate with external systems. Databridge Pro uses these endpoints as final destinations to route transformed information between systems, adding a custom EAM Endpoint Processors icon which will access a tenant's catalog from within EAM.

Users access the Endpoint catalog by selecting the DFS Catalog tab via the HXGN-DFS partner on the Databridge Partners screen.

![](_page_8_Figure_6.jpeg)

### **Catalog Definition**

**Endpoint ID:** A system generated sequence number for the endpoint catalog record.

**Description:** The name given to identify the endpoint catalog record.

**Active** (checkbox)**:** Indicator the endpoint catalog record is enabled.

### **Endpoint Definition**

An endpoint is a connection to a particular software application, web service, or other resource that enables other systems to communicate, interact, and exchange data. Endpoints serve as gateways for sending or receiving data in an integration process.

**Type:** The endpoint type categorizes endpoint connections based on the software, technology, or service to which they are associated, defining the general nature of communication.

**Method:** Endpoints work in partnership with methods to outline how data is sent or received from the endpoint. Methods are the allowable actions for the specific endpoint type.

**Processor Type:** The specific component utilized within Databridge Pro to establish the endpoint connection and communication in a data flow.

Based on the user selection of Type and Method, the system will set the Endpoint Processor value. The system will additionally reveal and display relevant Endpoint Property fields to further define the Endpoint Processor for Databridge Pro. The below table reflects the selection of Type and Method, the system assigned Endpoint Databridge Pro Processor, and the relevant Endpoint Properties.

| Type                   | Method      | Processor                  | Endpoint Property          |
|------------------------|-------------|----------------------------|----------------------------|
| AWS Kinesis            | Put         | PutKinesisStream           | Amazon Kinesis Stream Name |
|                        |             |                            | Region                     |
|                        |             |                            | Access Key ID              |
|                        |             |                            | Secret Access Key          |
|                        | Consume     | ConsumeKinensisStream      | Amazon Kinesis Stream Name |
|                        |             |                            | Region                     |
|                        |             |                            | Application Name           |
| Azure Blob Storage     | Delete      | DeleteAzureBlobStorage_v12 | Container Name             |
|                        |             |                            | Blob Name                  |
|                        | Fetch       | FetchAzureBlobStorage_v12  | Container Name             |
|                        |             |                            | Blob Name                  |
|                        | List        | ListAzureBlobStorage_v12   | Container Name             |
|                        |             |                            | Blob Name Prefix           |
|                        | Put         | PutAzureBlobStorage_v12    | Container Name             |
|                        |             |                            | Blob Name                  |
| Azure Datalake Storage | Delete      | DeleteAzureDatalakeStorage | Filesystem Name            |
|                        |             |                            | Directory Name             |
|                        |             |                            | File Name                  |
|                        |             |                            | Filesystem Object Type     |
|                        | Fetch       | FetchAzureDatalakeStorage  | Filesystem Name            |
|                        |             |                            | Directory Name             |
|                        |             |                            | File Name                  |
|                        | List        | ListAzureDatalakeStorage   | Filesystem Name            |
|                        |             |                            | Directory Name             |
|                        | Move        | MoveAzureDatalakeStorage   | Source Filesystem          |
|                        |             |                            | Source Directory           |
|                        |             |                            | File Name                  |
|                        |             |                            | Destination Filesystem     |
|                        |             |                            | Destination Directory      |
|                        | Put         | PutAzureDatalakeStorage    | Filesystem Name            |
|                        |             |                            | Directory Name             |
|                        |             |                            | File Name                  |
| BOD Processing         | Outbound    | BODFromEAM_V2              | Not applicable             |
|                        | Inbound     | BODToEAM                   |                            |
| HTTPS                  | HTTP Method | InvokeHTTP                 | HTTP Method                |

| Type          | Method | Processor      | Endpoint Property |
|---------------|--------|----------------|-------------------|
|               |        |                | HTTP URL          |
|               |        |                | Request Username  |
|               |        |                | Request Password  |
| AWS S3 Bucket | Delete | DeleteS3Object | Bucket            |
|               |        |                | Region            |
|               |        |                | Access Key ID     |
|               |        |                | Secret Access Key |
|               |        |                | Object Key        |
|               | Fetch  | FetchS3Object  | Bucket            |
|               |        |                | Region            |
|               |        |                | Access Key ID     |
|               |        |                | Secret Access Key |
|               |        |                | Object Key        |
|               | List   | ListS3         | Bucket            |
|               |        |                | Region            |
|               |        |                | Access Key ID     |
|               |        |                | Secret Access Key |
|               | Put    | PutS3Object    | Bucket            |
|               |        |                | Region            |
|               |        |                | Access Key ID     |
|               |        |                | Secret Access Key |
|               |        |                | Object Key        |
| SFTP          | Fetch  | FetchSFTP      | Hostname          |
|               |        |                | Port              |
|               |        |                | Username          |
|               |        |                | Password          |
|               |        |                | Remote File       |
|               | Get    | GetSFTP        | Hostname          |
|               |        |                | Port              |
|               |        |                | Username          |
|               |        |                | Password          |
|               |        |                | Remote Path       |
|               |        |                | File Filter Regex |
|               | List   | ListSFTP       | Hostname          |
|               |        |                | Port              |
|               |        |                | Username          |
|               |        |                | Password          |
|               |        |                | Remote Path       |
|               |        |                | File Filter Regex |
|               | Put    | PutSFTP        | Hostname          |
|               |        |                | Port              |
|               |        |                | Username          |
|               |        |                | Password          |
|               |        |                | Remote Path       |

### **System-delivered endpoint catalog records**

There are two system-delivered Endpoint Catalog records for the DFS Catalog tab with the following values:

| Endpoint ID | Description        | Active   | Type       | Method   | Processor Type |
|-------------|--------------------|----------|------------|----------|----------------|
| 1           | BOD Outbound from  | Not      | BOD        | Outbound | BODFromEAM_V2  |
|             | EAM                | selected | Processing |          |                |
| 2           | BOD Inbound to EAM | Not      | BOD        | Inbound  | BODToEAM       |
|             |                    | selected | Processing |          |                |

**Notes:** All Endpoint Property fields are null for these two records. The Description and Active check box are editable. These delivered records can be deleted by the customer in the scenario they are deemed irrelevant or unnecessary.

## <span id="page-11-0"></span>**Endpoint catalog UUID references**

The user can view the Databridge Pro reference details for an Endpoint Catalog Record by invoking the **UUID References** pop-up window. UUIDs are generated and assigned to Endpoint Catalog records by Databridge Pro each time the record is referenced in a data flow. Note, if an endpoint record is referenced twice in a single data flow, the endpoint record will be assigned two UUID reference values by Databridge Pro.

To access UUID References, the user will select an Endpoint Catalog record and then select **UUID References** from the Actions menu option on the DFS Catalog tab of the Databridge Partners screen.

![](_page_11_Picture_4.jpeg)

The **UUID** is a unique identifier assigned by Databridge Pro when the endpoint record is referenced in a defined data flow. The **Status** indicates the state of the Endpoint Processor in Databridge Pro. Valid **Status** values include Disabled, Enabled, Invalid, Running, and Stopped. The **Date Created** references when the Endpoint Processor was added to a data flow within Databridge Pro flow. If an endpoint record in a data flow is updated, the **Date Updated** would additionally be populated.

## <span id="page-11-1"></span>**Dataflow events**

When a data flow is executed in Databridge Pro, events are generated for each step or process taken within the data flow. The event records and associated flow files (or messages) can be viewed within EAM on the Dataflow Events tab accessed from the Databridge Message Status screen.

Each event record includes a Dataflow UUID referencing the flowfile moving in the process, the date and time of the event, the event ID, provenance event, event type, component name, component type, and a flowfile reference, giving the user a 360 view of transaction processing.

If the user clicks an Event ID hyperlink from the Event record, the system will display the payload content of the flowfile associated to that event.

![](_page_12_Figure_1.jpeg)

When the user clicks on the hyperlink populated to the Event ID column, the payload content of the flowfile will be displayed for review. The user can copy and save this information locally for additional review and analysis as indicated or desired.

![](_page_12_Figure_3.jpeg)

## <span id="page-13-0"></span>**Databridge Pro configuration**

Databridge Pro will be the primary middleware for cloud-based integrations.

## <span id="page-13-1"></span>**Process flow connection points**

Within Databridge Pro, the user will define a data flow step by step using the Endpoint Catalog records defined in EAM. Note, Endpoint Catalog records (defined in EAM) will be available for selection from the Databridge Pro EAM Endpoint Processors to add to the canvas.

In Databridge Pro, the user will click the EAM Endpoint Processor icon and drag it onto the Databridge Pro canvas. The Add EAM Endpoint Processor dialog window will display a listing of all available, and active, defined EAM endpoint catalog records. The user will select the desired endpoint processor record and then click **Add** to add it to the canvas. Only one endpoint processor entry can be selected at a time, enforcing a step-wise construction to build a process. For efficiency, it is advised to plan out all the steps necessary for the full process flow and then use the Endpoint Processor dialog window to make selections sequentially.

![](_page_13_Picture_5.jpeg)

As each connection point is selected and added, Databridge Pro will assign a UUID to the corresponding processor. This UUID reference is a value used to uniquely identify the processor and can be viewed in EAM by clicking the **UUID References** link option in the Actions menu on the DFS Catalog tab. Note, if a connection point will be used multiple times in the same process, the user can either create a copy of it (on the canvas) for each time it will be referenced, and each copy will be assigned a UUID value, or they can re-select the endpoint from the EAM Endpoint Processor dialog window.

In Databridge Pro, the user can click on the endpoint processor, and the settings for the connection point will be displayed in the Configure Processor dialog window; the UUID appears on the Settings tab.

![](_page_14_Figure_1.jpeg)

![](_page_14_Figure_2.jpeg)

## <span id="page-14-0"></span>**Defining and executing a process in Databridge Pro**

A process flow is further defined in Databridge Pro by connecting the included endpoint processors. To connect any two nodes, the user will hover over an endpoint processor and the connection icon will display ( ); the user will click this icon and drag the icon to the next sequential processor in the flow. The Create Connection dialog window will then open where the user will select the relationship to define the connection and how the data will be routed through the flow for the two involved processor points.

![](_page_15_Picture_0.jpeg)

The below diagram represents a process flow for transforming a requisition to a purchase order. Using the right-click menu in Databridge Pro, the user will start the process by clicking **Start** in the context menu**.** As each step is executed, there will be a corresponding event in EAM on the Dataflow Events tab.

![](_page_15_Picture_2.jpeg)

## <span id="page-15-0"></span>**Appendix A – Type System Delivered Values**

Type is defined by the Setup Type of Type and Entity of 'DFTP' (Dataflow Studio Endpoint Type)

| User Code | System Code | Description |
|-----------|-------------|-------------|
| AWSK      | *           | AWS Kinesis |

| User Code | System Code | Description            |
|-----------|-------------|------------------------|
| AZBS      | *           | Azure Blob Storage     |
| AZDS      | *           | Azure DataLake Storage |
| BOD       | *           | BOD Processing         |
| HG        | *           | HTTPS                  |
| S3        | *           | AWS S3 Bucket          |
| SFTP      | *           | SFTP                   |

# <span id="page-16-0"></span>**Appendix B – Method System Delivered Values**

Method is defined by the Setup Type of Code and Entity of 'DMTH' (Dataflow Studio Endpoint Method)

| User Code | System Code | Description |
|-----------|-------------|-------------|
| BFRM      | *           | Outbound    |
| BTO       | *           | Inbound     |
| CNSM      | *           | Consume     |
| DEL       | *           | Delete      |
| FTCH      | *           | Fetch       |
| GET       | *           | Get         |
| LIST      | *           | List        |
| MOVE      | *           | Move        |
| OPTN      | *           | Options     |
| PTCH      | *           | Patch       |
| POST      | *           | Post        |
| PUT       | *           | Put         |

# <span id="page-16-1"></span>**Appendix C – Region System Delivered Values**

Region is defined by the Setup Type of Code and Entity of 'DFRG' (Dataflow Studio Endpoint Region). Both the Region and Amazon Region LOVs will reference these values. Note, US West (Oregon) is the System Default.

| User Code | System Code | Description             |
|-----------|-------------|-------------------------|
| AGU       | *           | AWS GovCloud (US)       |
| AGUE      | *           | AWS GovCloud (US-East)  |
| UEVA      | *           | US East (N. Virginia)   |
| UEOH      | *           | US East (Ohio)          |
| UECA      | *           | US West (N. California) |
| UWOR      | *           | US West (Oregon)        |
| EUI       | *           | EU (Ireland)            |
| EUL       | *           | EU (London)             |
| EUP       | *           | EU (Paris)              |

| User Code | System Code | Description                |
|-----------|-------------|----------------------------|
| EUF       | *           | EU (Frankfurt)             |
| EUZ       | *           | EU (Zurich)                |
| EUST      | *           | EU (Stockholm)             |
| EUM       | *           | EU (Milan)                 |
| EUSP      | *           | EU (Spain)                 |
| APHK      | *           | Asia Pacific (Hong Kong)   |
| APM       | *           | Asia Pacific (Mumbai)      |
| APHY      | *           | Asia Pacific (Hyderabad)   |
| APSN      | *           | Asia Pacific (Singapore)   |
| APSY      | *           | Asia Pacific (Sydney)      |
| APJ       | *           | Asia Pacific (Jakarta)     |
| APT       | *           | Asia Pacific (Tokyo)       |
| APSE      | *           | Asia Pacific (Seoul)       |
| APOS      | *           | Asia Pacific (Osaka)       |
| SASP      | *           | South America (Sao Paulo)  |
| CHB       | *           | China (Beijing)            |
| CHN       | *           | China (Ningxia)            |
| CNC       | *           | Canada (Central)           |
| MEU       | *           | Middle East (UAE)          |
| MEB       | *           | Middle East (Bahrain)      |
| AFCT      | *           | Africa (Cape Town)         |
| UIE       | *           | US ISO East                |
| UIEO      | *           | US ISOB East (Ohio)        |
| UIW       | *           | US ISO West                |
| APMY      | *           | Asia Pacific (Malaysia)    |
| APML      | *           | Asia Pacific (Melbourne)   |
| APTP      | *           | Asia Pacific (Taipei)      |
| APTH      | *           | Asia Pacific (Thailand)    |
| CNWC      | *           | Canada West (Calgary)      |
| UIFE      | *           | US ISOF East1 (California) |
| UIFS      | *           | US ISOF South1 (Alpine)    |
| MXC       | *           | Mexico (Central)           |
| ILTA      | *           | Israel (Tel Aviv)          |

# <span id="page-17-0"></span>**Appendix D – HTTP Method System Delivered Values**

HTTP Method is defined by the Setup Type of Code and Entity of 'DFHM' (Dataflow Studio Endpoint HTTP Method). Note, GET is the System Default.

| User Code | System Code | Description |
|-----------|-------------|-------------|
| DEL       | *           | Delete      |
| GET       | *           | Get         |
| HEAD      | *           | Head        |
| OPTN      | *           | Options     |
| PTCH      | *           | Patch       |
| POST      | *           | Post        |

| User Code | System Code | Description |
|-----------|-------------|-------------|
| PUT       | *           | Put         |

# <span id="page-18-0"></span>**Appendix E – Filesystem Object Type Delivered Values**

Filesystem Object Type is defined by the Setup Type of Code and Entity of 'DFOT' (Dataflow Filesystem Object Type).

| User Code | System Code | Description |
|-----------|-------------|-------------|
| DIR       | *           | Directory   |
| FILE      | *           | File        |

# <span id="page-18-1"></span>**Appendix F – Databridge Event Subscriptions**

Databridge outbound event subscriptions specify the types of messages in response to various Databridge events.

For the HXGN-DFS partner, switch to the **Subscriptions** tab and add the events necessary for your integration needs, referring to the table below. To enable an event, select the **Enabled** checkbox and then click **Submit**.

**Note:** These event subscriptions will be pre-configured for the HXGN-DFS partner in a future release. The client will still need to enable the necessary event subscriptions.

| Event          | Document Type                    | Special Handling                        |
|----------------|----------------------------------|-----------------------------------------|
| ADDPO          | ProcessPurchaseOrder             | InforSoaDocumentExporter/R01/R02/IMS/BD |
| ADDPO          | SyncPurchaseOrder                | InforSoaDocumentExporter/R01/R02/IMS/BD |
| ADDREQUISTN    | SyncRequisition                  | InforSoaDocumentExporter/R01/R02/IMS/BD |
| ADDREQUISTN    | ProcessRequisition               | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CALLCENTER     | ProcessCustomerCall              | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CALLCENTER     | SyncCustomerCall                 | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CANCELPOHEADER | ProcessPurchaseOrder             | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CANCELPOHEADER | SyncPurchaseOrder                | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CANCELPOLINE   | SyncPurchaseOrder                | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CANCELPOLINE   | ProcessPurchaseOrder             | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CAPREQ         | ProcessEamCapitalPlanningRequest | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CAPREQ         | SyncEamCapitalPlanningRequest    | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CHANGEPO       | ProcessPurchaseOrder             | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CHANGEPO       | SyncPurchaseOrder                | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CHANGEREQUISTN | SyncRequisition                  | InforSoaDocumentExporter/R01/R02/IMS/BD |
| CHANGEREQUISTN | ProcessRequisition               | InforSoaDocumentExporter/R01/R02/IMS/BD |

| Event            | Document Type                               | Special Handling                        |
|------------------|---------------------------------------------|-----------------------------------------|
| CODEDEF          | ProcessCodeDefinition                       | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CODEDEF          | SyncCodeDefinition                          | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CONTRACTINVOICE  | SyncInvoice                                 | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CONTRACTINVOICE  | ProcessInvoice                              | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CSMGMT           | SyncEamCaseManagement                       | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CSMGMT           | ProcessEamCaseManagement                    | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CUSTOMER         | ProcessCustomerPartyMaster                  | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CUSTOMER         | SyncCustomerPartyMaster                     | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CUSTOMERCONTRACT | SyncContract                                | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CUSTOMERCONTRACT | ProcessContract                             | InforSoaDocumentExporter/R01/R01/IMS/BD |
| CUSTSURVEYEVENT  | SyncAssetTrackingDataForCustomerSurveyEvent | InforSoaDocumentExporter/R01/R01/IMS/BD |
| EMPEXCPN         | SyncEmployeeWorkScheduleForException        | InforSoaDocumentExporter/R01/R01/IMS/BD |
| EMPSHLB          | SyncEmployeeWorkScheduleForScheduleLabor    | InforSoaDocumentExporter/R01/R01/IMS/BD |
| EMPSHLB          | ProcessEmployeeWorkScheduleForScheduleLabor | InforSoaDocumentExporter/R01/R01/IMS/BD |
| EVENTLOG         | SyncAssetTrackingDataForEventLog            | InforSoaDocumentExporter/R01/R01/IMS/BD |
| FUELISSUES       | SyncAssetTrackingDataForFuelIssue           | InforSoaDocumentExporter/R01/R01/IMS/BD |
| GLFEED           | ProcessSourceSystemJournalEntry             | InforSoaDocumentExporter/R01/R01/IMS/BD |
| GLFEED           | SyncSourceSystemJournalEntry                | InforSoaDocumentExporter/R01/R01/IMS/BD |
|                  |                                             |                                         |
| GREENCALCULATION | SyncAssetMeterReadingGreen                  | InforSoaDocumentExporter/R01/R01/IMS/BD |
| INVYCOUNT        | SyncInventoryCount                          | InforSoaDocumentExporter/R01/R01/IMS/BD |
| LOADPAYABLE      | SyncSupplierInvoice                         | InforSoaDocumentExporter/R01/R01/IMS/BD |
| LOADPAYABLE      | ProcessSupplierInvoice                      | InforSoaDocumentExporter/R01/R01/IMS/BD |
| MANUFACTURER     | ProcessManufacturerPartyMaster              | InforSoaDocumentExporter/R01/R01/IMS/BD |
| MANUFACTURER     | SyncManufacturerPartyMaster                 | InforSoaDocumentExporter/R01/R01/IMS/BD |
| NONCONFORMITY    | SyncEamNonconformity                        | InforSoaDocumentExporter/R01/R01/IMS/BD |
| NONCONFORMITY    | ProcessEamNonconformity                     | InforSoaDocumentExporter/R01/R01/IMS/BD |
| PICKLIST         | ProcessShipment                             | InforSoaDocumentExporter/R01/R01/IMS/BD |
| PICKLIST         | SyncShipment                                | InforSoaDocumentExporter/R01/R01/IMS/BD |
| PORECEIVEPARTS   | SyncReceiveDelivery                         | InforSoaDocumentExporter/R01/R02/IMS/BD |
| PORECEIVEPARTS   | ProcessReceiveDelivery                      | InforSoaDocumentExporter/R01/R02/IMS/BD |
| PORECEIVESERVICE | SyncServiceConsumption                      | InforSoaDocumentExporter/R01/R02/IMS/BD |
| PORECEIVESERVICE | ProcessServiceConsumption                   | InforSoaDocumentExporter/R01/R02/IMS/BD |
| PRDREQ           | ProcessProductionOrder                      | InforSoaDocumentExporter/R01/R01/IMS/BD |
| PRDREQ           | SyncProductionOrder                         | InforSoaDocumentExporter/R01/R01/IMS/BD |
| PULSEBODEVENT    | SyncPulseNotification                       | InforSoaDocumentExporter/R01/R01/IMS/BD |
| PURCONTRACT      | SyncContractForPurchasingContract           | InforSoaDocumentExporter/R01/R01/IMS/BD |
| PURCONTRACT      | ProcessContractForPurchasingContract        | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SECROLE          | SyncSecurityRoleMaster                      | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SECUSER          | ProcessSecurityUserMaster                   | InforSoaDocumentExporter/R01/R01/IMS/BD |
| STRTOSTRREQ      | ProcessTransfer                             | InforSoaDocumentExporter/R01/R01/IMS/BD |
| STRTOSTRREQ      | SyncTransfer                                | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SUPPLIERRMA      | SyncSupplierRMA                             | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCITEM         | ProcessItemMaster                           | InforSoaDocumentExporter/R01/R02/IMS/BD |
| SYNCITEM         | SyncItemMaster                              | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCMAINTORDER   | ProcessMaintenanceOrder                     | InforSoaDocumentExporter/R01/R02/IMS/BD |
| SYNCMAINTORDER   | SyncMaintenanceOrder                        | InforSoaDocumentExporter/R01/R02/IMS/BD |
| SYNCOBJA         | ProcessAssetMaster                          | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCOBJA         | SyncAssetMaster                             | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCOBJL         | ProcessAssetMaster                          | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCOBJL         | SyncAssetMaster                             | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCOBJP         | ProcessAssetMaster                          | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCOBJP         | SyncAssetMaster                             | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCOBJS         | SyncAssetMaster                             | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCOBJS         | ProcessAssetMaster                          | InforSoaDocumentExporter/R02/R02/IMS/BD |
| SYNCPERS         | SyncPersonnel                               | InforSoaDocumentExporter/R01/R01/IMS/BD |
|                  |                                             |                                         |

| Event            | Document Type                    | Special Handling                        |
|------------------|----------------------------------|-----------------------------------------|
| SYNCPERS         | ProcessPersonnel                 | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCPRJ          | ProcessProjectMaster             | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCPRJ          | SyncProjectMaster                | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCSHIFTEMP     | SyncEmployeeWorkScheduleForShift | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCSHIFTS       | SyncWorkShiftMaster              | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCSHIFTS       | ProcessWorkShiftMaster           | InforSoaDocumentExporter/R01/R01/IMS/BD |
| SYNCSUP          | ProcessSupplierPartyMaster       | InforSoaDocumentExporter/R01/R02/IMS/BD |
| SYNCSUP          | SyncSupplierPartyMaster          | InforSoaDocumentExporter/R01/R01/IMS/BD |
| TKDATA           | SyncAssetTrackingData            | InforSoaDocumentExporter/R01/R01/IMS/BD |
| UPDATEPERSONTIME | SyncEmployeeWorkTime             | InforSoaDocumentExporter/R01/R01/IMS/BD |
| UPDATEPERSONTIME | ProcessEmployeeWorkTime          | InforSoaDocumentExporter/R01/R01/IMS/BD |
| UPDINV           | ExportInventoryTransactions      | InforSoaDocumentExporter/R02/R02/IMS/BD |
| WSPTRA           | SyncEamWSPromptTransaction       | InforSoaDocumentExporter/R01/R01/IMS/BD |

**Note:** For the UPDINV / ExportInventoryTransactions event subscription, if you need HxGN EAM to send BODs with a Sync verb, set Special Handling to 'InforSoaDocumentExporter/R01/R02/IMS/BD'; otherwise set Special Handling to 'InforSoaDocumentExporter/R02/R02/IMS/BD', and HxGN EAM will send BODs with a Process verb.

# <span id="page-20-0"></span>**Appendix G – Data Lake Connectivity and Support**

The Data Lake utility is capable of transmitting data to Databridge Pro in addition to the ION endpoint, this feature is supported only in the Hexagon cloud environment and is not available for Infor Cloud usage. To enable transmission of data to the Databridge Pro endpoint, the EAM install parameter DLUTXDBP should be set to YES. Currently, DLU transmits data in JSON format only and does not transmit schema details.

As delivered, Databridge Pro includes custom processors for Google BigQuery, Google Cloud Storage, Azure Data Lake, and Snowflake.

| Data Lake            | Databridge Pro Processors                                                                                                                  |  |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--|
| Google BigQuery      | PutBigQuery                                                                                                                                |  |
| Google Cloud Storage | DeleteGCSObject<br>FetchGCSObject<br>ListGCSBucket<br>PutGCSObject                                                                         |  |
| Azure Data Lake      | DeleteAzureDataLakeStorage<br>FetchAzureDataLakeStorage<br>ListAzureDataLakeStorage<br>MoveAzureDataLakeStorage<br>PutAzureDataLakeStorage |  |
| Snowflake            | GetSnowflakeIngestStatus<br>PutSnowflakeInternalStage<br>StartSnowflakeIngest                                                              |  |

### **Data Lake Databridge Pro Processors**

Any other connection to an external Data Lake would require configuration using existing Databridge Pro processors for enablement.