# HxGN EAM Databridge System Administrator

Hexagon Documentation

Generated 02/28/2026

# HxGN EAM Databridge System Administration

This document provides conceptual information on HxGN EAM Databridge.

### Intended Audience

This document is intended for system administrators, implementation consultants, product architects, and support specialists.

### Prerequisite knowledge

To fully understand the information presented in this document, you should first be familiar with the HxGN EAM products.

### Organization

This table shows the sections of the guide:

<table>
  <thead>
    <tr>
        <th>Section</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Installation tasks</td>
        <td>Instructions on installing the components, application server, installing on multiple servers, and configuration.</td>
    </tr>
    <tr>
        <td>System administrator tasks</td>
        <td>Instructions on setup, configuration, and system administration.</td>
    </tr>
    <tr>
        <td>Message management</td>
        <td>Instructions on using the message management features to administer processes for inbound and outbound events.</td>
    </tr>
    <tr>
        <td>General ledger process administration</td>
        <td>Instructions on managing and administering general ledger information, managing account detail information, and Flex SQL.</td>
    </tr>
  </tbody>
</table>



## Installation tasks

Install the EAM application server to install Databridge. The EAM installation enables you to install and configure the messaging services and Databridge components necessary for running Databridge.

### Installing Databridge

Databridge is installed during installation of the base EAM product by selecting to install the EAM messaging services and Databridge components through which Databridge operates. There are two types of installation scenarios for messaging services: single server and multiple server. See the following descriptions for more information:

*   Single server - A single server installation scenario involves the use of a single messaging provider. We strongly recommend using this method.
*   Multiple server - A multiple server messaging service installation scenario involves connecting to multiple messaging service providers by Databridge servers. This method is only applicable for specific environment requirements.

Because Databridge is installed as an extension of the base product, the Databridge installations documented in this section are intended to provide a basic overview of the Databridge installation with information specifically relevant to both the single and multiple server installation scenarios. The installation examples for both the single and multiple server installations are based on a Databridge installation being installed for an Oracle database on Windows using a JBoss application server.

> **NOTE** Although Databridge and EAM application server can be installed on the same application server, we strongly recommend installing Databridge on different application server(s) than the EAM application server.

© 2026-2027, Hexagon AB <https://hexagon.com/company/divisions/asset-lifecycle-intelligence> and/or its subsidiaries and affiliates
12.3.0.2
Published Monday, February 16, 2026 at 7:38 PM

Before installing Databridge, you must formulate an installation plan, which involves evaluating the system load, determining the number of machines/servers determining, the number of message queues, etc., by which you will determine the type of Databridge installation that is appropriate for your organization.

> NOTE You must identify the machines on which you will be installing the message queue(s), because the manner in which you enter the address for the message queue(s) is platform dependent.

## Installing on a single server

Install Databridge to connect to a single messaging service provider.

> NOTE See the for more information on installing EAM.

1. Insert the EAM CD, and run the installation.

    > NOTE If you are installing on Windows, locate and right-click `Setupwin32.exe` file, and run as an administrator.

    If you are installing on UNIX and auto mount is not in use, mount the CD. Then, in a shell session, change the directory to the root of the mount point, and launch the system by executing the following command: `./setuplinux.bin`. Ensure that you run the installation as a non-root user.

2. Select a language to be used for this wizard, and then click OK.

3. Click Next.

4. Specify the EAM CD key, and then click Next.

5. Select **I accept the terms of the license agreement** if you agree to the terms, and then click Next.

6. Select **I accept the terms of the license agreement** if you agree to the terms, and then click Next.

    If you are installing EAM on a Windows application server, the following dialog box is not displayed. Proceed to step 8.

7. Select **JBoss Application Server**, and then click Next.

8. Specify the directory in which to install the EAM application, and then click Next.

    > NOTE The directory in which you install EAM cannot have a name that contains spaces. For example, C:\My Files is not a valid directory; however, C:\MyFiles is valid.

9. Specify this information about the database server:

    - **Host Name** - Specify the name of the machine on which the database server resides.
    - **Port** - Specify the listener port number associated with the database server.
    - **Instance Name** - Specify the name of the database instance.
    - **Schema Name** - Specify the Oracle schema under which the system application will run.
    - **User Password** - Specify the password for the schema specified above.

10. Click Next.

11. Specify this information about the Java Virtual Machine:

    - **JVM Min Size (MB)** - Specify the minimum amount of memory to allocate to the Java Virtual Machine when running EAM.
    - **JVM Max Size (MB)** - Specify the maximum amount of memory to allocate to the Java Virtual Machine when running EAM. For production servers, set the JVM Min Size (MB) equal to the value selected for JVM Max Size (MB).

    > NOTE The actual memory usage is the value you entered in JVM Min Size (MB) plus 768 MB and the value you entered in JVM Max Size (MB) plus 768 MB.

12. Click Next.

13. Do you want to install EAM Advanced Reporting Server? Choose one of these options:

<table>
  <tbody>
    <tr>
        <td>Option</td>
        <td>Description</td>
    </tr>
    <tr>
        <th>Yes</th>
        <th>Select to connect the application server to the EAM advanced reporting server.</th>
    </tr>
    <tr>
        <th>No</th>
        <th>Select if you do not want to connect the application server to the EAM advanced reporting server.</th>
    </tr>
  </tbody>
</table>

> **NOTE** The advanced reporting server is not installed. It is configured to connect to a report server. If you selected yes to connect the application server to a report server, the next dialog box shown (not documented here) helps you configure the advanced reporting server details.

See the for more information on installing the Advanced Reporting Server.

14. Click **Next**.

15. Select **Yes** to install messaging services for operating Databridge.

16. Click **Next**.

17. In **Select the type of messaging services to install** field, select **Standard single user** to install the messaging services on the same server as the HxGN EAM application server.

18. Click **Next**.

19. Choose one of the following options to determine if the computer will host Databridge transactions:
    - **Yes** - Select if the computer on which you are installing Databridge will also host the Databridge transactions.
    - **No** - Select if you do not want to host the Databridge transactions on the computer on which you are installing Databridge.

    > **NOTE** The next dialog box is displayed **only** if you selected **Yes**.

20. Click **Next**.

21. Specify this directory information:
    - **Partner Documents Folder** - Specify the directory in which to store Databridge partner documents when exchanging files with Databridge.
    - **Setup Files Folder** - Specify the directory in which to install the Databridge partner setup files used for exchanging files with Databridge.

22. Click **Next**.

23. Click **Next**.

24. To start the application, choose one of the following options:

    > **NOTE** Before you start the server, see Adjusting database connection pool size for additional setup steps.

    * **Run the application on Windows** - Reboot your machine. The EAM application automatically starts when **Windows** starts.
    * **Run the application on Linux** - To control the application server, navigate to the application home installation directory selected during the installation. Start the server by executing:
      `./app.sh start`
      To stop the server, execute:
      `./app.sh stop`
      To stop and then restart the server, execute:

./app.sh restart

To check the status of the server, execute:

./app.sh status

25. Click Finish.

# Installing on multiple servers

Install Databridge for connecting to multiple messaging providers.

> **NOTE** This installation scenario does not apply to most cases. It is used for specific environment requirements where messaging servers are provided by separate individual providers.

1. Insert the EAM CD, and then run the installation.

> **NOTE** If you are installing on Windows, locate and right-click setupwin.exe file, and run as an administrator.

If you are installing on UNIX and auto mount is not in use, mount the CD. Then, in a shell session, change the directory to the root of the mount point, and launch the system by executing the following command: ./setuplinux.bin. Ensure that you run the installation as a non-root user.

2. Select a language to be used for this wizard, and then click **OK**.

3. Click **Next**.

4. Specify the EAM CD key, and then click **Next**.

5. Select **I accept the terms of the license agreement** if you agree to the terms, and then click **Next**.

6. Select **I accept the terms of the license agreement** if you agree to the terms, and then click **Next**.

> **NOTE** If you are installing EAM on a Windows application server, the following dialog box is not displayed. Proceed to step 8.

7. Select **JBoss Application Server**, and then click **Next**.

8. Specify the directory in which to install the EAM application, and then click **Next**.

> **NOTE** The directory in which you install EAM cannot have a name that contains spaces. For example, C:\My Files is not a valid directory; however, C:\MyFiles is valid.

9. Specify this information about the database:

- **Host Name** - Specify the name of the machine on which the database server resides.
- **Port** - Specify the listener port number associated with the database server.
- **Instance Name** - Specify the name of the database instance.
- **Schema Name** - Specify the Oracle schema under which the system application will run.
- **User Password** - Specify the password for the schema specified above.

10. Click **Next**.

11. Specify this information about the Java Virtual Machine:

- **JVM Min Size (MB)** - Specify the minimum amount of memory to allocate to the Java Virtual Machine when running EAM.
- **JVM Max Size (MB)** - Specify the maximum amount of memory to allocate to the Java Virtual Machine when running EAM. For production servers, set the JVM Min Size (MB) equal to the value selected for JVM Max Size (MB).

> **NOTE** The actual memory usage is the value you entered in JVM Min Size (MB) plus 768 MB and the value you entered in JVM Max Size (MB) plus 768 MB.

12. Click **Next**.

13. Select No in Do you want to install HxGN EAM Advanced Reporting Server?, and then click Next.

> NOTE See EAM Installation for more information on installing the Advanced Reporting Server for EAM.

14. Select Yes in Do you want to install messaging services?, to install messaging services for operating Databridge.

15. Click Next.

16. Select Advanced multi-server in Select the type of messaging services to install to install the messaging services for multiple servers.

