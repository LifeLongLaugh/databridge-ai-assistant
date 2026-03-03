![](_page_0_Picture_0.jpeg)

# **EAM Databridge Pro What's New for 24.3.0**

**Hexagon Documentation** 

Generated 02/28/2026

## **Table of Contents**

What's new in Databridge Pro?

November 2024 production update

Support, Copyright, and Legal Information

**Copyright Notice** 

Customer Support and Technical User Forum

Hexagon Policy Against Software Piracy

### What's new in Databridge Pro?

Check out what's new in the latest update of Databridge Pro.

This information is brief and not meant to be comprehensive.

For a full list of enhancements and changes in this latest update, see these documents:

Customer Support and Technical User Forum
Hexagon Policy Against Software Piracy

Copyright © 2024-2025, Intergraph Corporation <a href="https://hexagon.com/company/divisions/asset-lifecycle-intelligence">https://hexagon.com/company/divisions/asset-lifecycle-intelligence</a> and/or its subsidiaries and affiliates

ularies and animale

12.2

Published Friday, October 11, 2024 at 9:04 PM

### November 2024 production update

### New features and enhancements

### Several new screens were added to the Global Menu items

### **Certificate/Key Registry screen**

In the area of Private Certificate Registry, this screen enables the uploading and managing of private trust store or keystore certificates.

#### Password Policies screen

In the area of Tenant Password Policies, this screen allows the Administrator role to customize password policies for a tenant, including minimum length, character composition, and duration period.

■ NOTE Default password policies will be automatically implemented. As a result, existing users may be required to reset their password at login.

### **Enhancements to Dataflow Studio**

#### **Dataflow Studio (DFS) Cloud Connector service**

Several new components and screens were added to the DFS Cloud Connector service to facilitate integrations between Dataflow Studio Cloud and locally deployed or on-premises systems.

This includes:

- DFS Cloud Connector Locations New screen for managing locations of Connector instances in the local environment
- DFS Cloud Connector Downloads New screen for downloading the Cloud Connector package for local installation
- Cloud Connector Process Group New check box in the Process Group window to designate the group for use with a Cloud Connector
- Cloud Connector Broker New icon on the Component Toolbar which facilitates communication between a Cloud Connector in the local infrastructure and Dataflow Studio in the Cloud

# New processor added for use with EAM Data Lake Utility (DLU) connection

A new processor called <code>GetEAMDataLakeMessageProcessor</code> will be implemented within the canvas for existing customers utilizing EAM Data Lake (DLU) connection in Databridge Pro. This processor enables the distinction between transactional messages and messages specific to the data lake, to enhance performance and simplify processing.

### Improved performance of inbound messages

Performance of the Inbound Messages service was improved to increase the processing throughput time.

### Several new components were added

- ExecuteGroovyScript Allows users to write and execute Groovy scripts within the data flow, enabling dynamic behavior and complex transformations.
- GetEAMDataLakeMessageProcessor Reads <u>all</u> messages from a dedicated tenant queue, sent by the EAM Data Lake Utility tool.
  - ★ IMPORTANT Use only one instance of this processor, as it performs a comprehensive read of messages within the queue. Multiple instances of this processor will cause unexpected results.
- AvroSchemaRegistry Provides a service for registering and accessing schemas.

- DatabaseTableSchemaRegistry Provides a service for generating a record schema from a database table definition.
- HxGNPrivateSSLContextService Provides the ability to reference an available keystore or truststore certificate from the Certificate/Key Registry to use during the SSL handshake process for secure data transmission and communication.
- StandardJsonSchemaRegistry Provides a service for registering and accessing JSON schemas.

### Support, Copyright, and Legal Information

### **Copyright Notice**

### Copyright

Copyright © 2024-2025 Hexagon AB and/or its subsidiaries and affiliates.

This computer program, including software, icons, graphic symbols, documentation, file formats, and audio-visual displays; may be used only as pursuant to applicable software license agreement; contains confidential and proprietary information of Intergraph Corporation or a Hexagon Group Company and/or third parties which is protected by patent, trademark, copyright law, trade secret law, and international treaty, and may not be provided or otherwise made available without proper authorization from Hexagon AB and/or its subsidiaries and affiliates.

### **U.S. Government Restricted Rights Legend**

Use, duplication, or disclosure by the government is subject to restrictions as set forth below. For civilian agencies: This was developed at private expense and is "restricted computer software" submitted with restricted rights in accordance with subparagraphs (a) through (d) of the Commercial Computer Software - Restricted Rights clause at 52.227-19 of the Federal Acquisition Regulations ("FAR") and its successors, and is unpublished and all rights are reserved under the copyright laws of the United States. For units of the Department of Defense ("DoD"): This is "commercial computer software" as defined at DFARS 252.227-7014 and the rights of the Government are as specified at DFARS 227.7202-3.

