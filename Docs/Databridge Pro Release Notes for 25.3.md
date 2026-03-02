# Databridge Pro Release Notes for 25.3

Hexagon Documentation

Generated 02/28/2026

# Databridge Pro Release Notes

This document covers the general enhancements, list of components added, list of components deprecated, known issues, and a list of any customer-facing, resolved issues.

Details of previous updates for this year are not included in these documents.

© 2025-2026, Hexagon AB <https://hexagon.com/company/divisions/asset-lifecycle-intelligence> and/or its subsidiaries and affiliates
25.3
Published Sunday, September 28, 2025 at 11:48 PM

## November 2025 production update

### Solution enhancements

The following is a list of enhancements that are included with this release of Databridge Pro.

**Area**
* Enhancement
**User Interface Upgrade**
* The user interface (UI) was upgraded to follow modern and contemporary design principles with a more responsive design. The interface maintains familiar core experience while offering improved usability through more intutative navigation, streamlined layouts, user-selectable dark/light themes and clearer visual indicators for an improved overall experience.

**Login Authentication**
* External login authentication is available, allowing users to utilize same sign-on within their organization. New screens within System Controls are available for administrators to configure the tenant's authorization type (internal / external) and upload their Identity Provider SAML file for use by Databridge Pro. When configured, Databridge Pro will redirect to an external server which is responsible for login authentication.

**Cloud Connector (DCC)**
* A new version of the Cloud Connector (DCC) is available. It's recommended to upgrade all existing DCC instances to the latest version available through the Cloud Connector > Downloads screen to ensure compatibility and access to future features.
* Flow definition files specific for Cloud Connector now use JSON format instead of YAML. Existing flows will continue to function without modification.

**System Controls**
* Tenant-level configurations are consolidated to a new System Controls screen, accessible from the Global Menu. Administrator users can configure items such as tenant access to HxGN Alix, API Client Authorizations, Authentication Type for Login, Identity Providers for external login, and Password Policies for internal login authorization.

**EAM BODs**
* BOD Type selections in BODFromEAM_V2 and BODToEAM are aligned to all Process and Sync BODs supported in HxGN EAM.
* BODFromEAM_V2 does not formally include Acknowledge BODs. These will require management using the unmatched relationship for further routing. BODToEAM has support for selection of Acknowledge BODs.
* contentType selection (json or xml) is now available in BODToEAM properties. If contentType is not populated it is assumed as xml by HxGN EAM. (NOTE contentType was added to BODFromEAM_V2 properties with version 25.2, released in August 2025)

**Legacy Removals**
* Legacy components and functionality are removed and no longer supported, including:
* Variables - Variables are fully decommissioned, replaced by Parameters and Parameter Context.
* Base64EncodedContent processor - use alternative EncodeContent.
* ExecuteScript processor - use alternative GroovyExecutionService.
* ConvertAvroToJson processor - use alternative ConvertRecord.
* InvokeAWSGatewayApi processor - use alternative InvokeHTTP

# New components

## List of new components

<table>
  <thead>
    <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Processor</td>
        <td>ConsumeKafka</td>
        <td>Supports consumption of Kafka messages through the</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
        <th></th>
        <th></th>
        <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td rowspan="2"></td>
        <td rowspan="2"></td>
        <td>Apache Kafka Consumer API. Complementary processor for sending messages is PublishKafka.<br/><br/>**NOTE** ConsumeKafka replaces all older Kafka fetching components, including ConsumeKafka_2_6 and ConsumeKafkaRecord_2_6</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>PublishKafka</td>
        <td>Sends contents of a FlowFile as either a message or as individual records to Apache Kafka using the Kafka Producer API. Complementary processor for fetching messages is ConsumeKafka.<br/><br/>**NOTE** PublishKafka replaces all older Kafka publishing components, including PublishKafka_2_6 and PublishKafkaRecord_2_6</td>
    </tr>
  </tbody>
</table>

## Deprecated components

All deprecated components must be replaced with their recommended alternatives to prevent data flow disruptions in future releases. Once replacement components are configured and tested, the deprecated processors must be removed from the canvas entirely. Processors remaining on the canvas continue to consume system resources even when disabled and any deprecated or unsupported processor should be deleted to optimize performance.

# List of deprecated components

