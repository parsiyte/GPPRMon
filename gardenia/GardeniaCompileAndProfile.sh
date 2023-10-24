#!/bin/bash
if [ $# -eq 0 ];
then
  echo "$0: Application name is missing"
  exit 1
else
  filename="$1"
  arg1="$2"
  arg2="$3"
  arg3="$4"

  echo "Application name is: $filename"

  mkdir $filename 
  ncu --set full --target-processes all apps/$filename mtx 4 >  $filename/4.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx 4w > $filename/4w.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx asia_osm_coord > $filename/asia_osm_coord.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx asia_osm       > $filename/asia_osm.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx chesapeake     > $filename/chesapeake.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx coAuthorsCiteseer > $filename/coAuthorsCiteseer.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx coAuthorsDBLP     > $filename/coAuthorsDBLP.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx coPapersCiteseer  > $filename/coPapersCiteseer.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx coPapersDBLP      > $filename/coPapersDBLP.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx germany_osm_coord > $filename/germany_osm_coord.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx germany_osm       > $filename/germany_osm.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx great-britain_osm_coord > $filename/great-britain_osm_coord.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx great-britain_osm       > $filename/great-britain_osm.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx higgs-twitter_mention   > $filename/higgs-twitter_mention.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx higgs-twitter           > $filename/higgs-twitter.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx higgs-twitter_reply     > $filename/higgs-twitter_reply.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx higgs-twitter_retweet   > $filename/higgs-twitter_retweet.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx higgs-twitter_temporal_edges > $filename/higgs-twitter_temporal_edges.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx indochina-2004               > $filename/indochina-2004.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx italy_osm_coord              > $filename/italy_osm_coord.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx italy_osm    > $filename/italy_osm.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx min-1DeadEnd > $filename/min-1DeadEnd.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx min-2SCC     > $filename/min-2SCC.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx min-4SCC     > $filename/min-4SCC.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx min-NvgraphEx > $filename/min-NvgraphEx.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx soc-Epinions1 > $filename/soc-Epinions1.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx soc-LiveJournal1 > $filename/soc-LiveJournal1.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx soc-Slashdot0811 > $filename/soc-Slashdot0811.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx soc-Slashdot0902 > $filename/soc-Slashdot0902.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx test_bc  > $filename/test_bc.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx test_cc  > $filename/test_cc.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx test_mst > $filename/test_mst.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx test_pr  > $filename/test_pr.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx test_scc > $filename/test_scc.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx test_sgd > $filename/test_sgd.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx test_small_scc > $filename/test_small_scc.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx web-BerkStan   > $filename/web-BerkStan.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx web-Google     > $filename/web-Google.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx web-NotreDame  > $filename/web-NotreDame.txt $arg1 $arg2 $arg3
  ncu --set full --target-processes all apps/$filename mtx web-Stanford   > $filename/web-Stanford.txt $arg1 $arg2 $arg3

fi