Unpublished - rights reserved under the copyright laws of the United States.

Intergraph Corporation, Hexagon's Asset Lifecycle Intelligence Division 305 Intergraph Way Madison, AL 35758

#### **Documentation**

Documentation shall mean, whether in electronic or printed form, User's Guides, Installation Guides, Reference Guides, Administrator's Guides, Customization Guides, Programmer's Guides, Configuration Guides and Help Guides delivered with a particular software product.

#### Other Documentation

Other Documentation shall mean, whether in electronic or printed form and delivered with software or on Smart Community, SharePoint, box.net, or the Hexagon documentation web site, any documentation related to work processes, workflows, and best practices that is provided by Hexagon as guidance for using a software product.

#### **Terms of Use**

- a. Use of a software product and Documentation is subject to the Software License Agreement ("SLA") delivered with the software product unless the Licensee has a valid signed license for this software product with Intergraph Corporation, Hexagon's Asset Lifecycle Intelligence Division ("Hexagon"), a Hexagon Group Company. If the Licensee has a valid signed license for this software product with Hexagon, the valid signed license shall take precedence and govern the use of this software product and Documentation. Subject to the terms contained within the applicable license agreement, Hexagon gives Licensee permission to print a reasonable number of copies of the Documentation as defined in the applicable license agreement and delivered with the software product for Licensee's internal, non-commercial use. The Documentation may not be printed for resale or redistribution.
- b. For use of Documentation or Other Documentation where end user does not receive a SLA or does not have a valid license agreement with Hexagon, Hexagon grants the Licensee a non-exclusive license to use the Documentation or Other Documentation for Licensee's internal non-commercial use. Hexagon gives Licensee permission to print a reasonable number of copies of Other Documentation for Licensee's internal, non-commercial use. The Other Documentation may not be printed for resale or redistribution. This license contained in this subsection b) may be terminated at any time and for any reason by Hexagon by giving written notice to Licensee.

#### **Disclaimer of Warranties**

Except for any express warranties as may be stated in the SLA or separate license or separate terms and conditions, Hexagon disclaims any and all express or implied warranties including, but not limited to the implied warranties of merchantability and fitness for a particular purpose and nothing stated in, or implied by, this document or its contents shall be considered or deemed a modification or amendment of such disclaimer. Hexagon believes the information in this publication is accurate as of its publication date.

The information and the software discussed in this document are subject to change without notice and are subject to applicable technical product descriptions. Hexagon is not responsible for any error that may appear in this document.

The software, Documentation and Other Documentation discussed in this document are furnished under a license and may be used or copied only in accordance with the terms of this license. THE USER OF THE SOFTWARE IS EXPECTED TO MAKE THE FINAL EVALUATION AS TO THE USEFULNESS OF THE SOFTWARE IN HIS OWN ENVIRONMENT.

Hexagon is not responsible for the accuracy of delivered data including, but not limited to, catalog, reference and symbol data. Users should verify for themselves that the data is accurate and suitable for their project work.

### **Limitation of Damages**

IN NO EVENT WILL HEXAGON BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL INCIDENTAL, SPECIAL, OR PUNITIVE DAMAGES, INCLUDING BUT NOT LIMITED TO, LOSS OF USE OR PRODUCTION, LOSS OF REVENUE OR PROFIT, LOSS OF DATA, OR CLAIMS OF THIRD PARTIES, EVEN IF HEXAGON HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

UNDER NO CIRCUMSTANCES SHALL HEXAGON'S LIABILITY EXCEED THE AMOUNT THAT HEXAGON HAS BEEN PAID BY LICENSEE UNDER THIS AGREEMENT AT THE TIME THE CLAIM IS MADE. EXCEPT WHERE PROHIBITED BY APPLICABLE LAW, NO CLAIM, REGARDLESS OF FORM, ARISING OUT OF OR IN CONNECTION WITH THE SUBJECT MATTER OF THIS DOCUMENT MAY BE BROUGHT BY LICENSEE MORE THAN TWO (2) YEARS AFTER THE EVENT GIVING RISE TO THE CAUSE OF ACTION HAS OCCURRED.

IF UNDER THE LAW RULED APPLICABLE ANY PART OF THIS SECTION IS INVALID, THEN HEXAGON LIMITS ITS LIABILITY TO THE MAXIMUM EXTENT ALLOWED BY SAID LAW.

#### **Export Controls**