<table>
  <tbody>
    <tr>
        <td>Type</td>
        <td>Name</td>
        <td>Timing</td>
    </tr>
    <tr>
        <th>Processor</th>
        <th>ExecuteGroovyScript</th>
        <th>Processor is planned for removal in NOV-2026 release.<br/><br/>Please use the alternative: GroovyExecutionService.</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>ConsumeKafka_2_6</th>
        <th>Processor is planned for removal in NOV-2026 release.<br/><br/>Please use the alternative: ConsumeKafka.</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>ConsumeKafkaRecord_2_6</th>
        <th>Processor is planned for removal in NOV-2026 release.<br/><br/>Please use the alternative: ConsumeKafka.</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>PublishKafka_2_6</th>
        <th>Processor is planned for removal in NOV-2026 release.<br/><br/>Please use the alternative: PublishKafka.</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>PublishKafkaRecord_2_6</th>
        <th>Processor is planned for removal in NOV-2026 release.<br/><br/>Please use the alternative: PublishKafka.</th>
    </tr>
  </tbody>
</table>

Please use the alternative: PublishKafka.

# Known issues
List of known issues
None

# Resolved issues
List of resolved issues
None

# August 2025 production update
## Solution enhancements
The following is a list of enhancements that are included with this release of Databridge Pro.

<table>
  <tbody>
    <tr>
        <td>Area</td>
        <td>Enhancement</td>
    </tr>
    <tr>
        <td>Parameter Contexts</td>
        <td>Users can now create multiple Parameter Contexts within a tenant. Parameter Contexts can be created and associated with individual process groups, allowing for better separation and organization of Parameters across the tenant. Previously, only one Parameter Context was available at the tenant level.<br/><br/>IMPORTANT: Parameters will fully replace Variables in the 25.3, Nov-2025 release. Variables will no longer be available after that time. Please switch from Variables to Parameters ASAP.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
        <td>Groovy Scripting</td>
        <td>A new processor called GroovyExecutionService is introduced to enhance Groovy scripting capabilities. This processor connects to a remote service to offload script execution, allowing users access to a wider range of Groovy libraries with fewer restrictions.<br/><br/>IMPORTANT: ExecuteScript and ExecuteGroovyScript have been deprecated and should no longer be used. Please remove all instances of these processors ASAP and move to GroovyExecutionService.</td>
    </tr>
    <tr>
        <td>OSIsoft Pi connection</td>
        <td>New connection processor, InvokeOSIPI, is added to support connection to OSIsoft Pi servers through the PI Web API interface layer. This processor connection is supported both in the Cloud and the on-premise Cloud Connector (DCC) component.</td>
    </tr>
    <tr>
        <td>Local File System ~~-~~ DCC</td>
        <td>Local file system connection is now supported within the Cloud Connector (DCC). New processors are added to support functions for deleting, reading, creating, retrieving, and writing flowfiles to a local file system, using the Cloud Connector (DCC).</td>
    </tr>
    <tr>
        <td>BODToEAM</td>
        <td>BOD messages will now be sent in batches when using the BODToEAM processor to improve performance and overall throughput. Multiple FlowFiles, each containing a BOD message, will be grouped together into a single communication when transmitted to EAM. Previously, FlowFiles</td>
    </tr>
  </tbody>
</table>

were processed and sent individually, one at a time, when using BODToEAM.

<table>
    <tr>
        <td>**Branding Updates**</td>
        <td>Branding within the User Interface and reference documentation has been updated to reflect the new product name 'HxGN Databridge Pro'.</td>
    </tr>
    <tr>
        <td>**Variables**</td>
        <td>Variables can no longer be added or modified within the canvas. However, existing Variables that have already been defined will continue to function and be used within the specified flows.&lt;br/&gt;&lt;br/&gt;**IMPORTANT:** Parameters will fully replace Variables in the 25.3.0, Nov-2025 release. Variables will no longer be available after that time. Please switch from Variables to Parameters ASAP.</td>
    </tr>
</table>## New components

The following is a list of Dataflow Studio processors or controller services which have been added with this release of Databridge Pro.

### List of new components