17. Click Next.

18. Choose one of the following options in Will this computer host the Databridge transactions?:

- Yes - Select if the computer on which you are installing Databridge will also host the Databridge transactions.
- No - Select if you do not want to host the Databridge transactions on the computer on which you are installing Databridge.

19. Click Next.

20. Specify this directory information:

- Partner Documents Folder - Specify the directory in which to store Databridge partner documents when exchanging files with Databridge.
- Setup Files Folder - Specify the directory in which to install the Databridge partner setup files used for exchanging files with Databridge.

21. Click Next.

22. Choose one of the following options in Will this computer host a message queue?:

- Yes - Select if the computer on which you are installing the application server will also host a message queue.
- No - Select if you do not want to host a message queue on the computer on which you are installing the application server.

> NOTE For most installations, you will select Yes. However, you may want to select No for installation situations in which you are installing a large number of application servers for which you will only want to install JMS queues on a limited number of those application servers.

23. Click Next.

24. In Enter the address for message queue host server(s), specify the address of the application server(s) that are hosting message queue(s). Use a comma (,) to separate multiple addresses, e.g., usgv1002-machine:1099, usgv1003-machine2:1099, etc.

See the following example for more information:

- For a JBoss installation: - The address is in the form of <server name>:<JBoss JNDI port number>, e.g., usgv1002-machine:1099, usgv1003-machine2:1099, etc.

25. Click Next.

26. Click Next.

27. To start the application, choose one of the following options:

> NOTE Before you start the server, see Adjusting database connection pool size for additional setup steps.

- Run the application on Windows - Reboot your machine. The EAM application automatically starts when Windows starts.
- Run the application on Linux - To control the Application Server, navigate to the application home installation directory selected during the installation. Start the server by executing:

```
./app.sh start
```

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD3141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF BELARUS
FOR A
BELARUS EDUCATION MODERNIZATION PROJECT - ADDITIONAL FINANCING
MARCH 27, 2019

Education Global Practice
Europe And Central Asia Region

> This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**CURRENCY EQUIVALENTS**
(Exchange Rate Effective Feb 28, 2019)
Currency Unit = Belarusian Ruble (BYN)
BYN 2.14 = US$1
US$ 1.39 = SDR 1

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

# Enabling additional outbound event options

Enable or disable additional outbound events using installation parameters included in EAM. See EAM system administrator tasks for more information on installation parameters. The additional outbound event options provide you with more flexibility in implementing your integration scenarios.

See the table in Appendix A - Databridge Setup options with corresponding install parameters and values for a list and description of the Databridge installation parameters that enable all available Databridge outbound events. Values for these parameters are typically Y or N, indicating Yes or No. Additional parameter options and exceptions are noted as applicable.

## Defining account details definitions for Databridge setup

A multi-segment account code (account details) can be constructed when a requisition line item is created in HxGN EAM. This account code is important when a requisition is sent into a purchasing application. Specify the structure of the account to make it compatible with the account of the purchasing application. Define account details to define each segment of the account. HxGN EAM allows three segments in the account details.

1. Select **Administration > Databridge > Databridge Setup**.
2. Click the **Account Details Definition** tab.
3. Specify this information:

    **Segment 01** - Select one of the following accounts as the value of the first segment:
    - Organization
    - Store/Department
    - Cost Code
    - Fixed Value

    > **NOTE** If Fixed Value is selected, enter a value for Segment 01 Value.

    **Segment 02** - Select one of the following accounts as the value of the second segment:
    - Organization
    - Store/Department
    - Cost Code
    - Fixed Value

    > **NOTE** If Fixed Value is selected, enter a value for Segment 02 Value.

    **Segment 03** - Select one of the following accounts:
    - Organization
    - Store/Department
    - Cost Code
    - Fixed Value

    > **NOTE** If Fixed Value is selected, enter a value for Segment 03 Value.

    - Segment 01 Value - Specify a value for the Segment 01 account if Fixed Value is selected in Segment 01.
    - Segment 02 Value - Specify a value for the Segment 02 account if Fixed Value is selected in Segment 02.
    - Segment 03 Value - Specify a value for the Segment 03 account if Fixed Value is selected in Segment 03.

4. Click **Save Record**.

# Configuring Databridge partners

Configure the partners of your Databridge network to enable communication between Databridge and its integration partners. By default, the Databridge installation auto-populates the system with predefined partners. You can add additional partners as necessary.

See the following descriptions of the predefined partners:

<table>
  <tbody>
    <tr>
        <td>Partner</td>
        <td>Description</td>
    </tr>
    <tr>
        <th>My enterprise (*)</th>
        <th>The "My enterprise" partner represents your enterprise (HxGN EAM) to which to connect the external application using Databridge.<br/><br/>NOTE The * code assigned is used as the Partner code for the HxGN EAM system. You can modify the partner Description as necessary, but you cannot delete this record.<br/><br/>You must select an HxGN EAM user as the Databridge system user, and then enter the user ID and password of that user for the * (My enterprise) partner. DATABRIDGEINTERNALUSER is preset as the Databridge system user.</th>
    </tr>
    <tr>
        <th>Default integration partner (2)</th>
        <th>The "Default integration partner" (2) represents the partner server with which Databridge communicates, e.g., an ERP system.</th>
    </tr>
    <tr>
        <th>Infor ION partner (INFOR-ON- RAMP)</th>
        <th>The built-in connection to Infor ION for integration with other Infor applications using Infor SOA. See *HxGN EAM Configuration for Infor ION and Data Lake* for complete instructions on configuring Databridge to connect to Infor ION.<br/><br/>Do not delete any of the predefined partner records.</th>
    </tr>
    <tr>
        <th>Infor ION IMS partner (INFOR-IMS)</th>
        <th>The built-in connection to Infor ION with IMS or IMS via API Gateway connector for integration with other Infor applications using Infor SOA. See *HxGN EAM Configuration for Infor ION* for complete instructions on configuring Databridge to connect to Infor ION.</th>
    </tr>
    <tr>
        <th>Hexagon Databridge Pro partner (HXGN-DFS)</th>
        <th>The built-in connection to Hexagon Databridge Pro for integration between EAM and other applications using Infor SOA.<br/><br/>Do not delete any of the predefined partner records. In the Cloud, when the HXGN-DFS partner is enabled, the INFOR-ONRAMP and INFOR-IMS partners must be disabled.</th>
    </tr>
  </tbody>
</table>

1. Select **Administration > Databridge > Databridge Partners**.
2. Select the partner to configure, and then click the **Record View** tab.

> NOTE Active must be selected for the * partner for any outbound documents to be generated. You can clear this flag to temporarily stop the generation of outbound documents. The events occurring during the period when the flag is unselected are stored, and the outbound document is generated for them when the flag is selected.

When the Active flag is unselected for one of the other partners, the inbound documents from that partner are not be accepted by Databridge.

3. Specify this information:

*   **Description** - Specify or modify the description for your enterprise if necessary.
*   **Partner ID** - Modify the ID code by which to identify the partner in the business documents exchanged with the partner. This code is the LOGICALID in a Databridge document sent or received through Databridge.
*   **Default Organization** - Specify the organization of your enterprise.
*   **User ID** - Specify a code to identify the Databridge server user to be used for partner authentication for messages received by the Databridge HTTP web server. If this field is left blank, the partner is not required to include authentication information (user ID/password) in its HTTP requests sent to Databridge.
*   **Password** - Specify the password for the Databridge server user.
*   **Special Handling** - Specify a customized processor for special handling of logging into the Databridge server. For most cases leave this field blank.

> **NOTE** If you are upgrading from version 2.x, the value specified for **User ID** and **Password** must be identical to your WebMethods server user ID and password.

*   **HxGN EAM User ID** - Specify the user ID code identifying the HxGN EAM user. All inbound Databridge transactions from the partner are processed using the EAM user specified by this user ID.
*   **HxGN EAM Password** - Specify the password for the HxGN EAM user.

> **NOTE** For the * partner, you must enter the HxGN EAM User ID and HxGN EAM Password for the HxGN EAM user selected as the system user of the Databridge server. For other partners, you must enter an HxGN EAM User ID and HxGN EAM Password for an HxGN EAM user to run business transactions for the partner.

*   **Address** - For inbound processing, enter the URL to which to send the ConfirmBOD. For outbound processing, enter the default URL to which to send outbound documents.

> **NOTE** If you are upgrading from a previous version of Databridge, the value entered for **Address** must be the URL of the webMethods Integration Server used to receive messages. The values entered for **Login ID** and **Login Password** fields must be the webMethods Integration Server administrator's user ID and password.

If you are sending outbound documents to a file folder location using the Databridge partner file utility, enter PartnerFile into Address, and leave Login ID and Login Password blank.

*   **Login ID** - Specify the code used to log into the receiving system.
*   **Login Password** - Specify the password used to log into the receiving system.

> **NOTE** If you are upgrading from a previous version of Databridge, the values entered for **Login ID** and **Login Password** must be the webMethods Integration Server administrator's user ID and password.

If you are sending outbound documents to a file folder location using the Databridge partner file utility, enter PartnerFile into the Address field, and leave the following Login ID and Login Password blank.

See Sending and receiving Databridge document files later in this section of the document for information about Databridge document files and partner file utility.

*   **Response Special Handling** - Specify a customized processor for special handling of the delivery of messages to the partner's receiving system.
*   **Retry Count** - Specify the maximum number of times for the Databridge server to attempt to resend data to the partner (receiving system).
*   **Retry Interval (min.)** - Specify the amount of time to wait between repeated attempts to send data.
*   **Publication Format** - Optionally, select `XML` or `JSON` as the publication format for the partner record. The default value is `XML`.

