#!/bin/bash

check_txt_records() {
		local domain=$1
		local dns_server="8.8.8.8"  # Google Public DNS сервер
		local txt_records=$(nslookup -q=txt $domain $dns_server | grep "text =")
		
		if [ -n "$txt_records" ]; then
				#echo "TXT records for $domain:"
				#echo "$txt_records"
				if [[ $txt_records == *'text = "google-site-verification='* ]]; then
					echo "Found Google Console TXT record"
				else
					echo "TXT records for $domain not found."
				fi
		else
				echo "TXT records for $domain not found."
		fi
}

check_txt_records "iteching.info"