<table>
  <thead>
    <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Processor</td>
        <td>GroovyExecutionService</td>
        <td>Delegates Groovy script execution to a remote service. This processor is designed for users who want to run dynamic scripts in a less restrictive execution environment. The script is responsible for handling the incoming flow file (e.g.,</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
        <th></th>
        <th></th>
        <th></th>
        <th>transfer to SUCCESS or remove.) NOTE Replaces ExecuteGroovyScript.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Processor</td>
        <td>InvokeOSIPI</td>
        <td>OSI PI processor interacts with the PI Web API RESTful interface, giving client applications read and write access to their AF and PI data over HTTPS. The PI Server URL and HTTP Method are configurable. Processor is available in both Cloud and Cloud Connector (DCC).</td>
        <td></td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>DeleteFile</td>
        <td>Deletes a file from the filesystem. Available only for Cloud Connector (DCC) Process Groups. NOTE The DCC must have access to the file system to utilize this processor.</td>
        <td></td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>FetchFile</td>
        <td>Reads the contents of a file from disk and streams it into the contents of an incoming FlowFile. Available only for Cloud Connector (DCC) Process Groups. NOTE The DCC must have access to the file system to utilize this processor.</td>
        <td></td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>GetFile</td>
        <td>Creates FlowFiles from files in a directory. Available only for Cloud Connector (DCC) Process Groups. NOTE</td>
        <td></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
        <td></td>
        <td></td>
        <td>The DCC must have access to the file system to utilize this processor.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>ListFile</td>
        <td>Retrieves a listing of files from the input directory. For each file listed, creates a FlowFile that represents the file so that it can be fetched in conjunction with FetchFile. Available only for Cloud Connector (DCC) Process Groups. **NOTE** The DCC must have access to the file system to utilize this processor.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>PutFile</td>
        <td>Writes the contents of a FlowFile to the local file system. Available only for Cloud Connector (DCC) Process Groups. **NOTE** The DCC must have access to the file system to utilize this processor.</td>
    </tr>
    <tr>
        <td>Controller Service</td>
        <td>ParquetReader</td>
        <td>Parses Parquet data and returns each Parquet record as a separate Record object. The schema will come from the Parquet data itself. Can be utilized with processors, such as ConvertRecord.</td>
    </tr>
    <tr>
        <td>Controller Service</td>
        <td>ParquetRecordSetWriter</td>
        <td>Writes the contents of a RecordSet in Parquet format. Can be utilized with</td>
    </tr>
  </tbody>
</table>

processors, such as ConvertRecord.

# Deprecated components

List of deprecated components

<table>
  <tbody>
    <tr>
        <td>Type</td>
        <td>Name</td>
        <td>Timing</td>
    </tr>
    <tr>
        <th>Processor</th>
        <th>Base64EncodedContent</th>
        <th>Processor is planned for removal in a future release.<br/><br/>Please use the alternative: EncodeContent</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>ExecuteScript</th>
        <th>Processor is planned for removal in the Nov-2025 release.<br/><br/>Please use the alternative: GroovyExecutionService</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>ConvertAvroToJSON</th>
        <th>Processor is planned for removal in Nov-2025 release.<br/><br/>Please use the alternative: ConvertRecord</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>ConvertJSONToSQL</th>
        <th>Processor is planned for removal in Nov-2025 release.<br/><br/>Please use the alternative: ConvertRecord</th>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
        <td>Processor</td>
        <td>InvokeAWSGatewayApi</td>
        <td>Processor is planned for removal in Nov-2025 release.<br/><br/>Please use the alternative: InvokeHTTP.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>ExecuteGroovyScript</td>
        <td>Processor is planned for removal in the Nov-2026 release.<br/><br/>Please use the alternative: GroovyExecutionService</td>
    </tr>
  </tbody>
</table>

## Known issues

The following is a list of known issues with the latest version of Databridge Pro. Many of these are outside the control of the Databridge Pro development team and relate to issues within particular browsers. Our team will pursue solutions to these issues in the future, but many will require changes in the associated browsers to accomplish this.

### List of known issues

There are no known issues with this version.

## Resolved issues

### List of resolved issues

There are no resolved issues with this version.

## May 2025 production update

### Solution enhancements

The following is a list of enhancements that are included with this release of Databridge Pro.