> NOTE This field is protected unless the partner record is HXGN-DFS.

If JSON is selected, **Address** in the Response Details section cannot be INFOREAMIOBOX.

4. Click Save Record.

## Setting up partner processing retry schedules

Set up the message processing retry schedule for the partner. See Reprocessing and redelivering messages.

1. Select Administration > Databridge > Databridge Partners.
2. Select the partner to configure, and then click the Record View tab.
3. Specify this information:
    - **1st Retry again in [hh:mm]** - Specify the Hours and Minutes indicating the interval of time after which the system is to make the first attempt to reprocess messages.
    - **2nd Retry again in [hh:mm]** - Specify the Hours and Minutes indicating the interval of time after which the system is to make the second attempt reprocess messages.
    - **3rd Retry again in [hh:mm]** - Specify the Hours and Minutes indicating the interval of time after which the system is to make the third attempt to reprocess messages.
    - **4th Retry again in [hh:mm]** - Specify the Hours and Minutes indicating the interval of time after which the system is to make the fourth attempt to reprocess messages.
    - **5th Retry again in [hh:mm]** - Specify the Hours and Minutes indicating the interval of time after which the system is to make the fifth attempt to reprocess messages.
4. Click Save Record.

## Setting up partner subscriptions

Set up partner subscriptions for the partner to indicate the outbound transactions/documents that the partner receives.

1. Select Administration > Databridge > Databridge Partners.
2. Select the partner for which to view subscriptions, and then click the Subscriptions tab.
3. Select an event from the Subscriptions list.

> NOTE The current version of Databridge supports only the subscriptions that are provided by Databridge. If you choose to delete a transaction, you can use the add subscription feature to add the deleted transaction back to the system. To add a partner subscription record, click Add Subscription.

4. Select the Enabled check box to enable the event.
5. Specify this information:
    - **Address** - Specify the URL to which outbound documents are sent for the selected event. Only enter an address here if you want outbound messages to be delivered to a different location for this transaction than the one specified for the partner on the Record View page.
    - **User ID** - Specify the user ID for logging into the receiving system to which outbound documents are sent. Only enter value here if you want something different for this transaction than the one specified for the partner on the Record View page.
    - **Password** - Specify the password for the Databridge server user. Only enter a value here if you enter a value for User ID.
    - **Special Handling** - Specify the customized processor for special handling the delivery of outbound events.
6. Click Submit.

# Adding inbound document types for the INFOR-IMS partner

Add or view inbound document types for the INFOR-IMS partner.

> NOTE This tab supports the INFOR-IMS partner only.

1. Select Administration > Databridge > Databridge Partners.
2. Select the INFOR-IMS partner, and then click the Inbound Documents tab.
3. Click Add Inbound Document.
4. Specify this Inbound Document Details information:
   - **Inbound Document Type** - Specify the type of inbound document being added.
     - Optionally, select the **Enabled** check box to enable the events the INFOR-IMS partner receives for the inbound document type.
   - **Special Handling** - Optionally, specify the customized processor for special handling of the delivery of outbound events for the inbound document.
5. Click Submit.

## Configuring partner files

Databridge server hosts a Databridge partner file utility that allows Databridge document messages to be exchanged with other systems through files. A message to be sent to Databridge can be placed in a file in a folder to be picked up by Databridge, and outbound messages from Databridge can be stored to a folder as files, to be further processed by other programs, such as a partner job.

Before the Databridge partner file utility can function, you need to perform the following configurations.

### Setting up the locations of partner file folders

The following folders are used by Databridge partner file utility:
- **Partner Document Folder** - A folder to store Databridge document messages files. Message documents sent to or received from Databridge on behalf of Databridge partners are stored as files in this folder.
- **Setup Files Folder** - Partner configuration files, such as partner.xml, are stored in this folder.

The locations of these folders are configured when Databridge is deployed. The default locations are specified for Setup Files Folder and Partner Documents Folder during the Databridge installation.

See Installation tasks.

Typically, the partner documents folder is `<Application Root Folder>/PartnerService/data`, and the setup files folder is `<Application Root Folder>/PartnerService/conf`, where `<Application Root Folder>` is where the HxGN EAM application is installed. For example `c:\EAM\PartnerService\data` is a typical default Partner Document Files folder.

The steps included in this section document the process to set a different location for partner files if necessary. If you do not want to move these files to a new location, you do not need to complete these steps.

1. Open `databridge_properties.xml` file under `<Application Root Folder>/depconfig`.
2. Locate the following XML fragment:

```xml
<PartnerService>
<Document home="c:/HxGNEAM/PartnerService/data"></Document>
<Configuration home="c:/HxGNEAM/PartnerService/conf"></Configuration>
<Language>EN</Language>
</PartnerService>
```

The home attribute of the Document element specifies the folder location of the Partner Document Files folder, and the home attribute of the Configuration element specifies the folder location of the Partner Configuration Files folder.

3. Update the folder location. You can store these folders independently on the Databridge server hard disk or on network file servers.

4. Redeploy the HxGN EAM application of the Databridge server.

See EAM system administrator tasks for information on redeploying the HxGN EAM application.

## Configuring the network user for Databridge

If you are running the Databridge server in a Windows environment and you have configured the partner file folder to be on a network file server, you must set the network user for the Windows service that runs the HxGN EAM application so that Databridge can access these folders.

1. Select **Start > Control Panel > Administrative Tools > Tools**.

2. Double-click **HxGN EAM Application**.

3. Log into the application.

4. Specify this information:

    - **This account** - Specify the network user.
    - **Password** - Specify the network user password.
    - **Confirm password** - Specify the network user password to confirm password was entered correctly.

> **NOTE** To access the partner documents and setup file folders, the network user must have write permissions to these folders.

5. Click **OK**.

## Setting the message delivery address

For a Databridge outbound message to be delivered to a file location using Databridge file utility, set the message delivery address to PartnerFile. This is done at the partner level.

1. Log into the HxGN EAM application.

2. Select **Administration > Databridge > Databridge Partners**.

3. Select the partner for which to set the delivery address, and then click the **Record View** tab.

4. Specify this information:

    - **Address** - Specify PartnerFile.

5. Click **Save Record**.

## Changing the default tenant for a partner

An HxGN EAM server may use multiple tenants so that it can be used for different databases. By default, an HxGN EAM server has one tenant, DS_MP_1. Each Databridge partner should be associated with a defined tenant.

1. Open the partner.xml file under the partner configuration files folder.

2. For each partner defined in Databridge, there should be a `<Partner>` section, as shown in the following example of XML fragment:

```
<Partner>
<ProfileID>2</ProfileID> 
<DocumentDeliveryClass>com.dstm.databridge.receiver.DocumentJMSRouter</DocumentDeliveryClass>
```

<Tenant>DS_MP_1</Tenant> 
<DatabridgeServerURL>http://www.infor.com/toDatabridge</Databridge ServerURL> 
<User>R5</User> 
<Password>R5</Password> 
<SenderID>2</SenderID> 
<ReceiverID>1</ReceiverID> 
</Partner>

3. Set the value for each of the following elements:

- **Tenant** - Set the element value to match your HxGN EAM tenant into which the Databridge documents are sent.
- **SenderID** - Specify the same value as the ProfileID element.
- **ReceiverID** - Specify the Partner ID field value of the * partner record found on the HxGN EAM Partners form.

4. Click **Save Record**. The change will take effect in several minutes.

## Configuring the endpoint catalog for Databridge partners

Create a centralized endpoint catalog in EAM to configure and manage integration network connections; establishing communication "connections" between EAM, Databridge Pro, and third-party delivery applications or endpoints.

Define the endpoint connections and corresponding authorization protocols to enable Databridge Pro to communicate with external systems. Databridge Pro uses these endpoints as final destinations to route transformed information between systems. The EAM Endpoint Catalog icon in Databridge Pro provides access to the tenant catalog defined inside the EAM application.

1. Click **Administration > Databridge > Databridge Partners**.
2. Select the HXGN-DFS partner record to configure DFS catalog endpoints, and then click the **DFS Catalog** tab.
3. Click **Add Catalog Record**.
4. In the **Catalog** section, specify this information:
   - a. **Description** - Enter a description of the endpoint.
   - b. Optionally, click the **Active** check box to make the endpoint record available in Databridge Pro.

> ★ **IMPORTANT** If the **Active** check box is cleared at any time, it does not affect the previous or current connections in Databridge Pro.

5. In the **Endpoint Definition** section, specify this information:

> 📝 **NOTE** See the HxGN EAM Integrating with Databridge Pro technical brief for more information on the selection of Type, Method, Processor Type, the system assigned Endpoint Databridge Pro Processor, and the relevant Endpoint Properties.

   - a. **Type** - Select the type of endpoint connection. Some options include **AWS Kinesis**, **Azure Blob Storage**, **Azure DataLake Storage**, **HTTPS - General**, **S3**, **SFTP**, and **Smb File**.
   - b. **Method** - Select the endpoint method. Some options include: **Consume**, **Delete**, **Fetch**, **Get**, **List**, **Move**, **Put**, and **HTTP Method**.
   - c. **Processor Type** - Select the specific processor type.

6. In the **Endpoint Properties** section, specify this information:

> 📝 **NOTE** The fields in this section are optional and yet important for mapping purposes when configuring connection points.

