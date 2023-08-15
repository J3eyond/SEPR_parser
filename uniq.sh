#!/bin/bash

echo "Uniq Blocked:"
echo ""
cat risk_category/Blocked.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u
cat risk_category/Blocked.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u > alerts/blocked_uniq.txt

echo ""
echo "Uniq Deleted: "
echo ""
cat risk_category/Deleted.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u 
cat risk_category/Deleted.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u > alerts/deleted_uniq.txt

echo ""
echo "Uniq Newly infected: "
echo ""
cat risk_category/Newly\ infected.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u 
cat risk_category/Newly\ infected.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u > alerts/new_inf_uniq.txt

echo ""
echo "Uniq Quarantined: "
echo ""
cat risk_category/Quarantined.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u 
cat risk_category/Quarantined.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u > alerts/quarantined_uniq.txt


echo ""
echo "Uniq Still infected: "
echo ""
cat risk_category/Still\ infected.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u 
cat risk_category/Still\ infected.txt | awk {'print $1,$3,$9,$10,$11,$12,$13'} | sort -u > alerts/Still_inf_uniq.txt


echo ""
echo "AV engine off: "
echo ""
cat av_status/AV\ engine\ off.txt
cat av_status/AV\ engine\ off.txt > alerts/av_engine_off.txt

echo ""
echo "Sonar pro scan off: "
echo ""
cat av_status/Sonar\ pro\ scan\ off.txt
cat av_status/Sonar\ pro\ scan\ off.txt > alerts/sonar_pro_scan_off.txt