<table>
  <tbody>
    <tr>
        <td>Area</td>
        <td>Enhancement</td>
    </tr>
    <tr>
        <th>Inbound Messages</th>
        <th>Inbound Message API now supports OAuth2 authentication protocol alongside existing basic authentication. OAuth2 credentials can be generated within the new API Client Auth screen.</th>
    </tr>
    <tr>
        <th>API Client Auth - OAuth2</th>
        <th>A new tab called API Client Auth is added to the Settings window for Administrator users to create and manage API Client records, generating the necessary OAuth2 credentials for Inbound Messages API authentication. API Client Auth screen is accessible from the Settings option in the Global Menu.</th>
    </tr>
    <tr>
        <th>Monitoring</th>
        <th>A new menu option called Monitoring is available within the Global Menu, providing access for users to navigate to the Bulletin Board and new Log Files screens.</th>
    </tr>
    <tr>
        <th>Log Visibility</th>
        <th>A new screen called Log Files is added, enabling downloading of log files generated by LogMessage and LogAttribute processors. This screen features 30-day history retrieval with hourly logs displayed by default for the current day. Log Files screen is accessible from the Monitoring option in the Global Menu.</th>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
        <td>Certificate / Key Manager - SFTP</td>
        <td>The Certificate / Key Manager screen now supports uploading and management of both private and public SFTP key files, which can be referenced within SFTP processors.</td>
    </tr>
    <tr>
        <td>BODFromEAM_V2</td>
        <td>A new 'databridge.contentType' attribute is added to BODFromEAM_V2 processor that automatically reflects the publication format (json or xml) sent from EAM Databridge. The publication format is set on the HxGN-DFS partner record within HxGN EAM.</td>
    </tr>
    <tr>
        <td>Authentication Type</td>
        <td>A new tab, Authentication Type, is added to the Settings window as a placeholder only. This screen has no active functionality in the 25.1.0 release and will be built out in a future update.</td>
    </tr>
    <tr>
        <td>Connection Queue Clean-up</td>
        <td>A clean-up mechanism is implemented to automatically purge FlowFiles sitting in a connection (or relationship) queue after 5 days.</td>
    </tr>
  </tbody>
</table>

## New components

The following is a list of Dataflow Studio processors or controller services which have been added with this release of Databridge Pro.

### List of new components

<table>
  <thead>
    <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Processor</td>
        <td>ConsumeAMQP</td>
        <td>Consumes AMQP Messages from an AMQP Broker using AMQP 0.9.1 protocol. Each</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Processor</td>
        <td>ConsumeAMQP</td>
        <td>message received emits its own FlowFile from the consumed AMQP message, both body and attributes. Attributes are transferred into FlowFile attributes.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>CopyS3Object</td>
        <td>Copies a file from one bucket and key to another within AWS S3.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>DeleteSFTP</td>
        <td>Deletes a file residing on an SFTP server.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>GetS3ObjectMetadata</td>
        <td>Checks for the existence of a file in S3. Can be used to check on a file in S3 before proceeding with data processing.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>PublishAMQP</td>
        <td>Publishes the contents of a FlowFile to an AMQP-based messaging system, using AMQP 0.9.1 protocol. The AMQP message is constructed by extracting a FlowFile's content, both body and attributes.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>SplitExcel</td>
        <td>Splits a multi-sheet Excel spreadsheet into multiple Excel spreadsheets where each sheet from the original file is converted into an individual spreadsheet of its own. Note: Can only process .xlsx (XSSF 2007 OOXML)</td>
    </tr>
  </tbody>
</table>

file format), not older documents.

# Known issues

The following is a list of known issues with the latest version of Databridge Pro. Many of these are outside the control of the Databridge Pro development team and relate to issues within particular browsers. Our team will pursue solutions to these issues in the future, but many will require changes in the associated browsers to accomplish this.

## List of known issues

There are no known issues with this version.

# Resolved issues

This document provides information about the issues resolved in this latest update of the Databridge Pro application.

Details of previous issues resolved in this year are not included in this document.

## May 2025 production update

The following is a list of resolved issues that are included with this release of Databridge Pro.

### Resolved issues

* Ability to run DCC (Cloud Connector) Process Group flows within the Cloud canvas.
* **Resolution:** Now restricted.

## February 2025 production update

### Solution enhancements

The following is a list of enhancements that are included with this release of Databridge Pro.