To the extent prohibited by United States or other applicable laws, Intergraph Corporation, Hexagon's Asset Lifecycle Intelligence division ("Hexagon"), and a Hexagon Group Company's commercial-off-the-shelf software products, customized software, Technical Data, and/or third-party software, or any derivatives thereof, obtained from Hexagon, its subsidiaries, or distributors must not be exported or re-exported, directly or indirectly (including via remote access) under the following circumstances:

a. To Cuba, Iran, North Korea, Syria, or the Crimean, "Donetsk People's Republic", "Luhansk People's Republic," or Sevastopol regions of Ukraine, or any national of these countries or territories.

- b. To any person or entity listed on any United States government denial list, including, but not limited to, the United States Department of Commerce Denied Persons, Entities, and Unverified Lists, the United States Department of Treasury Specially Designated Nationals List, and the United States Department of State Debarred List. Visit www.export.gov for more information or follow this link for the screening tool: <a href="https://legacy.export.gov/csl-search">https://legacy.export.gov/csl-search</a>.
- c. To any entity when Customer knows, or has reason to know, the end use of the software product, customized software, Technical Data and/or third-party software obtained from Hexagon, its subsidiaries, or distributors is related to the design, development, production, or use of missiles, chemical, biological, or nuclear weapons, or other un-safeguarded or sensitive nuclear uses.
- d. To any entity when Customer knows, or has reason to know, that an illegal reshipment will take place.

Any questions regarding export/re-export of relevant Hexagon software product, customized software, Technical Data, and/or third-party software obtained from Hexagon, its subsidiaries, or distributors, should be addressed to Hexagon's Export Compliance Department, 305 Intergraph Way, Madison, Alabama 35758 USA or at exportcompliance@hexagon.com. Customer shall hold harmless and indemnify Hexagon and a Hexagon Group Company for any causes of action, claims, costs, expenses and/or damages resulting to Hexagon or a Hexagon Group Company from a breach by Customer.

#### **Trademarks**

Intergraph<sup>®</sup>, the Intergraph logo<sup>®</sup>, Intergraph Smart<sup>®</sup>, SmartPlant<sup>®</sup>, SmartMarine, SmartSketch<sup>®</sup>, SmartPlant Cloud<sup>®</sup>, PDS<sup>®</sup>, FrameWorks<sup>®</sup>, I-Route, I-Export, ISOGEN<sup>®</sup>, SPOOLGEN, SupportManager<sup>®</sup>, SupportModeler<sup>®</sup>, SAPPHIRE<sup>®</sup>, TANK, PV Elite<sup>®</sup>, CADWorx<sup>®</sup>, CADWorx DraftPro<sup>®</sup>, GTSTRUDL<sup>®</sup>, CAESAR II<sup>®</sup>, and HxGN SDx<sup>®</sup> are trademarks or registered trademarks of Intergraph Corporation or its affiliates, parents, subsidiaries. Hexagon and the Hexagon logo are registered trademarks of Hexagon AB or its subsidiaries. Other brands and product names are trademarks of their respective owners.

### **Customer Support and Technical User Forum**

For the latest support information for this product, use a web browser to connect to the <a href="Smart Community">Smart Community <a href="https://hexagon.com/support-success/asset-lifecycle-intelligence/community">https://hexagon.com/support-success/asset-lifecycle-intelligence/community</a>. You can submit any documentation comments or suggestions you might have by logging on to our documentation web site at <a href="https://docs.hexagonali.com">https://docs.hexagonali.com</a>.

To access the Technical User Forum, go to <a href="https://www.linkedin.com/groups/873447/">https://www.linkedin.com/groups/873447/</a>.

### **Hexagon Policy Against Software Piracy**

When you purchase or lease Hexagon's Asset Lifecycle Intelligence division software, Hexagon, Intergraph, or its affiliates, parents, subsidiaries retains ownership of the product. You become the licensee of the product and obtain the right to use the product solely in accordance with the terms of the Intergraph Corporation, doing business as Hexagon's Asset Lifecycle Intelligence division, Software License Agreement and applicable United States and/or international copyright laws.

You must have a valid license for each working copy of the product. You may also make one archival copy of the software to protect from inadvertent destruction of the original software, but you are not permitted to use the archival copy for any other purpose. An upgrade replaces the original license. Any use of working copies of the product for which there is no valid Intergraph Corporation, doing business as Hexagon's Asset Lifecycle Intelligence division, Software License Agreement constitutes Software Piracy for which there are very severe penalties. All Hexagon software products are protected by copyright laws and international treaty.

If you have questions regarding software piracy or the legal use of Hexagon software products, please call the Legal Department at 256-730-2362 in the U.S.

Updated June 2022

Document No. DDGL562C0

# Copyright

Copyright© Hexagon AB and/or its subsidiaries and affiliates. All rights reserved.