* Amazon Kinesis Stream Name
* Application Name
* Region
* Access Key ID
* Secret Access Key
* Container Name
* Blob Name
* Blob Name Prefix
* HTTP Method
* HTTP URL
* Amazon Region
* Amazon Gateway Api ResourceName
* Amazon Gateway Api Endpoint
* Request Username
* Request Password
* Filesystem Name
* Directory Name
* File Name
* Filesystem Object Type
* Source Filesystem
* Destination Directory
* Bucket
* Object Key
* Hostname
* Password
* Remote File
* Remote Path
* File Filter Regex
* Input Directory
* Share
* Directory
* Domain

7. Click **Submit**.
    a. Optionally, select one of these options:
        i. **Reset** - Click the **Reset** button to check the record's utilization in Databridge Pro.
        ii. **UUID References** - A UUID reference signifies the record's inclusion in Databridge Pro and potential usage. Each instance of the catalog record will produce its own unique UUID reference.

> **NOTE** UUID References are generated only after adding the Catalog record in Databridge Pro. If the record remains unadded and unused, no UUIDs will be displayed.

## Viewing UUID reference details for endpoint catalog records

Access the **UUID References** pop-up window to view the unique identifiers assigned by Databridge Pro.

1. Click **Administration > Databridge > Databridge Partners**.
2. Select the HXGN-DFS partner record, and then click the **DFS Catalog** tab.
3. Select an endpoint catalog record.
4. Click the **Actions** drop-down, and then click **UUID References**.
5. View the information.

> **NOTES** UUIDs are generated and assigned to Endpoint Catalog records by Databridge Pro each time an endpoint (processor) record is referenced in a defined data flow. If an endpoint catalog record is referenced twice in a single Databridge Pro process flow, the endpoint catalog record is assigned two UUID reference values.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD3141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF BELARUS
FOR A
BELARUS EDUCATION MODERNIZATION PROJECT - ADDITIONAL FINANCING
MARCH 27, 2019

Education Global Practice
Europe And Central Asia Region

> This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**CURRENCY EQUIVALENTS**
(Exchange Rate Effective Feb 28, 2019)
Currency Unit = Belarusian Ruble (BYN)
BYN 2.14 = US$1
US$ 1.39 = SDR 1

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

# Connecting to Databridge using HTTP

A Databridge partner application can send inbound messages and receive outbound messages to and from Databridge using HTTP protocol. This connection is ideally suited for a service-oriented architecture (SOA) because it does not involve any files, file storage, or batch style processing, allowing for a quicker response time and more reliable message exchanging.

## Sending a message using http to Databridge

Databridge uses a basic HTTP authentication header to carry the user ID and password for logging in. The user ID and password must match the user ID and password created for the partner record in the Databridge Login section of the Databridge **Partners** form.

See Configuring Databridge partners

* With the user credentials, set the HTTP authentication header using the following format:
  `addRequestHeader(HTTPConstants.HEADER_AUTHORIZATION, "Basic " + based64Encode(userid + ":" + password);`
* Set the Databridge document into the HTTP message as a named value pair with name="$xmldata" and value=the Databridge document XML.
* Send the HTTP message to the following address:
  `http://<databridge server address>/axis/servlet/DatabridgeReceiverServlet?TenantID=<tenant>`

If the Databridge server receives the message successfully, it responds with an HTTP OK status (200) and response text that carries the message ID allocated to the message.

> **NOTE** This message only indicates that the message has been received by the Databridge server. It does not indicate the message processing status.

If the Databridge server does not receive the message successfully for any reason, it will respond with a HTTP status failure code, such as HTTP 500. Possible reasons for the failure may include improperly formed Databridge XML, invalid partner or login information. The HTTP response text will carry more specific error information to help with debugging the issue that resulted in failure.

## Receiving a Databridge message in a HTTP request from Databridge

The partner must have a web server that provides an URL for receiving Databridge HTTP messages, including Databridge outbound documents, and the processing status messages (CONFORM BOD) that indicate the processing status for inbound messages.

Additionally, you must enter the web server access information in the Response Details section of the Databridge Partners form as displayed in the screen shot below.

See Configuring Databridge partners.

The response detail information must include the following:

<table>
  <thead>
    <tr>
        <th>Detail</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Address</td>
        <td>The URL of the HxGN EAM/Databridge web server.</td>
    </tr>
    <tr>
        <td>User ID</td>
        <td>The user ID to log into the web server receiving messages.</td>
    </tr>
    <tr>
        <td>Password</td>
        <td>The password of the **User ID**.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
        <td>Retry Count</td>
        <td>The number of retries the Databridge server should carry out if the receiver fails to receive the message.</td>
    </tr>
    <tr>
        <td>Retry Interval</td>
        <td>The number of minutes to wait between each retry attempt.</td>
    </tr>
  </tbody>
</table>

If you have different web server access information for s specific Databridge outbound document subscription, you can enter the information listed above on the Subscriptions page of the Partners form. See Setting up partner subscriptions.

> **NOTE** Information entered **Subscription** page will overwrite the one entered in the Response Details section on the **Record View**.

The format of an incoming message from Databridge is the same as the information described above for sending a message to Databridge.

If the receiving web server receives the message successfully, it must respond with HTTP OK status (200). If not, it must respond with an HTTP failure code that includes error information to help the operator with troubleshooting. If **Retry Count** and **Retry Interval** are set as indicated above, Databridge will attempt to resend the message if the receiver responds with a HTTP failure status.

## Linking to Databridge Remote Agent

Databridge Remote Agent is a server-based application installed separately from a Databridge server. Link to the Databridge Remote Agent in order for Databridge and other applications (partners) to exchange messages.

Databridge has to communicate over the Internet or WAN, the Databridge Remote Agent can be installed in the LAN with a partner application to perform the partner functions while communicating with the Databridge server remotely. It is typically used by hosted users of Databridge with HxGN EAM.

Databridge is preconfigured to use local partner file utility, but it can be set up to communicate with Databridge Remote Agent server if necessary.

See the HxGN EAM Databridge Help for Remote Agent for information on installing and configuring Databridge Remote Agent.

1. Select **Administration > Databridge > Databridge Partners**.
2. Select the partner to which the outbound messages are to be sent to a Databridge Remote Agent server (Typically this partner is 2.), and then click the **Record View** tab.
3. Specify this information:
   **Address** - Specify the URL of the Databridge Remote Agent server. For example, http: //MyRemoteAgent/partnerser vice/receiver.
4. Specify the **Login ID** and **Login Password** if required by the destination specified in **Address**.
5. Specify **Retry Count** and **Retry Interval** to set up a retry pattern. **Retry Interval** specifies the time interval in minutes between retries, and **Retry Count** specifies the maximum number of retries.
6. Click **Save Record**.

## Setting up partner subscriptions for Databridge Remote Agent

Set up subscriptions for the partner to indicate the outbound transactions/documents that the partner receives.

1. Select **Administration > Databridge > Databridge Partners**.
2. Select the partner for which to set up subscriptions, and then click the **Subscriptions** tab.
3. Select an event from the Subscriptions list.
4. Specify this information:
   **Event** - Enter EJCRON.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

<table>
  <thead>
    <tr>
        <th>Status</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>I</td>
        <td>In Progress</td>
    </tr>
    <tr>
        <td>C</td>
        <td>Completed</td>
    </tr>
    <tr>
        <td>F</td>
        <td>Failed</td>
    </tr>
  </tbody>
</table>

## Viewing message details

1. Select **Administration > Databridge > Databridge Message Status**.
2. Select the message for which to view the details, and then click the **Record View** tab.
> **NOTE** Search for specific outbound events using the search parameters. See information on defining quick filters in the EAM user tasks.
3. View the message processing, delivery, and retry details.

## Viewing XML documents for messages

1. Select **Administration > Databridge > Databridge Message Status**.
2. Select the message for which to view the XML documents, and then click the **Record View** tab.
> **NOTE** Search for specific Outbound Events using the search parameters. See information on defining quick filters in the HxGN EAM User Guide.
3. Click **View** for either the Processing Details or Delivery Details.
4. View the XML document information, and then close the pop-up window.

## Viewing related messages

Related messages are messages for which the **Context ID** or **Correlation ID** values are the same. For example, a single outbound event generates a Databridge event message and several Databridge delivery messages that have the same **Context ID**. Therefore, the messages are related.

1. Select **Administration > Databridge > Databridge Message Status**.
2. Select the message for which to view related messages, and then click the **Related Messages** tab.
> **NOTE** Search for specific Outbound or Inbound Events as necessary using the search parameters. See information on defining quick filters in the HxGN EAM User Guide.

The Related Messages list is automatically populated with all message records for which the **Context ID** is equal to the selected message.

3. Select the related message, and then click **Record View**.
4. View the related message information, and then click **Close**.

## Viewing processing history for messages

Each time a request message is processed or a sub-data area of a message, a processing history record is stored in the database and the record(s) are displayed on the **Processing** page of the **Message IDs** form. If a message does not have multiple sub-data areas, Time Processed, Status, and Status Message display the same values as the corresponding fields on the primary message status record. Data Area is always blank.

When a message is processed one sub-data area at a time, the processing status of each sub-data area is recorded. While the sub-data area is processing, the status information of the main record reflects the overall status of the sub-data area. Time Processed is populated with the time that the last sub-data area was processed.

1. Select **Administration > Databridge > Databridge Message Status**.

2. Select the message for which to view processing history, and then click the **Processing** tab.

> **NOTE** Search for specific Outbound or Inbound Events using the search parameters. See the information on defining quick filters in the HxGN EAM User Guide.

3. View the processing history for the message.