<table>
  <tbody>
    <tr>
        <td>Area</td>
        <td>Enhancement</td>
    </tr>
    <tr>
        <td>Bulletin Board</td>
        <td>A centralized Bulletin Board is now available from the Global Menu, displaying notifications, warnings, and errors from components within the canvas. Information displayed is dependent on the Bulletin level set within individual components. Users can monitor and check updates, as well as troubleshoot issues, from this centralized screen. All user roles have access to the Bulletin Board.</td>
    </tr>
    <tr>
        <td>HxGN Alix Integration</td>
        <td>HxGN Alix, Digital Asset's AI Assistant, is now integrated within Databridge Pro. Admin users can enable Alix within their tenant from a new Settings screen. When enabled, the Alix chat window will appear alongside the Navigate and Operatte palettes allowing all tenant users to interact with Alix as they work within the canvas.</td>
    </tr>
    <tr>
        <td>Parameters &amp; Parameter Context</td>
        <td>Parameter Context and Parameters are now available within the canvas. Parameters allow dynamic value substitution within flows, improving maintainability and reducing hardcoded configurations and errors. Parameters can be grouped into Parameter Contexts for efficient management across multiple components or process groups, as needed. All user roles have access to Parameters and Parameter Context.</td>
    </tr>
    <tr>
        <td>Processor Validation</td>
        <td>A validation occurs when single-instance processors, such as BODFromEAM_V2, InboundMessagesProcessor, or</td>
    </tr>
  </tbody>
</table>

GetEAMDataLakeMessageProcessor, are added to the canvas. Only one instance of these processor types should exist per tenant to function as designed. If a duplicate processor is detected, a warning message will be displayed to the user, indicating that multiple instances can lead to processing issues.

## New components

### List of new components

<table>
  <tbody>
    <tr>
        <td>Type</td>
        <td>Name</td>
        <td>Description</td>
    </tr>
    <tr>
        <th>Processor</th>
        <th>FetchDropbox</th>
        <th>Fetches files from a Dropbox location. Designed to be used in tandem with ListDropbox.</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>ListDropbox</th>
        <th>Retrieves a listing of files from Dropbox location.</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>PutDropbox</th>
        <th>Puts flowfile content into a designated Dropbox folder.</th>
    </tr>
    <tr>
        <th>Controller Service</th>
        <th>StandardDropboxCredential Service</th>
        <th>Shared service for defining credentials for the Dropbox processors.</th>
    </tr>
    <tr>
        <th>Processor</th>
        <th>PutBigQuery</th>
        <th>Writes the contents of a FlowFile to a Google BigQuery table.</th>
    </tr>
  </tbody>
</table>

# Deprecated components

## List of deprecated components

<table>
  <tbody>
    <tr>
        <td>Type</td>
        <td>Name</td>
        <td>Timing</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>Base64EncodedContent</td>
        <td>Processor is planned for removal in the Nov-2025 release.<br/><br/>Consider using the alternative: EncodeContent.</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>ExecuteScript</td>
        <td>Processor is planned for removal in the Nov-2025 release.<br/><br/>Please switch to the alternative: ExecuteGroovyScript.</td>
    </tr>
  </tbody>
</table>

# Known issues

The following is a list of known issues with the latest version of Databridge Pro. Many of these are outside the control of the Databridge Pro development team and relate to issues within particular browsers. Our team will pursue solutions to these issues in the future, but many will require changes in the associated browsers to accomplish this.

## List of known issues

There are no known issues with this version.

# Resolved issues

This document provides information about the issues resolved in this latest update of the Databridge Pro application.

Details of previous issues resolved in this year are not included in this document.

March 2025 production update

The following is a list of resolved issues that are included with this release of Databridge Pro.

# Resolved issues

Ports 4201 and 4202 have been opened for egress access with DataPower and SAP.

# Support, Copyright, and Legal Information

## Copyright Notice

### Copyright

Copyright © 2025-2026 Hexagon AB and/or its subsidiaries and affiliates.

This computer program, including software, icons, graphic symbols, documentation, file formats, and audio-visual displays; may be used only as pursuant to applicable software license agreement; contains confidential and proprietary information of Intergraph Corporation or a Hexagon Group Company and/or third parties which is protected by patent, trademark, copyright law, trade secret law, and international treaty, and may not be provided or otherwise made available without proper authorization from Hexagon AB and/or its subsidiaries and affiliates.

### U.S. Government Restricted Rights Legend

Use, duplication, or disclosure by the government is subject to restrictions as set forth below. For civilian agencies: This was developed at private expense and is "restricted computer software" submitted with restricted rights in accordance with subparagraphs (a) through (d) of the Commercial Computer Software ~~-~~ Restricted Rights clause at 52.227-19 of the Federal Acquisition Regulations ("FAR") and its successors, and is unpublished and all rights are reserved under the copyright laws of the United States. For units of the Department of Defense ("DoD"): This is "commercial computer software" as defined at DFARS 252.227-7014 and the rights of the Government are as specified at DFARS 227.7202-3.

