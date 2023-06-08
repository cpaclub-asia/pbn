# PBN (Private Blog Network) Project

## 🌐 Overview
This project aims to create PBNs (Private Blog Networks) 
<details>
  <summary>objectives can be</summary>
**📈 Traffic/Metrics Options**
- 🔝 Boost metrics of the main website.
- 🚀 Drive traffic to the main site.
- 📈 Improve metrics of the PBN websites.
- 🚗 Drive traffic to the PBN websites.

**💰 Monetization Options can include**
- 📊 Traffic monetization through Adwords.
- 💲 Traffic monetization through CPA.
- 🔗 Selling links and articles on the PBN.
- 🌐 Selling the entire PBN network.
</details>

<details>
  <summary>✨ Preliminary Requirements</summary>
Before diving into the project workflow, ensure you have the following preliminary requirements:

1. 📋 List of Our Website Domains
2. 📋 Lists of Competitors' Website Domains
3. 📋 Keyword Lists
</details>


## 📋 Domain
Domains can be classified as either "new" or "drop."

### New Domains
✨ No history

### Drop Domains
📝 Make a list from:
- Google
- Wikipedia
- GitHub (using Semrush)

⚙️ Process for drop domains:
1. Make a list of potential domains
2. Check the list by combining domain and parsed content

## ✏️ Content
Content can be classified as either "new" or "old."

### New Content
🔍 Parsed from web.archive.org or commoncrawl.org

⚙️ Process for new content:
- Use our own tools to parse content
- Restore content as CSV for later upload to our WordPress

### Old Content
📝 Easy to buy but limited quality

## 📝 Drop Domains
Drop domains can be further categorized into "new drops" or "old drops."

### New Drops and Bids
📝 To-do list

## ⚙️ Domain Selection
- Check the list of drop domains
- Consider factors such as content, PR (Page Rank), and manual domain selection

## ⬆️ WordPress Integration
After buying a domain, upload the old information to WordPress.

📊 **Project Workflow**

1. Identify domain needs:
   - Determine if a new or drop domain is required.
   - Define the content requirements (new or old).

2. Domain Acquisition:
   - For new domains:
     - Start with no history.
   - For drop domains:
     - Generate a list from Google, Wikipedia, and GitHub using Semrush.
     - Combine domain and parsed content to check the list.

3. Content Gathering:
   - For new content:
     - Parse content from web.archive.org or commoncrawl.org using our tools.
     - Restore content as CSV for later WordPress upload.
   - For old content:
     - Purchase domains with readily available content.

4. Drop Domains:
   - Categorize drop domains as new drops or old drops.
   - Manage new drops and bids based on priorities.

5. Domain Selection:
   - Perform manual domain selection based on factors like content quality, PR, etc.

6. WordPress Integration:
   - After domain acquisition, upload the old information to WordPress.

✨ **Scripts and Folders**

## ./content

This folder contains scripts related to content parsing and restoration.

- `webarchive_parser`:
  - Description: Parses content from web.archive.org.
  - File: `webarchive_parser.py`

- `webarchive_scrapper`:
  - Description: Scrapes content from web.archive.org.
  - File: `webarchive_scrapper.py`

## ./domains

This folder contains scripts related to domain management.

- `check_domains`:
  - Description: Contains various scripts for checking domain information.
  - Files:
    - `check_domain_connection`: Checks domain connection status.
    - `check_domain_whois`: Retrieves WHOIS information for a domain.
    - `check_if_dropped_domain`: Checks if a domain has been dropped.
    - `check_if_expired_domain`: Checks if a domain has expired.
    - `domains_csv_to_txt`: Converts domain information from CSV to TXT format.

- `make_domains_lists`:
  - Description: Contains scripts for generating domain lists.
  - File: `scrap_site_for_outgoing_domains`: Scrapes websites for outgoing domains.

Feel free to explore the scripts

 and folders for more details on their functionality and usage.