## Viewing delivery history for messages

Each time an attempt is made to deliver a response/outbound message or a sub-data area of a message to the destination, a delivery history record is stored in the database and the record(s) are displayed on the **Delivery** tab of the **Message IDs** form.

If a message does not have multiple sub-data areas, Time Delivered, Status, and Status Message display the same values as the corresponding fields on the primary message status record. Data Area is always blank.

When a message is delivered one sub-data area at a time, the delivery status of each sub-data area is recorded. While the sub-data area is processing, the status information of the main record reflects the overall status of the sub-data area. Time Delivered is populated with the time that the last sub-data area was delivered.

Address is populated with the actual URL or other destination to which the message or the sub-data area was delivered. Multiple addresses (URLs) can be associated with the destination. The last address to which the delivery attempt for the message failed displays and nothing displays if the address is not applicable.

1. Select **Administration > Databridge > Databridge Message Status**.

2. Select the message for which to view the delivery history, and then click the **Delivery** tab.

> **NOTE** Search for specific Outbound or Inbound Events using the search parameters. See the information on defining quick filters in the HxGN EAM User Guide.

3. View the delivery history for the message.

## Viewing Databridge Pro events for Databridge messages

1. Select **Administration > Databridge > Databridge Message Status**.

2. Select the message record, and then click the **Dataflow Events** tab.

> **NOTE** The primary message status record must be associated with the HXGN-DFS partner to view the information on this tab.

3. View the information captured for events generated from Databridge Pro.

## Reprocessing and redelivering messages

Reprocess transactions to re-route a document if Databridge does not process a transaction successfully.

Automatic attempts to reprocess a message are made if the **Processing Status** of the message is F (Failed) or PF (Partially failed) and if it is determined that the type of processing error requires it to be reprocessed. A record needs to be reprocessed if the processing failed due to a system/environment error or a business logic error. F processing status is assigned if all parts of the message fail. PF status is assigned to a message for which some parts of the processing failed, but not all.