Unpublished - rights reserved under the copyright laws of the United States.

Intergraph Corporation, Hexagon's Asset Lifecycle Intelligence Division
305 Intergraph Way

Madison, AL 35758

# Documentation

Documentation shall mean, whether in electronic or printed form, User's Guides, Installation Guides, Reference Guides, Administrator's Guides, Customization Guides, Programmer's Guides, Configuration Guides and Help Guides delivered with a particular software product.

# Other Documentation

Other Documentation shall mean, whether in electronic or printed form and delivered with software or on Smart Community, SharePoint, box.net, or the Hexagon documentation web site, any documentation related to work processes, workflows, and best practices that is provided by Hexagon as guidance for using a software product.

# Terms of Use

a. Use of a software product and Documentation is subject to the Software License Agreement ("SLA") delivered with the software product unless the Licensee has a valid signed license for this software product with Intergraph Corporation, Hexagon’s Asset Lifecycle Intelligence Division ("Hexagon"), a Hexagon Group Company. If the Licensee has a valid signed license for this software product with Hexagon, the valid signed license shall take precedence and govern the use of this software product and Documentation. Subject to the terms contained within the applicable license agreement, Hexagon gives Licensee permission to print a reasonable number of copies of the Documentation as defined in the applicable license agreement and delivered with the software product for Licensee's internal, non-commercial use. The Documentation may not be printed for resale or redistribution.

b. For use of Documentation or Other Documentation where end user does not receive a SLA or does not have a valid license agreement with Hexagon, Hexagon grants the Licensee a non-exclusive license to use the Documentation or Other Documentation for Licensee’s internal non-commercial use. Hexagon gives Licensee permission to print a reasonable number of copies of Other Documentation for Licensee’s internal, non-commercial use. The Other Documentation may not be printed for resale or redistribution. This license contained in this subsection b) may be terminated at any time and for any reason by Hexagon by giving written notice to Licensee.

# Disclaimer of Warranties

Except for any express warranties as may be stated in the SLA or separate license or separate terms and conditions, Hexagon disclaims any and all express or implied

warranties including, but not limited to the implied warranties of merchantability and fitness for a particular purpose and nothing stated in, or implied by, this document or its contents shall be considered or deemed a modification or amendment of such disclaimer. Hexagon believes the information in this publication is accurate as of its publication date.

The information and the software discussed in this document are subject to change without notice and are subject to applicable technical product descriptions. Hexagon is not responsible for any error that may appear in this document.

The software, Documentation and Other Documentation discussed in this document are furnished under a license and may be used or copied only in accordance with the terms of this license. THE USER OF THE SOFTWARE IS EXPECTED TO MAKE THE FINAL EVALUATION AS TO THE USEFULNESS OF THE SOFTWARE IN HIS OWN ENVIRONMENT.

Hexagon is not responsible for the accuracy of delivered data including, but not limited to, catalog, reference and symbol data. Users should verify for themselves that the data is accurate and suitable for their project work.

## Limitation of Damages

IN NO EVENT WILL HEXAGON BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL, INCIDENTAL, SPECIAL, OR PUNITIVE DAMAGES, INCLUDING BUT NOT LIMITED TO, LOSS OF USE OR PRODUCTION, LOSS OF REVENUE OR PROFIT, LOSS OF DATA, OR CLAIMS OF THIRD PARTIES, EVEN IF HEXAGON HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

UNDER NO CIRCUMSTANCES SHALL HEXAGON'S LIABILITY EXCEED THE AMOUNT THAT HEXAGON HAS BEEN PAID BY LICENSEE UNDER THIS AGREEMENT AT THE TIME THE CLAIM IS MADE. EXCEPT WHERE PROHIBITED BY APPLICABLE LAW, NO CLAIM, REGARDLESS OF FORM, ARISING OUT OF OR IN CONNECTION WITH THE SUBJECT MATTER OF THIS DOCUMENT MAY BE BROUGHT BY LICENSEE MORE THAN TWO (2) YEARS AFTER THE EVENT GIVING RISE TO THE CAUSE OF ACTION HAS OCCURRED.

