# PBN (Private Blog Network) Project

## 🌐 Overview
This project aims to create PBNs (Private Blog Networks) 
<details>
<summary>✨ Objectives can be</summary>
   
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
   
1. 📋 List of Our Website Domains
2. 📋 Lists of Competitors' Website Domains
3. 📋 Keyword Lists
   
</details>

<details>
<summary>🤝 Agreements</summary>
   
1. This project exclusively focuses on utilizing domains with a history, specifically drop domains.
2. We only consider domains that allow us to retrieve website content 
* From public archives (web.archive.org or commoncrawl.org)
* Alternatively, we may preserve the content ourselves when the domain is in the expired state but remains accessible.
We don't work with domains without history or without content
   
</details>



## 📊 Workflow
### Domains
#### 📋 Make potential list of domains

📝 Make a list from:
- Google
- Wikipedia
- GitHub

using Semrush or wget+rapser

#### 📝 Drop Domains
look for Domains, that are Expired(Potential New Drops) or Free/Available (old drops)


#### Potential New Drops and Bids technology
📝 To-do



### ✏️ Content
🔍 Parsed from web.archive.org or commoncrawl.org
⚙️ Processing of parsef content:
- Use our own tools to parse content
- Restore content as CSV for later upload to our WordPress


⚙️ Process for drop domains:
1. Make a list of potential domains
2. Check the list by combining domain and parsed content





### ⚙️ Domain Selection
- Check the list of drop domains
- Consider factors such as content, PR (Page Rank), and manual domain selection

### ⬆️ WordPress Integration
After buying a domain, upload the old information to WordPress.

📊 **Project Workflow**




   - Perform manual domain selection based on factors like content quality, PR, etc.

   - csv / After domain acquisition, upload the old information to WordPress





## ✨ **Scripts and Folders**

**./content**

This folder contains scripts related to content parsing and restoration.

- `webarchive_parser`:
  - Description: Parses content from web.archive.org.
  - File: `webarchive_parser.py`

- `webarchive_scrapper`:
  - Description: Scrapes content from web.archive.org.
  - File: `webarchive_scrapper.py`

**./domains**

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