Automatic attempts to re-deliver a message for request processing and response delivery are made, regardless of the current delivery status. However, a message is only qualified for re-delivery if the **Delivery Status** is F and if it is determined that the message needs to be re-delivered. It is determined that a record needs to be re-delivered if the delivery failed due to a system/environment error or a business logic error. TN status is assigned if a message has been successfully delivered to the trading network but has not yet completed the delivery cycle. TN status is only assigned to messages in a hosted Databridge installation (using Infor's ASP services).

Automatic attempts to reprocess qualified messages are made based on the following incremental schedule:

- An attempt to reprocess is made after 5 minutes
- A second attempt to reprocess is made 10 minutes after the first attempt
- A third attempt to reprocess is made 60 minutes after the second attempt
- A fourth attempt to reprocess is made 5 hours after the third attempt
- A fifth attempt to reprocess is made 24 hours after the fourth attempt
- After the fifth attempt to reprocess the record, no further automatic attempts to reprocess the record are made, which is indicated if Next Scheduled Retry is empty. However, you can manually attempt to reprocess records as necessary. See Reprocessing and redelivering messages manually.

> **NOTE** Next Scheduled Retry is based on the Processing Retry Schedule defined for the Databridge partner on the Partners form. See Configuring Databridge partners, Setting up partner processing retry schedules, and Setting up partner subscriptions.

## Reprocessing and redelivering messages manually

Several different options are provided for manually reprocessing records because of the failure or partial failure of messages.

### Reprocessing messages using the retry mechanism

1. Select **Administration > Databridge > Databridge Message Status**.
2. Select the message to reprocess, and then click the **Record View** tab.

> **NOTE** Search for specific Outbound or Inbound Events using the search parameters. See information on defining quick filters on the HxGN EAM User Guide.

3. Click **Retry** for either the Processing Details or Delivery Details.

> **NOTE** Retry is only enabled if the current Processing Status or Delivery Status requires reprocessing or if a message needs to be reprocessed. See Reprocessing and redelivering messages.

### Reprocessing multiple messages simultaneously

1. Select **Administration > Databridge > Databridge Message Status**.
2. Click **Retry Messages**.
3. Select the records to reprocess, and then click **Submit**.

The messages are reprocessed and the pop-up is closed. If a message is unable to process, then an error is displayed for the unsuccessful record in the Error Message column of that record.

> **NOTES**
>
- To select all the lines at once, check **Select**. To clear all the lines at once, clear the **Select** check box. Search for specific Outbound or Inbound Events using the search parameters. See the information on defining quick filters in the HxGN EAM User Guide.
- If Retry Schedule Suspended is selected for the record, the message is reprocessed based on the automatic retry schedule established on the **Partners** form. See Configuring Databridge partners, Setting up partner processing retry schedules, and Setting up partner subscriptions.
- Retry is only enabled if the current Processing Status or Delivery Status requires reprocessing or if it is determined that a message needs to be reprocessed. See Reprocessing and redelivering messages.

## Reprocessing and redelivering messages automatically

Several different options are provided for automatically reprocessing records because of the failure or partial failure of messages.

# Suspending the reprocessing schedule for multiple messages simultaneously

1. Select Administration > Databridge > Databridge Message Status.
2. Click Suspend Retry Schedule.
3. Select the records for which to suspend reprocessing, and then click Submit. The automatic reprocessing of the messages is suspended, *Retry Schedule Suspended* is selected for the records, and then the popup is closed.

# Resuming the reprocessing schedule for multiple messages simultaneously

1. Select Administration > Databridge > Databridge Message Status.
2. Click Resume Retry Schedule.
3. Select the messages for which to resume reprocessing, and then click Submit. The automatic reprocessing of the messages is suspended, *Retry Schedule Suspended* is unselected for the records, and then the popup is closed.

# Archiving and removing message status records

To prevent the tables storing message status information from becoming too large over time, the status records for old messages are archived. By default, status information is archived for messages with C (Completed) status for both processing and delivery, and for messages that have F (Failed) status for processing and/or delivery for which no further attempts to reprocess the message will be made. If install parameter @MSGARCA is set to Y, all old message status records will be archived regardless of their status. See Reprocessing and redelivering messages.

Status record information is archived, stored, and purged based on the following schedule:

- Message status records are archived 3 months after the message processing is completed. The setting of the @MSGARC installation parameter indicates the length of time for message archiving for Databridge. You can update the setting of the installation parameter in EAM as necessary. The value for @MSGARC is in number of days.
- Message status records are purged from the archive 15 months after message processing is completed. The setting of the @MSGDEL installation parameter indicates the length of time for message deleting for Databridge. You can update the setting of the installation parameter in EAM as necessary. The value for @MSGDEL is in number of days.

> NOTE See EAM system administrator tasks for information on these installation parameters.

# Message content storage

By default, the message contents are stored in CLOB fields in Oracle database or NTEXT fields in Microsoft SQL Server database. It sometimes becomes inconvenient to reduce database table spaces after large amount of old messages are purged in the system. We provide an alternative message content storage option that every message content will split into multiple records of regular CHAR fields with the setting of @MSGSPLT install parameter to Y.

- @MSGSPLT=N: Message Content is stored as a whole record in R5WSMESSAGES table's CLOB or NTEXT field. This is default setting.
- @MSGSPLT=Y: Message Content is stored as split blocks in R5WSMESSAGE LINES table's CHAR field.

# General ledger process administration

During normal business processing, HxGN EAM performs some basic transactions that affect the balancing of general ledger accounts. The Journal Entry Post batch XML transaction allows external ERP systems to import transactions from HxGN EAM to close the books and balance accounts. Depending on the transactions implemented, HxGN EAM maintains ownership of different transaction types. For each transaction executed in HxGN EAM, account code combinations need to be generated with Flex SQL for the expense account on the ERP application's general ledger. Setting up GL Process definitions and references for each transaction set allows ERP applications to import the transaction records for closing procedures by providing both the expense and offset accounts.

You can access Databridge features from the HxGN EAM Administration menu. See "Menu Bar" in the HxGN EAM User Guide.

However, depending on your system configuration, the Databridge administration pages may not be enabled. Contact your system administrator for additional information. See "Setting Up Menus for User Groups" in the HxGN EAM System Administrator Guide for additional information.

## Managing general ledger information

Manage general ledger information to define the processes and references necessary for exporting transaction data to an external general ledger and creating journal entries for the corporate accounting system. View general ledger values.

## Defining general ledger processes

Define parameters to enable general ledger processes to dynamically construct an SQL select statement to transfer transaction information from EAM to an ERP application. Dynamic SQL enables you to configure the selection and processing of EAM transactions based on the needs of your organization.

> **NOTE** The examples in this section use notations specific to Oracle database and PL/SQL. If your EAM database is Microsoft SQL Server, please use the MS SQL Server equivalent.

1. Select **Administration > Databridge > GL Process Definitions**.
2. Click **New Record**.
3. Specify this information:

    - **GL Process Definition** - Specify a unique code identifying the GL process definition, and then enter a description in the adjacent field, e.g., DS ISSUES.

        > **NOTE** The process you are creating should determine the unique code you enter. Commonly, the unique code refers to the combination of the process and group. For example, if you are creating an issue from store process for the GVL store, enter ISSUE_GVL.

    - **Row Identity** - Specify a unique record identifier for the row in the source database table for the general ledger process, e.g., r5translines.ROWID.

        > **NOTE** You must use the token row identifier ROWID to identify the source row in the database table.

    - **Scheduling Group** - Specify the table column name identifying the grouping value for the general ledger process, e.g. TRL_TYPE.

        > **NOTE** Scheduling groups often share relevant common values that are used in building the Where Statement for the process definition. Scheduling Group is also used on the GL References form to establish the financial application changes within the group.

    - **Journal Entry Category** - Specify a unique value identifying the ERP journal entry category for the feed reference group, e.g., trl_JECATEGORY. See your organization's financial manager for the correct value.

    - **Journal Entry Source** - Specify a unique value identifying the ERP journal entry source for the feed reference group, e.g., trl_JESOURCE. See your organization's financial manager for the correct value.

    - **Summary** - Select to include a summary for the general ledger process.

    - **Set of Books ID** - Specify the code identifying the ERP general ledger set of books for the feed reference group, e.g., tra_org. See your organization's financial manager for the correct code. If you use multiple sets of books, there - must be a relationship between the process definition and the reference group that classifies the correct - set of transactions.

    - **Date** - Specify the date to use for the general ledger journal entries. You can enter either the date of the original transaction, e.g., TRL_DATE, the date of the transaction transfer, e.g., SYSDATE, or the date identifying the end of the financial period for the transaction.

    - **Amount** - Specify the calculation for the monetary value of the transaction, e.g., TRL_PRICE * TRL_QTY or TRL_PRICE * TRL_QTY * 1.15 if an overhead factor is used in costing.

        > **NOTE** Use positive and negative values as necessary.

**Segments** - Specify the account code segments for the journal entries. If you have multiple segments activated on the ERP Accounting Definition, you must enter all the segments in this field, e.g.,, ACD_SEGMENT1, ACD_SEGMENT2, ACD_SEGMENT3, ACD_SEGMENT4,ACD_SEGMENT5, ACD_SEGMENT6,ACD_SEGMENT7.

> **NOTE** If you enter more than one segment, do not include conjunctive statements such as "and."

**From Statement** - Specify the EAM source table(s) required to meet all of the process definition constraints. You must enter at least the R5ACCOUNTDETAIL table and one transaction table, e.g.: r5translines, r5accountdetail, r5transactions.

> **NOTE** Do not include the word FROM in the text of the From Statement.

**Where Statement** - Specify the "where" condition clause. The "where" condition clause is dependent on the process definition. You must enter constraints for the join statement of all tables listed and for the values for XXX_GLTRANSFER and XXX_GLTRANSFERFLAG, which are used to prevent records from being submitted more than once, e.g.:

```
trl_acd = acd_code AND NVL(trl_gltransferflag, '-') = '-' AND tra_code = trl_trans AND tra_rstatus = 'A' and tra_type = 'I' and trl_type = 'I' and trl_event is not null and trl_QTY>0
```

The XXX_GLTRANSFER and XXX_GRTRANSFERFLAG columns are updated using the Source Update Statement. Therefore, you should limit the usage of the Source Update Statement within the Where Statement condition clause. For example, for a basic Where Statement for an issuance process that requires R5TRANSLINES and R5ACCOUNTDETAIL, you would enter trl_acd = acd_code and nvl(trl_gltransferflag,'+') != '+' and trl_rtype = 'I'.

> **NOTE** Do not use a semicolon as the terminator or include the word WHERE in the text of the Where Statement.

**Source Update Statement** - Specify an SQL statement to update the row in the transaction source table.

This statement flags a transaction record as processed so that it is not processed again. You must include the token :ROWID or :rowid in the statement.

See the following example of a source update statement that flags a transaction record as having been processed so that it is not processed again.

```
UPDATE r5translines SET trl_gltransferflag = '+', trl_gltransfer = sysdate WHERE rowid =:rowid
```

**Destination Update Statement** - Specify an SQL statement to update the R5GLINTERFACE table to contain the reference information required on the journal import. The Destination Update Statement populates reference fields in the R5GLINTERFACE table with custom information required for the installation. For example, include the stock code, description, and work order number for an inventory issue transaction in a reference field.

This reference information is then included in the journal entry. See the following example of a destination update statement that uses two tokens. One is :transid, which references the appropriate row in R5GLINTERFACE. The second is :rowid, which references the transaction source row identifier. The transaction source row identifier is used to retrieve additional transaction reference information.

```
Declare
Cursor C1 is
SELECT substr(v.PRV_VALUE,1,3) company, substr(v.PRV_VALUE,5,4) GLS, substr(v.PRV_VALUE,10,5) DEP,
substr(v.PRV_VALUE,16,6) EXP, substr(v.PRV_VALUE,23,4) PL , substr(v.PRV_VALUE,28,3) IC,
substr(v.PRV_VALUE,32,6) FU
from
R5TRANSLINES L, R5PROPERTYVALUES V
where l.rowid = :rowid
and v.prv_property (+) = 'INVOFF' and v.PRV_RENTITY (+) = 'STOR'
and v.PRV_CODE (+) = l.trl_store;
BEGIN
```

```sql
FOR r IN C1 LOOP
UPDATE r5glinterface
SET gli_segment1 = r.company, gli_segment2 = r.GLS,
gli_segment3 = r.DEP, gli_segment4 = r.EXP
WHERE gli_transid = :transid
and gli_segment2 = '****' ; END LOOP;
end;
```

4. Click **Save Record**.

## Defining general ledger references

Define general ledger reference information for your defined general ledger processes. Define references for each potential group value within a feed process.

1. Select **Administration > Databridge > GL References**.
2. Click **New Record**.
3. Specify this information:

    **GL Process Definition** - Specify the general ledger process definition code for which to define general ledger references, e.g., DS Issues.

    **Status** - Specify `NEW` as the status for the feed reference group. Because the journal import processes all new status records and updates Status if an error occurs, all general ledger references must start with a status of new.

    **Scheduling Group Value** - Specify the value identifying the general ledger process group.

    > **NOTE** Create only one entry for each transaction type. If you selected the column TRL_RTYPE for Scheduling Group Value when defining the general ledger process, you must select **I** (Issuance), **STTK** (Stocktakes), etc., when defining the general ledger references.

    **Journal Entry Category** - Specify a unique value identifying the ERP journal entry category for the feed reference group, e.g., `DS ISSUES`. See your organization's financial manager for the correct value.

    **Journal Entry Source** - Specify the value identifying the ERP journal entry source for the feed reference group, e.g., `HXGN`. See your organization's financial manager for the correct value.

    **Set of Books ID** - Specify the code identifying the ERP general ledger set of books for the feed reference group, e.g., 1. See your organization's financial manager for the correct code. If you use multiple sets of books, there must be a relationship between the process definition and the reference group that classifies the correct set of transactions.

    > **NOTE** The combination of GL Process Definition, Scheduling Group Value, Journal Entry Category, Journal Entry Source, and Set of Books ID represent the primary key that uniquely identifies the feed reference set for the selected column.

    **Financial User ID** - Specify the ERP user ID for the process group, e.g., `ERP-USER`.

    **Currency** - Specify the code identifying the currency for this feed reference group, e.g., `USD`.

    **Actual Flag** - Select one of the following options as the type of ERP batch for this process group:

<table>
  <thead>
    <tr>
        <th>Option</th>
        <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Actual</td>
        <td>Indicates that the values for the batch for this process group are the actual values.</td>
    </tr>
    <tr>
        <td>Budget</td>
        <td>Indicate that the values for the batch for this process group are the budgeted values.</td>
    </tr>
  </tbody>
</table>

Encumbrance Indicates that the values for the batch for this group are dependent values.

4. Click Save Record.

## Defining details for general ledger references

Define details for general ledger references to create values for each segment of a general ledger reference.

1. Select Administration > Databridge > GL References.
2. Click the Details tab.
3. Specify this information:
    - **Segment Column** - Select the appropriate column of the GL_INTERFACE table to use for the reference group, e.g., SEGMENT1.
    - **User Value** - Specify the user-defined value(s) for the feed reference group for the R5GLINTERFACE column(s), e.g., 01.

    Values must be assigned to all segment values defined on the Accounting definition of the ERP general ledger. These are the offset accounting combinations for the process/reference group. Each process group collects the expense account from the R5ACCOUNTDETAIL table; this page provides the second half of the accounting requirement.

4. Click Submit.

## Viewing and modifying general ledger values

View and modify general ledger values to access the internal general ledger values associated with system entities. Select an entity for which to view/modify general ledger values, view the associated general ledger codes, and update or delete the values as necessary.

The Accounted field indicates whether the general ledger value is a Credit or a Debit, and is always protected. The ACCOUNT installation parameter determines whether the Accounted field is required for GL values. If the ACCOUNT installation parameter is set to NO, then the system automatically populates Accounted with the (*) value.

> **NOTE** You can also copy an existing record to create a new record based on the existing record's key fields. Select the record to copy, and then click Copy Record. The system copies the key fields from the selected record and enters insert mode enabling you to update Record Details as necessary. The system populates Accounted with the opposite value of the record from which you are copying (Credit or Debit), and the field is protected. You cannot copy records for which the value of Accounted is (*).

The key fields displayed on the GL Values form are updated dynamically based on the Entity you select. For example, if you select Requisitions as the Entity, the system displays the Requisition Number and Organization as the key fields in Record Details and the GL Values list.

1. Select Administration > Databridge > GL Values.
2. Specify this information:
    - **Entity** - Select the entity for which to view and modify the general ledger values. The system displays the key fields associated with the selected entity in Record Details and updates the values list with all of the general ledger values associated with the selected entity.

    > **NOTE** If you select a new Entity after modifying a record without saving the changes, the system displays a warning message. If you click Cancel, the system refreshes the form based on the new Entity and the system retains the original values for the originally selected Entity without saving any changes.

3. Select the general ledger value to view or modify.
4. Edit the general ledger value information as necessary.
5. Click Submit.

# Administering general ledger processes

Administer general ledger (GL) processes to view schedule information for running GL processes on the Integration Server, enter and/or update schedule information, check schedule information, and/or remove schedules.

> **NOTE** You are a hosted (partner server) customer, you must contact EAM Hosting Services to schedule running a GL process to ensure that proper resources for running the GL process are planned and allocated by Hosting Services. Contact EAM Support in Hexagon Smart Community <https://smartcommunity.hexagonppm.com/> for more information about contacting Hosting Services.

## Viewing general ledger processes

View general ledger (GL) processes to view a list of existing GL processes and/or view detailed scheduling information for GL processes on the Integration Server. See Defining general ledger processes.

1. Select **Administration > Databridge > GL Process**.
2. View the list of GL processes, and then select the GL process for which to view existing scheduling information on the Integration Server.
3. Click the **Record View** tab.
4. View the GL process schedule information.

## Checking schedule information for general ledger processes

Check schedule information for general ledger (GL) processes to view existing scheduling information for running an existing GL process on the Integration Server.

1. Select **Administration > Databridge > GL Process**.
2. Select the GL process for which to check schedule information, and then click the **Record View** tab.
3. Click **Check Schedule**. The GL process schedule information is displayed in Schedule.

## Adding general ledger process schedule information

Add general ledger (GL) process schedule information to create or update scheduling information on the Integration Server to specify when to run existing GL processes. See Defining general ledger processes.

If you add new schedule information for GL processes, the existing schedule information for the process on the Integration Server is replaced with the new schedule information.

1. Select **Administration > Databridge > GL Process**.
2. Select the GL process for which to check schedule information, and then click the **Record View** tab.
3. Click **Check Schedule**. The existing schedule information is displayed on the Integration Server for the selected GL process.
4. Specify this information:
    - **Run on Day(s) and of the month at** - Select the day(s) of the month on which to run the GL process, and then select the time of the day at which to run the GL process.
5. Click **Add Process**. The schedule information for running the GL process is added to the Integration Server and updates Schedule.

## Removing existing schedule information for general ledger processes

Remove existing schedule information for general ledger (GL) processes to unschedule a GL process run on the Integration Server.

1. Select **Administration > Databridge > GL Process**.
2. Select the GL process for which to remove schedule information, and then click the **Record View** tab.
3. Click **Check Schedule**. The existing schedule information is displayed on the Integration Server for the selected GL process.

4. Click **Delete Process**. The existing process on the Integration Server is stopped, and Schedule is updated.

# Creating journal entries

Journal entries for EAM transactions are passed to ERP using the Journal Entry Post batch transaction. Before creating journal entries, consider the following issues:

- Whether more than one process is needed within a source, e.g., inventory transactions

    The GL process definitions are dynamically created in EAM for each customer, and multiple processes may be necessary within a journal source. With inventory, for example, this could be the relationship between inventory holding accounts and transaction expense accounts.

- Whether separate processes based on your organization, facility, or storeroom are required

    For example, in many cases the storeroom relates to a unique holding account on the chart of accounts. Therefore, each storeroom would require its own process.

- Whether the journal entries need more than one set of books or chart of accounts

    Remember that the set of books, journal source, journal category, and organization are all input on the **GL References** form, and this form is a sub component to the process definition defined on the **GL Process Definition** form. The process definition has to be configured to make use of the reference details, which have control over the set of books, journal source, journal category, and organization.

- How the journal entries will be grouped within a source. For example, inventory processes could be grouped by transaction type or by a combination of transaction type and storeroom, or by part class.

    When building reference details, you can use the Scheduling Group values on the **GL Process Definitions** form to divide the entries. Establishing the reference requirements will build the conditional parameters for the **Where Statement** on the **GL Process Definitions** form.

- How dates will be assigned for journal entries. Options include the date of the original transaction, the date the transaction was transferred to the ERP application, or the period end date.

- What monetary value the journal should have. Specify the straight transaction price multiplied by the transaction quantity. You can also include an overhead factor, if necessary.

- What determines the expense account segment values for a particular transaction.

    > **NOTE** Determining the expense account segment value is required for building the Flex SQL.

- What determines the offset account segment values for a particular transaction.

    The offset account is the second portion of the accounting transactions conducted solely in the EAM application. For example, consider requisitions generated in EAM that interface to and ERP applications where they are turned into purchase orders. Because the requisition feeds a purchasing process that is owned by the ERP application, there is no offset requirement in EAM. Contrast this with inventory transactions where EAM solely owns the issuance of inventory and the inventory management. When an issuance generates an expense cost against a charge account, it must also provide the offset account for import into the general ledger.

- Which filters should be applied when selecting transactions to transfer. These filters will drive the parameters necessary in the Where Statement on the **GL Process Definitions** form. The filters are dependent on many of the variables mentioned in this section.

- What detailed information about a transaction should be recorded in the journal entry, such as the work order number, part number, and/or asset number. This information will be used in **Destination Update Statement** on the **GL Process Definitions** form. The open interface for Journal Imports allows for transaction-specific data to be stored in reference fields. The reference data would be a component of the process and transaction group being interfaced.

# Managing account detail information

Manage your organization's account detail information to define account detail requirements and actually define account detail code combination for interface transactions.

# Defining account detail requirements for Oracle General Ledger

Define your organization's account detail (code combination) requirements for interface transactions. ERP applications typically provide a flexible accounting structure that enables you to customize general ledger account codes.

For both Flex SQL configuration and the General Ledger Feed process, each segment on the ERP General Ledger must have a corresponding segment value defined in EAM. These definitions are determined during the Financial Interface Scope Task.

> **NOTE** We highly recommend a qualified EAM technical services consultant assist in this process.

1. Define your organization's chart of accounts structure in the ERP application. Your chart of accounts structure outlines the account code segments required for conducting your business transactions.

2. Review the EAM business transactions that have a financial effect on your organization.

3. Define accounting requirements for each business transaction identified during the previous step. When defining these requirements, consider the number of account code segments required by your organization. Additionally, consider what values are allowed for account code segments, as well as the expected and default values for each account code segment. Identify routine cases, special cases, and validation requirements for each account code segment.

4. Determine your organization's method for collecting information required to create actual account code segments. When determining this method, try to achieve a balance among the effort required to set up the account code segments, the effort of entering and maintaining the segments in the system, the accuracy of the segments, and the amount the segments conform with your organization's fiscal policies. Consider who will be entering transaction information, what decisions must be made for each transaction, and what information is and should be available to the responsible party as they make decisions for each business transaction.

> **NOTE** Infor strongly recommends that you derive values for account code segments from entities within EAM. For example, most charts of accounts include an organizational component, such as departments or cost centers. Map departments in EAM to account code segments for your departments or cost centers, or define an object structure in EAM that corresponds to your organizational department and cost center structure.

If your chart of accounts contains a project segment as a cost center, use EAM project/budget codes to supply project segments by creating custom attributes for the PROJ (R5PROJECTS) entity in EAM to store the account code segment values for one or all project account code segments.

You should also consider creating user attributes in EAM that will store the account segment values. Creating these attributes allows you to enter the segment values without hard coding them into the fixed EAM tables.

## Defining account detail codes

Define account detail codes for your general ledger accounts. The degree of detail included in your account detail definition is specific to the business practices of your organization. For example, your general ledger may include the following segments: segment 1-1400-000 identifies your Organization, 1-1300-100 identifies your Accounts Receivable for Future Payments, 1-3300-000 identifies your fixed assets, etc. Create account code segments for each of these codes. You can also associate Flex SQL query codes with account codes. Flex SQL codes identify SQL query statements that are used to manipulate and validate data related to the account code segment in the database. After defining account detail codes, the codes are associated with transactions in the system at the entity level (such as purchase orders, invoices, etc) and are used to link system transactions with external accounting systems.

See Defining account details in the EAM system administrator tasks.

1. Select **Administration > Databridge > Account Detail Setup**.

2. Click **New Record**.

3. Specify this information:

    **Segment Column** - Specify the segment column used to store an account segment value in the R5ACCOUNTDETAIL table.

    > **NOTE** You can only create one record for each Segment Column.

    By default, the 30 available segment columns have non-specific names, e.g., ACD_SEGMENT1. You can change the name of a segment column using screen designer on the Account Details page of the forms for which account details are accessible

within the system.

**Query Code** - Specify the query code for the account detail code. Query codes are defined on the Queries form. See Defining queries in the EAM system administrator tasks.

**NOTES**
- The system enables you to reference another account segment within the SQL code list of values.
- To reference segment 2 inside the code you are defining, enter: 2.

**Default Value** - Specify the default value for the segment column.

**Required** - Select to indicate that the entry of the segment column is required.

4. Click **Save Record**.

## Understanding Flex business rules

Flex SQL is an application method to create database triggers (post-insert or post-update) to validate, insert, or update all HxGN EAM database objects. Flex SQL is used manually through the definition of SQL*Plus or PL/SQL statements. The primary function of these statements is to create and update account details for interface transactions, validate transactions for business process compliance, and customize HxGN EAM to meet the needs of your organization.

Specifically, creating and updating account details is required for any transaction originates in HxGN EAM that will be interfaced to the external (third-party) application. See these topics:

- Defining account detail requirements for Oracle General Ledger
- Defining general ledger processes
- Defining general ledger references

Flex SQL must be written in SQL*Plus or PL/SQL syntax. SQL*Plus is Oracle's tool for issuing database-level programming commands, and it is based on Structured Query Language (SQL). SQL enables you to insert, update, query, or delete database records with a simple language syntax. SQL statements begin with a command word, followed by a specification of what information to select within the command, followed by the object from which to select the information. The query is generally terminated with a semicolon (;). For the purposes of Flex SQL usage, the semicolon (;) terminator should always be left out. The syntax is dynamically compiled and executed so that the terminator is not required.

See the following example of syntax:

```
insert into r5accountdetail
acd_code, acd_rentity, acd_segment1, acd_segment2)
select rql_acd, 'REQ1', '01', rql_expensetype
from r5requislines
where rowid = :rowid
```

Flex SQL also utilizes a second type of structured query language called Programming Language/Structured Query Language (PL/SQL). PL/SQL is used to process commands in blocks, rather than using individual SQL statements. Blocks are groups of related SQL statements that can be nested inside larger blocks, which allows you to organize your SQL syntax to perform several commands at once.

See the following example of PL/SQL syntax:

```
DECLARE
cpar r5parts.par_code%type;
cref r5catalogue.cat_ref%type;
csupp r5companies.com_code%type;
cursor rql is
select rql_ref, rql_part, rql_supplier, rql_rstatus
```

from r5requislines
where rowid = :rowid;

BEGIN
OPEN rql;
FETCH rql into cref, cpar, csupp, crstat;
CLOSE rql;
IF cref is not null
AND crstat = 'A' THEN
UPDATE r5catalogue
SET cat_ref = cref
WHERE cat_part = cpar
AND cat_supplier = csupp;
END IF;
END;

Both the SQL*Plus and the PL/SQL examples would be placed in SQL Statement on the Flex SQL form. In these examples, the R5REQUISLINES table is being triggered; the SQL*Plus example is a post-insert trigger, and the PL/SQL example is a post-update trigger.

## Enabling Flex business rules on EAM transaction tables

If you are using HxGN EAM (Oracle Forms), you must manually enable Flex SQL functionality on the appropriate database tables in the HxGN EAM user schema that are used for Databridge integration/transactions. Flex SQL is primarily used to create and update account details for interface transactions. Because Flex SQL creates additional triggers on a table, it can also validate transactions for business process compliance and customize HxGN EAM to meet the needs of the business process for your organization.

> **NOTE** If you are using HxGN EAM or HxGN EAM for SQL Server, you do not need to manually enable Flex SQL, because Flex SQL is automatically activated on the database tables.

Enable Flex SQL for any table in the HxGN EAM user schema that is required to support the interface transactions being implemented. Every table in the HxGN EAM user schema is available for Flex SQL.

> **NOTE** The list of values in the Flex SQL tables form (YNFLXT) filters for tables beginning with R5.

Activating Flex SQL for a table creates two triggers in the HxGN EAM user schema, which adds "overhead" to the application. Balance the "overhead" caused by using Flex SQL with the interface business requirements.

1. Open the Flex SQL tables form (YNFLXT).
2. Select the Table for which to enable Flex SQL.
3. Select File > Save. The information is saved to the database.

> **NOTE** After enabling Flex SQL for the appropriate tables, you must define Flex SQL procedures for each of the tables for which you have enabled Flex SQL.

## Defining Flex business rules statements and procedures

Define Flex SQL statements to define validation rules that are specific to your organization. You can set up one or more statements to be processed for post-insert or post-update events.

Flex SQL processing supports data query (select) and data manipulation (insert, update, delete) statements. Use select statements to perform a check condition.

Uppercase and lowercase characters are allowed in the SQL statement. The row identifier token, however, must be either all uppercase or all lowercase (i.e., :ROWID or :rowid).

Every Flex SQL statement requires the use of a predefined :ROWID token. This token refers to the database row identifier for the record being processed in the specified table. The statement is executed for each record in the table affected by the insert or update operation.

The maximum statement length is 4000 characters. No statement termination character (;) is required.

Data manipulation statements are allowed, but make sure you do not begin an infinite cascading of trigger steps. For example, generally it is not recommended to create a Flex SQL statement that updates the base table identified in Table.

> NOTE We recommend that you define Flex SQL procedures in close cooperation with your HxGN EAM consultant.

1. Select Administration > Screen Configuration > Flex Business Rules.
2. Specify the Table for which to define Flex SQL statements and procedures.
3. Click Add Flex SQL.
4. Specify this information:

    - **Sequence Number** - Specify the order of Flex SQL processing.
    - **Trigger** - Specify the database operation that initiates the event. Post-insert and post-update triggers are supported.
    - **SQL Statement** - Specify the SQL statement to be executed when the specified operation takes place for a table.
    - **Failure Message** - Specify the message to display when the Flex SQL statement fails. A Flex SQL statement is successful when the statement processes one or more rows in a table. A Flex SQL statement fails when no rows are processed. To make the failure message active, select Abort on Failure.
    - **Comments** - Specify a description of the purpose of the Flex SQL statement.

5. Optionally, select the **Must Exist** check box to make the Flex SQL processor stop processing consecutive Flex SQL statements when the current statement processes no rows.

6. Optionally, select the **Abort on Failure** check box to stop the current operation when it fails and issue an error.

7. Optionally, select the **Reverse Return Code** check box to reverse the return status code for the current Flex SQL statement. If selected and the statement processes one or more rows, then the processor returns with a failure status. If the statement processes no rows, then the processor returns a success status.

8. Optionally, select the **Active** check box to enable the Flex SQL statement.

9. Click Test Flex SQL to ensure that the current Flex SQL statement is valid. If the statement contains errors (invalid syntax, for example), a message is displayed.

10. Click Submit.

See the following examples of Flex SQL definitions:

**Example 1** - Specify check statements or edits that supplement standard HxGN EAM processing. For example, entering a value for cost code is optional when creating a requisition in HxGN EAM. If the implementation depends on the use of cost code to derive account segment values, you must define a check statement that does not allow updating or insertion of requisitions without entering a value for cost code.

See the following example of a check statement to supplement the standard processing of the creation of a requisition in HxGN EAM:

- Table - Specify R5REQUISITIONS.
- Trigger - Specify POST-INSERT.
- Sequence Number - Specify 10.
- SQL Statement - Specify the following SQL statement to be executed:

```
SELECT NULL
FROM R5REQUISITIONS
WHERE ROWID=:ROWID
AND REQ_COSTCODE IS NOT NULL
```

- Failure Message - Specify Please enter a value for cost code.
- Select Must Exist.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD3141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF BELARUS
FOR A
BELARUS EDUCATION MODERNIZATION PROJECT - ADDITIONAL FINANCING
MARCH 27, 2019

Education Global Practice
Europe And Central Asia Region

> This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**CURRENCY EQUIVALENTS**
(Exchange Rate Effective Feb 28, 2019)
Currency Unit = Belarusian Ruble (BYN)
BYN 2.14 = US$1
US$ 1.39 = SDR 1

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

<table>
  <thead>
    <tr>
        <th></th>
        <th>and Price Corrections<br/><br/>@UPDINV=A: Events are generated as necessary to support Hexagon ION integration<br/><br/>NOTE If you are configuring Databridge for Infor ION, @UPDINV must be set to A to enable the Inventory Transactions Outbound event for Infor ION. Set @UPDINV to E if all inventory transaction types are applicable for generating an outbound event.</th>
        <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>@UPDPTM</td>
        <td>Enable Labor Time Outbound<br/><br/>@UPDPTM=N: No events are generated<br/><br/>@UPDPTM=Y: Events are generated when personnel time is recorded</td>
        <td>Yes (Y)<br/>No (N)</td>
    </tr>
    <tr>
        <td>@WOCKLST</td>
        <td>Whether to include WO checklist in outbound MaintenanceOrder BOD associated with SYNCMAINTORDER event<br/><br/>@WOCKLST=N: WO Checklist detail is not included in the MaintenanceOrder BOD<br/><br/>@WOCKLST=Y: WO Checklist detail is included in the MaintenanceOrder BOD<br/><br/>NOTE If WOCKLST=Y, then @SYNCWO must be enabled (Y, A, or S)</td>
        <td>Yes (Y)<br/>No (N)</td>
    </tr>
    <tr>
        <td>@WOCLASS</td>
        <td>Enable CodeDefinition for MRO Class Outbound<br/><br/>@WOCLASS=N: No events are generated<br/><br/>@WOCLASS=Y: Events are generated when a Class record is added or updated for the Work Order entity</td>
        <td>Yes (Y)<br/>No (N)</td>
    </tr>
    <tr>
        <td>@WOEMPLB</td>
        <td>Enable Book Labor in Work Order outbound<br/><br/>@WOEMPLB=N: WO Book Labor detail is not included in the MaintenanceOrder BOD<br/><br/>@WOEMPLB=Y: WO Book Labor detail is included in the MaintenanceOrder BOD</td>
        <td>Yes (Y)<br/>No (N)</td>
    </tr>
  </tbody>
</table>

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.

**The World Bank**
**FOR OFFICIAL USE ONLY**
Report No: PAD4141

# INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT
# PROJECT APPRAISAL DOCUMENT
ON A
PROPOSED LOAN
IN THE AMOUNT OF US$100 MILLION
TO THE
REPUBLIC OF INDONESIA
FOR THE
INDONESIA HEALTH AND REFORM PROGRAM (I-HERP)
MAY 24, 2021

Health, Nutrition & Population Global Practice
East Asia And Pacific Region

This document has a restricted distribution and may be used by recipients only in the performance of their official duties. Its contents may not otherwise be disclosed without World Bank authorization.