IF UNDER THE LAW RULED APPLICABLE ANY PART OF THIS SECTION IS INVALID, THEN HEXAGON LIMITS ITS LIABILITY TO THE MAXIMUM EXTENT ALLOWED BY SAID LAW.

## Export Controls

To the extent prohibited by United States or other applicable laws, Intergraph Corporation, Hexagon's Asset Lifecycle Intelligence division ("Hexagon"), and a Hexagon Group

Company's commercial-off-the-shelf software products, customized software, Technical Data, and/or third-party software, or any derivatives thereof, obtained from Hexagon, its subsidiaries, or distributors must not be exported or re-exported, directly or indirectly (including via remote access) under the following circumstances:

a. To Cuba, Iran, North Korea, Syria, or the Crimean, "Donetsk People's Republic", "Luhansk People's Republic," or Sevastopol regions of Ukraine, or any national of these countries or territories.

b. To any person or entity listed on any United States government denial list, including, but not limited to, the United States Department of Commerce Denied Persons, Entities, and Unverified Lists, the United States Department of Treasury Specially Designated Nationals List, and the United States Department of State Debarred List. Visit www.export.gov for more information or follow this link for the screening tool: https://legacy.export.gov/csl-search.

c. To any entity when Customer knows, or has reason to know, the end use of the software product, customized software, Technical Data and/or third-party software obtained from Hexagon, its subsidiaries, or distributors is related to the design, development, production, or use of missiles, chemical, biological, or nuclear weapons, or other un-safeguarded or sensitive nuclear uses.

d. To any entity when Customer knows, or has reason to know, that an illegal reshipment will take place.

Any questions regarding export/re-export of relevant Hexagon software product, customized software, Technical Data, and/or third-party software obtained from Hexagon, its subsidiaries, or distributors, should be addressed to Hexagon’s Export Compliance Department, 305 Intergraph Way, Madison, Alabama 35758 USA or at exportcompliance@hexagon.com. Customer shall hold harmless and indemnify Hexagon and a Hexagon Group Company for any causes of action, claims, costs, expenses and/or damages resulting to Hexagon or a Hexagon Group Company from a breach by Customer.

# Trademarks

Intergraph®, the Intergraph logo®, Intergraph Smart®, SmartPlant®, SmartMarine, SmartSketch®, Intergraph Smart® Cloud, PDS®, FrameWorks®Plus, I-Route, I-Export, Isogen®, Intergraph Spoolgen®, SupportManager®, SupportModeler®, SAPPHIRE®, TANK®, PV Elite®, CADWorx®, CADWorx DraftPro®, GT STRUDL®, CAESAR II®, and HxGN SDx® are trademarks or registered trademarks of Intergraph Corporation or its affiliates, parents, subsidiaries. Hexagon and the Hexagon logo are registered trademarks

of Hexagon AB or its subsidiaries. Other brands and product names are trademarks of their respective owners.

## Customer Support and Technical User Forum

For the latest support information for this product, use a web browser to connect to the Smart Community <https://hexagon.com/support-success/asset-lifecycle-intelligence/community>. You can submit any documentation comments or suggestions you might have by logging on to our documentation web site at <https://docs.hexagonali.com>.

## Hexagon Policy Against Software Piracy

When you purchase or lease Hexagon’s Asset Lifecycle Intelligence division software, Hexagon, or its affiliates, parents, subsidiaries retains ownership of the product. You become the licensee of the product and obtain the right to use the product solely in accordance with the terms of the Intergraph Corporation, doing business as Hexagon’s Asset Lifecycle Intelligence division, Software License Agreement and applicable United States and/or international copyright laws.

You must have a valid license for each working copy of the product. You may also make one archival copy of the software to protect from inadvertent destruction of the original software, but you are not permitted to use the archival copy for any other purpose. An upgrade replaces the original license. Any use of working copies of the product for which there is no valid Intergraph Corporation, doing business as Hexagon’s Asset Lifecycle Intelligence division, Software License Agreement constitutes Software Piracy for which there are very severe penalties. All Hexagon software products are protected by copyright laws and international treaty.

If you have questions regarding software piracy or the legal use of Hexagon software products, please call the Legal Department at 256-730-2362 in the U.S.

Updated June 2022

Document No. DDGL562C0

## Copyright

Copyright © Hexagon AB and/or its subsidiaries and affiliates. All rights reserved.