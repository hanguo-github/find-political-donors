The key to find the median of the running contributions: using two heaps that a max-heap for the lower half transactions and a min-heap for the upper half transactions to maintain the current median so far.

Core data structure for zip-orientated statistics: zip_stats[i][0:7] (for the ith distinct row characterized by CMTE_ID + ZIP_CODE)

zip_stats[i][0] = CMTE_ID
zip_stats[i][1] = ZIP_CODE
zip_stats[i][2] = current median
zip_stats[i][3] = current num of transactions received by recipient from the zip
zip_stats[i][4] = current amount of transactions received by recipient from the zip
zip_stats[i][5] = max-heap for the lower half transactions
zip_stats[i][6] = min-heap for the upper half transactions
zip_stats[i][7] = length(the max-heap) - length(the min-heap)

Similar structure for the date_stats[j][0:7].
