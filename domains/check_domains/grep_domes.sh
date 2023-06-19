grep -r -E 'shop|school|hotel|technology|3d|vr|360|planet|museum|wedding|travel|conf|exhib|marketing|brand|invest|realty|house|home|technology' . | grep -E '\com,/|\org,/|\net,/|\info,|\ru,' | grep "\"eng\""  > ../domes.txt

# grep "\"eng\"" | grep -Eo '[A-Za-z0-9.-]+\.([A-Za-z]{2,}|[A-Za-z]{2}\.[A-Za-z]{2})'